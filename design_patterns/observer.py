"""
The Observer pattern defines a one-to-many dependency between objects 
so that when one object changes state, all its dependents are notified 
and updated automatically.
"""


class Subject:
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
        raise NotImplementedError


class ConcreteObserver(Observer):
    def update(self, subject):
        print("Observer updated with subject state:", subject.state)


class ConcreteSubject(Subject):
    def __init__(self):
        super().__init__()
        self._state = None

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, state):
        self._state = state
        self.notify()


# Example usage
subject = ConcreteSubject()
observer1 = ConcreteObserver()
observer2 = ConcreteObserver()
subject.attach(observer1)
subject.attach(observer2)
subject.state = "New State"
# Output:
# Observer updated with subject state: New State
# Observer updated with subject state: New State
