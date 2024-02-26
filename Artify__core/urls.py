from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.index, name='index'),
    path('admin_panel/',views.admin_panel,name='admin_panel'),
    path('signup/',views.signup, name='signup'),
    path('login/',views.login, name='login'),
    path('signupuser/',views.signupuser, name='signupuser'),
    path('signupforAA/',views.signupforAA, name='signupforAA'),
    path('signupforAM/',views.signupforAM, name='signupforAM'),
    path('signinpage/',views.signinpage, name='signinpage'),
    path('loginuser/',views.loginuser, name='loginuser'),
    path('edit/<str:Customer_username>/',views.edit, name='edit'),
    path('editArtist/<str:Artist_username>/',views.editArtist, name='editArtist'),
    path('editArtGalleryManager/<str:Username>/',views.editArtGalleryManager, name='editArtGalleryManager'),
    path('editProduct/<int:Product_id>/',views.editProduct, name='editProduct'),
    path('update/<str:Customer_username>',views.update, name='update'),
    path('updateArtist/<str:Artist_username>',views.updateArtist, name='updateArtist'),
    path('updateArtGalleryManager/<str:Username>',views.updateArtGalleryManager, name='updateArtGalleryManager'),
    path('updateProduct/<int:Product_id>',views.updateProduct, name='updateProduct'),
    path('delete/',views.delete, name='delete'),
    path('destroy/<str:Customer_username>',views.destroy, name='destroy'),
    path('destroyArtist/<str:Artist_username>',views.destroyArtist, name='destroyArtist'),
    path('destroyArtGalleryManager/<str:Username>',views.destroyArtGalleryManager, name='destroyArtGalleryManager'),
    path('signupforAA/',views.signupforAA, name='signupforAA'),
    path('signupuserforArtist/',views.signupuserforArtist, name='signupuserforArtist'),
    path('signupuserforartgallerymanager/',views.signupuserforartgallerymanager, name='signupuserforartgallerymanager'),
    path('mail',views.send_mail_to_client,name="mail"),
    path('mail',views.send_mail_to_verify,name="mail"),
    path('userpageforadmin/',views.userpageforadmin,name='userpageforadmin'),
    path('eventspageforadmin/',views.eventspageforadmin,name='eventspageforadmin'),
    path('products/',views.products,name='products'),
    path('orderpageforadmin/',views.orderpageforadmin,name='orderpageforadmin'),
    path('loginAV',views.loginAPIview.as_view(),name='loginAV'),
    path('artist_panel/<str:Admin_username>/',views.artist_panel,name='artist_panel'),
    path('displayproducts/',views.displayproducts,name='displayproducts'),
    path('productsListPageForArtist/<int:Artist_id>/',views.productsListPageForArtist,name='productsListPageForArtist'),
    

    
]

