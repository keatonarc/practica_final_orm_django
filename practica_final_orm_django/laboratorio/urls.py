from django.urls import path
from . import views

app_name = 'laboratorio'

urlpatterns = [
    path('', views.LaboratorioListView.as_view(), name='laboratorio_list'),
    path('nuevo/', views.LaboratorioCreateView.as_view(), name='laboratorio_create'),
    path('<int:pk>/editar/', views.LaboratorioUpdateView.as_view(), name='laboratorio_edit'),
    path('<int:pk>/eliminar/', views.LaboratorioDeleteView.as_view(), name='laboratorio_delete'),
    path('<int:pk>/', views.LaboratorioDetailView.as_view(), name='laboratorio_detail'),
]
