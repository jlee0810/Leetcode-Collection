import threading

class FooBar:
    def __init__(self, n):
        self.n = n
        self.foo_e = threading.Event()
        self.bar_e = threading.Event()

        self.foo_e.set()

    def foo(self, printFoo: 'Callable[[], None]') -> None:
        for i in range(self.n):
            self.foo_e.wait()
            printFoo()
            self.foo_e.clear()
            self.bar_e.set()

    def bar(self, printBar: 'Callable[[], None]') -> None:
        for i in range(self.n):
            self.bar_e.wait()
            printBar()
            self.bar_e.clear()
            self.foo_e.set()