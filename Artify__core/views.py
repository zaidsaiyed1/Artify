from django.shortcuts import redirect, render
from . models import *
# Create your views here.
def admin_panel(request):
     artist = Artist.objects.all()
     customer = Customer.objects.all()
     admin=Admin.objects.all()
     artgallerymanager = ArtGalleryManager.objects.all()
     return render(request,'templates/admin.html',{'artist':artist,'customer':customer,'admin':admin,'artgallerymanager': artgallerymanager})

def signup(request):
     return render(request,'templates/signup.html',{})
def signupforAA(request):
     return render(request,'templates/signupforAA.html',{})

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
       
       
     return redirect('signinpage')

def loginuser(request):
     if request.method == 'POST': 
      lusername = request.POST['username']
      lpassword = request.POST['password']
          
      user_exists = Customer.objects.filter(Customer_username=lusername, Customer_password=lpassword).exists() 
    
     if user_exists:
       return redirect('verification')
     else:
       return redirect('test')
      
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
    return redirect('delete')