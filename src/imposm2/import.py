# Copyright 2011 Omniscale (http://omniscale.com)
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from imposm.mapping import (
    Options,
    Points, LineStrings, Polygons,
    String, Bool, Integer, OneOfInt,
    set_default_name_type, LocalizedName,
    WayZOrder, ZOrder, Direction,
    GeneralizedTable, UnionView,
    PseudoArea, meter_to_mapunit, sqr_meter_to_mapunit,
)

# # internal configuration options
# # uncomment to make changes to the default values
import imposm.config
# 
# # import relations with missing rings
imposm.config.import_partial_relations = False
# 
# # select relation builder: union or contains
imposm.config.relation_builder = 'contains'
# 
# # log relation that take longer than x seconds
# imposm.config.imposm_multipolygon_report = 60
# 
# # skip relations with more rings (0 skip nothing)
# imposm.config.imposm_multipolygon_max_ring = 0


# # You can prefer a language other than the data's local language
# set_default_name_type(LocalizedName(['name:en', 'int_name', 'name']))

db_conf = Options(
    # db='osm',
    host='localhost',
    port=5432,
    user='osm',
    password='osm',
    sslmode='allow',
    prefix='osm_new_',
    proj='epsg:900913',
)






# Custom tables for OpenSeaMap features

manmade = Points(
  name = 'manmade',
  mapping = {
    'man_made': (
      'beacon',
      'chimney',
      'crane',
      'lighthouse',
      'monitoring_station',
      'storage_tank'
      'tower',
      'wastewater_plant',
      'water_tower',
      'water_works',
    ),
})

manmade_ways = LineStrings(
  name = 'manmade_ways',
  mapping = {
    'man_made': (
      'breakwater',
      'groyne',
      'pier',
      'pipeline',
    )
  }
)

beacons = Points(
  name = 'beacons',
  mapping = {
    'seamark:type': (
      'beacon_cardinal',
      'beacon_isolated_danger',
      'beacon_lateral',
      'beacon_safe_water',
      'beacon_special_purpose',
    )
  },
  fields = (
    ('seamark:name', String()),
    ('seamark:beacon_lateral:shape', String()),
    ('seamark:beacon_lateral:category', String()),
    ('seamark:beacon_lateral:colour', String()),
    ('seamark:beacon_lateral:colour:pattern', String()),
    ('seamark:beacon_safe_water:shape', String()),
    ('seamark:beacon_safe_water:category', String()),
    ('seamark:beacon_safe_water:colour', String()),
    ('seamark:beacon_safe_water:colour:pattern', String()),
    ('seamark:beacon_cardinal:shape', String()),
    ('seamark:beacon_cardinal:category', String()),
    ('seamark:beacon_cardinal:colour', String()),
    ('seamark:beacon_cardinal:colour:pattern', String()),
    ('seamark:isolated_danger:shape', String()),
    ('seamark:isolated_danger:colour', String()),
    ('seamark:isolated_danger:colour:pattern', String()),
    ('seamark:beacon_special_purpose:shape', String()),
    ('seamark:beacon_special_purpose:colour', String()),
    ('seamark:radar_reflector', String()),
    ('seamark:light:colour', String()),
    ('seamark:topmark:shape', String()),
    ('seamark:topmark:colour', String()),
    ('seamark:fixme', String()),
    ('seamark:light_character', String()),
  )
)

buoys = Points(
  name = 'buoys',
  mapping = {
    'seamark:type': (
      'buoy_cardinal',
      'buoy_installation',
      'buoy_isolated_danger',
      'buoy_lateral',
      'mooring',
      'buoy_safe_water',
      'buoy_special_purpose',
    )
  },
  fields = (
    ('seamark:name', String()),
    ('seamark:buoy_cardinal:shape', String()),
    ('seamark:buoy_cardinal:category', String()),
    ('seamark:buoy_cardinal:colour', String()),
    ('seamark:buoy_cardinal:colour_pattern', String()),

    ('seamark:buoy_installation:shape', String()),
    ('seamark:buoy_installation:category', String()),
    ('seamark:buoy_installation:colour', String()),
    ('seamark:buoy_installation:colour_pattern', String()),

    ('seamark:buoy_isolated_danger:shape', String()),
    ('seamark:buoy_isolated_danger:category', String()),
    ('seamark:buoy_isolated_danger:colour', String()),
    ('seamark:buoy_isolated_danger:colour_pattern', String()),

    ('seamark:buoy_lateral:shape', String()),
    ('seamark:buoy_lateral:category', String()),
    ('seamark:buoy_lateral:colour', String()),
    ('seamark:buoy_lateral:colour_pattern', String()),

    ('seamark:buoy_safe_water:shape', String()),
    ('seamark:buoy_safe_water:colour', String()),
    ('seamark:buoy_safe_water:colour_pattern', String()),

    ('seamark:buoy_special_purpose:shape', String()),
    ('seamark:buoy_special_purpose:colour', String()),

    ('seamark:seamark:buoy_installation:category', String()),
    
    ('seamark:radar_reflector', String()),
    ('seamark:topmark:shape', String()),
    ('seamark:topmark:colour', String()),
    ('seamark:light:colour', String()),
    ('seamark:fixme', String()),
    ('seamark:light_character', String()),
  )
)

lights = Points(
  name = 'lights',
  mapping = {
    'seamark:type': (
      'light_major',
      'light_vessel',
      'light_float',
      'light_minor',

    )
  },
  fields = (
    ('seamark:name', String()),
    ('seamark:light:colour', String()),
    ('seamark:light:sequence', String()),
    ('seamark:light:period', String()),
    ('seamark:light:category', String()),
    ('seamark:light:height', String()),
    ('seamark:light:multiple', String()),
    ('seamark:light:range', String()),
    ('seamark:light:group', String()),
    ('seamark:light_vessel:name', String()),
    ('seamark:light_vessel:colour', String()),
    ('seamark:light_vessel:colour_pattern', String()),
    ('seamark:light_float:name', String()),
    ('seamark:light_float:colour', String()),
    ('seamark:light_float:colour_pattern', String()),
    ('seamark:topmark:shape', String()),
    ('seamark:topmark:colour', String()),
    ('seamark:fixme', String()),
    ('seamark:light_character', String()),
    )
)


light_arc = LineStrings (
    name='light_arc',
    mapping = {
        'seamark:light:object': (
            'light_major',
            'light_minor',
            )
        },
    fields = (
        ('seamark:arc_style', String()),
        ('seamark:light:object', String()),
        ('seamark:light:sector_nr', String()),
        ('seamark:light_arc', String()),
        ('seamark:light_radial', Integer()),
        ('seamark:light_character', String()),
    )
)


sealane = LineStrings (
    name='sealane',
    mapping = {
        'seamark:type': (
            'separation_boundary',
            'separation_lane',
            'separation_zone',
        )
    },
    
    fields = (
        ('name', String()),
    )
)


marinefarm = Polygons (
    name='marinefarm',
    mapping = {
        'seamark:type': (
            'marine_farm',
        )
    },
    
    fields = (
        ('seamark:marine_farm:category', String()),
        ('KSJ2:fish_right:product', String())
    )
)

rock = Points(
  name = 'rock',
  mapping = {
    'seamark:type': (
        'rock',
    )
  },
  fields = (
        ('seamark:rock:water_level', String()),
  )
)


horbour = Points(
  name = 'horbour',
  mapping = {
    'seamark:type': (
        'harbour',
        'harbour_basin',
        'dock',
        'dry_dock',
        'floating_dock',
        'berth',
    )
  },
  fields = (
      ('seamark:harbour:category', String()),
      ('website', String()),
      ('phone', String()),
  )
)



landmarks = Points(
  name = 'landmarks',
  mapping = {
    'natural': (
      'bay',
      'beach',
      'cave_entrance',
      'cliff',
      'island',
      'stone',
      'ridge',
      'water',
      'wetland',
      'wood',
    )
  }
)

