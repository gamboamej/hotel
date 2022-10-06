from django.shortcuts import render
from .models import *
from django.conf import settings

def index(request):
    lst_forma_pago      = i002t_forma_pago.objects.filter(in_activo=True)
    data = {'MONEDA_PAIS': settings.MONEDA_MONEDERO_PRATAPO,'lst_forma_pago': lst_forma_pago}
    return render(request, 'formapago/index.html',data)
