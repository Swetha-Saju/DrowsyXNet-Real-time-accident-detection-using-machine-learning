from django.db import models

# Create your models here.

class Register(models.Model):
    name=models.CharField(max_length=100,null=True,blank=True)
    email=models.CharField(max_length=100,unique=True)
    GENDER_CHOICES = [
        ('M','male'),
        ('F','female'),
        ('O','other'),
    ]
    gender=models.CharField( max_length=1,choices=GENDER_CHOICES,null=True,blank=True)
    password=models.CharField(max_length=100,null=True,blank=True)
    STATE_CHOICES= [
        ('K','kerala'),
        ('KA','karnataka'),
        ('T','tamilnadu'),
        ('O','other'),
    ]
    state=models.CharField(max_length=2,choices=STATE_CHOICES,null=True,blank=True)
    
    age=models.IntegerField(null=True,blank=True)
    phone_no=models.IntegerField(null=True,blank=True)
    licenceno=models.CharField(max_length=50,null=True,blank=True)
    image=models.FileField(upload_to='image/',null=True,blank=True)
    

class Vehicle(models.Model):
    VEHICLE_TYPES = [
        ('Taxi', 'Taxi'),
        ('Truck', 'Truck'),
        ('Other', 'Other'),
    ]

    STATUS_CHOICES = [
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
        ('Maintenance', 'Maintenance'),
    ]

    vehicle_number = models.CharField(max_length=50,null=True, blank=True)
    vehicle_name = models.CharField(max_length=100, null=True, blank=True)
    vehicle_type = models.CharField(max_length=20, choices=VEHICLE_TYPES, null=True, blank=True)
    capacity = models.PositiveIntegerField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Active')
    image = models.ImageField(upload_to='vehicle_images/', null=True, blank=True)
    
    
class Driver(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    photo = models.ImageField(upload_to='driver_photos/', null=True, blank=True)
    license_number = models.CharField(max_length=50, null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    experience = models.PositiveIntegerField(null=True, blank=True)
    
    STATUS_CHOICES = [
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Active')

    def __str__(self):
        return self.name or "Unnamed Driver"


class Upload_documents(models.Model):
       name = models.CharField(max_length=100, null=True, blank=True)
       description = models.TextField(max_length=100, null=True, blank=True)
       uploaded_at = models.DateField(auto_now_add=True)
       uploaded_documents = models.FileField(upload_to='documents/', null=True, blank=True)

class Notification(models.Model):
     message = models.TextField(max_length=200, null=True, blank=True)
     date = models.DateField(auto_now_add=True)
      
       

   
   