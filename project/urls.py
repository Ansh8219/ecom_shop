"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from apk import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("admin/", admin.site.urls),
    path('',views.main,name='main'),
    path('home/',views.home,name='home'),
    path('shop/',views.shop,name='shop'),
    path('about/',views.about,name='about'),
    path('blog/',views.blog,name='blog'),
    path('contact/',views.contact,name='contact'),
    path('cart/',views.cart,name='cart'),
    path('checkout/',views.checkout,name='checkout'),
    path('blog_single/',views.blog_single,name='blog_single'),
    path('product_single/<int:id>',views.product_single,name='product_single'),
    path('login/',views.login,name='login'),
    path('signup/',views.signup,name='signup'),
    path('profile/',views.profile,name='profile'),
    path('Logout/',views.Logout,name='Logout'),
    path('logsign/',views.logsign,name='logsign'),
    path('ChangePassword/',views.ChangePassword,name='ChangePassword'),
    path('update/',views.update,name='update'),
    path('userdata/',views.userdata,name='userdata'),
    path('show_user_data/',views.show_user_data,name='show_user_data'),
    # path('username/',views.username,name='username'),
    path('demo/',views.demo,name='demo'),
    path('shoes/',views.shoes,name='shoes'),
    path('shirt_product/<int:id>',views.shirt_product,name='shirt_product'),
    path('mens_shirt/',views.mens_shirt,name='mens_shirt'),
    path('mens_tshirt/',views.mens_tshirt,name='mens_tshirt'),
    path('mens_jeans/',views.mens_jeans,name='mens_jeans'),
    path('mens_jacket/',views.mens_jacket,name='mens_jacket'),






]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)