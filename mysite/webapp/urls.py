from django.urls import path

from .views import (
    IndexView,
    ProductView,
)

app_name = 'webapp'

urlpatterns = [
    path('', IndexView.as_view(), name='list'),
    path('<int:pk>/', ProductView.as_view(), name='view'),
]