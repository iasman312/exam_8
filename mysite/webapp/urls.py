from django.urls import path

from .views import (
    IndexView,
    ProductView,
    CreateProductView
)

app_name = 'webapp'

urlpatterns = [
    path('', IndexView.as_view(), name='list'),
    path('add/', CreateProductView.as_view(), name='add'),
    path('<int:pk>/', ProductView.as_view(), name='view'),
]