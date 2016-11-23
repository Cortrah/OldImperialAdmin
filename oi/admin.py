__author__ = 'Cort'

from django.contrib import admin

from oi.models import ActionCategory
from oi.models import AgentType
from oi.models import AllegianceType
from oi.models import BorderType
from oi.models import BuildLocationType
from oi.models import ConstructType
from oi.models import FeatureType
from oi.models import Game
from oi.models import Kindred
from oi.models import MajorMap
from oi.models import MinorMap
from oi.models import MovementType
from oi.models import Province
from oi.models import TrainingType
from oi.models import TerrainType
from oi.models import SpellType
from oi.models import Religion
from oi.models import PublicRealm
from oi.models import SecretKindredSeer
from oi.models import SecretMajorMapSeer
from oi.models import SecretMinorMapSeer
from oi.models import SecretPublicConstructSeer
from oi.models import SecretPublicRealmSeer
from oi.models import SecretPublicRegionSeer
from oi.models import SecretRegionBorderSeer
from oi.models import SecretRegionFeatureSeer
from oi.models import SecretSpellTypeSeer
from oi.models import SecretUnitTypeSeer
from oi.models import SpellsReligion
from oi.models import ItemType
from oi.models import Item
from oi.models import PrivateConstruct
from oi.models import UnitType
from oi.models import UnitTypeBuildLocationType
from oi.models import PublicPlayer
from oi.models import PublicRegion
from oi.models import PublicRegionItem
from oi.models import RegionBorder
from oi.models import RegionFeature
from oi.models import UnitTypeGroup
from oi.models import Leader
from oi.models import PublicConstruct
from oi.models import LeaderAction
from oi.models import LeaderItem
from oi.models import LeaderUnitTypeGroup
from oi.models import PrivatePlayer
from oi.models import PrivateRealm
from oi.models import PrivateRegion
from oi.models import DeiPlayer
from oi.models import DeiRealm
from oi.models import DeiRegion

admin.site.register(ActionCategory)
admin.site.register(AgentType)
admin.site.register(AllegianceType)
admin.site.register(BorderType)
admin.site.register(BuildLocationType)
admin.site.register(ConstructType)
admin.site.register(FeatureType)
admin.site.register(Game)
admin.site.register(Kindred)
admin.site.register(MajorMap)
admin.site.register(MinorMap)
admin.site.register(MovementType)
admin.site.register(Province)
admin.site.register(TrainingType)
admin.site.register(TerrainType)
admin.site.register(SpellType)
admin.site.register(Religion)
admin.site.register(PublicRealm)
admin.site.register(SecretKindredSeer)
admin.site.register(SecretMajorMapSeer)
admin.site.register(SecretMinorMapSeer)
admin.site.register(SecretPublicConstructSeer)
admin.site.register(SecretPublicRealmSeer)
admin.site.register(SecretPublicRegionSeer)
admin.site.register(SecretRegionBorderSeer)
admin.site.register(SecretRegionFeatureSeer)
admin.site.register(SecretSpellTypeSeer)
admin.site.register(SecretUnitTypeSeer)
admin.site.register(SpellsReligion)
admin.site.register(ItemType)
admin.site.register(Item)
admin.site.register(PrivateConstruct)
admin.site.register(UnitType)
admin.site.register(UnitTypeBuildLocationType)
admin.site.register(PublicPlayer)
admin.site.register(PublicRegion)
admin.site.register(PublicRegionItem)
admin.site.register(RegionBorder)
admin.site.register(RegionFeature)
admin.site.register(UnitTypeGroup)
admin.site.register(Leader)
admin.site.register(PublicConstruct)
admin.site.register(LeaderAction)
admin.site.register(LeaderItem)
admin.site.register(LeaderUnitTypeGroup)
admin.site.register(PrivatePlayer)
admin.site.register(PrivateRealm)
admin.site.register(PrivateRegion)
admin.site.register(DeiPlayer)
admin.site.register(DeiRealm)
admin.site.register(DeiRegion)