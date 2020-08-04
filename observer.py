class Observable:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)
    
    def notify(self):
        for observer in self._observers:
            observer.update(self)

class Observer:
    def update(self, subject):
        pass

class Event:
    def __init__(self):
        self._subscribers = []
    
    def register(self, method):
        self._subscribers.append(method)

    def unregister(self, method):
        self._subscribers.remove(method)

    def call(self, arg):
        for subscriber in self._subscribers:
            subscriber(arg)