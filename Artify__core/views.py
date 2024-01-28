from django.shortcuts import redirect, render
from . models import *
# Create your views here.
def admin_panel(request):
     artist = Artist.objects.all()
     customer=Customer.objects.all()
     admin=Admin.objects.all()
     artgallerymanager = ArtGalleryManager.objects.all()
     return render(request,'templates/admin.html',{'artist':artist,'customer':customer,'admin':admin,'artgallerymanager': artgallerymanager})

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

def test(request):
     return render(request,'templates/test.html',{})

def verification(request):
    return render(request,'templates/varification.html',{})

def delete(request):
    return render(request, 'templates/delete.html',{})

def signupuser(request):
     if request.method == 'POST':
       sname = request.POST['name'];
       susername = request.POST['username'];
       semail = request.POST['email'];
       spassword = request.POST['password'];
       scontact = request.POST['contact'];
       user = Customer(Customer_name=sname,Customer_username = susername, Contact_no=scontact,Customer_Email=semail,Customer_password=spassword);
       user.save();
     return redirect('login')
 
def loginuser(request):
     if request.method == 'POST': 
      lusername = request.POST['username']
      lpassword = request.POST['password']
      if Customer.objects.filter(Customer_username=lusername, Customer_password=lpassword).exists():     
        return redirect('admin_panel')
      elif Artist.objects.filter(Artist_username=lusername, Artist_pass=lpassword).exists():
         return redirect('admin_panel')
      elif ArtGalleryManager.objects.filter(Username=lusername,password=lpassword).exists():
          return redirect('admin_panel')
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
          
          return redirect('/admin_panel')  
       return render(request, 'templates/edit.html', {'Customer': data})  

def destroy(request, Customer_username):
    dataget = Customer.objects.get(Customer_username=Customer_username)
    dataget.delete()
    return redirect('admin_panel')

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
          
          return redirect('/admin_panel')  
       return render(request, 'templates/editArtist.html', {'artist': data})  

def destroyArtist(request, Artist_username):
    dataget = Artist.objects.get(Artist_username=Artist_username)
    dataget.delete()
    return redirect('admin_panel')
def signupuserforartgallerymanager(request):
     if request.method == 'POST':
       Amname = request.POST['name'];
       Amusername = request.POST['username'];
       Amemail = request.POST['email'];
       Ampassword = request.POST['password'];
       Amcontact = request.POST['contact'];
       Amidproof = request.POST['id_proof']
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