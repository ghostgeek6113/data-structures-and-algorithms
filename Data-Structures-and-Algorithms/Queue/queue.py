class QueueArray:
    """
    A queue is FIFO, first in first out
    """
    def __init__(self):
        """
        initialize an empty array as the queue
        """
        self.queue = []

    def enqueue(self, data):
        """
        appends data to the queue object
        :param data: data to be appended
        """
        self.queue.append(data)

    def dequeue(self):
        """
        removes the first data from the queue
        """
        self.queue.pop(0)

    def is_empty(self):
        """
        Check whether the queue is empty.
        :return: Boolean
        """
        if len(self.queue) == 0:
            return True
        return False

    def print_queue(self):
        """
        Prints the queue object
        """
        if self.is_empty():
            return "Empty queue"
        for i in range(len(self.queue)):
            print(self.queue[-i])
