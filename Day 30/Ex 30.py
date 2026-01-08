MAX_SIZE = 7
queue = [None] * MAX_SIZE
front = -1
rear = -1

def enqueue(item):
    global front, rear

    if rear == MAX_SIZE - 1:
        print(f"Cannot Add Element, Queue is Full:", item)
        return

    if front == -1:
        front = 0
    rear += 1
    queue[rear] = item

    print(f"Input: enqueue({item})")
    print(f"Output: {item} added at index {rear}. Queue now: {queue[:rear+1]}\n")

enqueue(10)
enqueue(20)
enqueue(30)
enqueue(40)
enqueue(50)
enqueue(60)
enqueue(70)
enqueue(80)

