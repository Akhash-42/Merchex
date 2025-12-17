"""
URL configuration for merchex project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from listings import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.band_list),
    path('bands/', views.band_list, name='band-list'),
    path('about-us/', views.about, name = 'about'),
    path('contact-us/', views.contact, name= 'contact'),
    path('listings/', views.listings,name='list'),
    path("bands/<int:band_id>/",views.band_detail, name='band-detail'),
    path('listings/<int:id>', views.listing_detail, name = 'list-detail'),
    path('email/', views.email, name='email-sent'),
    path('bands/add/',views.band_create,name = 'band-create'),
    path('listings/add/',views.listing_create,name = 'list-create'),
    path("bands/<int:band_id>/change/",views.band_update, name='band-update'),
    path('listings/<int:id>/change/', views.listing_update, name = 'list-update'),
    path("bands/<int:band_id>/delete/",views.band_delete, name='band-delete'),
    path('listings/<int:id>/delete/', views.listing_delete, name = 'list-delete'),
    # path("listings/<int:id>/bands/<int:band_id>/",views.listing_detail, name='band-detail'),
]
