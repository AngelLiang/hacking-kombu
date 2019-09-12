from __future__ import absolute_import, unicode_literals, print_function

from kombu import Connection  # noqa


with Connection('amqp://guest:guest@localhost:5672//') as conn:
    simple_queue = conn.SimpleQueue('simple_queue')  # 创建队列
    message = simple_queue.get(block=True, timeout=1)  # 接收消息
    print('Received: {0}'.format(message.payload))
    message.ack()
    simple_queue.close()  # 关闭队列
