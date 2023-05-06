from django.urls import path
from . import views

urlpatterns =[
    path('',views.anasayfa,name="anasayfa"),
    path('hasta/hastalogin/',views.login_view,name="hastalogin"),
    path('hasta/anasayfa/',views.hastaanasayfa,name="hastaanasayfa"),
    path('hasta/randevuislem/',views.randislem,name="randislem"),
    path('hasta/randal/', views.randevu_formu, name='randal'),
    path('hasta/sifre', views.sifre, name='sifreekranı'),
    
    
]