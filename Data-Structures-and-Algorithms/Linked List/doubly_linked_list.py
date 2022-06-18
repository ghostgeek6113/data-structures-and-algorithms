class Node:
    def __init__(self, data=None, next=None, prev=None):
        """
        the class node will represent all the elements to be added in a single linked list
        :param data: the data that has to be parsed in the linked list
        :param next: the pointer to the next element
        """
        self.data = data
        self.next = next
        self.prev = prev


class DoublyLinkedList:
    def __init__(self):
        """
        The single linked list is initialised with a head pointer. It is to note that the head of the single linked
        list has data, next and prev attributes as soon as it becomes a done
        """
        self.head = None

    def insert_at_the_beginning(self, data):
        """
        We insert at the beginning so the head pointer is pointing to the new node created. If the head node has a
        previous pointer and is not null then we update the prev pointer to the node we just added
        :param data: data to be inserted
        """
        if self.head is None:
            node = Node(data, self.head, None)
            self.head = node
        else:
            node = Node(data, self.head, None)
            self.head.prev = node
            self.head = node

    def insert_at_the_end(self, data):
        """
        We insert at the end of the linked list. We first check whether the linked list is empty. If it is,
        then the node becomes the head node, the next and prev are None. If it is not empty we have to iterate
        through the entire list to find the end of the list then set the next pointer of the last item in the list to
        the new node (itr = itr.next) then update the next item to be the node to create, where next is None and
        prev is itr.prev
        :param data:
        :return:
        """
        if self.head is None:
            self.head = Node(data, None, None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None, itr.prev)

    def insert_value_at_index(self, data, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid index")
        if index == 0:
            self.insert_at_the_beginning(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next, itr)
                if node.next:
                    node.next.prev = node
                itr.next = node
                break
            itr = itr.next
            count += 1

    def insert_after_value(self, data_after, data_to_insert):
        if self.head is None:
            return
        if self.head.data == data_after:
            self.head.next = Node(data_to_insert, self.head.next, None)
        itr = self.head
        while itr.next:
            if itr.data == data_after:
                node = Node(data_to_insert, itr.next, itr)
                itr.next = node
                break
            itr = itr.next

    def remove_at_index(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid index")
        if index == 0:
            self.head = self.head.next
            return
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                itr.next.prev = itr.prev
                break
            itr = itr.next
            count += 1

    def remove_by_value(self, data):
        if self.head is None:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        itr = self.head
        while itr:
            if itr.data == data:
                itr.next = itr.next.next
                break
            itr = itr.next

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def get_last_node(self):
        itr = self.head
        while itr.next:
            itr = itr.next

        return itr

    def print_forward(self):
        if self.head is None:
            print("Linked list is empty")
            return

        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + '--->'
            itr = itr.next
        print(llstr)

    def print_backward(self):
        if self.head is None:
            print("Linked list is empty")
            return

        last_node = self.get_last_node()
        itr = last_node
        llstr = ''
        while itr:
            llstr += str(itr.data) + '--->'
            itr = itr.prev
        print(llstr)


if __name__ == '__main__':
    ll = DoublyLinkedList()
    ll.insert_at_the_beginning(5)
    ll.insert_at_the_beginning(20)
    ll.insert_at_the_beginning(30)
    ll.insert_after_value(20, 40)
    # ll.remove_by_value(40)
    # ll.print_backward()
    # ll.remove_at_index(2)
    ll.remove_by_value(40)
    ll.print_forward()
