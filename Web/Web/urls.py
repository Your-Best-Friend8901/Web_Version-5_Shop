"""
URL configuration for Web project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from sito_web import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Main_Page, name='Main'),

    ####################### Авторизация
    path('registration/', views.Registration, name='Registration'),
    path('main_auth/', views.Main_auth, name='Main_auth'),
    path('login/', views.Login, name='Login'),
    path('Verification_email/', views.Verificate_Email, name='Login2'),
    ########################

    ######################## Корзина
    path('cart/',views.Cart,name='Cart'),
    path('cart/add/<int:id_product>/',views.Cart_add,name='Cart_add'),
    ########################
    path('category/<str:category_name>/',views.Category,name='Category'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
