from django.shortcuts import render
from .models import Magazen


def welcome(request):
    context = {
        'magazens': Magazen.objects.all()
    }
    return render(request, 'main/welcome.html', context)


def magazens_view(request):
    magazens = Magazen.objects.all()
    return render(request, 'main/magazens.html', {'magazens': magazens})


def detail_view(request, magazen_id):
    magazen = Magazen.objects.get(id=magazen_id)
    return render(request, 'main/detail.html', {'magazen': magazen})


def about(request):
    return render(request, 'main/about.html')


def jurnals_view(request):
    return None


def jurnal_view(request):
    return None


def gazetas_view(request):
    return None


def gazeta_view(request):
    return None


def maqolas_view(request):
    return None


def maqola_view(request):
    return None