# Generated by Django 5.2 on 2025-04-13 03:19

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='message',
            name='deal',
        ),
        migrations.RemoveField(
            model_name='offer',
            name='deal',
        ),
        migrations.RemoveField(
            model_name='message',
            name='sender',
        ),
        migrations.RemoveField(
            model_name='offer',
            name='estimated_hours',
        ),
        migrations.RemoveField(
            model_name='offer',
            name='message',
        ),
        migrations.RemoveField(
            model_name='offer',
            name='perpetuity',
        ),
        migrations.RemoveField(
            model_name='offer',
            name='revisions_included',
        ),
        migrations.RemoveField(
            model_name='offer',
            name='sender',
        ),
        migrations.RemoveField(
            model_name='offer',
            name='split_percent',
        ),
        migrations.RemoveField(
            model_name='offer',
            name='upfront_fee',
        ),
        migrations.AddField(
            model_name='message',
            name='sender_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='offer',
            name='accepted',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='offer',
            name='base_pay',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='offer',
            name='created_by',
            field=models.ForeignKey(default=0.0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='offer',
            name='notes',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='offer',
            name='revisions',
            field=models.IntegerField(default=2),
        ),
        migrations.AddField(
            model_name='offer',
            name='royalty_percentage',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to='profiles/'),
        ),
        migrations.AlterField(
            model_name='message',
            name='content',
            field=models.TextField(blank=True),
        ),
        migrations.CreateModel(
            name='AttachedFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='attachments/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('message', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attachments', to='api.message')),
            ],
        ),
        migrations.AddField(
            model_name='message',
            name='sender_guest',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.guest'),
        ),
        migrations.CreateModel(
            name='MessageThread',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('client', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='client_threads', to=settings.AUTH_USER_MODEL)),
                ('engineer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='message_threads', to=settings.AUTH_USER_MODEL)),
                ('guest', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='guest_threads', to='api.guest')),
            ],
        ),
        migrations.AddField(
            model_name='message',
            name='thread',
            field=models.ForeignKey(default=0.0, on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='api.messagethread'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='offer',
            name='thread',
            field=models.ForeignKey(default=0.0, on_delete=django.db.models.deletion.CASCADE, related_name='offers', to='api.messagethread'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Deal',
        ),
    ]
