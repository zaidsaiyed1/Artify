import os
from random import randint, random
from django.shortcuts import redirect, render
from . models import *
from django.contrib.auth import *
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .serializer import *
from django.core.mail import send_mail
class loginAPIview(APIView):
    def post(self,request):
        try:
            data = request.data
            serializer = loginserializer(data=data)
            if serializer.is_valid():
                username = serializer.data['username']
                password = serializer.data['password']
                user = authenticate(username = username, password=password)
                if user is None:
                       return Response({
                       'status': 400,
                       'message':'Check the details',
                       'data': {}
                        })
                refresh = RefreshToken.for_user(user)  
 
                return {
               'refresh': str(refresh),
               'access': str(refresh.access_token),
              }

            return Response({
                'status': 400,
                'message':'Check the details',
                'data': serializer.error
            })
        
        except Exception as e:
            print(e)
          

def send_mail_to_verify(request,semail):
      no = randint(1000,9999)
      subject = "Email verification for your account"
      message = "Your otp is "+ str(no)
      from_email = settings.EMAIL_HOST_USER
      recipient_list = [semail]
      send_mail(subject=subject,message=message,from_email=from_email,recipient_list=recipient_list)

def send_mail_to_client(request,semail):
              subject = "Congratulation ! for signup into Artify"
              message = "Welcome to the Artify. The world of ART"
              from_email = settings.EMAIL_HOST_USER
              recipient_list  = [semail]
              send_mail(subject=subject,message=message,from_email=from_email,recipient_list=recipient_list)
              send_mail_to_verify(request,semail)

def index(request):
     productindex = Product.objects.all()
     return render(request,'templates/index.html',{'productindex':productindex})

def indexcustomer(request,Customer_username):
     customer = Customer.objects.get(Customer_username=Customer_username)
     return render(request,'templates/indexcustomer.html',{'customer':customer})

def admin_panel(request,Admin_username):
     admin = Admin.objects.get(Admin_username=Admin_username)
     artist = Artist.objects.last()
     customer=Customer.objects.last()
     admin=Admin.objects.last()
     artgallerymanager = ArtGalleryManager.objects.last()
     product = Product.objects.all()
     productTotal = Product.objects.count()
     customerTotal = Customer.objects.count()
     artistTotal = Artist.objects.count()
     artgallerymanagerTotal = ArtGalleryManager.objects.count()
     adminTotal = Admin.objects.count()
     event = Event.objects.last()
     userTotal  = customerTotal + artistTotal + artgallerymanagerTotal + adminTotal
     return render(request,'templates/admin.html',{'admin':admin,'artist':artist,'customer':customer,'admin':admin,'artgallerymanager': artgallerymanager,'product':product,'productTotal':productTotal,'userTotal':userTotal,'event':event    })

def signup(request):
     return render(request,'templates/signup.html',{})


def signupforAA(request):
     return render(request,'templates/signupforAA.html',{})

def signupforAM(request):
     return render(request,'templates/signupforAM.html',{})

def login(request):
     return render(request,'templates/login.html',{})

def signinpage(request):
     return render(request,'templates/signinpage.html',{})

def verification(request):
    return render(request,'templates/varification.html',{})

def delete(request):
    return render(request, 'templates/delete.html',{})

def userpageforadmin(request):
     artist = Artist.objects.all()
     customer=Customer.objects.all()
     admin=Admin.objects.all()
     artgallerymanager = ArtGalleryManager.objects.all()
     return render(request,'templates/user.html',{'artist':artist,'customer':customer,'admin':admin,'artgallerymanager': artgallerymanager})
def signupuser(request):
     if request.method == 'POST':
       sname = request.POST['name'];
       susername = request.POST['username'];
       semail = request.POST['email'];
       spassword = request.POST['password'];
       scontact = request.POST['contact'];
       user = Customer(Customer_name=sname,Customer_username = susername, Contact_no=scontact,Customer_Email=semail,Customer_password=spassword);
       
       if Customer.objects.filter(Customer_name=sname,Customer_username=susername,Customer_Email=semail,Contact_no=scontact).exists():
            messages.error(request,'The user is already register with the same detaiils')
            return redirect('signup')
       elif Customer.objects.filter(Customer_name=sname).exists():
            messages.error(request,'Name is already taken!')
            return redirect('signup')
       elif Customer.objects.filter(Customer_Email=semail).exists():
            messages.error(request,'Email is already register!')
            return redirect('signup')
       elif  Customer.objects.filter(Customer_username=susername).exists():
            messages.error(request,'The username is already taken!')
            return redirect('signup')
       else:
        user.save();
        send_mail_to_client(request,semail)
        messages.success(request,'Your account has been created!')
        #return redirect('signup')
       #authenticate(request,username=susername,password=spassword,email=semail)
     return indexcustomer(request,susername)
 
def loginuser(request):
     cust = False
     if request.method == 'POST': 
      lusername = request.POST['username']
      lpassword = request.POST['password']
      if Customer.objects.filter(Customer_username=lusername, Customer_password=lpassword).exists():     
         return indexcustomer(request,lusername)
      elif Artist.objects.filter(Artist_username=lusername, Artist_pass=lpassword).exists():
         return artist_panel(request,Artist_username=lusername)
      elif ArtGalleryManager.objects.filter(Username=lusername,password=lpassword).exists():
          return redirect('index')
      elif Admin.objects.filter(Admin_username=lusername,Admin_pass=lpassword):
           return admin_panel(request,Admin_username=lusername)  
      else:
          return redirect('login')
 
def edit(request,Customer_username):
     customer = Customer.objects.get(Customer_username=Customer_username)  
     return render(request,'templates/edit.html', {'Customer':customer})
      
def update(request, Customer_username):  
       dataget = Customer.objects.get(Customer_username = Customer_username)
       data = Customer.objects.filter(Customer_username=Customer_username)
       if request.method == "POST":
          uname = request.POST['name'];
          uusername = request.POST['username'];
          uemail = request.POST['email'];
          upassword = request.POST['password'];
          ucontact = request.POST['contact'];
          dataget.Customer_name = uname
          dataget.Customer_username = uusername
          dataget.Customer_Email = uemail
          dataget.Customer_password = upassword
          dataget.Contact_no = ucontact
          dataget.save()
          
          return redirect('login')  
       return render(request, 'templates/edit.html', {'Customer': data})  

def destroy(request, Customer_username):
    dataget = Customer.objects.get(Customer_username=Customer_username)
    dataget.delete()
    return redirect('login')

def artist_panel(request,Artist_username):
      artist = Artist.objects.get(Artist_username=Artist_username)
      product = Product.objects.filter(Artist_id = artist.Artist_id)
      return render(request,'templates/artist.html',{'artist':artist,'product':product})

def signupuserforArtist(request):
     if request.method == 'POST':
       Arname = request.POST['name'];
       Arusername = request.POST['username'];
       Aremail = request.POST['email'];
       Arpassword = request.POST['password'];
       Aidproof = request.POST['id_proof'];
       Arcontact = request.POST['contact'];
       userArtist = Artist(Artist_name=Arname,Artist_username = Arusername,Artist_pass=Arpassword,Artist_email=Aremail,Artist_idProof=Aidproof, Artist_contact_no=Arcontact);
       userArtist.save();
     
     return redirect('login')

def editArtist(request,Artist_username):
     artist = Artist.objects.get(Artist_username=Artist_username)  
     return render(request,'templates/editArtist.html', {'artist':artist})
      
def updateArtist(request, Artist_username):  
       dataget = Artist.objects.get(Artist_username = Artist_username)
       data = Artist.objects.filter(Artist_username=Artist_username)
       if request.method == "POST":
          uname = request.POST['name'];
          uusername = request.POST['username'];
          uemail = request.POST['email'];
          upassword = request.POST['password'];
          ucontact = request.POST['contact'];
          uidproof = request.POST['id_proof']
          dataget.Artist_name = uname
          dataget.Artist_username = uusername
          dataget.Artist_email = uemail
          dataget.Artist_pass = upassword
          dataget.Artist_contact_no = ucontact
          dataget.Artist_idProof = uidproof
          dataget.save();
          
          return artist_panel(request,uusername) 
       return render(request, 'templates/editArtist.html', {'artist': data})  

def destroyArtist(request, Artist_username):
    dataget = Artist.objects.get(Artist_username=Artist_username)
    dataget.delete()
    return redirect('login')
def signupuserforartgallerymanager(request):
     if request.method == 'POST':
       Amname = request.POST['name'];
       Amusername = request.POST['username'];
       Amemail = request.POST['email'];
       Ampassword = request.POST['password'];
       Amcontact = request.POST['contact'];
       Amidproof = request.POST['id_proof'];
       user = ArtGalleryManager(Name=Amname, Contact_no=Amcontact,Username = Amusername,Email=Amemail,id_proof=Amidproof,password=Ampassword);
       user.save(); 
     return redirect('login')

def editArtGalleryManager(request,Username):
     artgallerymanager = ArtGalleryManager.objects.get(Username=Username)  
     return render(request,'templates/editArtgallerymanager.html', {'artgallerymanager':artgallerymanager})
      
def updateArtGalleryManager(request, Username):  
       dataget = ArtGalleryManager.objects.get(Username = Username)
       data = ArtGalleryManager.objects.filter(Username=Username)
       if request.method == "POST":
          uname = request.POST['name'];
          uusername = request.POST['username'];
          uemail = request.POST['email'];
          upassword = request.POST['password'];
          ucontact = request.POST['contact'];
          uidproof = request.POST['id_proof']
          dataget.Name = uname
          dataget.Username = uusername
          dataget.Email = uemail
          dataget.password = upassword
          dataget.Contact_no = ucontact
          dataget.id_proof = uidproof
          dataget.save();
          
          return redirect('/admin_panel')  
       return render(request, 'templates/editArtgallerymanager.html', {'artgallerymanager':data})  

def destroyArtGalleryManager(request, Username):
    dataget = ArtGalleryManager.objects.get(Username=Username)
    dataget.delete()
    return redirect('admin_panel')

def productsPageforAdmin(request):
     products = Product.objects.all()
     return render(request,'templates/product.html',{'products':products})

def AddProduct(request,Artist_id):
     artist = Artist.objects.get(Artist_id=Artist_id)
     return render(request,'templates/Addproduct.html',{'artist':artist})

def addProduct(request,Artist_id):
      artist = Artist.objects.get(Artist_id=Artist_id)
      if request.method == "POST":
       pname = request.POST['name'];
       pdescription = request.POST['description'];
       product_weight = request.POST['weight'];
       #pArtist_id = request.POST['Artist_id'];
       #if len(request.FILES) !=0:
       ppicture = request.FILES['picture'];
       pprice = request.POST['price'];
       #Artist_id = request.POST['Artist_id'];
       user = Product(Name=pname,Description=pdescription,Weight=product_weight,Price=pprice,Artist_id=artist,Picture=ppicture)     
       user.save();
       return artist_panel(request,artist.Artist_username)
       
def editProduct(request,Product_id):
     product = Product.objects.get(Product_id=Product_id)
     return render(request,'templates/editpr.html',{'product':product})

def updateProduct(request,Product_id):
       dataget = Product.objects.get(Product_id=Product_id)
       data = Product.objects.filter(Product_id=Product_id)
       if request.method == "POST":

          pname = request.POST['name'];
          pdescription = request.POST['description'];
          product_weight = request.POST['weight'];
          if len(request.FILES) !=0:
           if len(dataget.Picture)>0:
                os.remove(dataget.Picture.path)
                ppicture = request.FILES['picture'];
          pprice = request.POST['price'];
          dataget.Name = pname
          dataget.Description = pdescription
          dataget.Weight = product_weight
          if len(request.FILES) !=0:
           if len(dataget.Picture)>0:
                os.remove(dataget.Picture.path)
           dataget.Picture = ppicture
          dataget.Price = pprice
          dataget.save();
          return redirect('login')  
       return render(request, 'templates/editpr.html', {'product':data}) 

def destroyProduct(request,Product_id):
     productdestroy = Product.objects.get(Product_id=Product_id)
     productdestroy.delete()
     return redirect('login')

def eventspageforadmin(request):
     events = Event.objects.all()
     return render(request,'templates/events.html',{'events':events})

def orderpageforadmin(request):
     order = Order.objects.all()
     return render(request,'templates/order.html',{'order':order})

def displayproducts(request):
     product = Product.objects.all()
     return render(request,'templates/productList.html',{'product':product})

def productsListPageForArtist(request,Artist_id):
    artist = Artist.objects.get(Artist_id=Artist_id)
    products = Product.objects.filter(Artist_id=Artist_id)
    return render(request,'templates/productsPageForArtist.html',{'products':products,'artist':artist})

def AddCustomerForAdmin(request):
     return render(request,'templates/Addcustomer.html',{})

def AddArtistForAdmin(request):
     return render(request,'templates/Addartist.html',{})

def AddArtgallerymanagerForAdmin(request):
     return render(request,'templates/Addmanager.html',{})

def cart(request):
     return render(request,'templates/cart.html',{})

def notificationforartist(request):
     return render(request,'templates/notification.html',{})

def comunicatewithmanagerforartist(request):
     return render(request,'templates/comunicatewithmanager.html',{})

def bookslotsforartist(request):
     return render(request,'templates/blockslots.html',{}) 
def managehistoryforartist(request):
     return render(request,'templates/managerhistory.html',{})

def managestockforartist(request):
     return render(request,'templates/managestock.html',{})

def managepaymentforartist(request):
     return render(request,'templates/managepayment.html',{})

def artistprofile(request,Artist_username):
     artist = Artist.objects.get(Artist_username=Artist_username)
     return render(request,'templates/profile.html',{'artist':artist})

def customerprofile(request,Customer_username):
     customer = Customer.objects.get(Customer_username=Customer_username)
     return render(request,'templates/profile2.html',{'customer':customer})

def adminprofile(request,Admin_username):
     admin = Admin.objects.get(Admin_username=Admin_username)
     return render(request,'templates/profileadmin.html',{'admin':admin})

def order(request,Customer_username):
    customer = Customer.objects.get(Customer_username=Customer_username)
    product = Product.objects.get(Product_id=customer)
    order = Order.objects.filter(Customer_id = customer,Product_id=product)
    return render(request,'templates/cart.html',{'Order':order})