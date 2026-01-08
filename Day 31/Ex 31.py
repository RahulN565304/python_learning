Max_Size = 5
queue = [None] * Max_Size
front = -1
rear = -1
def enqueue(item):
    global front, rear
    if rear == Max_Size - 1:
        print("Cannot add, because queue is full", item)
        return
    if front == -1:
        front = 0
    rear += 1
    queue[rear] = item
    print(f"Input: enqueue({item})")
    print(f"Output: {item} added at index {rear}. Queue now: {queue[:rear+1]}\n")

def dequeue():
    global front, rear
    if front == -1:
        print("Cannot remove, because the queue is empty", item)
        return None
    removed = queue[front]
    print(f"Input : dequeue()")
    print(f"Output: {removed} removed from index {front}.")
    if front == rear:
        front = rear = -1
        print(f"Queue is Now Empty")
    else:
        front += 1
        print(f"Queue now: {queue[front:rear+1]}, front = {front}, rear = {rear}")

enqueue(10)
enqueue(20)
enqueue(30)
dequeue()
enqueue(40)
enqueue(50)
dequeue()
enqueue(60)
dequeue()
dequeue()
dequeue()