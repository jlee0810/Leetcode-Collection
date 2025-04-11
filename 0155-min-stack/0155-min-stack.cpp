class MinStack {
private:
    stack<int> sstack;
    stack<int> min_stack;

public:
    MinStack() {
        
    }
    
    void push(int val) {
        if (min_stack.size() && min_stack.top() < val) {
            min_stack.push(min_stack.top());
        }
        else {
            min_stack.push(val);
        }
        sstack.push(val);
    }
    
    void pop() {
        sstack.pop();
        min_stack.pop();
    }
    
    int top() {
        return sstack.top();
    }
    
    int getMin() {
        return min_stack.top();
    }
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(val);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */