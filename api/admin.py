from django.contrib import admin
from .models import UserProfile, Guest, MessageThread, Message, Offer, AttachedFile


admin.site.register(UserProfile)
admin.site.register(Guest)
admin.site.register(MessageThread)
admin.site.register(Message)
admin.site.register(Offer)
admin.site.register(AttachedFile)
#admin.py
