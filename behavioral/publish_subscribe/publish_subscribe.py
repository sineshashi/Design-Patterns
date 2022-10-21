'''
In observer pattern, we defined the observer class, which consisted of the obserables and observable class defined a function update_all() to update every observer on every change.

But in publish subscribe pattern, author do not need to know about his subscribers but subscribers also do not need to observe the author.
In this way, we need more decoupling in the pattern than that in observer pattern.
'''
class Subscriber:
    def process(self, observed):
        print("Observing: {}".format(observed))
class Publisher:
    def __init__(self):
        self.subscribers = set()
    def subscribe(self, subscriber):
        self.subscribers.add(subscriber)
    def unsubscribe(self, subscriber):
        self.subscribers.discard(subscriber)
    def unsubscribe_all(self):
        self.subscribers = set()
    def publish(self):
        for subscriber in self.subscribers:
            subscriber.process(self)

'''The above is the implementation by observer pattern in which publisher need to store the subscribers and subsrciber too need to know about the publisher. Which we do not want any more now.

We can decouple these using a thrid class, messages and both the classes use it. Publisher writes the msg and subsriber consumes it.'''

class Message:
    def __init__(self):
        self.payload = None

class Subscriber:
    def process(self, message):
        print(message.payload)
class Publisher:
    def __init__(self):
        self.subscribers = set()
    def subscribe(self, subscriber):
        self.subscribers.add(subscriber)
    def unsubscribe(self, subscriber):
        self.subscribers.discard(subscriber)
    def unsubscribe_all(self):
        self.subscribers = set()
    def publish(self, message):
        for subscriber in self.subscribers:
            subscriber.process(message)

'''In this way, we made subsriber unknown about the publisher. Now we need to remove this link too. For that, we use a dispatcher which dispatches the msgs to subsriber and takes msg from publisher.'''

class Message:
    def __init__(self):
        self.payload = None

class Dispatcher(object):
    def __init__(self):
        self.subscribers = set()
    def subscribe(self, subscriber):
        self.subscribers.add(subscriber)
    def unsubscribe(self, subscriber):
        self.subscribers.discard(subscriber)
    def unsubscribe_all(self):
        self.subscribers = set()
    def send(self, message):
        for subscriber in self.subscribers:
            subscriber.process(message)

class Subscriber:
    def __init__(self, dispatcher):
        dispatcher.subscribe(self)
    def process(self, message):
        print(message.payload)

class Publisher:
    def __init__(self, dispatcher):
        self.dispatcher = dispatcher
    def process(self, message):
        self.dispatcher.send(message)

'''In this way, we only need to change dispatcher class obeject to subsribe or publish. This is the concept equivalent of many to many relationships in relational database where we need a third a table to relate the two tables.'''