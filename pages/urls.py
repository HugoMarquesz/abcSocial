from django.urls import path

# importa as views que a gente criou
from .views import PaginaInicial
# Tem que ser urlpatterns porque é padrão do Django
urlpatterns = [
  # Todo path tem endereço, sua_view.as_view() e nome
  path('', PaginaInicial.as_view(), name='index'),

  
]