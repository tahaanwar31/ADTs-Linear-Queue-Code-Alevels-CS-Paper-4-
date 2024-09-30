global QueueArray
global HeadPointer
global TailPointer
QueueArray=[0]*10
HeadPointer=-1
TailPointer=0
def Enqueue(Data):
    global QueueArray
    global HeadPointer
    global TailPointer
    if TailPointer>9:
        print("Queue is full")
    else:
        QueueArray[TailPointer]=Data
        TailPointer=TailPointer+1
        if HeadPointer==-1:
            HeadPointer=0
def Dequeue():
    global QueueArray
    global HeadPointer
    global TailPointer
    if HeadPointer==-1:
        print("Queue is empty")
    else:
        item=QueueArray[HeadPointer]
        HeadPointer=HeadPointer+1
        print(item)
    if HeadPointer==TailPointer:
        HeadPointer=-1
        TailPointer=0
        
