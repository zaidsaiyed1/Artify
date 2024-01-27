from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('admin_panel/',views.admin_panel,name='admin_panel'),
    path('signup/',views.signup, name='signup'),
    path('login/',views.login, name='login'),
    path('signupuser/',views.signupuser, name='signupuser'),
    path('signupforAA/',views.signupforAA, name='signupforAA'),
    path('signupforAM/',views.signupforAM, name='signupforAM'),
    path('signinpage/',views.signinpage, name='signinpage'),
    path('loginuser/',views.loginuser, name='loginuser'),
    path('test/',views.test, name='test'),
    path('edit/<str:Customer_username>/',views.edit, name='edit'),
    path('update/<str:Customer_username>',views.update, name='update'),
    path('delete/',views.delete, name='delete'),
    path('destroy/<str:Customer_username>',views.destroy, name='destroy'),
    path('verification/',views.verification, name='verification'),
    path('signupforAA/',views.signupforAA, name='signupforAA'),
    path('signupuserforArtist/',views.signupuserforArtist, name='signupuserforArtist'),
    path('signupuserforartgallerymanager/',views.signupuserforartgallerymanager, name='signupuserforartgallerymanager'),
]

