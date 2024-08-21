# kchat


#### KAFKA Producer

Added python file pro.py which produces json file and shows difference in time
```bash
$ python src/kchat/kafka/pro.py
[DONE with time]: 0.02263021469116211
```

```bash
$ $KAFKA_HOME/bin/kafka-console-consumer.sh --topic topic1 --from-beginning --bootstrap-server localhost:9092

{"str": "value0"}
{"str": "value1"}
{"str": "value2"}
{"str": "value3"}
{"str": "value4"}
{"str": "value5"}
{"str": "value6"}
{"str": "value7"}
{"str": "value8"}
{"str": "value9"}
```


```bash
python src/kchat/kafka/pro_chat.py
Chating program - sending message
Please print your message, enter 'exit' to quit
YOU: hey
YOU: you
YOU: are you there
YOU: what is the thingie
YOU: 헤이요
YOU: ㄱ 저기로가요
YOU: exit
Ending chat
```
