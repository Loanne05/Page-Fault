def run():
    print("Enter the number of frames: ", end="")
    capacity = int(input())
    frame, st, fault = [], [], 0
    print("Enter the reference string (must be separated by space): ", end="")
    string = list(map(int, input().strip().split()))

    print(end='')
    for i in string:
        if i not in frame:
            if len(frame) < capacity:
                frame.append(i)
                st.append(len(frame)-1)
            else:
                ind = st.pop(0)
                frame[ind] = i
                st.append(ind)

            fault += 1
        else:
            st.append(st.pop(st.index(frame.index(i))))

        print("   %d\t\t" % i, end='')
        for x in frame:
            print(x, end=' ')
        for x in range(capacity-len(frame)):
            print(' ', end=' ')
        print(" ")
    print("\nTotal Page Faults:", fault)
