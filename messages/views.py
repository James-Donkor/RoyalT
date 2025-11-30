from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def messages_dashboard(request):
    # Fake threads for demo
    threads = [
        {'id': 1, 'title': 'EP Mixdown', 'sender': 'ClientA'},
        {'id': 2, 'title': 'Live Recording Review', 'sender': 'EngineerX'},
        {'id': 3, 'title': 'Final Master Delivery', 'sender': 'ClientB'},
    ]
    return render(request, 'messages/dashboard.html', {'threads': threads})


@login_required
def thread_detail(request, thread_id):
    # Fake messages for demo
    messages = [
        {'from': 'ClientA', 'text': 'Can you turn the snare up a bit?'},
        {'from': 'You', 'text': 'Sure, here’s a new mix.', 'audio_url': '/static/audio/sample_audio.wav'},
        {'from': 'ClientA', 'text': 'Sounds great, approved!'},
    ]
    return render(request, 'messages/thread_detail.html', {
        'thread_id': thread_id,
        'messages': messages
    })
#views.py in messages