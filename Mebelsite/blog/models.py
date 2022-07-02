from django.db import models

# Create your models here.
class Mebel_turi(models.Model):
    kategoriya = models.CharField(max_length=100)

    def __str__(self):
        return self.kategoriya

class Brand(models.Model):
    brand = models.CharField(max_length=100)

    def __str__(self):
        return self.brand

class Mebel(models.Model):
    kategoriya = models.ForeignKey(Mebel_turi,on_delete=models.CASCADE)
    image = models.ImageField(upload_to="Media/mebel_img")
    mah_nomi = models.CharField(max_length=100)
    narxi = models.CharField(max_length=100)
    description = models.TextField()
    contact = models.CharField(max_length=100)
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE)

    def __str__(self):
        return self.mah_nomi

class OurBrand(models.Model):
    image = models.ImageField(upload_to='Media/brand_img')
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Logo(models.Model):
    image1 = models.ImageField(upload_to='Media/logo_img')
    main_img = models.ImageField(upload_to='Media/main_img')
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Mebelforma(models.Model):
    Ism = models.CharField(max_length=100)
    Tel = models.CharField(max_length=100)
    Manzil = models.CharField(max_length=100)

    def __str__(self):
        return self.Ism