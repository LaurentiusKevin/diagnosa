from django.db import models

# Create your models here.
class DataAsli(models.Model):
    penyakit = models.TextField()
    gejala = models.TextField()

class NamaPenyakit(models.Model):
    penyakit = models.TextField()

class NamaGejala(models.Model):
    gejala = models.TextField()

class PenyakitGejala(models.Model):
    penyakit = models.ForeignKey(NamaPenyakit, on_delete=models.PROTECT)
    gejala = models.ForeignKey(NamaGejala, on_delete=models.PROTECT)

    def __str__(self):
        return self.penyakit