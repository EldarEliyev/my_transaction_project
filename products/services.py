from django.db import transaction
from .models import Product

def create_product(name, description, price):
    with transaction.atomic():
        if price < 0:
            raise ValueError("Qiymət mənfi ola bilməz!")
        
        product = Product.objects.create(
            name=name, 
            description=description, 
            price=price
        )
        return product