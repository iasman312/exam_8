from django.urls import path

from .views import (
    IndexView,
    ProductView,
    CreateProductView,
    ProductUpdateView,
    ProductFeedbackCreate
)

app_name = 'webapp'

urlpatterns = [
    path('', IndexView.as_view(), name='list'),
    path('add/', CreateProductView.as_view(), name='add'),
    path('<int:pk>/', ProductView.as_view(), name='view'),
    path('<int:pk>/update', ProductUpdateView.as_view(), name='update'),
    path('<int:pk>/feedbacks/add/', ProductFeedbackCreate.as_view(), name='feedback-create')
]