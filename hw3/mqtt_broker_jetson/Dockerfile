FROM alpine

RUN apk --no-cache add mosquitto mosquitto-clients

# Expose MQTT port
EXPOSE 1883

ENV PATH /usr/sbin:$PATH

ENTRYPOINT ["/usr/sbin/mosquitto"]