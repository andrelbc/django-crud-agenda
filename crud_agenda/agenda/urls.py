from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.form_Contatos, name='form_contato'),
    path('<int:id>/', views.form_Contatos, name='contato_update'),
    path('delete/<int:id>/', views.deletar_Contatos, name='delete_contato'),
    path('lista/', views.lista_Contatos, name='lista_contatos'),

]
