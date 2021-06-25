def run():
    print("Enter the number of frames: ", end="")
    capacity = int(input())
    frame, fault, top = [], 0, 0
    print("Enter the reference string (must be separated by space): ", end="")
    string = list(map(int, input().strip().split()))

    print(end='')
    for i in string:
        if i not in frame:
            if len(frame) < capacity:
                frame.append(i)
            else:
                frame[top] = i
                top = (top+1) % capacity
            fault += 1

        print("   %d\t\t" % i, end='')
        for x in frame:
            print(x, end=' ')
        for x in range(capacity-len(frame)):
            print(' ', end=' ')
        print(" ")
    print("\nTotal Page Faults:", fault)
