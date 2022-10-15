# python3
"""Represents the queue of the times when the computer will finish
processing the packets which are currently stored in the network buffer.
Samples:
>>> size, count = 1, 0
>>> requests = []
>>> buffer = Buffer(size)
>>> responses = [buffer.process(r) for r in requests]
>>> print_responses(responses)
>>>
>>> # Explanation: If there are no packets, you shouldn't output anything.
>>> size, count = 1, 1
>>> requests = [Request(0, 0)]
>>> buffer = Buffer(size)
>>> responses = [buffer.process(r) for r in requests]
>>> print_responses(responses)
0
>>> # Explanation: The only packet arrived at time 0, and computer started
>>> # processing it immediately.
>>> size, count = 1, 2
>>> requests = [Request(0, 1), Request(0, 1)]
>>> buffer = Buffer(size)
>>> responses = [buffer.process(r) for r in requests]
>>> print_responses(responses)
0
-1
>>> # Explanation: The first packet arrived at time 0, the second packet
>>> # also arrived at time 0, but was dropped, because the network buffer
>>> # has size 1 and it was full with the first packet already.
>>> # The first packet started processing at time 0, and the second packet
>>> # was not processed at all.
>>> size, count = 1, 2
>>> requests = [Request(0, 1), Request(1, 1)]
>>> buffer = Buffer(size)
>>> responses = [buffer.process(r) for r in requests]
>>> print_responses(responses)
0
1
>>> # Explanation: The first packet arrived at time 0, the computer started
>>> # processing it immediately and finished at time 1. The second packet
>>> # arrived at time 1, and the computer started processing it immediately.
"""
from collections import namedtuple

Request = namedtuple("Request", ["arrived_at", "time_to_process"])
Response = namedtuple("Response", ["was_dropped", "started_at"])


class Buffer:
    def __init__(self, size):
        self.size = size
        self.finish_time = []

    @property
    def is_full(self):
        """Return True if the buffer is full, False otherwise."""
        if len(self.finish_time) == self.size:
            return True
        return False

    @property
    def is_empty(self):
        """Return True if the buffer is empty, False otherwise."""
        if len(self.finish_time) == 0:
            return True
        return False

    @property
    def last_element(self):
        """Returns the last element of the buffer."""
        return self.finish_time[-1]

    def flush_processed(self, request):
        """
        Flushes processed elements of the buffer by the request's arrival time.
        """
        while self.finish_time:
            if self.finish_time[0] <= request.arrival_time:
                self.finish_time.pop(0)
            else:
                break

    def process(self, request):
        self.flush_processed(request)

        if self.is_full:
            return Response(True, -1)

        if self.is_empty:
            self.finish_time = [request.arrival_time + request.process_time]
            return Response(False, request.arrival_time)

        response = Response(False, self.last_element)
        self.finish_time.append((self.last_element + request.process_time))
        return response

class Request:
    """Incoming network packet."""

    def __init__(self, arrival_time, process_time):
        self.arrival_time = arrival_time
        self.process_time = process_time


class Response:
    """Response of the network buffer."""

    def __init__(self, dropped, start_time):
        self.dropped = dropped
        self.start_time = start_time


def read_requests(count):
    requests = []
    for i in range(count):
        arrival_time, process_time = map(int, input().strip().split())
        requests.append(Request(arrival_time, process_time))
    return requests


def process_requests(requests, buffer):
    return [buffer.process(r) for r in requests]


def print_responses(responses):
    for response in responses:
        print(response.start_time if not response.dropped else -1)

# def process_requests(requests, buffer):
#     responses = []
#     for request in requests:
#         responses.append(buffer.process(request))
#     return responses


def main():
    # buffer_size, n_requests = map(int, input().split())
    # requests = []
    # for _ in range(n_requests):
    #     arrived_at, time_to_process = map(int, input().split())
    #     requests.append(Request(arrived_at, time_to_process))
    #
    # buffer = Buffer(buffer_size)
    # responses = process_requests(requests, buffer)
    #
    # for response in responses:
    #     print(response.started_at if not response.was_dropped else -1)
    size, count = map(int, input().strip().split())
    requests = read_requests(count)
    buffer = Buffer(size)
    responses = process_requests(requests, buffer)

    print_responses(responses)


if __name__ == "__main__":
    main()
