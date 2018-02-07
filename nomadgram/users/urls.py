from django.conf.urls import url

from . import views

urlpatterns = [
    url(
        regex=r'explore/$',
        view=views.ExploreUsers.as_view(),
        name='expore_users'
    ),
    url(
        regex=r'(?P<user_id>\d+)/follow/$',
        view=views.FollowUser.as_view(),
        name='follow_user'
    ),
    url(
        regex=r'(?P<user_id>\d+)/unfollow/$',
        view=views.UnFollowUser.as_view(),
        name='unfollow_user'
    ),
    url(
        regex=r'(?P<username>\w+)/followers/$',
        view=views.UserFollowers.as_view(),
        name='user_followers'
    ),
    url(
        regex=r'(?P<username>\w+)/following/$',
        view=views.UserFollowing.as_view(),
        name='user_following'
    ),
    url(
        regex=r'search/$',
        view=views.Search.as_view(),
        name='user_search'
    ),
    url(
        regex=r'^login/facebook/$',
        view=views.FacebookLogin.as_view(),
        name='fb_login'
    ),
    url(
        regex=r'(?P<username>\w+)/password/$',
        view=views.ChangePassword.as_view(),
        name='change_password'
    ),
    url(
        regex=r'(?P<username>\w+)/$',
        view=views.UserProfile.as_view(),
        name='user_profile'
    ),
]
