# from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from . import models, serializers
from nomadgram.users import models as user_models
from nomadgram.notifications import views as notification_views
from nomadgram.users import serializers as user_serializers


class Images(APIView):
    """
    Get the latest posts of users that you're following
    Also get the latest posts of mine
    """
    def get(self, request, format=None):
        # 1. get users that our request.user follows
        user = request.user
        following_users = user.following.all()

        # 2. get the latest 2 images
        image_list = []
        for following_user in following_users:
            user_images = following_user.images.all()[:2]

            for image in user_images:
                image_list.append(image)

        my_images = user.images.all()[:2]

        for image in my_images:
            image_list.append(image)

        sorted_list = sorted(
            image_list,
            key=lambda image: image.created_at,
            reverse=True
        )

        serializer = serializers.ImageSerializer(sorted_list, many=True)

        return Response(serializer.data)


    def post(self, request, format=None):

        user = request.user

        serializer = serializers.InputImageSerializer(
            data=request.data
        )

        if serializer.is_valid():
            serializer.save(creator=user)
            return Response(
                data=serializer.data,
                status=status.HTTP_201_CREATED
            )
        else:
            return Response(
                data=serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )



""" Like an Image """
class LikeImage(APIView):

    # When a user clicks 'likes' on the specific image,
    # Show the users who like that image
    def get(self, request, image_id, format=None):

        # find all likes where image__id equals to image_id
        likes = models.Like.objects.filter(image__id=image_id)

        # Returns a QuerySet that returns dictionaries
        like_creators_ids = likes.values('creator_id')

        # Find users with ids in like_creators_id
        users = user_models.User.objects.filter(id__in=like_creators_ids)

        serializer = user_serializers.ListUserSerializer(users, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)


    def post(self, request, image_id, format=None):
        # Find the logged in user/the user who likes this image
        user = request.user

        # Find the image that the 'user' likes
        try:
            found_image = models.Image.objects.get(id=image_id)
        except models.Image.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        # Is this image alreday liked by this user?
        #   then return with status code 304
        #   else create the new Like object for that image
        #       then create the notification object
        try:
            preexisting_like = models.Like.objects.get(
                creator=user,
                image=found_image
            )
            return Response(status=status.HTTP_304_NOT_MODIFIED)

        except models.Like.DoesNotExist:
            new_like = models.Like.objects.create(
                creator=user,
                image=found_image
            )

            new_like.save()

            notification_views.create_notification(
                user,
                found_image.creator,
                'like',
                found_image,
                None
            )

            return Response(status=status.HTTP_201_CREATED)


class UnLikeImage(APIView):

    def delete(self, request, image_id, format=None):

        user = request.user

        try:
            found_image = models.Image.objects.get(id=image_id)

        except models.Image.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        try:
            preexisting_like = models.Like.objects.get(
                creator=user,
                image=found_image
            )
            preexisting_like.delete()

            return Response(status=status.HTTP_204_NO_CONTENT)

        except models.Like.DoesNotExist:

            return Response(status=status.HTTP_304_NOT_MODIFIED)


class CommentOnImage(APIView):

    def post(self, request, image_id, format=None):

        user = request.user

        try:
            found_image = models.Image.objects.get(id=image_id)
        except models.Image.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = serializers.CommentSerializer(data=request.data)

        if serializer.is_valid():

            serializer.save(creator=user, image=found_image)

            notification_views.create_notification(
                user,
                found_image.creator,
                'comment',
                found_image,
                serializer.data['message']
            )

            return Response(
                data=serializer.data,
                status=status.HTTP_201_CREATED
            )

        else:

            return Response(
                data=serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )


""" Delete a comment that I make """
class Comment(APIView):

    def delete(self, request, comment_id, format=None):

        # Find the user who created this comment
        user = request.user

        # Find the comment of which id=comment_id and creator=user
        # Delete the comment
        try:
            comment = models.Comment.objects.get(id=comment_id, creator=user)
            comment.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except models.Comment.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class Search(APIView):

    def get(self, request, format=None):

        # One big string
        hashtags = request.query_params.get('hashtags', None)

        if hashtags is not None:

            hashtags = hashtags.split(',')

            images = models.Image.objects.filter(
                tags__name__in=hashtags
            ).distinct()

            serializer = serializers.CountImageSerializer(images, many=True)

            return Response(data=serializer.data, status=status.HTTP_200_OK)

        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


""" Delete a comment on my Image """
class ModerateComments(APIView):

    def delete(self, request, image_id, comment_id, format=None):

        # Find the user who is the owner of the image
        user = request.user

        # Find the comment to delete, where
        #   id of the comment: comment_id
        #   id of the image: image_id
        #   creator of the image: user
        try:
            comment_to_delete = models.Comment.objects.get(
                id=comment_id,
                image__id=image_id,
                image__creator=user
            )
            comment_to_delete.delete()
        except models.Comment.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        return Response(status=status.HTTP_204_NO_CONTENT)


class ImageDetail(APIView):

    def find_own_image(self, image_id, user):
        try:
            image = models.Image.objects.get(id=image_id, creator=user)
            return image
        except models.Image.DoesNotExist:
            return None


    def get(self, request, image_id, format=None):

        user = request.user

        image = self.find_own_image(image_id, user)

        if image is None:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = serializers.ImageSerializer(image)

        return Response(data=serializer.data, status=status.HTTP_200_OK)


    # Update the only image that I created
    def put(self, request, image_id, format=None):

        user = request.user

        image = self.find_own_image(image_id, user)

        if image is None:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

        if serializer.is_valid():

            serializer.save(creator=user)

            return Response(
                data=serializer.data,
                status=status.HTTP_204_NO_CONTENT
            )

        else:
            return Response(
                data=serializer.erros,
                status=status.HTTP_400_BAD_REQUEST
            )

    def delete(self, request, image_id, format=None):

        user = request.user

        image = self.find_own_image(image_id, user)

        if image is None:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

        image.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
"""
Examples for rest framework

class ListAllImages(APIView):

    def get(self, request, format=None):

        all_images = models.Image.objects.all()
        serializer = serializers.ImageSerializer(all_images, many=True)

        return Response(data=serializer.data)


class ListAllComments(APIView):

    def get(self, request, format=None):

        all_comments = models.Comment.objects.all()
        serializer = serializers.CommentSerializer(all_comments, many=True)

        return Response(data=serializer.data)


class ListAllLikes(APIView):

    def get(self, request, format=None):

        all_likes = models.Like.objects.all()
        serializer = serializers.LikeSerializer(all_likes, many=True)

        return Response(data=serializer.data)
"""
