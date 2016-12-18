#
#	japan.latest.pbf
#		-> japan.land.pbf
#		-> japan.sea.osm
#
#	japan.sea.osm + /ORG/japan.sea.osm -> sea.osm -> smfilter -> sea.pbf
#	
#	imposm land.pbf
#	imposm sea.pbf
#
#

DATADIR=/import

WORKDIR = $(DATADIR)/WORK

ORGPBF=$(WORKDIR)/japan-latest.osm.pbf
RAWPBF=$(WORKDIR)/japan.org.pbf

JAPAN_LAND_PBF=$(DATADIR)/japan.land.pbf
JAPAN_LAND_OSM=$(DATADIR)/japan.land.osm
JAPAN_SEA_PBF=$(WORKDIR)/japan.sea.pbf
JAPAN_SEA_OSM=$(WORKDIR)/japan.sea.osm


JAPAN_SEAFILTER_OSM=$(WORKDIR)/japan.seafilter.osm

FISH_RIGHT_OSM=$(WORKDIR)/fish.osm
FISH_RIGHT_PBF=$(DATADIR)/fish.pbf

JAPAN_FILTER_PBF=$(DATADIR)/japan.seafilter.pbf

all: $(JAPAN_LAND_PBF) $(JAPAN_FILTER_PBF) $(FISH_RIGHT_PBF) $(WORKDIR)

clean:
	rm -f $(JAPAN_LAND_PBF) $(JAPAN_FILTER_PBF)

$(WORKDIR):
	mkdir -p $(WORKDIR)

$(JAPAN_SEA_OSM):	$(WORKDIR)
	osmosis --read-pbf $(ORGPBF) \
		--tf accept-ways seamark:type=*	\
		--tf accept-node seamark:type=*	\
		--tf accept-relations seamark:type=* \
		--write-xml file=$(JAPAN_SEA_OSM)

$(JAPAN_LAND_PBF):	 $(WORKDIR)
	osmosis --read-pbf $(ORGPBF) \
		--tf reject-ways seamark:type=*	\
		--tf reject-node seamark:type=*	\
		--tf reject-relations seamark:type=* \
		--write-pbf file=$(JAPAN_LAND_PBF)

$(JAPAN_SEAFILTER_OSM): $(JAPAN_SEA_OSM)
	smrender -i $(JAPAN_SEA_OSM) -r /rules.osm -G -M -w $(JAPAN_SEAFILTER_OSM)

$(JAPAN_FILTER_PBF): $(JAPAN_SEAFILTER_OSM)
	osmosis --read-xml file=$(JAPAN_SEAFILTER_OSM) --write-pbf file=$(JAPAN_FILTER_PBF)


download: $(WORKDIR)
	wget  http://download.geofabrik.de/asia/japan-latest.osm.pbf -O $(ORGPBF)

clip:
	osmconvert  -b=139,34,140,36  /import/org/japan-latest.osm.pbf -o=$(ORGPBF)


$(FISH_RIGHT_OSM):
	wget https://github.com/yasstake/ksj2osm/raw/master/fish.osm -O $(FISH_RIGHT_OSM)


$(FISH_RIGHT_PBF): $(FISH_RIGHT_OSM)
	osmosis --read-xml file=$(FISH_RIGHT_OSM) --write-pbf $(FISH_RIGHT_PBF)


