from django.db import models

# Create your models here.
class Admin(models.Model):
   Admin_id = models.BigAutoField(primary_key=True)
   Admin_username = models.CharField(max_length=20,null=False)
   Admin_name = models.CharField(max_length=10, null=False)
   Admin_pass = models.TextField(max_length=10, null=False)
   Admin_email = models.EmailField(null=False)

class Meta:
   db_table = "Admin_table"

class Artist(models.Model):
   Artist_id = models.BigAutoField(primary_key=True)
   Artist_name = models.CharField(max_length=50,null=False)
   Artist_username = models.CharField(max_length=40,null=False)
   Artist_pass = models.TextField(max_length=25, null=False)
   Artist_email = models.EmailField(null=False)
   Artist_idProof = models.ImageField(null=False)
   Artist_contact_no = models.IntegerField(null=False)

class Meta:
   db_table = "Artist_table"

class ArtGalleryManager(models.Model):
   Manager_id = models.BigAutoField(primary_key=True)
   Name = models.CharField(max_length=10, null = False)
   Contact_no = models.IntegerField(null = False)
   Username = models.CharField(max_length=40,null = False)
   Email = models.EmailField(null = False)
   id_proof = models.ImageField(null = False)

class Meta:
   db_table="ArtGalleryManager"

class Customer(models.Model):
   Customer_id = models.BigAutoField(primary_key=True)
   Customer_name = models.CharField(max_length=10,null = False)
   Contact_no = models.IntegerField(null = False)
   Customer_Email = models.EmailField(null = False)
   Customer_idProof = models.ImageField(null = False)

class Meta:
   db_table = 'Customer'

class Event(models.Model):
   Event_id = models.BigAutoField(primary_key=True)
   Event_name = models.CharField(max_length=10,null = False)
   Event_time = models.TimeField(null = False)
   Event_date = models.DateField(null = False)
   Event_venue = models.CharField(max_length=30,null = False)
   Event_capacity = models.IntegerField(null = False)

class Meta:
   db_table = 'Event'

class Product(models.Model):
   Product_id = models.BigAutoField(primary_key=True)
   Name = models.CharField(max_length=30,null = False)
   Description = models.CharField(max_length=50,null = False)
   Weight = models.FloatField(max_length=10,null = False)
   Price = models.IntegerField(null = False)
   Artist_id = models.ForeignKey(Artist,on_delete=models.CASCADE)
   Picture = models.ImageField(null = False)

class Meta:
   db_table='Product'

class Order(models.Model):
   Order_id = models.BigAutoField(primary_key=True, null=False)
   OrderNo = models.IntegerField(null=False)
   Order_Amount = models.IntegerField(null=False)
   Order_Date = models.DateField(null=False)
   Order_quantity = models.IntegerField(null=False)
   Product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
   Customer_id = models.ForeignKey(Customer,on_delete=models.CASCADE)

class Meta:
   db_table = 'Order'