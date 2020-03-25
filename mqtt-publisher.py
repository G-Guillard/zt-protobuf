import paho.mqtt.publish as publish
import protobuf_classes.DataProtocol_pb2 as DataProtocol_pb2


# Publish data to MQTT broker
def send_data(topic, payload, hostname, port):

    print("Publishing to", hostname + ":" + str(port) + ".")
    publish.single(topic, payload, hostname=hostname, port=port)


# Encode dict to protobuf
def encode_to_protobuf(metadata):

    message = DataProtocol_pb2.ProtocolMessages()
    message.header.dayNumber = 1 # dummy
    message.header.IMEIpart1 = 1 # dummy
    message.header.IMEIpart2 = 1 # dummy

    gps = message.gps.add()
    gps.time = metadata['created_at']
    gps.latitude = metadata['lat']
    gps.longitude = metadata['lon']
    gps.altitude = metadata['ele']

    return message.SerializeToString()


### Main function.
if __name__ == "__main__":

    # Connection details.
    imei = 1234
    topic = "world/poc-ultim-zenaterra/" + str(imei)
    payload = "payload"
    hostname = "localhost"
    port = 1883
#    hostname = "37.58.164.129"
#    port = 5053

    # Input.
    metadata = {'lat': 123,
                'lon': 456,
                'ele': 789,
                'created_at': 123456789
               }

    # Send encoded input to MQTT broker
    send_data(topic, encode_to_protobuf(metadata), hostname, port)

    print("Finished.")
