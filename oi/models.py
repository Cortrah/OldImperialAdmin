# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

from django.db import models

class ActionCategory(models.Model):
    name = models.CharField(max_length=255, blank=True)
    code = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = u'action_category'
        ordering = ['name']


class AgentType(models.Model):
    name = models.CharField(max_length=255, blank=True)
    code = models.CharField(max_length=255, blank=True)
    agent_type_description_xml = models.TextField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = u'agent_type'
        ordering = ['name']


class AllegianceType(models.Model):
    name = models.CharField(max_length=255, blank=True)
    code = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = u'allegiance_type'
        ordering = ['name']


class BorderType(models.Model):
    name = models.TextField(blank=True)
    code = models.TextField(blank=True)
    land_cost = models.IntegerField(null=True, blank=True)
    air_cost = models.IntegerField(null=True, blank=True)
    naval_cost = models.IntegerField(null=True, blank=True)
    border_type_effect_xml = models.TextField(blank=True)
    is_directional = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        db_table = u'border_type'
        ordering = ['name']


class BuildLocationType(models.Model):
    name = models.TextField(blank=True)
    code = models.TextField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = u'build_location_type'
        ordering = ['name']


class ConstructType(models.Model):
    name = models.TextField(blank=True) # This field type is a guess.
    code = models.TextField(blank=True) # This field type is a guess.
    gp_cost = models.IntegerField(null=True, blank=True)
    ap_cost = models.IntegerField(null=True, blank=True)
    nfp_cost = models.IntegerField(null=True, blank=True)
    mana_cost = models.IntegerField(null=True, blank=True)
    upgradefromtype_id = models.IntegerField(null=True, blank=True)
    construct_type_effect_xml = models.TextField(blank=True)
    construct_type_description_xml = models.TextField(blank=True)
    provides_gp = models.IntegerField(null=True, blank=True)
    provides_ap = models.IntegerField(null=True, blank=True)
    provides_nfp = models.IntegerField(null=True, blank=True)
    provides_mana = models.IntegerField(null=True, blank=True)
    city_forts = models.IntegerField(null=True, blank=True)
    display_symbol = models.TextField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = u'construct_type'
        ordering = ['name']


class FeatureType(models.Model):
    name = models.CharField(max_length=255, blank=True)
    code = models.CharField(max_length=255, blank=True)
    feature_description_xml = models.TextField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = u'feature_type'
        ordering = ['name']


class Game(models.Model):
    name = models.TextField(blank=True)
    turn = models.IntegerField(null=True, blank=True)
    year = models.IntegerField(null=True, blank=True)
    datapath = models.TextField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = u'game'
        ordering = ['name']


class Kindred(models.Model):
    name = models.CharField(max_length=255, blank=True)
    code = models.CharField(max_length=255, blank=True)
    kindred_description_xml = models.TextField(blank=True)
    notes_xml = models.TextField(blank=True)
    age_of_majority = models.IntegerField(null=True, blank=True)
    average_life_expectancy = models.IntegerField(null=True, blank=True)
    average_couth = models.IntegerField(null=True, blank=True)
    average_ferocity = models.IntegerField(null=True, blank=True)
    average_intelligence = models.IntegerField(null=True, blank=True)
    average_lifespan = models.IntegerField(null=True, blank=True)
    average_loyalty = models.IntegerField(null=True, blank=True)
    is_amphibian = models.BooleanField(default=False)
    is_flyer = models.BooleanField(default=False)
    is_armored = models.BooleanField(default=False)
    is_vacuum_protected = models.BooleanField(default=False)
    is_secret = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        db_table = u'kindred'
        ordering = ['name']


class MajorMap(models.Model):
    name = models.CharField(max_length=255, blank=True)
    filepath = models.TextField(blank=True)
    x = models.IntegerField(null=True, blank=True)
    y = models.IntegerField(null=True, blank=True)
    is_secret = models.BooleanField( default=False)

    def __str__(self):
        return self.name

    class Meta:
        db_table = u'major_map'
        ordering = ['name']


class MinorMap(models.Model):
    name = models.TextField(blank=True)
    code = models.TextField(blank=True)
    filepath = models.TextField(blank=True)
    x = models.IntegerField(null=True, blank=True)
    y = models.IntegerField(null=True, blank=True)
    is_secret = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        db_table = u'minor_map'
        ordering = ['name']


class MovementType(models.Model):
    name = models.CharField(max_length=255, blank=True)
    code = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = u'movement_type'
        ordering = ['name']


class Province(models.Model):
    name = models.TextField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = u'province'
        ordering = ['name']


class TrainingType(models.Model):
    name = models.CharField(max_length=255, blank=True)
    code = models.CharField(max_length=255, blank=True)
    training_effect_xml = models.TextField(blank=True)
    training_description_xml = models.TextField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = u'training_type'
        ordering = ['name']


class TerrainType(models.Model):
    name = models.CharField(max_length=255, blank=True)
    code = models.CharField(max_length=255, blank=True)
    land_cost = models.IntegerField(null=True, blank=True)
    air_cost = models.IntegerField(null=True, blank=True)
    naval_cost = models.IntegerField(null=True, blank=True)
    display_symbol = models.IntegerField(null=True, blank=True)
    display_x = models.IntegerField(null=True, blank=True)
    display_y = models.IntegerField(null=True, blank=True)
    terrain_type_description_xml = models.TextField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = u'terrain_type'
        ordering = ['name']


class SpellType(models.Model):
    name = models.CharField(max_length=255, blank=True)
    code = models.CharField(max_length=255, blank=True)
    level = models.CharField(max_length=255, blank=True)
    nsr = models.IntegerField(null=True, blank=True, default=0)
    mana_initial_cost = models.IntegerField(null=True, blank=True, default=0)
    mana_per_unit_cost = models.IntegerField(null=True, blank=True, default=0)
    time_to_cast = models.IntegerField(null=True, blank=True, default=0)
    when_to_cast = models.TextField(blank=True, default="any")
    is_allow_multiple_casters = models.BooleanField(default=True)
    spell_type_effect_xml = models.TextField(blank=True)
    spell_type_description_xml = models.TextField(blank=True)
    is_secret = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        db_table = u'spell_type'
        ordering = ['name']


class Religion(models.Model):
    name = models.CharField(max_length=255, blank=True)
    religion_effect_xml = models.TextField(blank=True)
    religion_description_xml = models.TextField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = u'religion'
        ordering = ['name']


class PublicRealm(models.Model):
    name = models.TextField(blank=True)
    display_color = models.IntegerField(null=True, blank=True, default=0)
    tv = models.IntegerField(null=True, blank=True, default=0)
    isi = models.DecimalField( max_digits=8, decimal_places=2, blank=True, default=0, null=True ) # This field type is a guess.
    trade_partners = models.ManyToManyField("self", blank=True, null=True)
    nonhostile_partners  = models.ManyToManyField("self", blank=True, null=True)
    realm_type = models.TextField(blank=True, null=True)
    private_realm_id = models.OneToOneField('PrivateRealm')
    homeland_region_id = models.ForeignKey('PublicRegion')
    capital_construct_id = models.ForeignKey('PublicConstruct')
    religion_id = models.ForeignKey('Religion')
    is_secret = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        db_table = u'public_realm'
        ordering = ['name']


class SecretKindredSeer(models.Model):
    kindred_id = models.ForeignKey('Kindred', null=True, blank=True)
    public_realm_id = models.ForeignKey('PublicRealm',null=True, blank=True)
    class Meta:
        db_table = u'secret_kindred_seer'


class SecretMajorMapSeer(models.Model):
    major_map_id = models.ForeignKey('MajorMap',null=True, blank=True)
    public_realm_id = models.ForeignKey('PublicRealm',null=True, blank=True)
    class Meta:
        db_table = u'secret_major_map_seer'


class SecretMinorMapSeer(models.Model):
    minor_map_id = models.ForeignKey('MinorMap',null=True, blank=True)
    public_realm_id = models.ForeignKey('PublicRealm',null=True, blank=True)
    class Meta:
        db_table = u'secret_minor_map_seer'


class SecretPublicConstructSeer(models.Model):
    public_realm_id = models.IntegerField(null=True, blank=True)
    public_construct_id = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'secret_public_construct_seer'


class SecretPublicRealmSeer(models.Model):
    secret_public_realm_id = models.ForeignKey('PublicRealm',null=True, blank=True, related_name="+s")
    public_realm_id = models.ForeignKey('PublicRealm',null=True, blank=True, related_name="+r")
    class Meta:
        db_table = u'secret_public_realm_seer'


class SecretPublicRegionSeer(models.Model):
    public_region_id = models.ForeignKey('PublicRegion',null=True, blank=True)
    public_realm_id = models.ForeignKey('PublicRealm',null=True, blank=True)
    class Meta:
        db_table = u'secret_public_region_seer'


class SecretRegionBorderSeer(models.Model):
    region_border_id = models.ForeignKey('RegionBorder',null=True, blank=True)
    public_realm_id = models.ForeignKey('PublicRealm',null=True, blank=True)
    class Meta:
        db_table = u'secret_region_border_seer'


class SecretRegionFeatureSeer(models.Model):
    region_feature_id = models.ForeignKey('RegionFeature',null=True, blank=True)
    public_realm_id = models.ForeignKey('PublicRealm',null=True, blank=True)
    class Meta:
        db_table = u'secret_region_feature_seer'


class SecretSpellTypeSeer(models.Model):
    spell_type_id = models.ForeignKey('SpellType',null=True, blank=True)
    public_realm_id = models.ForeignKey('PublicRealm',null=True, blank=True)
    class Meta:
        db_table = u'secret_spell_type_seer'


class SecretUnitTypeSeer(models.Model):
    public_realm_id = models.ForeignKey('PublicRealm',null=True, blank=True)
    unit_type_id = models.ForeignKey('UnitType',null=True, blank=True)
    class Meta:
        db_table = u'secret_unit_type_seer'


class SpellsReligion(models.Model):
    spell_type_id = models.ForeignKey('SpellType', null=True, blank=True)
    religion_id = models.ForeignKey('Religion', null=True, blank=True)
    class Meta:
        db_table = u'spells_religion'


class ItemType(models.Model):
    name = models.CharField(max_length=255, blank=True)
    code = models.CharField(max_length=255, blank=True)
    mana_cost = models.IntegerField(null=True, blank=True)
    ap_cost = models.IntegerField(null=True, blank=True)
    nfp_cost = models.IntegerField(null=True, blank=True)
    gp_cost = models.IntegerField(null=True, blank=True)
    item_description_xml = models.TextField(blank=True)
    item_effect_xml = models.TextField(blank=True)
    mana_charge = models.IntegerField(null=True, blank=True)
    blank_cost = models.IntegerField(null=True, blank=True)
    spell_type_id = models.ForeignKey('SpellType',null=True, blank=True)
    class Meta:
        db_table = u'item_type'

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=255, blank=True)
    code = models.CharField(max_length=255, blank=True)
    public_region_id = models.ForeignKey('PublicRegion', null=True, blank=True)
    location = models.TextField(blank=True)
    mana_cost = models.IntegerField(null=True, blank=True)
    ap_cost = models.IntegerField(null=True, blank=True)
    nfp_cost = models.IntegerField(null=True, blank=True)
    gp_cost = models.IntegerField(null=True, blank=True)
    item_description_xml = models.TextField(blank=True)
    item_effect = models.TextField(blank=True)
    mana_charge = models.IntegerField(null=True, blank=True)
    blank_cost = models.IntegerField(null=True, blank=True)
    spell_type_id = models.ForeignKey('SpellType',null=True, blank=True)
    item_type_id = models.ForeignKey('ItemType', null=True, blank=True)
    class Meta:
        db_table = u'item'

    def __str__(self):
        return self.name


class PrivateConstruct(models.Model):
    name = models.TextField(blank=True)
    provides_gp = models.IntegerField(null=True, blank=True)
    provides_ap = models.IntegerField(null=True, blank=True)
    provides_nfp = models.IntegerField(null=True, blank=True)
    provides_sfp = models.IntegerField(null=True, blank=True)
    provides_mana = models.IntegerField(null=True, blank=True)
    city_forts = models.IntegerField(null=True, blank=True)
    notes_xml = models.TextField(blank=True)
    construct_type_id = models.ForeignKey('ConstructType',null=True, blank=True)
    class Meta:
        db_table = u'private_construct'

    def __str__(self):
        return self.name


class UnitType(models.Model):
    name = models.CharField(max_length=255, blank=True)
    code = models.CharField(max_length=255, blank=True)
    cost_gp = models.IntegerField(null=True, blank=True)
    cost_ap = models.IntegerField(null=True, blank=True)
    cost_nfp = models.IntegerField(null=True, blank=True)
    cost_cargo = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True) # This field type is a guess.
    mta = models.IntegerField(null=True, blank=True)
    move = models.IntegerField(null=True, blank=True)
    react = models.IntegerField(null=True, blank=True)
    land_movement = models.IntegerField(null=True, blank=True)
    naval_movement = models.IntegerField(null=True, blank=True)
    air_movement = models.IntegerField(null=True, blank=True)
    underland_movement = models.IntegerField(null=True, blank=True)
    gate_movement = models.IntegerField(null=True, blank=True)
    mtu = models.IntegerField(null=True, blank=True)
    gq = models.IntegerField(null=True, blank=True)
    mq = models.IntegerField(null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    qrtype = models.TextField(blank=True, null=True)
    is_allied = models.BooleanField(default=False)
    air_cargo_capacity =models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True) # This field type is a guess.
    naval_cargo_capacity = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)# This field type is a guess.
    ground_cargo_capacity = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True) # This field type is a guess.
    movement_type_id = models.ForeignKey('MovementType', null=True, blank=True)
    is_secret = models.BooleanField(default=False)

    class Meta:
        db_table = u'unit_type'

    def __str__(self):
        return self.name


class UnitTypeBuildLocationType(models.Model):
    unit_type_id = models.ForeignKey('UnitType',null=True, blank=True)
    build_location_type_id = models.ForeignKey('BuildLocationType',null=True, blank=True)
    class Meta:
        db_table = u'unit_type_build_location_type'


class PublicPlayer(models.Model):
    name = models.TextField(blank=True) # This field type is a guess.
    public_realm_id = models.ForeignKey('PublicRealm',null=True, blank=True)
    private_player_id = models.OneToOneField('PrivatePlayer', null=True, blank=True)
    class Meta:
        db_table = u'public_player'

    def __str__(self):
        return self.name


class PublicRegion(models.Model):
    name = models.TextField(blank=True)
    minormap_quadrant = models.TextField(blank=True)
    gp = models.IntegerField(null=True, blank=True)
    ap = models.IntegerField(null=True, blank=True)
    nfp = models.IntegerField(null=True, blank=True)
    mana = models.IntegerField(null=True, blank=True)
    is_has_road = models.BooleanField(default=False)
    is_borders_volcano = models.BooleanField( blank=True)
    is_inimical = models.BooleanField( blank=True)
    is_floating = models.BooleanField( blank=True)
    is_flying = models.BooleanField( blank=True)
    display_path = models.TextField(blank=True)
    display_x = models.IntegerField(null=True, blank=True)
    display_y = models.IntegerField(null=True, blank=True)
    is_secret = models.BooleanField( blank=True)
    major_map_id = models.ForeignKey('MajorMap',null=True, blank=True)
    minor_map_id = models.ForeignKey('MinorMap',null=True, blank=True)
    allegiance_type_id = models.ForeignKey('AllegianceType',null=True, blank=True)
    public_realm_id = models.ForeignKey('PublicRealm',null=True, blank=True, related_name='+o')
    secondtributorrealm_id = models.ForeignKey('PublicRealm',null=True, blank=True, related_name='+t')
    terrain_type_id = models.ForeignKey('TerrainType',null=True, blank=True)
    kindred_id = models.ForeignKey('Kindred',null=True, blank=True)
    province_id = models.ForeignKey('Province', null=True, blank=True)
    religion_id = models.ForeignKey('Religion',null=True, blank=True)
    private_region_id = models.OneToOneField('PrivateRegion',null=True, blank=True)
    class Meta:
        db_table = u'public_region'

    def __str__(self):
        return self.name


class PublicRegionItem(models.Model):
    name = models.TextField(blank=True)
    public_region_id = models.ForeignKey('PublicRegion',null=True, blank=True)
    item_id = models.ForeignKey('Item', null=True, blank=True)
    class Meta:
        db_table = u'public_region_item'

    def __str__(self):
        return self.name

class RegionBorder(models.Model):
    name = models.TextField(blank=True)
    is_secret = models.BooleanField(default=False)
    source_id = models.ForeignKey('PublicRegion',null=True, blank=True, related_name='+source')
    sink_id = models.ForeignKey('PublicRegion',null=True, blank=True, related_name='+sink')
    border_type_id = models.ForeignKey('BorderType', null=True, blank=True)
    class Meta:
        db_table = u'region_border'

    def __str__(self):
        return self.name


class RegionFeature(models.Model):
    name = models.TextField(blank=True)
    display_symbol = models.IntegerField(null=True, blank=True)
    display_x = models.IntegerField(null=True, blank=True)
    display_y = models.IntegerField(null=True, blank=True)
    is_secret = models.BooleanField(default=False)
    feature_type_id = models.ForeignKey('FeatureType',null=True, blank=True)
    public_region_id = models.ForeignKey('PublicRegion',null=True, blank=True)
    location = models.TextField(blank=True)
    class Meta:
        db_table = u'region_feature'

    def __str__(self):
        return self.name


class UnitTypeGroup(models.Model):
    name = models.TextField(blank=True) # This field type is a guess.
    count = models.IntegerField(null=True, blank=True)
    unit_type_id = models.ForeignKey('UnitType',null=True, blank=True)
    public_realm_id = models.ForeignKey('PublicRealm',null=True, blank=True, related_name='+orealm')
    public_region_id = models.ForeignKey('PublicRegion',null=True, blank=True, related_name='+currentregion')
    location = models.TextField(blank=True)
    home_region_id = models.ForeignKey('PublicRegion',null=True, blank=True, related_name='+homeregion')
    is_allied = models.BooleanField(default=False)
    display_symbol = models.IntegerField(null=True, blank=True)
    display_x = models.IntegerField(null=True, blank=True)
    display_y = models.IntegerField(null=True, blank=True)
    air_cargo_capacity = models.DecimalField( max_digits=7, decimal_places=2, blank=True, null=True) # This field type is a guess.
    naval_cargo_capacity = models.DecimalField( max_digits=7, decimal_places=2, blank=True, null=True) # This field type is a guess.
    ground_cargo_capacity =models.DecimalField( max_digits=7, decimal_places=2, blank=True, null=True) # This field type is a guess.
    air_cargo_used = models.DecimalField( max_digits=7, decimal_places=2, blank=True, null=True) # This field type is a guess.
    naval_cargo_used = models.DecimalField( max_digits=7, decimal_places=2, blank=True, null=True) # This field type is a guess.
    ground_cargo_used = models.DecimalField( max_digits=7, decimal_places=2, blank=True, null=True) # This field type is a guess.
    class Meta:
        db_table = u'unit_type_group'

    def __str__(self):
        return self.name


class Leader(models.Model):
    name = models.TextField(blank=True) # This field type is a guess.
    code = models.TextField(blank=True) # This field type is a guess.
    public_realm_id = models.ForeignKey('PublicRealm',null=True, blank=True)
    public_region_id = models.ForeignKey('PublicRegion',null=True, blank=True,related_name='+current')
    location = models.TextField(blank=True)
    agent_type_id = models.ForeignKey('AgentType',null=True, blank=True)
    command = models.IntegerField(null=True, blank=True)
    loyalty = models.IntegerField(null=True, blank=True)
    combat = models.IntegerField(null=True, blank=True)
    diplomacy = models.IntegerField(null=True, blank=True)
    sorcery = models.IntegerField(null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    sex = models.TextField(blank=True)
    carrying_ap = models.IntegerField(null=True, blank=True)
    carrying_gp = models.IntegerField(null=True, blank=True)
    notes_xml = models.TextField(blank=True)
    display_symbol = models.IntegerField(null=True, blank=True)
    display_x = models.IntegerField(null=True, blank=True)
    display_y = models.IntegerField(null=True, blank=True)
    home_region_id = models.ForeignKey('PublicRegion',null=True, blank=True,related_name='+home')
    training_id = models.ForeignKey('TrainingType',null=True, blank=True)
    kindred_id = models.ForeignKey('Kindred',null=True, blank=True)
    class Meta:
        db_table = u'leader'

    def __str__(self):
        return self.code + ":" + self.name

class PublicConstruct(models.Model):
    name = models.TextField(blank=True)
    code = models.TextField(blank=True)
    construct_type_id = models.ForeignKey('ConstructType',null=True, blank=True, related_name='+type')
    public_realm_id = models.ForeignKey('PublicRegion',null=True, blank=True, related_name='+rlm')
    public_region_id = models.ForeignKey('PublicRegion',null=True, blank=True, related_name='+rgn')
    location = models.TextField(blank=True)
    construct_description = models.TextField(blank=True)
    level = models.IntegerField(null=True, blank=True)
    current_investment = models.IntegerField(null=True, blank=True)
    display_symbol = models.IntegerField(null=True, blank=True)
    display_x = models.IntegerField(null=True, blank=True)
    display_y = models.IntegerField(null=True, blank=True)
    is_secret = models.BooleanField(default=False)
    private_construct_id = models.OneToOneField('PrivateConstruct',null=True, blank=True)
    class Meta:
        db_table = u'public_construct'


class LeaderAction(models.Model):
    name = models.CharField(max_length=255, blank=True)
    code = models.CharField(max_length=255, blank=True)
    is_usesroad = models.BooleanField(default=False)
    starting_phase = models.IntegerField(null=True, blank=True)
    movement_cost = models.IntegerField(null=True, blank=True)
    is_secret = models.BooleanField(default=False)
    monitor_level = models.TextField(blank=True)
    gp_cost = models.IntegerField(null=True, blank=True)
    ap_cost = models.IntegerField(null=True, blank=True)
    nfp_cost = models.IntegerField(null=True, blank=True)
    sfp_cost = models.IntegerField(null=True, blank=True)
    mana_cost = models.IntegerField(null=True, blank=True)
    total_mana_cost = models.IntegerField(null=True, blank=True)
    is_withothers = models.BooleanField(default=False)
    is_primarytarget = models.BooleanField(default=True)
    unittype_code = models.TextField(blank=True)
    unit_count = models.IntegerField(null=True, blank=True)
    item_name = models.TextField(blank=True)
    notes = models.TextField(blank=True)
    effect = models.TextField(blank=True)
    description = models.TextField(blank=True)
    action_category_id = models.ForeignKey('ActionCategory',null=True, blank=True)
    movement_type_id = models.ForeignKey('MovementType',null=True, blank=True)
    public_realm_id = models.ForeignKey('PublicRealm',null=True, blank=True)
    at_public_region_id = models.ForeignKey('PublicRegion',null=True, blank=True, related_name='+at')
    at_location = models.TextField(blank=True)
    to_public_region_id = models.ForeignKey('PublicRegion',null=True, blank=True,related_name='+to')
    to_location = models.TextField(blank=True)
    unit_type_id = models.ForeignKey('UnitType',null=True, blank=True)
    item_id = models.ForeignKey('Item',null=True, blank=True)
    class Meta:
        db_table = u'leader_action'

    def __str__(self):
        return self.name


class LeaderItem(models.Model):
    name = models.TextField(blank=True)
    leader_id = models.ForeignKey('Leader',null=True, blank=True)
    item_id = models.ForeignKey('Item',null=True, blank=True)
    class Meta:
        db_table = u'leader_item'

    def __str__(self):
        return self.name


class LeaderUnitTypeGroup(models.Model):
    name = models.TextField(blank=True)
    air_cargo_capacity = models.DecimalField(max_digits=5, decimal_places=2, blank=True,null=True) # This field type is a guess.
    naval_cargo_capacity = models.DecimalField(max_digits=5, decimal_places=2, blank=True,null=True) # This field type is a guess.
    ground_cargo_capacity = models.DecimalField( max_digits=5, decimal_places=2, blank=True,null=True) # This field type is a guess.
    air_cargo_used = models.DecimalField(max_digits=5, decimal_places=2, blank=True,null=True) # This field type is a guess.
    naval_cargo_used = models.DecimalField( max_digits=5, decimal_places=2, blank=True,null=True) # This field type is a guess.
    ground_cargo_used = models.DecimalField( max_digits=5, decimal_places=2, blank=True,null=True) # This field type is a guess.
    leader_id = models.ForeignKey('Leader',null=True, blank=True)
    unit_type_group_id = models.ForeignKey('UnitTypeGroup',null=True, blank=True)
    class Meta:
        db_table = u'leader_unit_type_group'

    def __str__(self):
        return self.name


class PrivatePlayer(models.Model):
    email = models.EmailField(blank=True, null=True)
    password = models.TextField(blank=True, null=True)
    first_name = models.TextField(blank=True)
    last_name = models.TextField(blank=True)
    credits = models.IntegerField(null=True, blank=True)
    public_player_id = models.OneToOneField('PublicPlayer',null=True, blank=True)
    dei_player_id = models.OneToOneField('DeiPlayer',null=True, blank=True)
    class Meta:
        db_table = u'private_player'

    def __str__(self):
        return self.first_name + " " + self.last_name


class PrivateRealm(models.Model):
    mana = models.DecimalField(max_digits=6, decimal_places=2, blank=True,null=True) # This field type is a guess.
    region_gp = models.DecimalField( max_digits=7, decimal_places=2, blank=True,null=True) # This field type is a guess.
    urban_gp = models.DecimalField(max_digits=7, decimal_places=2, blank=True,null=True) # This field type is a guess.
    ict_gp = models.DecimalField(max_digits=7, decimal_places=2, blank=True,null=True) # This field type is a guess.
    pwb_gp = models.DecimalField( max_digits=7, decimal_places=2, blank=True,null=True) # This field type is a guess.
    road_gp = models.DecimalField( max_digits=7, decimal_places=2, blank=True,null=True)
    saved_gp = models.DecimalField( max_digits=8, decimal_places=2, blank=True,null=True) # This field type is a guess.
    prod_ap = models.DecimalField( max_digits=8, decimal_places=2, blank=True,null=True)# This field type is a guess.
    saved_ap =models.DecimalField( max_digits=7, decimal_places=2, blank=True,null=True)# This field type is a guess.
    total_ap = models.DecimalField( max_digits=7, decimal_places=2, blank=True,null=True) # This field type is a guess.
    nfp =models.DecimalField(max_digits=7, decimal_places=2, blank=True,null=True) # This field type is a guess.
    sfp =models.DecimalField(max_digits=7, decimal_places=2, blank=True,null=True) # This field type is a guess.
    army_support = models.DecimalField(max_digits=7, decimal_places=2, blank=True,null=True)# This field type is a guess.
    cav_qr = models.IntegerField(null=True, blank=True)
    inf_qr = models.IntegerField(null=True, blank=True)
    sge_qr = models.IntegerField(null=True, blank=True)
    nav_qr = models.IntegerField(null=True, blank=True)
    air_qr = models.IntegerField(null=True, blank=True)
    nsr_qr = models.IntegerField(null=True, blank=True)
    ir_qr = models.IntegerField(null=True, blank=True)
    bl_qr = models.IntegerField(null=True, blank=True)
    rs_qr = models.DecimalField( max_digits=7, decimal_places=2, blank=True,null=True) # This field type is a guess.
    cav_investment = models.IntegerField(null=True, blank=True)
    inf_investment = models.IntegerField(null=True, blank=True)
    sge_investment = models.IntegerField(null=True, blank=True)
    nav_investment = models.IntegerField(null=True, blank=True)
    air_investment = models.IntegerField(null=True, blank=True)
    ir_investment = models.IntegerField(null=True, blank=True)
    bl_investment = models.IntegerField(null=True, blank=True)
    nsr_investment = models.IntegerField(null=True, blank=True)
    notes_xml = models.TextField(blank=True)
    public_realm_id = models.OneToOneField('PublicRealm',null=True, blank=True)
    dei_realm_id = models.OneToOneField('DeiRealm',null=True, blank=True)
    class Meta:
        db_table = u'private_realm'


class PrivateRegion(models.Model):
    name = models.TextField(blank=True,null=True) # This field type is a guess.
    pwb = models.IntegerField(null=True, blank=True)
    tv = models.IntegerField(null=True, blank=True)
    resistance = models.IntegerField(null=True, blank=True)
    status = models.TextField(blank=True)
    notes_xml = models.TextField(blank=True)
    public_region_id = models.OneToOneField('PublicRegion',null=True, blank=True)
    dei_region_id = models.OneToOneField('DeiRegion',null=True, blank=True)

    class Meta:
        db_table = u'private_region'


class DeiPlayer(models.Model):
    notes_xml = models.TextField(blank=True)
    private_player_id = models.OneToOneField('PrivatePlayer',null=True, blank=True)
    class Meta:
        db_table = u'dei_player'


class DeiRealm(models.Model):
    corruption_percentage = models.IntegerField(null=True, blank=True)
    plague_percentage = models.IntegerField(null=True, blank=True)
    notes_xml = models.TextField(blank=True)
    private_realm_id = models.OneToOneField('PrivateRealm',null=True, blank=True)
    class Meta:
        db_table = u'dei_realm'


class DeiRegion(models.Model):
    notes_xml = models.TextField(blank=True)
    status_mult = models.TextField(blank=True) # This field type is a guess.
    private_region_id = models.OneToOneField('PrivateRegion', null=True, blank=True)
    class Meta:
        db_table = u'dei_region'
