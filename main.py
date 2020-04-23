"""
MQTT client connection
@author: Maria Jose Briceño

"""
import paho.mqtt.client as mqtt
import parameters as param
import json as json
import constants as const


def mqtt_connection():
    # Connection to mqtt broker
    try:
        client.connect(param.HOST,
                       param.PORT)
        print("Connecting to mqtt broker")
    except Exception as msg:
        print("An exception occurred ", msg)


def mqtt_subscribe():
    # Publish in a MQTT topic
    client.subscribe(param.TOPIC_SUB,
                     param.QOS_SUB,
                     param.RETAIN)
    print("Subscribing at mqtt topic")


def mqtt_publish(msg):
    # Publish a message in MQTT topic
    print(msg)
    client.publish(param.TOPIC_PUB, msg)


def to_string(msg):
    # Convert json to string
    msg = json.dumps(msg)
    return msg


def increase_time(msg, j: object):
    # Increase the time's value
    data1 = dict(msg)
    data1['fecha'] += j
    return data1


def mqtt_unsubscribe():
    client.unsubscribe(param.TOPIC_SUB)


def mqtt_disconnect():
    client.disconnect()


# Main
if __name__ == "__main__":
    message = const.MESSAGE
    client = mqtt.Client(param.CLIENT_ID)
    print("Create MQTT client")
    mqtt_connection()
    mqtt_subscribe()
    # Send a lot of messages
    for i in range(const.MESSAGES_NUMBER):
        data = increase_time(message, i)
        data = to_string(data)
        mqtt_publish(data)
    print("All messages were sending")
    mqtt_unsubscribe()
    print("Unsubscribe topic:", param.TOPIC_SUB)
    mqtt_disconnect()
    print("Disconnect client")
