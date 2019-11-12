from django.urls import path
from homework1 import views

urlpatterns = [
    path('table/', views.table_list),
    path('tables/', views.table_list),
    path('table/<int:pk>', views.table_detail),
    path('columns/', views.column_list),
    path('column/', views.column_list),
    path('column/<int:pk>', views.column_detail),

]