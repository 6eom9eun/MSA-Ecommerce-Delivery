import pika 

params = pika.URLParameters('amqps://sislvaqt:2-yxbkQ5rB8Q3nMZGif0f5nIMPYKY3bQ@dingo.rmq.cloudamqp.com/sislvaqt')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='boss')

def callback(ch, method, properties, body):
    print('Received in boss')
    print(body)

channel.basic_consume(queue='boss', on_message_callback=callback)

print('Started consuming')

channel.start_consuming()

channel.close()