FROM mdillon/postgis:9.4

RUN apt-get update && apt-get install -y --no-install-recommends \
      wget \
      unzip \
      gdal-bin \
    && rm -rf /var/lib/apt/lists/*


RUN mkdir -p /data/import/land \
    && wget http://data.openstreetmapdata.com/land-polygons-split-3857.zip \
    && unzip -oj land-polygons-split-3857.zip -d /data/import/land \
    && rm land-polygons-split-3857.zip


ENV IMPORT_DATA_DIR=/data/import

COPY . /usr/src/app
WORKDIR /usr/src/app

CMD ["./import-land.sh"]
