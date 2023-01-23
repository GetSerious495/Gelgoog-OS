import paho.mqtt.client as mqtt

#(Copy)

host  = 'test.mosquitto.org'
port = 1883
group = 'calculus2'
yourname = 'kotchaporn'
topic = group + '/' + yourname
username = ''
password = ''

client = mqtt.Client()
client.username_pw_set(username, password)
client.connect(host, port)

data = 6909
print('Input Data Type : {}'.format(type(data)))

try:
    client.publish(topic = topic, payload = data, qos = 0, retain = True)
    print('Publish Success')
except:
    print('Failed')
