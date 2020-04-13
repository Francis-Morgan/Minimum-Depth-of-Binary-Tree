# Minimum-Depth-of-Binary-Tree

## About task
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
 A leaf is a node with no children.

##### For example

## Solution ideas
We have two options: depth-first search (**DFS**) and breadth-first search (**BFS**).

In my program, I used depth-first search.
#### Briefly about the differences.
wait

## How does the program work?
DFS explores all possible paths down to some leaf in the tree, goes back and explores another path (thus doing a search with a return). 

We check every node, check if it is a leaf node. If yes, then return 1.

If the node has no left sub-tree, then check  the right sub-tree.

If the node has no right sub-tree, then check the left sub-tree.

If the node has both right and left descendants, we check both subtrees using the algorithm described above. 
##### For example
We have a tree:

![](https://github.com/chichikow/Minimum-Depth-of-Binary-Tree/blob/master/bin.png)

The DFS will give results: 8-3-1-6-10-14.

1. Start at the root (8).
2. Go to the left descendant (3).
3. Then go to the left descendant (1).  (This node has no descendants)
4. Return and transition to the right descendant (6). (This node has no descendants)
5. Return to the root node and move to the right progeny (10). (This node have a right descendants)
6. Return and transition to the right descendant (14). (This node has no descendants)

Done.


## Code explanation 
[There](https://github.com/chichikow/Minimum-Depth-of-Binary-Tree/blob/master/min_depth.py) you can see in programm.


