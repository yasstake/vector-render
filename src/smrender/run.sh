#!/bin/sh

cd /import
#make -f /Makefile

DATADIR=/import
WORKDIR=$DATADIR/WORK

SEA_PBF=$DATADIR/world.sea.pbf
SEA_OSM=$WORKDIR/world.osm
SEA_FILTER_OSM=$WORKDIR/world.sea.filter.osm


FISH_RIGHT_OSM=$WORKDIR/fish.osm
FISH_RIGHT_PBF=$DATADIR/fish.pbf

#wget https://github.com/yasstake/ksj2osm/raw/master/fish.osm -O $FISH_RIGHT_OSM
#wget http://tiles.openseamap.org/seamark/world.osm -O $SEA_OSM

osmosis --read-xml file=$FISH_RIGHT_OSM --write-pbf file=$FISH_RIGHT_PBF

smrender -i $SEA_OSM -r /rules.osm -G -M -w $SEA_FILTER_OSM
osmosis --read-xml file=$SEA_FILTER_OSM --write-pbf file=$SEA_PBF




