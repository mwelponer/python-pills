#include "Stack.h"
#include <stack>
#include <iostream>
#include <vector>
#include "MinStack.h"

bool Stack::isValid(std::string s){
    if (s.length() % 2 != 0)
        return false;

    std::stack<int> st;

    for (int i=0; i < s.length(); i++){
        //std::cout << s.at(i) << " ";
        char ch = s.at(i);
        if (ch == '(' or ch == '[' or ch == '{')
            st.push(ch);
        else
            if (st.empty()) 
                return false;
            else if (    (ch == ')' && st.top() != '(') or  
                    (ch == ']' && st.top() != '[') or 
                    (ch == '}' && st.top() != '{') )
                return false;
            else
                st.pop();
    }

    return !st.size();        
}

int main(){
    std::string s;

    Stack st;

    /* 1. Given a string s containing just the characters '(', ')', '{', '}', 
    '[' and ']', determine if the input string is valid.

    An input string is valid if:
        1. Open brackets must be closed by the same type of brackets.
        2. Open brackets must be closed in the correct order.
        3. Every close bracket has a corresponding open bracket of the same type.*/
    std::cout << "\nIs Valid" << std::endl;

    s = "()[]{}"; std::cout << s << ": " << st.isValid(s) << std::endl;
    s = "(]"; std::cout << s << ": " << st.isValid(s) << std::endl;
    s = "(("; std::cout << s << ": " << st.isValid(s) << std::endl;
    s = "){"; std::cout << s << ": " << st.isValid(s) << std::endl;


    /* 2. Design a stack that supports push, pop, top, and retrieving the 
    minimum element in constant time.
    Implement the MinStack class:
    - MinStack() initializes the stack object.
    - void push(int val) pushes the element val onto the stack.
    - void pop() removes the element on the top of the stack.
    - int top() gets the top element of the stack.
    - int getMin() retrieves the minimum element in the stack.
    You must implement a solution with O(1) time complexity for each function.
    */
    std::cout << "\nMin Stack" << std::endl;
    MinStack ms;
    ms.push(-2);
    ms.push(0);
    ms.push(-3);
    std::cout << ms.getMin() << std::endl;
    ms.pop();
    std::cout << ms.top() << std::endl;
    std::cout << ms.getMin() << std::endl;

}