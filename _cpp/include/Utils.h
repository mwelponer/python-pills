#pragma once

#include <vector>
#include <iostream>
#include <sstream>
#include <queue>
#include <unordered_map>
#include <unordered_set>
#include <stack>

namespace mike {

    template<typename T>
    void printVector(const std::vector<T>& vec, bool printEndOfLine=true){
        if (vec.empty()) {
            std::cout << "[]" << std::endl;
            return;
        }

        std::cout << "[";
        auto it = vec.begin();
        std::cout << *it;
        
        while (++it != vec.end()) {
            std::cout << ", " << *it;
        }

        std::cout << "]";
        if (printEndOfLine) std::cout << std::endl;
    }

    template<typename T>
    void printVec2d(const std::vector<std::vector<T>>& vec){
        if (vec.empty()) {
            std::cout << "[]" << std::endl;
            return;
        }

        std::cout << "[";
        auto outerIt = vec.begin();
        printVector(*outerIt, false); 

        while (++outerIt != vec.end()) {
            std::cout << ", ";
            printVector(*outerIt, false);
        }

        std::cout << "]" << std::endl;        
    }

    struct ListNode {
        int val;
        ListNode* next;

        ListNode() : val(0), next(nullptr) {}
        ListNode(int val) : val(val), next(nullptr) {}
        ListNode(int val, ListNode* next) : val(val), next(next) {}

        virtual ~ListNode() {
            //std::cout << "deleting node " << val << std::endl;

            if (next) delete next;
            // ListNode* current = this;
            // while (current) {
            //     ListNode* nextNode = current->next;
            //     delete current;
            //     current = nextNode;
            // }
        }

        std::string toString() const {
            std::string s;
            const ListNode* current = this;

            while (current) {
                s += std::to_string(current->val);
                if (current->next) {
                    s += ", ";
                }
                current = current->next;
            }

            return "[" + s + "]";
        }

        void print() const {
            std::cout << this->toString() << std::endl;
        }
    };

    struct TreeNode {
        int val;
        TreeNode* left;
        TreeNode* right;

        TreeNode()
            : val(0), left(nullptr), right(nullptr){}
        TreeNode(int val) 
            : val(val), left(nullptr), right(nullptr){}
        TreeNode(int val, TreeNode* left, TreeNode* right) 
            : val(val), left(left), right(right){}
        ~TreeNode(){
            // std::cout << "deleting node " << val << std::endl;
            if (left) delete left;
            if (right) delete right;
        }

        std::string toString() const {
            std::vector<std::string> v {"["};
            
            std::queue<const TreeNode*> qu;
            qu.push(this);

            while (!qu.empty()){
                const TreeNode* t = qu.front();

                if (t){
                    v.push_back(std::to_string(t->val));
                    v.push_back(", ");
                }else{
                    v.push_back("null");
                    v.push_back(", ");
                    qu.pop();
                    continue;
                }

                qu.pop();
                qu.push(t->left);
                qu.push(t->right);

/*
                if (t) {
                    v.emplace_back(std::to_string(t->val));
                    v.emplace_back(", ");
                    qu.push(t->left);
                    qu.push(t->right);
                } else {
                    v.emplace_back("null");
                    v.emplace_back(", ");
                }
*/
            }

            while(v.back() == ", " || v.back() == "null")
                v.pop_back();

            std::stringstream ss;
            for (auto e : v)
                ss << e;

            return ss.str() + "]";
        }

        void print() const {
            std::cout << this->toString() << std::endl;
        }
    };

    class Node {
    private:
        // used to collect nodes to be deleted when the memory is freed
        void collect(std::unordered_set<Node*>& to_delete, Node* ptr) {
            //std::cout << "to_delete size: " << to_delete.size() << std::endl;
            // try to insert ptr, if it was already in the set then return
            if (not to_delete.emplace(ptr).second) {
                // std::cout << "node " << ptr->val << " already collected! size: " 
                //     << to_delete.size() << std::endl;
                return;
            // emplace returns a pair (iterator, boolean)
            // false if element was already in the set
            }

            // swap ptr->neighbors with an empty vector
            std::vector<Node*> tmp; // create an empty vector 
            std::swap(tmp, ptr->neighbors);
            // now ptr->neighbors is empty and tmp contains ptr old neighbors

            for(Node* c : tmp)       // loop over the neighbors pointers
                collect(to_delete, c);  // collect recursively
        }
    public:
        int val;
        std::vector<Node*> neighbors;
        Node() {
            val = 0;
            neighbors = std::vector<Node*>();
        }
        Node(int _val) {
            val = _val;
            neighbors = std::vector<Node*>();
        }
        Node(int _val, std::vector<Node*> _neighbors) {
            val = _val;
            neighbors = _neighbors;
        }
        ~Node() {
            // ref. https://stackoverflow.com/questions/67472213/avoid-infinite-recursion-in-destructor
            if (neighbors.empty()) return;
            
            // this part will be only for "this" node
            //std::cout << "collect baby" << std::endl;
            std::unordered_set<Node*> to_delete;
            collect(to_delete, this);
            to_delete.erase(this); // remove this from the to_delete list

            //std::cout << "to_delete size: " << to_delete.size() << std::endl;
            for (auto n : to_delete) {// delete all - they have no children by now
                //std::cout << "deleting node " << n->val << std::endl;
                delete n;
            }
        }
        bool operator<( const Node& another ) const {
            return val < another.val;
        }

        std::string toString() {
            std::unordered_map<int, Node*> map;
            // fill a map with all graph nodes
            std::stack<Node*> stack;
            stack.push(this);
            while (!stack.empty()) {
                Node* node = stack.top();
                stack.pop();
                map[node->val] = node;
                for (Node* nei : node->neighbors)
                    if (map.find(nei->val) == map.end()) 
                        stack.push(nei);
            }

            // build the stringstream
            std::stringstream ss;
            ss << "[";
            for (int i = 1; i <= map.size(); i++) {
                ss << "[";
                Node* node = map[i];
                for (Node* nei : node->neighbors){
                    ss << std::to_string(nei->val);
                    if (nei != node->neighbors.back()) ss << ", ";
                }
                ss << "]";
                if (i < map.size()) ss << ", ";
            }
            return ss.str() + "]";
            return " ";
        }

        void print(){
            std::cout << this->toString() << std::endl;
        }
    };

    Node* createNode(int val, std::unordered_map<int, Node*> map, 
        std::vector<std::vector<int>> adjlist){
        if (adjlist.size() == 0)
            return nullptr;

        // if node is not in map 
        if (map.find(val) == map.end()) {
            Node* node = new Node(val); // create it
            map[val] = node;
            for (int i : adjlist[val-1]) {
                Node* nei = createNode(i, map, adjlist);
                node->neighbors.push_back(nei);
                map[i] = nei;
            }
        }

        return map[val];
    }

    Node* buildGraph(std::vector<std::vector<int>> adjlist) {
        std::unordered_map<int, Node*> map;
        return createNode(1, map, adjlist);
    }
}

// void printVector(const std::vector<int>& vec);