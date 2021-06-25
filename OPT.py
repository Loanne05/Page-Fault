def run():
    print("Enter the number of frames: ", end="")
    capacity = int(input())
    frame, fault = [], 0
    print("Enter the reference string (must be separated by space): ", end="")
    string = list(map(int, input().strip().split()))

    print(end='')
    occurance = [None for i in range(capacity)]
    for i in range(len(string)):
        if string[i] not in frame:
            if len(frame) < capacity:
                frame.append(string[i])
            else:
                for x in range(len(frame)):
                    if frame[x] not in string[i+1:]:
                        frame[x] = string[i]
                        break
                    else:
                        occurance[x] = string[i+1:].index(frame[x])
                else:
                    frame[occurance.index(max(occurance))] = string[i]
            fault += 1

        print("   %d\t\t" % string[i], end='')
        for x in frame:
            print(x, end=' ')
        for x in range(capacity-len(frame)):
            print(' ', end=' ')
        print(" ")
    print("\nTotal Page Faults:", fault)
