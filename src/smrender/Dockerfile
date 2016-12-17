FROM ubuntu:latest

RUN apt-get update -y && apt-get install -y xz-utils make gcc pkg-config fontconfig libcairo* libgtk2.0-dev lib2.0-dev automake autotools-dev wget emacs make unzip git cmake


RUN cd /tmp && wget http://www.abenteuerland.at/download/smrender/archive/4.0/smrender-4.0.r1854.tar.xz &&  xzcat smrender-4.0.r1854.tar.xz | tar xvf - && cd smrender-4.0.r1854 && sed -i -e "1i #include<glib.h>"  src/smrender_dev.h

RUN (export LDFLAGS=-lglib-2.0;export LD_LIBRARY_PATH=/usr/local/lib;cd /tmp/smrender-4.0.r1854;./configure --;make;make install)

RUN wget -O - http://m.m.i24.cc/osmconvert.c | cc -x c - -lz -O3 -o /bin/osmconvert

RUN /sbin/ldconfig

RUN apt-get install -y osmosis


ADD rules/rules.osm /
ADD Makefile /
ADD run.sh /

CMD /run.sh





