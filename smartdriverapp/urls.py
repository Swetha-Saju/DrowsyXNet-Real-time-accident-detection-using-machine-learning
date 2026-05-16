from django.urls import path
from .import views


urlpatterns=[
    path('',views.index,name="index"),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('home/',views.home,name='home'),
    path('profile/',views.profile,name='profile'),
    path('editprofile/',views.editprofile,name='editprofile'),
    path('adminlogin/',views.adminlogin,name='adminlogin'),
    path('adminhome/',views.adminhome,name='adminhome'),
    path('userlist/',views.userlist,name='userlist'),
    path('deleteuserlist/<int:id>/',views.deleteuserlist,name='deleteuserlist'),
    path('camera/', views.camera,name='camera'),
    path('add_vehicle/', views.add_vehicle,name='add_vehicle'),
    path('add_driver/',views.add_driver,name='add_driver'),
    path('drivers/', views.driver_list, name='driver_list'),
    path('drivers/delete/<int:id>/',views.delete_driver, name='delete_driver'),
    path('vehicles/', views.vehicle_list, name='vehicle_list'),
    path('vehicles/delete/<int:id>/',views.delete_vehicle, name='delete_vehicle'),
    path('camera/',views.capture_image,name='capture_image'),
    path('documents/',views.upload_documents,name='documents'),
    path('documents_list/',views.documents_list,name='documents_list'),
    path('documents_delete/<int:id>/',views.documents_delete,name='documents_delete'),
    path("video_feed/", views.video_feed),
    
    
   

]
    
