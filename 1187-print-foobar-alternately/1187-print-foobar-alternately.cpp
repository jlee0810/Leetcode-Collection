#include <semaphore.h>

class FooBar {

private:
    int n;
    sem_t foo_lock;
    sem_t bar_lock;

public:
    FooBar(int n) {
        this->n = n;
        sem_init(&foo_lock, 0, 0);
        sem_init(&bar_lock, 0, 1);
    }

    void foo(function<void()> printFoo) {
        
        for (int i = 0; i < n; i++) {
            sem_wait(&bar_lock);
        	// printFoo() outputs "foo". Do not change or remove this line.
        	printFoo();
            sem_post(&foo_lock);
        }
    }

    void bar(function<void()> printBar) {
        
        for (int i = 0; i < n; i++) {
            sem_wait(&foo_lock);
        	// printBar() outputs "bar". Do not change or remove this line.
        	printBar();
            sem_post(&bar_lock);
        }
    }
};