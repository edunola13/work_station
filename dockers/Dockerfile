# Set the base image to use to Ubuntu
FROM python:3.6-alpine

# Set the file maintainer (your name - the file's author)
MAINTAINER Eduardo Sebastian Nola

COPY requirements.txt .

RUN apk add --no-cache --virtual .build-deps \
    build-base \
    postgresql-dev \
    libffi-dev \
    jpeg-dev \
    zlib-dev \
    musl-dev \
    libressl-dev \
    gcc \
    python3-dev \
    git \
    && pip install -r requirements.txt \
    && pip install gevent requests[security] \
    && find /usr/local \
        \( -type d -a -name test -o -name tests \) \
        -o \( -type f -a -name '*.pyc' -o -name '*.pyo' \) \
        -exec rm -rf '{}' + \
    && runDeps="$( \
        scanelf --needed --nobanner --recursive /usr/local \
                | awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \
                | sort -u \
                | xargs -r apk info --installed \
                | sort -u \
    )" \
    && apk add --virtual .rundeps $runDeps \
    && apk del .build-deps \
    && apk add gettext-dev


# Directory in container for all project files
ENV DOCKYARD_SRVHOME=/srv
# Directory in container for project source files
ENV DOCKYARD_SRVPROJ=$DOCKYARD_SRVHOME/work_station
ENV DOCKYARD_SRVLOGS=$DOCKYARD_SRVHOME/logs

# Create application subdirectories
RUN mkdir -p \
    $DOCKYARD_SRVPROJ \
    $DOCKYARD_SRVLOGS

VOLUME ["$DOCKYARD_SRVLOGS"]

WORKDIR $DOCKYARD_SRVPROJ
COPY . $DOCKYARD_SRVPROJ

RUN rm $DOCKYARD_SRVPROJ/.env

# Port to expose
# EXPOSE 8000

# Copy entrypoint script into the image
COPY dockers/docker-entrypoint.sh /
RUN ["chmod", "+x", "/docker-entrypoint.sh"]

ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["action-arg"]
