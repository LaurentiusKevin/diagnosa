from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def daftarPenyakitView(request):
    return render(request, 'daftar-penyakit.html')