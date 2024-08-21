from kafka import TopicPartition, KafkaConsumer
from json import loads
import os

OFFSET_FILE = 'consumer_offset.txt'

def save_offset(offset):
	with open(OFFSET_FILE, 'w') as f:
		f.write(str(offset))

def read_offset():
	if os.path.exists(OFFSET_FILE):
		with open(OFFSET_FILE, 'r') as f:
			return int(f.read().strip())
	return None

saved_offset = read_offset()
consumer = KafkaConsumer(
#	'topic1',
	bootstrap_servers=['localhost:9092'],
	value_deserializer=lambda x: loads(x.decode('utf-8')),
	consumer_timeout_ms=5000,
	auto_offset_reset='earliest' if saved_offset is None else 'none',
	group_id='fbi3',
	enable_auto_commit=True
)

print("Start consumer")

p = TopicPartition('topic1', 0)
consumer.assign([p])

if saved_offset is not None:
	consumer.seek(p, saved_offset)
else:
	consumer.seek_to_beginning(p)

for m in consumer:
	print(f"topic={m.topic}, offset={m.offset}")
	save_offset(m.offset)
print("End consumer")
