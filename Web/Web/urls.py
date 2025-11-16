
from django.contrib import admin
from django.urls import path
from sito_web import views_CBV,views_FBV
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    ####################### <Админка>
    path('admin/', admin.site.urls),
    #######################
    
    ####################### Основная Страница
    path('', views_FBV.Main_Page, name='Main'),
    ####################### <Админка/>

    ####################### <Авторизация>
    #### FBV
    path('main_auth/', views_FBV.Main_auth, name='Main_auth'),
    #### CBV
    path('registration/', views_CBV.RegistrationView.as_view(), name='Registration'),
    path('login/', views_CBV.LoginView.as_view(), name='Login'),
    path('Verification_email/', views_CBV.CodeView.as_view(), name='Login2'),
    ######################## <Авторизация/>

    ######################## <Корзина>
    #### FBV
    path('cart/<str:function>/<int:id_product>/',views_FBV.Add_delete_product,name='Cart_add/delete'),
    #### CBV
    path('cart/',views_CBV.Cart.as_view(),name='Cart'),
    ######################## <Корзина/>

    ######################## <Категорий>
    #### FBV
    path('category/',views_FBV.Category,name='Category'),
    path('category/<str:category_name>/',views_FBV.Category_products,name='Category_products'),
    ######################## <Категорий/>

    ######################## <Выход> 
    #### FBV
    path('exit/<str:Page>/',views_FBV.Exit,name='Exit'),
    ######################## <Выход/> 

    ######################## <Оплата>
    path('buy/',views_FBV.Buy_product,name='Buy'),
    ######################## <Оплата/>

    ######################## <Профиль>
    path('profile/',views_CBV.Profile.as_view(),name='Profile'),
    path('profile/edit/',views_CBV.Profile_edit_Succes.as_view(),name='Profile_edit'),
    ######################## <Профиль/>

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
