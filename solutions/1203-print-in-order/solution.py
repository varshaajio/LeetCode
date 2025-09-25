import threading

class Foo(object):
    def __init__(self):
        # Events start in "unset" state
        self.first_done = threading.Event()
        self.second_done = threading.Event()

    def first(self, printFirst):
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        # Signal that first() is done
        self.first_done.set()

    def second(self, printSecond):
        # Wait until first() is done
        self.first_done.wait()
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        # Signal that second() is done
        self.second_done.set()

    def third(self, printThird):
        # Wait until second() is done
        self.second_done.wait()
        # printThird() outputs "third". Do not change or remove this line.
        printThird()

