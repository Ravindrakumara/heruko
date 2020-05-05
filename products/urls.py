from django.conf import settings
from django.conf.urls.static import static
from django.urls import path ,reverse
from products.views import HomeView,ProductView,ShopView,add_to_cart,login,sign_up
#from.import views


app_name='products'
urlpatterns = [
   path('',HomeView.as_view(), name='home'),
   path('product',ShopView.as_view(), name='product'),
   path('product/<slug>/',ProductView.as_view(), name='pro'), # Here this detail view is work
   path('add-to-cart/<Slug>/', add_to_cart, name='add-to-cart'),
   #
   path('go',login.as_view(), name='log'),
   path('sign-up',sign_up.as_view(), name='cart-list'),
]

