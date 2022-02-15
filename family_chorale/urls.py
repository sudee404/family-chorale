"""sample1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views

urlpatterns = [
    path('become-a-member/',views.MemberCreateView.as_view(),name='recruit'),
    path('members/',views.MemberListView.as_view(), name='member-list'),
    path('songs/',views.AlbumsListView.as_view(), name='songs'),
    path('songs/<int:pk>',views.AlbumsDetailView.as_view(), name='album-detail'),
    path('audio/',views.AudioListView.as_view(), name='audio'),
    path('audio/<int:pk>',views.AudioDetailView.as_view(), name='audio-detail'),
    path('video/',views.VideoListView.as_view(), name='video'),
    path('video/<int:pk>',views.VideoDetailView.as_view(), name='video-detail'),
    path('leaders/',views.LeadersListView.as_view(), name='leader'),
    path('leaders/<int:pk>',views.LeadersDetailView.as_view(), name='leader-detail'),
    path('gallery/',views.GalleryView.as_view(), name='gallery'),
    path('events/',views.CalendarView.as_view(),name='events'),
    path('music/',views.music,name='music'),
]