from django.contrib import admin
from .models import Member,VideoTrack,AudioTrack,Album,Leader,Gallery,Event
# Register your models here.
admin.site.register(Member)
admin.site.register(VideoTrack)
admin.site.register(AudioTrack)
admin.site.register(Album)
admin.site.register(Leader)
admin.site.register(Gallery)
admin.site.register(Event)