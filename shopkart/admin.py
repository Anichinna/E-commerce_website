from django.contrib import admin

from shopkart.models import Catagory
from shopkart.models import Product
from shopkart.models import Cart
from shopkart.models import Favourite

admin.site.register(Catagory)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Favourite)