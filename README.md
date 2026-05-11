1.python manage.py shell:
from products.services import create_product
from products.models import Product

print(f"Başlanğıc sayı: {Product.objects.count()}")

try:
   create_product("Xarab",  "Test",  -10)
except ValueError as e:
      print(f"Xeta tutuldu: {e}")

print(f"Yekun sayi: {Product.objects.count()}")

Qeyd: Eger qiymeti menfi daxil etsez artim olmayacaq yeni count artmayacaq. 
