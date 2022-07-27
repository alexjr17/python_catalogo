from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="catalogo.index"),
    path('create', views.create, name="catalogo.create"),
    path('edit', views.edit, name="catalogo.edit")
]