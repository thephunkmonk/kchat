from kafka import KafkaProducer
from json import dumps
import time

p = KafkaProducer(
	
)

print("Chating program - sending message")
print("Please print your message, enter 'exit' to quit")

while True:
	msg = input("YOU: ")
	if msg.lower() == 'exit':
		break
	
	data = {'message':msg, 'time':time.time()}
print("Ending chat")
