from __future__ import absolute_import, unicode_literals

import datetime

from kombu import Connection


with Connection('amqp://guest:guest@localhost:5672//') as conn:
    simple_queue = conn.SimpleQueue('simple_queue')  # 创建队列
    message = 'helloworld, sent at {0}'.format(datetime.datetime.today())
    simple_queue.put(message)  # 发送消息
    print('Sent: {0}'.format(message))
    simple_queue.close()  # 关闭队列
