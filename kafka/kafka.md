# How to start kafka

1. Start Zookeeper
```bash
bin/zookeeper-server-start.sh config/zookeeper.properties
```

2. Start Kafka
```bash
bin/kafka-server-start.sh config/server.properties
```


3. Create topic
```bash
bin/kafka-topics.sh --create --zookeeper localost:2181 --replication-factor 1 --partitions 1 --topic streaming-demo
```