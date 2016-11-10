


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


import-sea:
	docker-compose up -d postgis
	docker-compose up import-external
	docker-compose up imposm2


import-tiles: docker-compose.yml
	docker-compose up -d postgis
	docker-compose up import-external
	docker-compose up import-osm
	docker-compose up import-sql

export-tiles:docker-compose.yml
	docker-compose run \
		  -e BBOX="8.34,47.27,8.75,47.53" \
		  -e MIN_ZOOM="8" \
		  -e MAX_ZOOM="14" \
		  export
