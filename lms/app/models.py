from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    forgot_password_token=models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.user.username
class Laundry(models.Model):
    L_TYPE=(
        ('WASH_IRON','Wash and Iron'),
        ('DRY_CLEAN','Dry Clean'),
        ('WASH','Wash'),
        ('IRON','Iron'),
    )
    WEAR_TYPE=(
        ('SHIRT','Shirt'),
        ('PANT','Pant'),
        ('SAREE','Saree'),
        ('TOWEL','Towel'),
        ('BED_SHEET','Bed Sheet'),
        ('BLANKET','Blanket'),
        ('CURTAIN','Curtain'),
        ('CARPET','Carpet'),
        ('OTHERS','Others'),
    )
    name=models.CharField(max_length=100)
    email=models.EmailField(null=True,blank=True)
    phone=models.IntegerField()
    address=models.CharField(max_length=100)
    pick_date=models.DateField()
    pick_time=models.TimeField()
    quantity=models.IntegerField()
    wear_type=models.CharField(max_length=100,choices=WEAR_TYPE)
    loundery_type=models.CharField(max_length=100,choices=L_TYPE)
    def __str__(self):
        return f'{self.wear_type} - {self.loundery_type}-{self.name}'

class Price(models.Model):
    WEAR_TYPE=(
        ('SHIRT','Shirt'),
        ('PANT','Pant'),
        ('SAREE','Saree'),
        ('TOWEL','Towel'),
        ('BED_SHEET','Bed Sheet'),
        ('BLANKET','Blanket'),
        ('CURTAIN','Curtain'),
        ('CARPET','Carpet'),
        ('OTHERS','Others'),
    )
    L_TYPE=(
        ('WASH_IRON','Wash and Iron'),
        ('DRY_CLEAN','Dry Clean'),
        ('WASH','Wash'),
        ('IRON','Iron'),
    )
    wear_type=models.CharField(max_length=100,choices=WEAR_TYPE)
    loundery_type=models.CharField(max_length=100,choices=L_TYPE)
    price=models.IntegerField()
    def __str__(self):
        return f'{self.wear_type} - {self.loundery_type} - {self.price}'
    
class Status(models.Model):
    status=(
        ('PENDING','Pending'),
        ('ACCEPTED','Accepted'),
        ('REJECTED','Rejected'),
        ('COMPLETED','Completed'),

    )
    laund=models.ForeignKey(Laundry,on_delete=models.CASCADE)
    status=models.CharField(max_length=100,choices=status,default='PENDING')
    def __str__(self):
        return f'{self.laund.id} - {self.status}'