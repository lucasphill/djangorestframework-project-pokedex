from apps.pokedex.models import TblPokemon, TblTypes
from apps.pokedex.serializers import PokemonSerializer, TypeSerializer
from rest_framework import viewsets, generics, filters
from django_filters.rest_framework import DjangoFilterBackend

class PokemonViewSet(viewsets.ModelViewSet):
    queryset = TblPokemon.objects.all().order_by('num_pokedex_pokemon')
    serializer_class = PokemonSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['type_1_pokemon', 'type_2_pokemon', 'generation_pokemon','legendary_pokemon']
    search_fields = ['num_pokedex_pokemon', 'name_pokemon']
    ordering_fields = ['total_pokemon', 'hp_pokemon', 'atk_pokemon', 'def_pokemon', 'sp_atk_pokemon', 'sp_def_pokemon', 'speed_pokemon']

class TypeViewSet(viewsets.ModelViewSet):
    queryset = TblTypes.objects.all()
    serializer_class = TypeSerializer

class ListaPokemonsTypeViewSet(generics.ListAPIView):
    def get_queryset(self):
        # queryset = TblPokemon.objects.filter(type_1_pokemon=self.kwargs['type'])
        queryset = TblPokemon.objects.raw(f'SELECT * FROM db_pokedex.tbl_pokemon WHERE type_1_pokemon = "{self.kwargs['type']}" or type_2_pokemon = "{self.kwargs['type']}"') 
        return queryset
    serializer_class = PokemonSerializer

