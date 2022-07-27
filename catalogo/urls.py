from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="catalogos_index"),
    path('create', views.create, name="catalogos_create"),
    path('edit', views.edit, name="catalogos_edit")
]