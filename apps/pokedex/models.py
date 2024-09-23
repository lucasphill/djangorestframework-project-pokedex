from django.db import models

# def get_types():
#     return TblTypes.objects.all()

class TblPokemon(models.Model):
    LEGENDARY = (
        ('1', 'Sim'),
        ('0', 'Não'),
    )
    id_pokemon = models.AutoField(primary_key=True)
    num_pokedex_pokemon = models.IntegerField()
    name_pokemon = models.CharField(unique=True, max_length=40)
    img_pokemon = models.CharField(max_length=255, blank=True, null=True)
    type_1_pokemon = models.ForeignKey('TblTypes', models.DO_NOTHING, db_column='type_1_pokemon')
    type_2_pokemon = models.ForeignKey('TblTypes', models.DO_NOTHING, db_column='type_2_pokemon', related_name='tblpokemon_type_2_pokemon_set', blank=True, null=True)
    total_pokemon = models.IntegerField()
    hp_pokemon = models.IntegerField()
    atk_pokemon = models.IntegerField()
    def_pokemon = models.IntegerField()
    sp_atk_pokemon = models.IntegerField()
    sp_def_pokemon = models.IntegerField()
    speed_pokemon = models.IntegerField()
    generation_pokemon = models.IntegerField()
    legendary_pokemon = models.BooleanField(max_length=1, blank=True, null=True, choices=LEGENDARY)

    class Meta:
        managed = False
        db_table = 'tbl_pokemon'
    
    def __str__(self):
        return self.name_pokemon

class TblTypes(models.Model):
    type = models.CharField(primary_key=True, max_length=20)
    weaknesses_1 = models.CharField(max_length=20, blank=True, null=True)
    weaknesses_2 = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_types'

    def __str__(self):
        return self.type
