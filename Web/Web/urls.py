
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
    path('', views_FBV.main_page, name='main'),
    ####################### <Админка/>

    ####################### <Авторизация>
    #### FBV
    path('main_auth/', views_FBV.main_auth, name='main_auth'),
    #### CBV
    path('registration/', views_CBV.RegistrationView.as_view(), name='registration'),
    path('login/', views_CBV.Login_view.as_view(), name='login'),
    path('Verification_email/', views_CBV.CodeView.as_view(), name='login2'),
    ######################## <Авторизация/>

    ######################## <Корзина>
    #### FBV
    path('cart/<str:function>/<int:id_product>/',views_FBV.delete_or_add_product,name='Cart_add/delete'),
    #### CBV
    path('cart/',views_CBV.Cart.as_view(),name='Cart'),
    ######################## <Корзина/>

    ######################## <Категорий>
    #### FBV
    path('category/',views_FBV.category_page,name='category'),
    path('category/<str:category_name>/',views_FBV.category_products,name='category_products'),
    ######################## <Категорий/>

    ############### <Отправка кода>
    path('send_code/',views_FBV.send_code_to_email,name='send_code'),
    ############### <Отправка кода/>
    
    ######################## <Выход> 
    #### FBV
    path('exit/<str:Page>/',views_FBV.exit,name='exit'),
    ######################## <Выход/> 

    ######################## <Оплата>
    path('buy/',views_FBV.buy_product,name='buy'),
    ######################## <Оплата/>

    ######################## <Профиль>
    path('profile/',views_CBV.Profile.as_view(),name='Profile'),
    path('profile/edit/',views_CBV.Profile_edit.as_view(),name='Profile_edit'),
    ######################## <Профиль/>

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
