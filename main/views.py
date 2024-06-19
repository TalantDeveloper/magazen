from django.shortcuts import render
from .models import Magazen


def welcome(request):
    context = {
        'magazens': Magazen.objects.all()
    }
    return render(request, 'main/welcome.html', context)


def detail_view(request, magazen_id):
    magazen = Magazen.objects.get(id=magazen_id)
    return render(request, 'main/detail.html', {'magazen': magazen})


def about(request):
    return render(request, 'main/about.html')
