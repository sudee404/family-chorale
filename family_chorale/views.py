from django.shortcuts import render
from django.views import generic
from .models import AudioTrack, Leader, Member, Album, VideoTrack,Gallery,Event

# Create your views here.


def index(request):
    pictures = Gallery.objects.filter(featured=True)[:2]
    events = Event.objects.filter(upcoming=True)[:3]
    context = {
        'pics':pictures,
        'events':events,
    }
    return render(request, 'index.html',context=context)

def music(request):
    videos = VideoTrack.objects.all()
    audios = AudioTrack.objects.all()
    context = {
        'vids':videos,
        'audios':audios,
    }
    return render(request, 'music.html',context=context)


class MemberCreateView(generic.CreateView):
    model = Member
    fields = ('name', 'age', 'phone')


class AlbumsListView(generic.ListView):
    model = Album


class AlbumsDetailView(generic.DetailView):
    model = Album


class MemberListView(generic.ListView):
    model = Member


class AudioDetailView(generic.DetailView):
    model = AudioTrack


class AudioListView(generic.ListView):
    model = AudioTrack


class VideoDetailView(generic.DetailView):
    model = VideoTrack


class VideoListView(generic.ListView):
    model = VideoTrack


class LeadersDetailView(generic.DetailView):
    model = Leader


class LeadersListView(generic.ListView):
    model = Leader

class GalleryView(generic.ListView):
    model = Gallery

class CalendarView(generic.ListView):
    model = Event