from kafka import KafkaProducer
import time
import json
from tqdm import tqdm
prod = KafkaProducer(
	bootstrap_servers=['localhost:9092'],
	value_serializer=lambda x:json.dumps(x).encode('utf-8'),
)

start = time.time()

for i in tqdm(range(10)):
	data = {'str':'value' + str(i)}
	prod.send('topic1', value=data)
	prod.flush()

end = time.time()
print("[DONE with time]:", end - start)
