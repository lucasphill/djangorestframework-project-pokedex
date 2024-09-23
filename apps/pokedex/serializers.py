from rest_framework import serializers
from apps.pokedex.models import TblPokemon, TblTypes
from apps.pokedex.validators import img_pokemon_invalid

import re
def is_valid_url(url):
    pattern = r'^(http|https):\/\/([\w.-]+)(\.[\w.-]+)+([\/\w\.-]*)*\/?$'
    return bool(re.match(pattern, url))

class PokemonSerializer(serializers.ModelSerializer):
    class Meta:
        model = TblPokemon
        # fields = '__all__'
        exclude = ['id_pokemon']

    def validate(self, dados):
        if img_pokemon_invalid(dados['img_pokemon']):
            raise serializers.ValidationError({'img_pokemon':'Img deve ser um link para a imagem do Pokemon'})
        return dados

class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TblTypes
        fields = '__all__'