from django.db import models
from django.urls import reverse
from datetime import date as dt
# Create your models here.


class Member(models.Model):
    name = models.CharField(max_length=255, help_text='Enter your full name')
    age = models.PositiveIntegerField(help_text='Enter your age')
    phone = models.CharField(
        max_length=10, help_text='Enter a number beginning with 07')

    def get_absolute_url(self):
        return reverse('member-list')

    def __str__(self) -> str:
        return self.name


class Album(models.Model):
    name = models.CharField(max_length=255, help_text='Enter album name')
    release_date = models.DateTimeField()
    album_art = models.ImageField(
        default='media/album_art/default.png', upload_to='media/album_art/')
    detail = models.TextField()

    def get_absolute_url(self):
        return reverse('album-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return self.name


class AudioTrack(models.Model):
    name = models.CharField(max_length=255, help_text="Track's name")
    audio = models.FileField(upload_to='media/audio/',
                             help_text='upload audio file if available')
    album = models.ForeignKey(Album, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('audio-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return self.name


class VideoTrack(models.Model):
    name = models.CharField(max_length=255, help_text="Track's name")
    video = models.FileField(upload_to='media/video/',
                             help_text='upload video file if available')
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    link = models.TextField(
        help_text='Enter the youtube share link',blank=True,null=True)

    def get_absolute_url(self):
        return reverse('video-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return self.name


class Leader(models.Model):
    name = models.CharField(max_length=255, help_text='Enter your full name')
    age = models.PositiveIntegerField(help_text='Enter your age')
    leaders_pic = models.ImageField(upload_to='media/leaders/')
    phone = models.CharField(
        max_length=10, help_text='Enter a number beginning with 07')
    term_start = models.DateField()
    term_end = models.DateField()
    current = models.BooleanField(default=False)


    def iscurrent(self):
        if self.current == True:
            return True
        return False

    def __str__(self) -> str:
        return self.name


class Gallery(models.Model):
    location = models.CharField(max_length=255, help_text='Location where picture was taken')
    picture = models.ImageField(upload_to='media/gallery/',
                                help_text='upload picture')
    featured = models.BooleanField(default=False)

    def __str__(self):
        return self.location


class Event(models.Model):
    title = models.CharField(max_length=200)
    poster = models.ImageField(upload_to='posters/',default='posters/default.jpeg')
    description = models.TextField()
    date = models.DateField()
    time = models.PositiveSmallIntegerField(help_text='Duration of the event',default='6')
    location = models.CharField(max_length=200,default='Kisumu')
    upcoming = models.BooleanField(default = False)

    @property
    def expired(self):
        if self.date and dt.today() > self.date:
            return True
        return False

    def __str__(self) -> str:
        return self.title