from django.db import models

# Create your models here.

# class Kategori(models.Model):
#     kategori_adi = models.CharField(max_length=50)

#     def __str__(self):
#         return self.kategori_adi
    

    


class Urun(models.Model):
    urun_adi = models.CharField(max_length=50)
    urun_aciklamasi = models.CharField(max_length=100)
    urun_fotografi = models.CharField(max_length=500)
    urun_kategorisi = models.CharField(max_length=50)
    # urun_kategorisi = models.ForeignKey(Kategori, on_delete=models.CASCADE, null=True)
    #* on_delete=models.CASCADE yaptığımda o kategori silinirse ona ait olan urunde silinir

    def __str__(self):
        return self.urun_adi
    