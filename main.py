'''
we are going to use rq to create an rq template
we have to make a worker
we have to make some job functions
'''

from redis import Redis
from rq import Queue

import jobs

if __name__ == '__main__':
    q = Queue(connection=Redis())

    q.enqueue(jobs.do_a_thing, 2)

