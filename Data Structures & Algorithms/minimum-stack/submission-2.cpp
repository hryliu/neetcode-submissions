class MinStack {
public:
    vector<int> stack;
    vector<int> minStack;

    MinStack() {
        // Constructor (no initialization needed)
    }
    
    void push(int val) {
        stack.push_back(val);
        // If minStack is empty or val <= current min, push it
        if (minStack.empty() || val <= minStack.back()) {
            minStack.push_back(val);
        }
    }
    
    void pop() {
        // If popped value is also current min, pop from both
        if (stack.back() == minStack.back()) {
            minStack.pop_back();
        }
        stack.pop_back();
    }
    
    int top() {
        return stack.back();
    }
    
    int getMin() {
        return minStack.back();
    }
};