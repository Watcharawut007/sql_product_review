from review_production.models import *

def run():
    product.objects.all().delete()