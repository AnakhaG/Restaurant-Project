from django.urls import path
from WebApp import views
urlpatterns=[
    path('home/',views.homepagefn,name='home'),
    path('menu_fn/',views.menu_fn,name='menu_fn'),
    path('about_page/',views.about_page,name='about_page'),
    path('service_pg/',views.service_pg,name='service_pg'),
    path('contact_pg/',views.contact_pg,name='contact_pg'),
    path('save_contact/',views.save_contact,name='save_contact'),
    path('products_filtered/<fud_name>/',views.products_filtered,name='products_filtered'),
    path('singlepg/<int:fud_id>/',views.singlepg,name='singlepg'),

    path('Signupp/',views.Signupp,name='Signupp'),
    path('save_signup/',views.save_signup,name='save_signup'),
    path('',views.loginpg,name='loginpg'),
    path('userlo/',views.userlo,name='userlo'),
    path('userlogout/',views.userlogout,name='userlogout'),
    path('Save_cart/',views.Save_cart,name='Save_cart'),
    path('ur_order/',views.ur_order,name='ur_order'),
    path('decart_item/<int:d_id>/',views.decart_item,name='decart_item'),
    path('payment/', views.payment, name='payment'),
    path('propay/', views.propay, name='propay'),
    path('SaveOrder/', views.SaveOrder, name='SaveOrder'),

]