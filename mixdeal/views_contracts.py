from django.shortcuts import render
from django.http import HttpResponse

def statistics_view(request):
    return HttpResponse("📊 Stats coming soon...")


def contracts_view(request):
    dummy_contracts = [
        {
            'song': 'Crazy in Love',
            'artist': 'Beyoncé',
            'date_released': '2003-05-18',
            'deposit_status': 'Paid',
            'attachments': ['crazy_in_love_contract.pdf'],
        },
        {
            'song': 'Halo',
            'artist': 'Beyoncé',
            'date_released': '2008-01-20',
            'deposit_status': 'Pending',
            'attachments': ['halo_contract.pdf'],
        },
    ]
    return render(request, 'contracts.html', {'contracts': dummy_contracts})
