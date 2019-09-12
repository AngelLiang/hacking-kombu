
- `kombu/asynchronous`：异步操作的 函数 和 类
- `kombu/transport`：兼容各种 MQ 的类
- `kombu/utils`: 一些辅助 函数 和 类

`kombu/entity.py`: 实体类，主要包括`Exchange`和`Queue`。

Kombu 的概念

- Message：生产消费的基本单位，其实就是我们所谓的一条条消息
- Connection：对 MQ 连接的抽象，一个 Connection 就对应一个 MQ 的连接
- Transport：真实的 MQ 连接，也是真正连接到 MQ(redis/rabbitmq) 的实例
- Producers: 发送消息的抽象类
- Consumers：接受消息的抽象类
- Exchange：MQ 路由，这个和 RabbitMQ 差不多，支持 5 类型
- Queue：对应的 queue 抽象，其实就是一个字符串的封装
