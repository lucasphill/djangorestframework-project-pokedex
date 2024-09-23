from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from apps.pokedex.views import PokemonViewSet, TypeViewSet, ListaPokemonsTypeViewSet

router = routers.DefaultRouter()
router.register('pokemon', PokemonViewSet, basename='Pokemon')
router.register('type', TypeViewSet, basename='Type')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('type/<str:type>/pokemons', ListaPokemonsTypeViewSet.as_view()),
    path("api-auth/", include("rest_framework.urls")),
]
