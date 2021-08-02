from django.urls import path
from . import views

urlpatterns = [
    path('change_status/<new_status_id>/<receipt_id>', views.change_status, name='change_status'),
    path('all_receipt_list', views.all_receipt_list, name='all_receipt_list'),
    path('my_receipt_list', views.my_receipt_list, name='my_receipt_list'),
    path('receipt_check', views.receipt_check, name='receipt_check'),
    path('delete_product_in_cart/<change>', views.delete_product_in_cart, name='delete_product_in_cart'),
    path('backet_data_save/<change>', views.backet_data_save, name='backet_data_save'),
    path('registration_check', views.registration_check, name='registration_check'),
    path('registration', views.registration, name='registration'),
    path('change_user_data', views.change_user_data, name='change_user_data'),
    path('log_out', views.log_out, name='log_out'),
    path('profile', views.profile, name='profile'),
    path('log_in_check', views.log_in_check, name='log_in_check'),
    path('log_in', views.log_in, name='log_in'),
    path('contact', views.contact, name='contact'),
    path('delivery', views.delivery, name='delivery'),
    path('market', views.market, name='market'),
    path('main', views.main, name='main'),
    path('test', views.test, name='test'),
    path('', views.new_main, name='main'),
]
