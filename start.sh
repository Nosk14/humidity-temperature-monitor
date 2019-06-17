docker stop humidity-temperature-monitor
docker rm humidity-temperature-monitor
docker run -d \
    -e LOCATION=$1 \
    -e MQTT_ADDRESS=$2 \
    --restart unless-stopped \
    --name humidity-temperature-monitor \
    humidity-temperature-monitor