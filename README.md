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

I think the best option is to show the work of this script on the example of the tree described above. 

So the first thing we do is check the root of the tree. If it has the type **None**, return 0.

We can still use this design because our algorithm is recursive.

    if root==None:
        return 0

Ok, our tree's not empty, so let's check the following conditions.

    if root.left==None and root.right==None: 
        return 1
 
This condition is looking for a leaf. If our tree had no roots, its depth would be 1.

We check the following 2 conditions. 

     if root.left==None:
            return self.minDepth(root.right)+1
        
     if root.right==None:
            return self.minDepth(root.left)+1
          
As long as our tree does not meet these conditions, we will return to them later.

That leaves the last one.

    return min(self.minDepth(root.left)+1,self.minDepth(root.right)+1)
   
This is a recursive call to our function. We are looking for the leaves of the tree and their depth.

The left root of our subtree with value 3 is transferred to our function.

She'll go the same way, only with her sub-trees.

**Note that the test always starts with the left.**

Then they will recursively return min-values with summation 1.

But a sheet with a value of 1 will meet the second condition and return 1. Same for the right.

I tried to portray it:

![](https://github.com/chichikow/Minimum-Depth-of-Binary-Tree/blob/master/example.png)

After checking the left sub-tree, we check the right one. It has a similar algorithm, but it has a node with only one descendant.
