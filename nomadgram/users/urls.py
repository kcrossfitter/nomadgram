from django.conf.urls import url

from . import views

urlpatterns = [
    url(
        regex=r'explore/$',
        view=views.ExploreUsers.as_view(),
        name='expore_users'
    ),
]
