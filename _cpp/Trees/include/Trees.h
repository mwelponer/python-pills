#pragma once
#include "Utils.h"
#include <algorithm>

using namespace mike;

class Trees {
private:
    int res = -1;
public:
    /////////////////////////// invert a binary tree
    TreeNode* invertTree(TreeNode* root);

    /////////////////////////// depth of a binary tree
    int maxDepth_dfs(TreeNode* root);
    int maxDepth(TreeNode* root);
    
    /////////////////////////// tree diameter
    int diameterOfBinaryTree_dfs(TreeNode* root);
    int diameterOfBinaryTree(TreeNode* root);
    
    /////////////////////////// is binary tree balanced
    std::pair<int, bool> isBalanced_dfs(TreeNode* root);
    bool isBalanced(TreeNode* root);
};