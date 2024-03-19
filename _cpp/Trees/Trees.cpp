#include "Trees.h"

TreeNode* Trees::invertTree(TreeNode* root){
    if (!root)
        return root;
    
    TreeNode* left = root->left;
    TreeNode* right = root->right;
    root->left = invertTree(right);
    root->right = invertTree(left);

    return root;
}

/////////////////////////// depth of a binary tree
int Trees::maxDepth_dfs(TreeNode* root) {
    if (root == nullptr)
        return 0;
    return 1 + std::max(maxDepth_dfs(root->left), maxDepth_dfs(root->right));
}

int Trees::maxDepth(TreeNode* root) {      
    return maxDepth_dfs(root);
}

/////////////////////////// tree diameter
int Trees::diameterOfBinaryTree_dfs(TreeNode* root){
    if (!root)
        return -1;

    int left = diameterOfBinaryTree_dfs(root->left);
    int right = diameterOfBinaryTree_dfs(root->right);

    int diameter = std::max(left, right) + 2;
    res = std::max(res, diameter);

    return 1 + std::max(left, right);
}

int Trees::diameterOfBinaryTree(TreeNode* root){
    diameterOfBinaryTree_dfs(root);
    return res;
}

/////////////////////////// is binary tree balanced
std::pair<int, bool> Trees::isBalanced_dfs(TreeNode* root){
    if (!root)
        return {-1, true};
    
    std::pair<int, bool> ressL = isBalanced_dfs(root->left);
    std::pair<int, bool> ressR = isBalanced_dfs(root->right);
    int leftH = 1 + ressL.first;
    int rightH = 1 + ressR.first;
    int height = std::max(leftH, rightH);
    
    return {height, std::abs(leftH - rightH) <= 1 && ressL.second && ressR.second};
}

bool Trees::isBalanced(TreeNode* root) {
    return isBalanced_dfs(root).second;
}


int main(){
    TreeNode* root;

    Trees tr;

    /* 1. Given the root of a binary tree, invert the tree, and return its root. */
    std::cout << "\nInvert Binary Tree" << std::endl;

    root = new TreeNode(4, new TreeNode(2, new TreeNode(1), 
        new TreeNode(3)), new TreeNode(7, new TreeNode(6), new TreeNode(9)));
    root->print();
    tr.invertTree(root)->print();

    delete root;

    /* 2. Given the root of a binary tree, return its maximum depth.
    A binary tree's maximum depth is the number of nodes along the longest path 
    from the root node down to the farthest leaf node.
    */
    std::cout << "\nMaximum Depth of Binary Tree" << std::endl;
    root = new TreeNode(3, new TreeNode(9), new TreeNode(20, 
        new TreeNode(15), new TreeNode(7)));
    root->print();
    std::cout << tr.maxDepth(root) << std::endl;

    delete root;

    /* 3. Given the root of a binary tree, return the length of the diameter of 
    the tree. The diameter of a binary tree is the length of the longest path 
    between any two nodes in a tree. This path may or may not pass through the root.
    The length of a path between two nodes is represented by the number of edges 
    between them.
    */
    std::cout << "\nDiameter of Binary Tree" << std::endl;
    root = new TreeNode(1, new TreeNode(2, new TreeNode(4), new TreeNode(5)), new TreeNode(3));
    root->print();
    std::cout << tr.diameterOfBinaryTree(root) << std::endl;


    /* 4. Given a binary tree, determine if it is height-balanced.
    */
    std::cout << "\nBalanced Binary Tree" << std::endl;
    root = new TreeNode(3, new TreeNode(9), new TreeNode(20, new TreeNode(15), new TreeNode(7)));
    root->print();
    std::cout << tr.isBalanced(root) << std::endl;
}