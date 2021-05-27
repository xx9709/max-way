from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=124, blank=False, null=False)
    combo = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

class MinImage(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    min_image = models.FileField(upload_to='imoges/', blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True, null=False)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=150, blank=False, null=False)
    price = models.IntegerField(blank=False, null=False)
    image = models.ImageField(upload_to='imoges/', blank=False, null=False)
    min_image = models.ForeignKey(MinImage, blank=True, null=True, on_delete=models.SET_NULL)
    is_hot = models.BooleanField(default=False)
    description = models.TextField(blank=False, null=False)
    category = models.ForeignKey(Category, blank=False, null=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True, null=False)

    def __str__(self):
        return self.name

class Order(models.Model):
    products = models.JSONField(null=False)
    total_price = models.IntegerField(blank=False, null=False)
    status = models.IntegerField(blank=False, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=False)

class Customer(models.Model):
    order = models.ForeignKey(Order, blank=False, null=True, on_delete=models.SET_NULL)
    phone_numer = models.IntegerField(blank=False, null=False)
    first_name = models.CharField(max_length=50, blank=False, null=False)
    last_name = models.CharField(max_length=50, blank=False, null=False)
    pay_type = models.IntegerField(blank=False, null=False)
    adress = models.CharField(max_length=200, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True, null=False)

    def __str__(self):
        return self.first_name


