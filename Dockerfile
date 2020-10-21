FROM l4t:latest

# Definition of a Device & Service
ENV POSITION=Runtime \
    SERVICE=get-robot-data-triggered-by-ui \
    AION_HOME=/var/lib/aion

RUN mkdir ${AION_HOME}
WORKDIR ${AION_HOME}
# Setup Directoties
RUN mkdir -p \
    $POSITION/$SERVICE
WORKDIR ${AION_HOME}/$POSITION/$SERVICE/
ADD . .
RUN python3 setup.py install

CMD ["/bin/sh", "docker-entrypoint.sh"]
