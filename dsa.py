# # 1. Delete the elements in an linked list whose sum is equal to zero======================================


class Node:
    def __init__(self, data=0):
        self.data = data
        self.next = None


def delete_zero_sum_nodes(head):
    dummy = Node(0)
    dummy.next = head

    current = dummy
    while current:
        sum = 0
        node = current.next
        while node:
            sum += node.data
            if sum == 0:
                current.next = node.next
                break
            node = node.next
        if not node:
            current = current.next

    return dummy.next


# Example usage:
head = Node(3)
head.next = Node(4)
head.next.next = Node(-7)
head.next.next.next = Node(5)
head.next.next.next.next = Node(-6)
head.next.next.next.next.next = Node(6)
head.next.next.next.next.next.next = Node(-4)

print("Original linked list:")
current = head
while current:
    print(current.data, end=" -> ")
    current = current.next
print("None")

modified_head = delete_zero_sum_nodes(head)

print("Modified linked list:")
current = modified_head
while current:
    print(current.data, end=" -> ")
    current = current.next
print("None")




# 2. Reverse a linked list in groups of given size===================================================


class Node:
  
    def __init__(self, data):
        self.data = data
        self.next = None
  
class LinkedList:
  
    def __init__(self):
        self.head = None
  
    def reverse(self, head, k):
        
        if head == None:
          return None
        current = head
        next = None
        prev = None
        count = 0

        while(current is not None and count < k):
            next = current.next
            current.next = prev
            prev = current
            current = next
            count += 1
  
        # next is now a pointer to (k+1)th node
        # recursively call for the list starting
        # from current. And make rest of the list as
        # next of first node
        if next is not None:
            head.next = self.reverse(next, k)
  
       
        return prev
  
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
  
  
    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data,end=' ')
            temp = temp.next
  
  
# Driver program
llist = LinkedList()
llist.push(9)
llist.push(8)
llist.push(7)
llist.push(6)
llist.push(5)
llist.push(4)
llist.push(3)
llist.push(2)
llist.push(1)
  
print("Given linked list")
llist.printList()
llist.head = llist.reverse(llist.head, 3)
  
print ("\nReversed Linked list")
llist.printList()




# 3. Merge a linked list into another linked list at alternative positions===============================

class Node(object):
	def __init__(self, data:int):
		self.data = data
		self.next = None
class LinkedList(object):
	def __init__(self):
		self.head = None
		
	def push(self, new_data:int):
		new_node = Node(new_data)
		new_node.next = self.head
		
		self.head = new_node
		
	def printList(self):
		temp = self.head
		while temp != None:
			print(temp.data)
			temp = temp.next
			
	def merge(self, p, q):
		p_curr = p.head
		q_curr = q.head
		while p_curr != None and q_curr != None:


			p_next = p_curr.next
			q_next = q_curr.next
			q_curr.next = p_next 
			p_curr.next = q_curr 

			p_curr = p_next
			q_curr = q_next
			q.head = q_curr

llist1 = LinkedList()
llist2 = LinkedList()
llist1.push(1)
llist1.push(2)
llist1.push(3)
llist1.push(4)

for i in range(8, 3, -1):
	llist2.push(i)
print("First Linked List:")
llist1.printList()
print("Second Linked List:")
llist2.printList()
llist1.merge(p=llist1, q=llist2)
print("Modified first linked list:")
llist1.printList()
print("Modified second linked list:")
llist2.printList() 

# 4.In an array count pairs with given sum  ==============================================================


def count_pairs_with_given_sum(array, target_sum):
    freq = {}
    count = 0

    for num in array:
        complement = target_sum - num
        if complement in freq:
            count += freq[complement]
        freq[num] = freq.get(num, 0) + 1

    return count



array = [1, 5, 3, 7, 2, 4, 6, 8, 9, 6]
target_sum = 10

pairs_count = count_pairs_with_given_sum(array, target_sum)

print("Number of pairs with the sum", target_sum, ":", pairs_count)




# 5 Find duplicates in an array   =======================================================================


def find_duplicates(array):
    unique_set = set()
    duplicates = []

    for num in array:
        if num in unique_set:
            duplicates.append(num)
        else:
            unique_set.add(num)

    return duplicates



array = [1, 2, 3, 4, 5, 2, 4, 6, 7, 8, 4, 9, 1, 1]
duplicate_elements = find_duplicates(array)

print("Duplicate elements:", duplicate_elements)





# 6 . Find the Kth largest and Kth smallest number in an array =============================================


def kth_smallest_largest(array, k):
    sorted_array = sorted(array)
    kth_smallest = sorted_array[k - 1]
    kth_largest = sorted_array[-k]
    return kth_smallest, kth_largest



array = [3, 7, 1, 5, 2, 4, 6]
k = 3
kth_smallest, kth_largest = kth_smallest_largest(array, k)

print("Kth smallest:", kth_smallest)
print("Kth largest:", kth_largest)




# 7. Move all the negative elements to one side of the array ============================================


def move_negatives(array):
    left = 0
    right = len(array) - 1
    
    while left <= right:
        if array[left] < 0 and array[right] < 0:
            left += 1
        elif array[left] >= 0 and array[right] < 0:
            array[left], array[right] = array[right], array[left]
            left += 1
            right -= 1
        elif array[left] >= 0 and array[right] >= 0:
            right -= 1
        else:
            left += 1
            right -= 1


array = [-2, 3, -7, 1, -4, 0, 6, -5, -6]
move_negatives(array)
print(array)



# 8. Reverse a string using stack data structure =======================================

def reverse_string(string):
    stack = []
    reversed_string = ""
    
    for char in string:
        stack.append(char)
    
 
    while stack:
        reversed_string += stack.pop()
    
    return reversed_string


string = input("enter a string:")
reversed_string = reverse_string(string)
print(reversed_string)



# 9. Evaluate a postfix expression using stack ===============================================================

class Evaluate:
	
	def __init__(self, capacity):
		self.top = -1
		self.capacity = capacity
		self.array = []
	
	def isEmpty(self):
		return True if self.top == -1 else False

	def peek(self):
		return self.array[-1]
	
	def pop(self):
		if not self.isEmpty():
			self.top -= 1
			return self.array.pop()
		else:
			return "$"
	
	def push(self, op):
		self.top += 1
		self.array.append(op)

	def evaluatePostfix(self, exprsn):
		
		for i in exprsn:
			
			if i.isdigit():
				self.push(i)

			else:
				val1 = self.pop()
				val2 = self.pop()
				self.push(str(eval(val2 + i + val1)))
				return int(self.pop())
				
exprsn = "231*+9-"
obj = Evaluate(len(exprsn))
print ("postfix evaluation of the given one : %d"%(obj.evaluatePostfix(exprsn)))




# 10. Implement a queue using the stack data structure ===================================


class Queue:
    def __init__(self):
        self.in_stack = []    
        self.out_stack = []  

    def enqueue(self, item):
        self.in_stack.append(item)

    def dequeue(self):
        if not self.out_stack:
            
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        if not self.out_stack:
            return None   
        return self.out_stack.pop()

    def is_empty(self):
        return not self.in_stack and not self.out_stack

    def size(self):
        return len(self.in_stack) + len(self.out_stack)
obj = Queue()
obj.enqueue(1)
obj.enqueue(2)
obj.enqueue(3)
obj.enqueue(4)


print(obj.dequeue())
print(obj.dequeue())
print(obj.dequeue())
print(obj.dequeue())


# ------------------------------------------------------------------------------------------------------------------------------------