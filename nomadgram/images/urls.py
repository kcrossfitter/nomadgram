from django.conf.urls import url

from . import views

urlpatterns = [

    url(
        regex=r'^$',
        view=views.Images.as_view(),
        name='images'
    ),
    url(
        regex=r'^(?P<image_id>\d+)/$',
        view=views.ImageDetail.as_view(),
        name='image_detail'
    ),
    url(
        regex=r'^(?P<image_id>\d+)/likes/$',
        view=views.LikeImage.as_view(),
        name='like_image'
    ),
    url(
        regex=r'^(?P<image_id>\d+)/unlikes/$',
        view=views.UnLikeImage.as_view(),
        name='unlike_image'
    ),
    url(
        regex=r'^(?P<image_id>\d+)/comments/$',
        view=views.CommentOnImage.as_view(),
        name='comment_image'
    ),
    url(
        regex=r'^(?P<image_id>\d+)/comments/(?P<comment_id>\d+)/$',
        view=views.ModerateComments.as_view(),
        name='comment_image'
    ),
    url(
        regex=r'^comments/(?P<comment_id>\d+)/$',
        view=views.Comment.as_view(),
        name='comment'
    ),
    url(
        regex=r'^search/$',
        view=views.Search.as_view(),
        name='search'
    ),

    # Urls below are for testing purpose.
    # url(
    #     regex=r'all/$',
    #     view=views.ListAllImages.as_view(),
    #     name='all_images'
    # ),
    # url(
    #     regex=r'comments/$',
    #     view=views.ListAllComments.as_view(),
    #     name='all_comments'
    # ),
    # url(
    #     regex=r'likes/$',
    #     view=views.ListAllLikes.as_view(),
    #     name='all_likes'
    # ),

]
