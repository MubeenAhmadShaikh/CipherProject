from django.urls import URLPattern, path
from . import views

urlpatterns = [
    path('', views.hillEncrypt, name='hill-encrypt'),
    path('hill-decrypt/', views.hillDecrypt, name='hill-decrypt'),
    path('affine-encrypt/', views.affineEncrypt, name='affine-encrypt'),
    path('affine-decrypt/', views.affineDecrypt, name='affine-decrypt'),
]