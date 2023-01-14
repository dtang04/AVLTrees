class Empty:
    
    def __init__(self):
        pass

    def is_empty(self):
        return True

    def is_leaf(self):
        return False

    def num_nodes(self):
        return 0

    def height(self):
        return 0

    def contains(self, n):
        return False

    def insert(self, n):
        return Node(n, Empty(), Empty())
    
    def min_item(self):
        return
    
    def max_item(self):
        return
    
    def balance_factor(self):
        return 0
    
    def balanced_everywhere(self):
        return True

class Node:
    def __init__(self,value,left,right):
        self.value = value
        self.left = left
        self.right = right

    def insert(self, n): 
        """
        We insert as we would a regular BST, but at each level we check
        for tree balance, and then rotate if the tree is sufficiently
        unbalanced.
        """
        if n < self.value:
            t = Node(self.value, self.left.insert(n), self.right)
        elif n > self.value:
            t = Node(self.value, self.left, self.right.insert(n))
        else:
            return self
        
        if abs(t.balance_factor()) > 1:
            if t.left_heavy():
                if t.left.left_heavy(): #left-left imbalance
                    return t.right_rot()
                else: #left-right imbalance
                    t2 = Node(t.value,t.left.left_rot(),t.right)
                    return t2.right_rot()
            else:
                if t.right.right_heavy(): #right-right imbalance
                    return t.left_rot()
                else: #right-left imbalance
                    t2 = Node(t.value,t.left,t.right.right_rot())
                    return t2.left_rot()
        else: #tree is balanced enough, just return
            return t


    def height(self):
        return 1 + max(self.left.height(), self.right.height())
    
    def balance_factor(self):
        left = self.left.height()
        right = self.right.height()
        return right - left
    
    def right_rot(self):
        x = self.value
        k = self.left.value
        t1 = self.left.left
        t2 = self.left.right
        t3 = self.right
        return Node(k,t1,Node(x,t2,t3))
    
    def left_rot(self):
        x = self.value
        t1 = self.left
        k = self.right.value
        t2 = self.right.left
        t3 = self.right.right
        return Node(k,Node(x,t1,t2),t3)
    
    def left_heavy(self):
        return self.balance_factor() < 0
    
    def right_heavy(self):
        return self.balance_factor() > 0
    
    def inorder(self):
        lst = []
        if self.left.is_empty() == True and self.right.is_empty() == True:
            return [self.value]
        if self.left.is_empty() == False:
            lst += self.left.inorder()
            lst.append(self.value)
        if self.right.is_empty() == False:
            if self.value not in lst:
                lst.append(self.value)
            lst += self.right.inorder()
        return lst

    def is_empty(self):
        return False

#Tester
nums = list(range(1,1001))
avl = Empty()
for i in nums:
    avl = avl.insert(i)
print(avl.balance_factor())