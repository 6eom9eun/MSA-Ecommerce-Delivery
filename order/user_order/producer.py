import pika 

params = pika.URLParameters('amqps://sislvaqt:2-yxbkQ5rB8Q3nMZGif0f5nIMPYKY3bQ@dingo.rmq.cloudamqp.com/sislvaqt')

connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish():
    channel.basic_publish(exchange='', routing_key='boss', body = 'hello')