import paho.mqtt.client as mqtt
import json

#(Copy)
#-------------------------------------------------------------------------#

host  = 'test.mosquitto.org'
port = 1883
group = 'calculus2'
yourname = 'Kotchaporn'
topic = group + '/' + yourname
username = ''
password = ''

#--------------------------------------------------------------------------#

client = mqtt.Client()
client.username_pw_set(username, password)
client.connect(host, port)

#---------------Define a data-----------------------#

data = {}
data['name'] = 'Kotchaporn Chunhakuntaros'
data['nickname'] = 'Friend'
data['age'] = '19'
data['occupation'] = ['student']
data['com-lang'] = ['Python', 'C#']
data['table'] = 0
print('Original Input Data Type : {}'.format(type(data)))

data = json.dumps(data)
print('Converted Input Data Type : {}'.format(type(data)))

try:
    client.publish(topic = topic, payload = data, qos = 0, retain = True)
    print('Publish Success')
except:
    print('Failed')