from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import DataAsli, NamaGejala
from .naiveBayes import naiveBayes

# Create your views here.
def daftarPenyakitView(request):
	all_data_penyakit = DataAsli.objects.all()
	return render(request, 'daftar-penyakit.html',
		{'all_data': all_data_penyakit})

def daftarGejalaView(request):
	daftar_gejala = NamaGejala.objects.all().order_by('gejala')
	return render(request, 'diagnosa.html',
		{'all_data': daftar_gejala})

def cekPenyakit(request):
	# penyakit = NamaPenyakit.objects.all()
	# gejala = NamaGejala.objects.all()
	# pg = PenyakitGejala.objects.all()

	selected = request.POST.getlist('pilihGejala')
	hasil = naiveBayes(selected)
	return render(request, 'hasil-penyakit.html',
		{'all_data': hasil})