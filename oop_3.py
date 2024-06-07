class Node:
    def init(self, val):
        self.val = val
        self.left = None
        self.right = None

    def n(self):
        node = self
        score = 0
        while node is not None:
            print(node.val)
            s1 = input("answer? ")
            s2 = input("True or False (T or F)= ")
            if s2 == "T":
                node = node.left
                score += 1
                print("score =", score)
                print("----------------------")
            else:
                node = node.right
                if node is not None:  
                    print(node.val)
                    s3 = input("answer? ")
                    s4 = input("True or False (T or F)= ")
                    if s4 == "T":
                        node = node.left
                        score += 1
                        print("score =", score)
                        print("----------------------")
                    else:
                        node = None  
                        print("score =", score)
                        print("--------Finish--------------")
            if node is None:
                print("--------Finish--------------")



node1 = Node("Question 1")
node2 = Node("Question 2")
node3 = Node("Question 3")
node4 = Node("Correct Answer 1")
node5 = Node("Wrong Answer 1")
node6 = Node("Correct Answer 2")
node7 = Node("Wrong Answer 2")

node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node3.left = node6
node3.right = node7


node1.n()