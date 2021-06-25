def run():
    print("Enter number of frames: ", end="")
    capacity = int(input())
    print("Enter the reference string (must be separated by space): ", end="")
    string = list(map(int, input().strip().split()))
    frame, fault = [], 0

    tally = dict.fromkeys(string, 0)

    for i in string:
        if i not in frame:
            if len(frame) < capacity:
                frame.append(i)
                tally[i] += 1
            else:
                list_check = {}
                for k, v in tally.items():
                    if k in frame:
                        list_check[k] = v

                most_recently_used = max(list_check, key=list_check.get)

                for j in range(len(frame)):
                    if frame[j] == most_recently_used:
                        frame[j] = i
                        tally[i] += 1

                        value = tally.pop(most_recently_used)
                        newDict = {most_recently_used: value}
                        tally.update(newDict)
            fault += 1
        else:
            tally[i] += 1

        print("   %d\t\t" % i, end='')
        for x in frame:
            print(x, end=' ')
        for x in range(capacity - len(frame)):
            print(' ', end=' ')
        print(" ")

    print("\nTotal Page Faults:", fault)
