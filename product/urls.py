from django.urls import path, include

from .views import ProductCreateAPIView, ProductRetriveUpdateDestroyAPIView

urlpatterns = [
    path('<int:pk>/', ProductRetriveUpdateDestroyAPIView.as_view()),
    path('create/', ProductCreateAPIView.as_view())
]
