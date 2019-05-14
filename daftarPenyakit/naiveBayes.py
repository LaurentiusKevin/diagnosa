from .models import NamaPenyakit, NamaGejala, PenyakitGejala
from operator import itemgetter
# from django.db.models import Count

def naiveBayes(data):
  listPenyakit = NamaPenyakit.objects.all()
  listGejala = NamaGejala.objects.all()
  penyakit_gejala = PenyakitGejala.objects.all()

  input_gejala = data
  n = 1
  p = n / listPenyakit.count()
  m = listGejala.count()
  ncGejala = 0

  nilai_penyakit = []
  for peny in listPenyakit:
    hasil = []
    idGejala = []
    filterGejala = penyakit_gejala.filter(penyakit = peny.id)
    for fg in filterGejala:
      idGejala.append(fg.gejala)

    for ig in input_gejala:
      if ig in idGejala:
        nilaiP = 0
        # Nilai Nc
        nc = 1
        ncGejala += 1
        # Menghitung Nilai P(Ai | Vj) dan menghitung nilai P(Vj)
        nilaiP = (nc + (m * p)) / (n + m)
        # SIMPAN
        hasil.append(nilaiP)
      else:
        nilaiP = 0
        # Nilai Nc
        nc = 0
        # Menghitung Nilai P(Ai | Vj)
        nilaiP = (nc + (m * p)) / (n + m)
        # SIMPAN
        hasil.append(nilaiP)
    
    # Menghitung P(Ai | Vj) * P(Vj)
    totalHasil = 0
    for hsl in hasil:
      if totalHasil == 0:
        totalHasil = hsl
      else:
        totalHasil *= hsl
    nilaiAkhir = p * totalHasil
    dataHasil = {
      'penyakit': peny.penyakit,
      'nilai': nilaiAkhir,
      'total_gejala': filterGejala.count(),
      'total_ada': ncGejala
    }
    nilai_penyakit.append(dataHasil)
  
  sorting = sorted(nilai_penyakit, key=itemgetter('nilai'), reverse=True)
  return sorting