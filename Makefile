


OSM2VEC=osm2vectortiles
OSMFILE=./import/japan-latest.osm.pbf


setup:
	sudo apt install -y docker.io
	sudo apt install -y docker-compose


clone:
	git clone https://github.com/osm2vectortiles/osm2vectortiles.git


docker-compose.yml: $(OSM2VEC)/docker-compose.yml src/docker-compose.yml
	cat $(OSM2VEC)/docker-compose.yml src/docker-compose.yml > docker-compose.yml


japan-pbf: $(OSMFILE)

$(OSMFILE): 
	wget -v http://download.geofabrik.de/asia/japan-latest.osm.pbf -O $(OSMFILE)


smrender:
	docker-compose up smrender


import-sea: docker-compose.yml
	date
	docker-compose up -d postgis
	date
	docker-compose up smrender
	date
	docker-compose up imposm2
	date
	docker-compose up import-external
	date
	docker-compose up import-land

import-tiles: docker-compose.yml
	docker-compose up -d postgis
	docker-compose up import-external
	docker-compose up import-osm
	docker-compose up import-sql


mapbox:
	docker-compose up -d mapbox-studio


DOCROOT=/mnt/hdd/www/seatile
MBTILES=./export/tiles.mbtiles

export-tiles:docker-compose.yml
	- rm -f $(MBTILES)
	docker-compose run -e BBOX="138,30,152,40" -e MIN_ZOOM="9" -e MAX_ZOOM="14" export

website:
	- rm -rf $(DOCROOT)

	mb-util --image_format=pbf $(MBTILES)  $(DOCROOT)
	cp www/htaccess $(DOCROOT)/.htaccess

coastline:
	docker run -v /home/yass/project/vector-render/import/WORK:/data -it osmcoastline ./osmcoastline.sh /data/japan-latest.osm.pbf land
