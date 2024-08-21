from kafka import KafkaConsumer
from json import loads

consumer = KafkaConsumer(
	'chat',
	bootstrap_servers=['localhost:9092'],
	auto_offset_reset='earliest',
	enable_auto_commit=True,
	group_id='chat-group',
	value_deserializer=lambda x: loads(x.decode('utf-8'))
)

print('Chating Program - Message sending')

print('Waiting message...')

try:
	for m in consumer:
		data = m.value
		print(f"[FRIENDS!!] {data['message']}")

except KeyboardInterrupt:
	print('Ending chat')
finally:
	consumer.close()
