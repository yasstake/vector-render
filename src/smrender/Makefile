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

JAPAN_SEA_PBF=$(WORKDIR)/japan.sea.pbf
ORG_SEA_PBF=$(WORKDIR)/seafilter.pbf
MERGE_SEA_OSM=$(WORKDIR)/japan.mergesea.osm
JAPAN_FILTER_OSM=$(WORKDIR)/japan.mergefilter.osm
FISH_RIGHT_OSM=$(WORKDIR)/fish.osm

FISH_RIGHT_PBF=$(DATADIR)/fish.pbf
JAPAN_FILTER_PBF=$(DATADIR)/japan.mergefilter.pbf

all: $(JAPAN_FILTER_PBF) $(FISH_RIGHT_PBF) $(WORKDIR)

clean:
	rm -f $(RAWPBF).osm

$(WORKDIR):
	mkdir -p $(WORKDIR)

download-pbf: $(WORKDIR)
	wget  http://download.geofabrik.de/asia/japan-latest.osm.pbf -O $(ORGPBF)

$(RAWPBF).osm: 
#	osmosis --read-pbf $(ORGPBF) --bounding-box bottom=35 top=36 left=139 right=140 --write-xml file=$(RAWPBF).osm
	osmconvert $(ORGPBF)  -b="139,35,140,36" > $(RAWPBF).osm

alldata: $(ORGPBF)
	cp $(ORGPBF) $(RAWPBF)

$(JAPAN_FILTER_PBF): $(RAWPBF).osm
	smrender -i $(RAWPBF).osm -r /rules.osm -G -M -w $(JAPAN_FILTER_PBF).osm
#	osmosis --read-xml file=$(JAPAN_FILTER_PBF).osm --write-pbf file=$(JAPAN_FILTER_PBF)
	! osmconvert $(JAPAN_FILTER_PBF).osm -o=$(JAPAN_FILTER_PBF)

$(FISH_RIGHT_OSM):
	wget https://github.com/yasstake/ksj2osm/raw/master/fish.osm -O $(FISH_RIGHT_OSM)


$(FISH_RIGHT_PBF): $(FISH_RIGHT_OSM)
#	python ../ksj2osm/fish.py $(FISH_RIGHT_KJS2) $(FISH_RIGHT_OSM)
#	osmosis --read-xml file=$(FISH_RIGHT_OSM) --write-pbf $(FISH_RIGHT_PBF)
	osmconvert $(FISH_RIGHT_OSM) -o=$(FISH_RIGHT_PBF)

