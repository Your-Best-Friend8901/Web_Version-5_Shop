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
from sito_web import views_CBV,views_FBV
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    ####################### Админка
    path('admin/', admin.site.urls),
    #######################
    
    ####################### Основная Страница
    path('', views_FBV.Main_Page, name='Main'),
    #######################

    ####################### Авторизация
    #### FBV
    path('main_auth/', views_FBV.Main_auth, name='Main_auth'),
    #### CBV
    path('registration/', views_CBV.RegistrationView.as_view(), name='Registration'),
    path('login/', views_CBV.LoginView.as_view(), name='Login'),
    path('Verification_email/', views_CBV.CodeView.as_view(), name='Login2'),
    ########################

    ######################## Корзина
    #### FBV
    path('cart/add/<int:id_product>/',views_FBV.Cart_add,name='Cart_add'),
    #### CBV
    path('cart/',views_CBV.Cart.as_view(),name='Cart'),
    ########################

    ######################## Категорий
    #### FBV
    path('category/<str:category_name>/',views_FBV.Category,name='Category'),
    ########################
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
