import paho.mqtt.client as mqtt
import protobuf_classes.DataProtocol_pb2 as DataProtocol_pb2


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):

    print("Connected with result code", rc)

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    imei = 1234
    client.subscribe("world/poc-ultim-zenaterra/" + str(imei))


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):

    # Decode the protobuf message.
    message = DataProtocol_pb2.ProtocolMessages()
    message.ParseFromString(msg.payload)

    # Print dummy data
    print(message.header.dayNumber)
    print(message.gps[0].latitude, message.gps[0].longitude, message.gps[0].altitude)


### Main function.
if __name__ == "__main__":

    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    host = "localhost"
    port = 1883
#    host = "37.58.164.129"
#    port = 5053
    client.connect(host, port, 60)

    # Blocking call that processes network traffic, dispatches callbacks and
    # handles reconnecting.
    # Other loop*() functions are available that give a threaded interface and a
    # manual interface.
    client.loop_forever()
    
