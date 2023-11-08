from flask import Flask, render_template

from paho.mqtt import client as mqtt_client

app = Flask(__name__)
#Set the Hostname, Port & TopicName
broker = 'broker.emqx.io'
port = 1883
topic = "topicName/space"
client_id = 'test'
username = 'emqx'
password = ''

def connect_mqtt():
    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)
    client.connect(broker, port)
    return client

#Define the button page of the web application
@app.route('/main', methods = ['POST'])
def main():
    return render_template('main.html')

#Define the Release Orbital Arm button and connect with MQTT server
@app.route('/1', methods=["POST"])
def empty():
    empty_test()
    return render_template('1.html')
def empty_test():
    client = connect_mqtt()
    client.loop_start()
#Define the Main Engine Test button and connect with MQTT server

@app.route('/2', methods=["POST"])
def roomEntered():
    roomEntered_test()
    return render_template('2.html')

def roomEntered_test_test():
    client = connect_mqtt()
    client.loop_start()

if __name__ == "__main__":
    app.run(port=5001)





