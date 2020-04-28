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
# Computador: local Cote
# audio = consola/COTEUBUNTU/audioin
# mensajes = "consola/5/COTEUBUNTU/mensajes"

# Consola: 555
# audio = consola/555/audioin
# mensajes = "consola/5/555/mensajes"
TOPIC_PUB = "consola/5/555/mensajes"
PAYLOAD = None
QOS_SUB = 2
RETAIN = "False"
PROPERTIES=None

# Subscribe topic
# audio = consola/COTEUBUNTU/audioin
# mensajes = "consola/5/COTEUBUNTU/mensajes"
TOPIC_SUB = "consola/5/555/mensajes"
QOS_PUB = 2


