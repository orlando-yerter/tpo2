from django.urls import path
from .views import remove, remove_item

urlpatterns = [
    path('', remove),
    path('remove_item/<int:pk>', remove_item),
]