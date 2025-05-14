from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from rest_framework import viewsets
from django.shortcuts import render, redirect
from django.utils.timezone import now

import json


from .models import UserProfile, Guest, MessageThread, Offer, Message, AttachedFile
from .serializers import UserProfileSerializer, OfferSerializer, MessageSerializer

# 🧾 Thread Detail View
# 🧾 Thread Detail View with Dummy Data + Offer Support
dummy_threads = {
    1: [
        {'from': 'ClientA', 'text': 'Can you turn the snare up a bit?'},
        {'from': 'You', 'text': 'Sure, here’s a new mix.', 'audio_url': '/static/audio/sample_audio.wav'},
        {'from': 'ClientA', 'text': 'Sounds great, approved!'},
        {
            'from': 'Mix Engineer',
            'text': '🎛️ New Deal Offer sent!',
            'is_offer': True,
            'offer_data': {
                'base_pay': '500',
                'master_royalties': '15',
                'publishing_royalties': '10',
                'bonus_clause': '$1000 if it hits 1M streams',
                'performance_royalties': '$50/show',
                'backend_points': '5',
                'term_years': '3',
                'territory': 'Global',
                'usage_rights': 'Sync, Commercial',
                'credit_format': 'Mixed by James Donkor',
                'revisions_allowed': '2',
                'delivery_timeline': '5',
                'buyout_option': '1000',
                'indemnity_notes': 'N/A'
            }
        },
        {'from': 'You', 'text': 'Sounds good, let me check.'},
    ],
    2: [
        {'from': 'EngineerX', 'text': 'Live mix is ready, review attached.', 'pic': 'avatars/ProfilePic_EngineerX.jpeg'},
        {'from': 'You', 'text': 'Will do, thank you!'},
    ],
    3: [
        {'from': 'ClientB', 'text': 'Final masters sound great. Send invoice.', 'pic': 'avatars/ProfilePic_ClientB.jpeg'},
        {'from': 'You', 'text': 'Sent! Pleasure working with you.'},
    ]
}

import json
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

@login_required
def thread_detail(request, thread_id):
    thread_id = int(thread_id)
    messages = dummy_threads.get(thread_id, [])

    if request.method == 'POST':
        print("POST payload:", request.POST)
        is_offer = request.POST.get('is_offer') in ['true', '1']
        print("✅ POST received:", request.POST.dict())



        if is_offer:
            # Prefer JSON-based offer payload
            offer_data_raw = request.POST.get('offer_json')
            try:
                offer_data = json.loads(offer_data_raw) if offer_data_raw else {}
            except json.JSONDecodeError:
                offer_data = {}

            # Fallback if no offer_json was submitted
            if not offer_data:
                offer_data = {
                    'base_pay': request.POST.get('base_pay'),
                    'master_royalties': request.POST.get('master_royalties'),
                    'publishing_royalties': request.POST.get('publishing_royalties'),
                    'bonus_clause': request.POST.get('bonus_clause'),
                    'performance_royalties': request.POST.get('performance_royalties'),
                    'backend_points': request.POST.get('backend_points'),
                    'term_years': request.POST.get('term_years'),
                    'territory': request.POST.get('territory'),
                    'usage_rights': request.POST.get('usage_rights'),
                    'credit_format': request.POST.get('credit_format'),
                    'revisions_allowed': request.POST.get('revisions_allowed'),
                    'delivery_timeline': request.POST.get('delivery_timeline'),
                    'buyout_option': request.POST.get('buyout_option'),
                    'indemnity_notes': request.POST.get('indemnity_notes'),
                }

            messages.append({
                'from': 'You',
                'text': '🎛️ New Deal Offer sent!',
                'is_offer': True,
                'offer_data': offer_data
            })

        else:
            # Standard text message
            text = request.POST.get('message', '').strip()
            if text:
                messages.append({
                    'from': 'You',
                    'text': text,
                    'is_offer': False
                })

        dummy_threads[thread_id] = messages
        return redirect('thread_detail', thread_id=thread_id)

    return render(request, 'messages/thread_detail.html', {
        'thread_id': thread_id,
        'messages': messages
    })

@login_required
def contracts_view(request):
    dummy_contracts = [
        {
            'song_name': 'Crazy in Love',
            'artist': 'Beyoncé',
            'release_date': '2003-05-14',
            'deposit_submitted': True,
            'attachments': [
                {'label': 'Recording Contract', 'url': '/static/docs/crazy_in_love_contract.pdf'},
                {'label': 'Label Email Thread', 'url': '/static/docs/crazy_in_love_emails.pdf'},
            ],
            'isrc': 'USSM10304554'
        }
    ]
    return render(request, 'contracts.html', {'contracts': dummy_contracts})




# 📨 Messages Dashboard
def messages_dashboard(request):
    if request.user.is_authenticated:
        profile = get_object_or_404(UserProfile, user=request.user)
        threads = MessageThread.objects.filter(engineer=request.user).order_by('-created_at')
    else:
        # TEMP: fallback for UI testing
        test_user = User.objects.first()
        profile = UserProfile.objects.filter(user=test_user).first()
        threads = [
            {'id': 1, 'title': 'EP Mixdown', 'sender': 'ClientA', 'pic': 'avatars/ProfilePic_ClientA.jpeg'},
            {'id': 2, 'title': 'Live Recording Review', 'sender': 'EngineerX', 'pic': 'avatars/ProfilePic_EngineerX.jpeg'},
            {'id': 3, 'title': 'Final Master Delivery', 'sender': 'ClientB', 'pic': 'avatars/ProfilePic_ClientB.jpeg'},
        ]
        return render(request, 'messages/dashboard.html', {
            'profile': profile,
            'threads': threads,
            'current_thread': threads[0] if threads else None
        })

    return render(request, 'messages/dashboard.html', {
        'profile': profile,
        'threads': threads,
        'current_thread': threads[0] if threads else None
    })


# 🌍 Public Profile View
def public_profile(request, slug):
    profile = get_object_or_404(UserProfile, slug=slug)

    if request.method == 'POST':
        name = request.POST.get('name', 'Guest')
        email = request.POST.get('email', '')
        content = request.POST.get('message')

        thread = MessageThread.objects.create(profile=profile, name=name, email=email)
        Message.objects.create(thread=thread, content=content, sender='client')

        return redirect('public-profile', slug=slug)

    return render(request, 'profile.html', {'profile': profile})


@login_required
def select_role(request):
    profile, created = UserProfile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        selected_roles = request.POST.getlist('roles')
        # For now, just take the first one (later, expand to support multiple roles)
        profile.role = selected_roles[0] if selected_roles else 'client'
        profile.is_onboarded = True
        profile.save()
        return redirect('messages-dashboard')

    return render(request, 'select_role.html', {'profile': profile})


@login_required
def post_login_redirect(request):
    profile, _ = UserProfile.objects.get_or_create(user=request.user)
    print(f"User: {request.user}")
    print(f"UserProfile: {profile}")
    print(f"Role: {profile.role}")


    if not profile.role or not profile.is_onboarded:
        return redirect('select_role')
    
    return redirect('messages-dashboard')  # Change to your actual dashboard route




# 🏠 Home Page
def home(request):
    return render(request, 'home.html')


# 💬 Messages View (Multi-thread support)
def messages_view(request, thread_id=None):
    threads = MessageThread.objects.filter(users=request.user)
    current_thread = None

    if thread_id:
        current_thread = get_object_or_404(threads, id=thread_id)

    return render(request, 'messages.html', {
        'threads': threads,
        'current_thread': current_thread
    })


# 🔌 API ViewSets
class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class OfferViewSet(viewsets.ModelViewSet):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

#views.py in TEMPLATES