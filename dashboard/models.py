from django.db import models
from django.contrib.auth.models import User

# Create your models here.
CATEGORY = (
    ('Plywood','Plywood'),
    ('Hardware','Hardware'),
    ('cetring','cetring'),
    ('PUC','PUC'),
    ('machinery','machinery'),
)
class Supplier(models.Model):
    supplier_name = models.CharField(max_length=100, null=True)
    supplier_product =models.CharField(max_length=20, null=True)
    category = models.CharField(max_length=20, choices=CATEGORY, null=True)
    supplier_quantity = models.PositiveBigIntegerField(null=True)
    
    class Meta:
        verbose_name_plural = 'Supplier'
        
    def __str__(self):
        return f'{self.supplier_name}--{self.supplier_product}'

class Product(models.Model):
    product_name = models.CharField(max_length=100, null=True)
    category = models.CharField(max_length=20, choices=CATEGORY, null=True)
    quantity = models.PositiveBigIntegerField(null=True)
  
    class Meta:
        verbose_name_plural = 'Product'  # in admin panel change the product table name

    def __str__(self):
        return f'{self.product_name}--{self.quantity}' # show the product name and quantity in djngo admin side product table

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    staff = models.ForeignKey(User, models.CASCADE, null=True)
    order_quantity = models.PositiveBigIntegerField(null=True)
    date = models.DateTimeField (auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Order' # in admin panel change the order table name

    def __str__(self):
        return f'{self.product} orderd by  {self.staff.username}'
    
 # show the product name and quantity in djngo admin side product table