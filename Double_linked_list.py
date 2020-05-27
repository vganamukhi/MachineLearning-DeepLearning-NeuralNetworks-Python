# A complete working Python program to demonstrate all
# Queue operations using doubly linked list

# Node class
class Node:

    # Function to initialise the node object
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize next as null
        self.prev = None  # Initialize prev as null


# Queue class contains a Node object
class Queue:

    # Function to initialize head
    def __init__(self):
        self.head = None
        self.last = None

    # Function to add an element data in the Queue
    def enqueue(self, data):
        if self.last is None:
            self.head = Node(data)
            self.last = self.head
        else:
            self.last.next = Node(data)
            self.last.next.prev = self.last
            self.last = self.last.next

    # Function to remove first element and return the element from the queue
    def dequeue(self):

        if self.head is None:
            return None
        else:
            temp = self.head.data
            self.head = self.head.next
            #self.head.next = None
            return temp

        # Function to return top element in the queue

    def first(self):

        return self.head.data

    # Function to return the size of the queue
    def size(self):

        temp = self.head
        count = 0
        while temp is not None:
            count = count + 1
            temp = temp.next
        return count

    # Function to check if the queue is empty or not
    def isEmpty(self):
        if self.head is None:
            print(" head is none")
            return True
        else:
            #print("head is not none")
            return False

    # Function to print the stack
    def printqueue(self):

        print("queue elements are:")
        temp = self.head
        if temp is None:
            print("Queue is empty")
            return None
        else:
            while temp is not None:
                print(temp.data, end="->")
                temp = temp.next


# Code execution starts here
if __name__ == '__main__':

    # Start with the empty queue
    queue = Queue()
    queue.enqueue(6)
    queue.enqueue(12)
    queue.printqueue()
    print("\n The first element is : ", queue.first())
    print("The size of the queue is : ", queue.size())
    queue.enqueue(18)
    queue.enqueue(24)
    queue.printqueue()
    queue.dequeue()
    print("Queue follows First in First out policy")
    queue.printqueue()
    queue.dequeue()
    queue.dequeue()
    print("\n Only one element is left in the queue")
    queue.printqueue()
    #queue.dequeue()

    queue.printqueue()

    #Check if Queue is empty
    #True: if queue is empty
    #False: if queue is not empty
    print("\n Check if queue is empty: ", queue.isEmpty())
    queue.dequeue()
    print("\n Check if queue is empty: ", queue.isEmpty())