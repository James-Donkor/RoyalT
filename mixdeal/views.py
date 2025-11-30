from django.contrib.auth.views import LoginView
from django.shortcuts import render, get_object_or_404
from api.models import MessageThread
from django.shortcuts import render



class CustomLoginView(LoginView):
    template_name = 'login.html'
    next_page = '/select-role/' # ✅ this ensures it works

    

def messages_view(request, thread_id=None):
    threads = MessageThread.objects.filter(users=request.user)
    current_thread = None
    


    if thread_id:
        current_thread = get_object_or_404(threads, id=thread_id)

    return render(request, 'messages.html', {
        'threads': threads,
        'current_thread': current_thread
    })


def browse_view(request):
    return render(request, 'browse.html')


def contracts_view(request):
    dummy_contracts = [
        {
            'song': 'Crazy in Love',
            'artist': 'Beyoncé',
            'date_released': '2003-05-18',
            'deposit_status': 'Paid',
            'attachments': ['crazy_in_love_contract.pdf'],
        },
        # You can add more test rows here
    ]
    return render(request, 'contracts.html', {'contracts': dummy_contracts})

#views.py in mixdeal\
