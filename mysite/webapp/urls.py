from django.urls import path

from .views import (
    IndexView,
    ProductView,
    CreateProductView,
    ProductUpdateView,
    ProductDeleteView,
    ProductFeedbackCreate,
    ProductFeedbackUpdate,
    ProductFeedbackDelete,
    NotModeratedList
)

app_name = 'webapp'

urlpatterns = [
    path('', IndexView.as_view(), name='list'),
    path('add/', CreateProductView.as_view(), name='add'),
    path('<int:pk>/', ProductView.as_view(), name='view'),
    path('<int:pk>/update', ProductUpdateView.as_view(), name='update'),
    path('<int:pk>/delete', ProductDeleteView.as_view(), name='delete'),
    path('<int:pk>/feedbacks/add/', ProductFeedbackCreate.as_view(), name='feedback-create'),
    path('feedbacks/<int:pk>/update/', ProductFeedbackUpdate.as_view(),
         name='feedback-update'),
    path('feedbacks/<int:pk>/delete/', ProductFeedbackDelete.as_view(), name='feedback-delete'),
    path('feedback/list', NotModeratedList.as_view(), name='feedback-list')
]