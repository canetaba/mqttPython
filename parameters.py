""""
MQTT Constants
@author: Maria Jose
"""

# Client instance
CLIENT_ID = "P1"
CLEAN__SESSION = True
USER_DATA = None
PROTOCOL = 2
TRANSPORT = "tcp"

# Broker
HOST = "localhost"
PORT = 1883
KEEP_ALIVE = 60
BIND_ADDRESS = ""

# Publishing messages
TOPIC_PUB = "consola/555/audioin"
PAYLOAD = None
QOS_SUB = 2
RETAIN = "False"
PROPERTIES=None

# Subscribe topic
TOPIC_SUB = "consola/555/audioin"
QOS_PUB = 2


