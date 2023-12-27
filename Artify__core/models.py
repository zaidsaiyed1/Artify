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
   Artist_idProof = models.IntegerField(null=False)
   Artist_contact_no = models.IntegerField(null=False)

class Meta:
   db_table = "Artist_table"