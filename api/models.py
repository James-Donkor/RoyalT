from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


class UserProfile(models.Model):
    ROLE_CHOICES = (
        ('client', 'Client'),
        ('engineer', 'Engineer'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='client')
    bio = models.TextField(blank=True)
    profile_image = models.ImageField(upload_to='profiles/', blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.role}"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.user.username)
        super().save(*args, **kwargs)


class Guest(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name or self.email


class MessageThread(models.Model):
    engineer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='message_threads')
    client = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='client_threads')
    guest = models.ForeignKey(Guest, on_delete=models.SET_NULL, null=True, blank=True, related_name='guest_threads')
    created_at = models.DateTimeField(auto_now_add=True)
    subject = models.CharField(max_length=255)
    users = models.ManyToManyField(User)

    def __str__(self):
        return f"Thread with {self.client or self.guest} → {self.engineer.username}"


class Message(models.Model):
    thread = models.ForeignKey(MessageThread, on_delete=models.CASCADE, related_name='messages')
    sender_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    sender_guest = models.ForeignKey(Guest, on_delete=models.SET_NULL, null=True, blank=True)
    text = models.TextField(blank=True)
    is_offer = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    audio_url = models.URLField(blank=True, null=True)
    offer_data = models.JSONField(blank=True, null=True)

    def __str__(self):
        return f"Message at {self.created_at} in {self.thread.subject}"

    @property
    def sender_name(self):
        if self.sender_user:
            return self.sender_user.username
        elif self.sender_guest:
            return self.sender_guest.name or self.sender_guest.email
        return "Unknown"


class Offer(models.Model):
    thread = models.ForeignKey(MessageThread, on_delete=models.CASCADE, related_name='offers')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    base_pay = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    royalty_percentage = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    revisions = models.IntegerField(default=2)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    accepted = models.BooleanField(null=True, blank=True)

    def __str__(self):
        return f"Offer by {self.created_by.username} on thread {self.thread.id}"


class AttachedFile(models.Model):
    message = models.ForeignKey(Message, on_delete=models.CASCADE, related_name='attachments')
    file = models.FileField(upload_to='attachments/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"File attached to message {self.message.id}"

#models.py