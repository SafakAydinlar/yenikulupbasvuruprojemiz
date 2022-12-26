
from django.urls import path
from . import views

urlpatterns = [

    path('basvuru/', views.basvuru, name='basvuru'),
    path('basvuru2/', views.basvuru2, name='basvuru2'),
    path('basvuru3/', views.basvuru3, name='basvuru3'),
    path('basvuru4/', views.basvuru4, name='basvuru4'),
    path('basvuru5/', views.basvuru5, name='basvuru5'),
    path('', views.Anasayfa, name='anasayfa'),
    path('export_excel/', views.export_excel, name='export_excel'),
]