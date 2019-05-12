from django.shortcuts import render
from django.http import HttpResponse
from .models import DataAsli

# Create your views here.
def daftarPenyakitView(request):
    all_data_penyakit = DataAsli.objects.all()
    return render(request, 'daftar-penyakit.html',
        {'all_data': all_data_penyakit})