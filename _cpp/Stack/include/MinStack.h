#include <stack>

class MinStack {
private:
    std::stack<int> st, min;
public:
    void push(int val) {
        st.push(val);
        if (min.empty() || min.top() >= val)
            min.push(val);
    }

    void pop() {
        int top = this->top();

        if (!min.empty() && min.top() == top)
            min.pop();
        st.pop();
    }

    int top() {
        return st.top();
    }

    int getMin() {
        return min.top();
    }
};