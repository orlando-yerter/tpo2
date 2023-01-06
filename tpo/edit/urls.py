from django.urls import path
from .views import edit, edit_item

urlpatterns = [
    path('', edit),
    path('edit_item/<int:pk>', edit_item),
]