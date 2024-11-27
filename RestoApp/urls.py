from django.urls import path
from RestoApp import views
urlpatterns = [
    path('Index_page/',views.Index_page,name='Index_page'),
    path('add_food/',views.add_food,name='add_food'),
    path('save_food/',views.save_food,name='save_food'),
    path('display_food/',views.display_food,name='display_food'),
    path('edit_food/<int:fud_id>/',views.edit_food,name='edit_food'),
    path('update_food/<int:fud_id>/',views.update_food,name='update_food'),
    path('delete_food/<int:fud_id>/',views.delete_food,name='delete_food'),

    #Food Items
    path('add_food_items/',views.add_food_items,name = 'add_food_items'),
    path('save_food_items/',views.save_food_items,name = 'save_food_items'),
    path('display_food_items/',views.display_food_items,name = 'display_food_items'),
    path('edit_food_items/<int:fud_id>/',views.edit_food_items,name = 'edit_food_items'),
    path('update_food_items/<int:fud_id>/',views.update_food_items,name = 'update_food_items'),
    path('delete_food_items/<int:fud_id>/',views.delete_food_items,name = 'delete_food_items'),


    path('contact_det/',views.contact_det,name = 'contact_det'),
    path('Dele_contact/<con_id>/',views.Dele_contact,name = 'Dele_contact'),



    path('admin_login/',views.admin_login,name = 'admin_login'),
    path('admin_loginfn/',views.admin_loginfn,name = 'admin_loginfn'),
    path('admin_logout/',views.admin_logout,name = 'admin_logout'),
]