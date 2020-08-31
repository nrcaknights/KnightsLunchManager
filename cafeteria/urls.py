from django.urls import include, path

from cafeteria import views

urlpatterns = [
    path('', views.index, name='index'),
    path('delete-order/', views.delete_order, name='delete'),
    path('submit-order/', views.submit_order, name='submit'),
    path('todays-order/', views.todays_order, name='today'),
    
    path('admin/', views.admin_dashboard, name='admin'),
    path('admin/batch-entry', views.batch_entry, name='batch-entry'),
    path('admin/submit-batch-entry', views.submit_batch_entry, name='submit-batch-entry'),
    path('admin/homeroom-orders-report', views.homeroom_orders_report, name='homerooms-report'),
    path('admin/transactions/', include('transactions.urls')),
    path('admin/profiles/', include('profiles.urls')),
    # path('admin/transactions/', views.manage_transactions, name='transactions'),
    # path('admin/user/', include('profiles.urls'))
]