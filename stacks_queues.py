#Stacks


'''In general, we could use a list as a stack
It would be amortized O(1) to push and pop from the end of the list
But it would not be consistent O(1) since lists are dynamic arrays
and these arrays would occassionally need to be resized. 

But do NOT push/pop from the beginning of the list!!!!, since this would
entail an O(n) operation since we must shift all the elements to the left/right
when we pop/push
'''


s = []

s.append("eat")
s.append("sleep")
s.append("code")

print(s.pop())
print(s.pop())
print(s.pop())

'''Alternative is to use the deque class from collections module. 
The deque class is based on a doubly linked list
hence it would be consistent O(1) as there is no resizing needed. 
However, it would be O(n) to randomly access an element in the deque
whereas it would be O(1) for a list since it is a dynamic array

'''

from collections import deque
s = deque()
s.append("eat")
s.append("sleep")
s.append("code")

print(s.pop())
print(s.pop())
print(s.pop())

#Btw u can also use LifoQueue if u want a thread safe queue 
# i.e. it deals all the locking and unlocking manually for synchronized access
#But u should only use this type of queue for the above reasons
#If u are not using for any parallelized programming, then it will add unnecessary overhead


#Queues

#"enqueue" means to add to the back of the queue
#"dequeue" means to remove fromt the front of the queue

#Do NOT use a "list" as a queue since deleting/inserting from the beginning of the list
#is very expensive: O(n)

#Better alternative: deque
#consistent O(1) for adding/removing elements from either end, since deque is implemented as doubly linked list

q = deque()
q.append("eat")
q.append("sleep")
q.append("code")

print(q.popleft())
print(q.popleft())
print(q.popleft())

#Also u could have a thread safe queue using queue.Queue which provides synchronized access
# and locking/unlocking
#u could also use multprocessing.Queue to create a Shared Job Queue 
# which allows items in the queue to be processed in parallel. 



#Priority Queues (PQ)
#First good way to implement a PQ is to use "heapq"
#heapq is by default a min-heap, and is backed by a list

import heapq
q = []
heapq.heappush(q, (2, "eat"))
heapq.heappush(q, (1, "code"))
heapq.heappush(q, (3, "sleep"))

while q:
    next_item = heapq.heappop(q)
    print(next_item)


#Another alternative is to use queue.PriorityQueue
#This is thread safe and is synchronized, but may contain more overhead
#Also it has a better name than heapq tbh


from queue import PriorityQueue
q = PriorityQueue()
q.put((2, "eat"))
q.put((1, "code"))
q.put((3, "sleep"))

while not q.empty():
    next_item = q.get()
    print(next_item)

    

