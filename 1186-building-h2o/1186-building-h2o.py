import threading

class H2O:
    def __init__(self):
        self.cond = threading.Condition()
        self.h_count = 0  # Count of hydrogen atoms ready
        self.o_count = 0  # Count of oxygen atoms ready

    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:
        with self.cond:
            while self.h_count == 2 and self.o_count == 0:
                self.cond.wait()  # Wait until it's possible to add hydrogen
            self.h_count += 1
            releaseHydrogen()  # Output "H"
            if self.h_count == 2 and self.o_count == 1:
                self.h_count = 0
                self.o_count = 0
            self.cond.notify_all()  # Notify one thread

    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
        with self.cond:
            while self.o_count == 1:
                self.cond.wait()  # Wait until it's possible to add oxygen
            self.o_count += 1
            releaseOxygen()  # Output "O"
            if self.h_count == 2 and self.o_count == 1:
                self.h_count = 0
                self.o_count = 0
            self.cond.notify_all()  # Notify all threads to proceed
