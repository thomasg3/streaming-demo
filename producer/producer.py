from kafka import KafkaProducer 
import numpy as np 
import time




mu, sigma = 10, 1
s = np.random.normal(mu, sigma, 100)

# producer = KafkaProducer(bootstrap_servers='localhost:9092')

for value in s:
    value_bytes = value.tobytes()

    print(value)
    print(value_bytes)
    print(np.frombuffer(value_bytes, dtype=float)[0])

    time.sleep(1)