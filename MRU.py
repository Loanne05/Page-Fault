def run():
    print("Enter number of frames: ", end="")
    capacity = int(input())
    print("Enter the reference string (must be separated by space): ", end="")
    string = list(map(int, input().strip().split()))
    frame, st, fault = [], [], 0
    most_recently_used = None

    for i in string:
        if i not in frame:
            if len(frame) < capacity:
                frame.append(i)
                st.append(len(frame) - 1)
            else:
                index = frame.index(most_recently_used)
                frame[index] = i
                st.append(index)
            fault += 1
        most_recently_used = i

        print("   %d\t\t" % i, end='')
        for x in frame:
            print(x, end=' ')
        for x in range(capacity - len(frame)):
            print(' ', end=' ')
        print(" ")

    print("\nTotal Page Faults:", fault)
