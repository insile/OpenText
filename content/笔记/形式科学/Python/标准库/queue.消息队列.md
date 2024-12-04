##### queue.消息队列
```python
from threading import Thread  
from queue import Queue  
  
  
class MsgProducer(Thread):  
    # 生产者线程，生产消息放进队列，阻塞至全部放进去  
    def __init__(self, name: str, count: int, queue: Queue):  
        super().__init__()  
  
        self.setName(name)  
        self.count = count  
        self.queue = queue  
  
    def run(self) -> None:  
        for n in range(self.count):  
            msg = f'{self.getName()} - {n}'  
            self.queue.put(msg, block=True)  
  
  
class MsgConsumer(Thread):  
    # 消费者线程，队列提取消息  
    def __init__(self, name: str, queue: Queue, pth: Thread):  
        super().__init__()  
  
        self.setName(name)  
        self.queue = queue  
        self.pth = pth  
  
    def run(self) -> None:  
        while self.pth.is_alive() or not self.queue.empty():  
            msg = self.queue.get(block=True)  
            print(f'{self.getName()} - {msg}\n', end='')  
  
  
nqueue = Queue(3)  
threads = list()  
threads.append(MsgProducer('PA', 5, nqueue))  
threads.append(MsgProducer('PB', 5, nqueue))  
  
threads.append(MsgConsumer('CA', nqueue, threads[0]))  
threads.append(MsgConsumer('CB', nqueue, threads[1]))  
  
for t in threads:  
    t.start()  
  
for t in threads:  
    t.join()
```