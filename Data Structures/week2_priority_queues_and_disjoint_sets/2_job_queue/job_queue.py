# python3
"""Simulation of a program that processes a list of jobs in parallel.
Samples:
>>> job_queue = JobQueue()
>>> job_queue.num_workers = 2
>>> job_queue.jobs = [1, 2, 3, 4, 5]
>>> job_queue.assign_jobs()
>>> job_queue.write_response()
0 0
1 0
0 1
1 2
0 4
>>> # Explanation:
>>> # 1. The two threads try to simultaneously take jobs from the list, so
>>> # thread with index 0 actually takes the first job and starts
>>> # working on it at the moment 0.
>>> # 2. The thread with index 1 takes the second job and starts
>>> # working on it also at the moment 0.
>>> # 3. After 1 second, thread 0 is done with the first job and takes
>>> # the third job from the list, and starts processing it immediately
>>> # at time 1.
>>> # 4. One second later, thread 1 is done with the second job and takes
>>> # the fourth job from the list, and starts processing it immediately
>>> # at time 2.
>>> # 5. Finally, after 2 more seconds, thread 0 is done with the third job
>>> # and takes the fifth job from the list, and starts processing it
>>> # immediately at time 4.
>>> job_queue = JobQueue()
>>> job_queue.num_workers = 4
>>> job_queue.jobs = [1] * 20
>>> job_queue.assign_jobs()
>>> job_queue.write_response()
0 0
1 0
2 0
3 0
0 1
1 1
2 1
3 1
0 2
1 2
2 2
3 2
0 3
1 3
2 3
3 3
0 4
1 4
2 4
3 4
>>> # Explanation: Jobs are taken by 4 threads in packs of 4, processed in
>>> # 1 second, and then the next pack comes. This happens 5 times starting
>>> # at moments 0, 1, 2, 3 and 4. After that all the 5 × 4 = 20 jobs
>>> # are processed.
"""

# from collections import namedtuple
import heapq


#
# AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])
#
#
# def assign_jobs(n_workers, jobs):
#     # TODO: replace this code with a faster algorithm.
#     # result = []
#     # next_free_time = [0] * n_workers
#     # for job in jobs:
#     #     next_worker = min(range(n_workers), key=lambda w: next_free_time[w])
#     #     result.append(AssignedJob(next_worker, next_free_time[next_worker]))
#     #     next_free_time[next_worker] += job
#     #
#     # return result
#     results = []
#     worker_queue = [i for i in range(n_workers)]
#     for job in jobs:
#         worker = heapq.heappop(worker_queue)
#         results.append(AssignedJob(worker, next_free_time[next_worker]))
#         next_free_time[next_worker] += job


class Worker:
    def __init__(self, thread_id, release_time=0):
        self.thread_id = thread_id
        self.release_time = release_time

    def __lt__(self, other_worker):
        if self.release_time == other_worker.release_time:
            return self.thread_id < other_worker.thread_id
        return self.release_time < other_worker.release_time

    def __gt__(self, other_worker):
        if self.release_time == other_worker.release_time:
            return self.thread_id > other_worker.thread_id
        return self.release_time > other_worker.release_time


class JobQueue:
    def __init__(self):
        self.size = None
        self.n_workers = None
        self.jobs = None

    def read_data(self):
        self.n_workers, n_jobs = map(int, input().split())
        self.jobs = list(map(int, input().split()))
        self.size = len(self.jobs)
        assert len(self.jobs) == n_jobs

    def assign_jobs(self):
        self.results = []
        self.worker_queue = [Worker(i) for i in range(self.n_workers)]
        for job in self.jobs:
            worker = heapq.heappop(self.worker_queue)
            self.results.append((worker.thread_id, worker.release_time))
            worker.release_time += job
            heapq.heappush(self.worker_queue, worker)
        return self.results


def main():
    job_queue = JobQueue()
    job_queue.read_data()
    assigned_jobs = job_queue.assign_jobs()

    # assigned_jobs = assign_jobs(n_workers, jobs)

    for worker_id, start_time in assigned_jobs:
        print(worker_id, start_time)


if __name__ == "__main__":
    main()
