class FooBar:
    def __init__(self, n):
        self.n = n
        self.foo_e = threading.Event()
        self.bar_e = threading.Event()
        self.foo_e.set()  # Allow `foo` to start first

    def foo(self, printFoo: 'Callable[[], None]') -> None:
        for i in range(self.n):
            self.foo_e.wait()  # Wait until it's `foo`'s turn
            printFoo()  # Print "foo"
            self.foo_e.clear()  # Reset `foo` event
            self.bar_e.set()  # Signal `bar` to proceed

    def bar(self, printBar: 'Callable[[], None]') -> None:
        for i in range(self.n):
            self.bar_e.wait()  # Wait until it's `bar`'s turn
            printBar()  # Print "bar"
            self.bar_e.clear()  # Reset `bar` event
            self.foo_e.set()  # Signal `foo` to proceed
