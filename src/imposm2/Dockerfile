FROM ubuntu

RUN apt-get update
RUN apt-get install -y build-essential python-dev protobuf-compiler \
                      libprotobuf-dev libtokyocabinet-dev python-psycopg2 \
		                            libgeos-c1v5 python-pip

RUN pip install imposm

VOLUME /data/import /data/cache

ENV IMPORT_DATA_DIR=/data/import \
    IMPOSM_CACHE_DIR=/data/cache 

RUN mkdir -p /usr/src/app
COPY . /usr/src/app/
WORKDIR /usr/src/app

CMD ["./import-pbf.sh"]
