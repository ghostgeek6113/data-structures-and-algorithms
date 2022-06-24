from collections import deque


class StackArray:
    """
    Stack implementation with the list
    """

    def __init__(self):
        self.stack = []

    def pop(self):
        """
        Check whether the stack is empty. If empty, pass. If not, then remove the last element in the stack (
        implemented in an array)
        :return: stack without the last element (last element inserted in the stack)
        """
        if self.is_empty():
            return
        return self.stack.pop()

    def push(self, data):
        """
        add data to the stack
        """
        self.stack.append(data)

    def is_empty(self):
        """
        Check the stack is empty or not.
        :return: boolean
        """
        if len(self.stack) == 0:
            return True
        return False

    def peek(self):
        """
        print the last element in the stack (last element in the list)
        """
        if self.is_empty():
            print("stack is empty")
        else:
            print(self.stack[-1])

    def print_stack(self):
        """
        print the stack
        """
        stack_values = ''
        if self.is_empty() is False:
            for each in self.stack:
                stack_values += str(each) + "---"
            print(stack_values)
        else:
            print("Stack is empty")


class Node:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class StackWithLinkedList:
    def __init__(self):
        self.head = None

    def pop(self):
        if self.head is None:
            return "Stack empty"
        elif self.head.next is None:
            temp = self.head.data
            self.head = None
            return "{} removed".format(temp)
        else:
            temp = self.head.data
            self.head = self.head.next
            self.head.prev = None
            return "{} removed".format(temp)

    def push(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            node = Node(data, self.head, None)
            self.head.prev = node
            self.head = node

    def peek(self):
        if self.head is None:
            return "Stack empty"
        else:
            print(self.head.data)
            return self.head.data

    def is_empty(self):
        if self.head is None:
            return True
        return False

    def print_stack(self):
        stack_values = ''
        itr = self.head
        if self.is_empty():
            return "Stack empty"
        else:
            while itr:
                stack_values += str(itr.data) + '--->'
                itr = itr.next
        print(stack_values)

    def get_size(self):
        if self.head is None:
            return 0
        itr = self.head
        count = 0
        while itr:
            count += 1
            itr = itr.next


class StackWithCollections:
    def __init__(self):
        self.stack = deque()

    def pop(self):
        self.stack.pop()

    def push(self, data):
        self.stack.appendleft(data)

    def peek(self):
        return self.stack[0]

    def get_size(self):
        return len(self.stack)

    def print_stack(self):
        print(self.stack)
