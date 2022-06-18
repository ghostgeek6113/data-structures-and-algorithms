class Node:
    def __init__(self, data=None, next=None):
        """
        the class node will represent all the elements to be added in a single linked list
        :param data: the data that has to be parsed in the linked list
        :param next: the pointer to the next element
        """
        self.data = data
        self.next = next


class SingleLinkedList:

    def __init__(self):
        """
        The single linked list is initialised with a head pointer. It is to note that the head of the single linked
        list has data and next attributes as soon as it becomes a done
        """
        self.head = None

    def insert_at_the_beginning(self, data):
        """
        We insert at the beginning so the head pointer is pointing to the new node created.
        :param data: data to be inserted
        """
        node = Node(data, self.head)
        self.head = node

    def insert_at_the_end(self, data):
        """
        We insert at the end of the linked list. We first check whether the linked list is empty. If it is,
        then the node becomes the head node and the next is None. If it is not empty we have to iterate through
        the entire list to find the end of the list then set the next pointer of the last item in the list to the
        new node
        :param data:
        :return:
        """
        if self.head is None:
            self.head = Node(data, None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def insert_values(self, values):
        """
        Inserting a list of values at the end of the linked list
        :param values: list of values to be inserted
        :return:
        """
        self.head = None
        for data in values:
            self.insert_at_the_end(data)

    def insert_value_at_index(self, data, index):
        """
        Inserting a value at index i. If the index is out of range, raise an exception. If index is 0 then it is the
        head we are deleting, the pointer head will point to the next element. if the index is right, then we stop at
        the previous index and change its pointer to the element we are trying to add
        :param data:
        :param index:
        :return:
        """
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid index")
        if index == 0:
            self.insert_at_the_beginning(data)
            return
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break
            itr = itr.next
            count += 1

    def insert_after_value(self, data_after, data_to_insert):
        """
        To insert after a given value. We first check if the list is empty by checking if the head is None. If not
        empty we check if the data in the head (head.data) is equal to the value we want to insert at, and if equal,
        then we create a new node and link it to the pointer if not then we start iterating from the head while
        checking the value of the iterative element's data (itr.data) and comparing it to the data after which we
        have to insert
        :param data_after: data after which we insert
        :param data_to_insert: data to be inserted as
        new node :return:
        """
        if self.head is None:
            return

        if self.head.data == data_after:
            self.head.next = Node(data_to_insert, self.head.next)
            return

        itr = self.head
        while itr:
            if itr.data == data_after:
                node = Node(data_to_insert, itr.next)
                itr.next = node
                break
            itr = itr.next

    def remove_at_index(self, index):
        """
        Deleting elements at index. If the index is out of range, raise an exception. If index is 0 then it is the
        head we are deleting, the pointer head will point to the next element. otherwise, we count till the element
        preceding the index, then the next pointer of the preceding element is set to the next element after the index.
        :param index: index where we are to remove
        :return:
        """
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
                break
            itr = itr.next
            count += 1

    def remove_by_value(self, data):
        """
        We first check if the list is empty by checking if the head is None. If not empty we check if the data in the
        head (head.data). Then we check if the head is not equal to the data that we want to delete, if it is then we
        change the pointer to next. otherwise, we iterate through the list till we find the element we want to erase.
        we use the attribute next to find the element by being one element behind (itr.next.data means data of the
        next element after itr). We set the next pointer of itr to 2 elements after itr instead of one (itr.next =
        itr.next.next)
        :param data: data of node to be deleted
        :return:
        """
        if self.head is None:
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        itr = self.head
        while itr:
            if itr.next.data == data:
                itr.next = itr.next.next
                break
            itr = itr.next

    def get_length(self):
        """
        Gets the length of the single linked list
        :return: count: the number of values in the list
        """
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def print_linked_list(self):
        """To print the list"""
        if self.head is None:
            print("Linked list is empty")
            return
        itr = self.head
        linked_list_string = ''
        while itr:
            linked_list_string += str(itr.data) + '--->'
            itr = itr.next

        print(linked_list_string)


if __name__ == '__main__':
    ll = SingleLinkedList()
    ll.insert_at_the_beginning(5)
    ll.insert_at_the_beginning(20)
    ll.insert_at_the_beginning(30)
    ll.insert_after_value(20, 40)
    ll.remove_by_value(40)
    ll.print_linked_list()
