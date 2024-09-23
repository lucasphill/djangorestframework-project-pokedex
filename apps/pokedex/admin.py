from django.contrib import admin
from apps.pokedex.models import TblPokemon, TblTypes

class Pokemons(admin.ModelAdmin):
    list_display = [
        'num_pokedex_pokemon',
        'name_pokemon',
        'type_1_pokemon',
        'type_2_pokemon',
        'total_pokemon',
        'generation_pokemon',
        'legendary_pokemon',
        ]
    list_display_links = [
        'num_pokedex_pokemon',
        'name_pokemon',
        ]
    list_per_page = 20
    ordering = ['num_pokedex_pokemon',]
    search_fields = [
        'num_pokedex_pokemon',
        'name_pokemon',
        ]

admin.site.register(TblPokemon, Pokemons)

class Types(admin.ModelAdmin):
    list_display = [
        'type',
        'weaknesses_1',
        'weaknesses_2',
    ]
    list_display_links = [
        'type',
    ]

admin.site.register(TblTypes, Types)