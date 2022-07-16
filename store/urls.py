from django.contrib import admin
from django.urls import path
from .views.home import Index , store
from .views.signup import Signup
from .views.sec import sec
from .views.submit import submit
from .views.contact import contact
from .views.login import Login , logout

from .views.first import home
from .views.cart import Cart
from .views.checkout import CheckOut
from .views.aboutus import about
from .views.orders import OrderView
from .middlewares.auth import  auth_middleware


urlpatterns = [
    path('', Index.as_view(), name='homepage'),
    path('store', store , name='store'),
    path('home', home.as_view(), name='home'),
    path('submit', submit.as_view(), name='submit'),
    path('sec', sec.as_view(), name='sec'),
    path('signup', Signup.as_view(), name='signup'),
    path('login', Login.as_view(), name='login'),
    path('contact', contact.as_view(), name='contact'),
    path('about', about.as_view(), name='about'),
    path('logout', logout , name='logout'),
    path('cart', auth_middleware(Cart.as_view()) , name='cart'),
    path('check-out', CheckOut.as_view() , name='checkout'),
    path('orders', auth_middleware(OrderView.as_view()), name='orders'),
]
