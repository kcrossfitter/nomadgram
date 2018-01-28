from django.conf.urls import url

from . import views

urlpatterns = [

    url(
        regex=r'^$',
        view=views.Feed.as_view(),
        name='feed'
    )

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
