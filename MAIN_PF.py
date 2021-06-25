import FIFO
import OPT
import LRU
import MRU
import LFU
import MFU
# 0 1 2 3 0 1 4 0 1
# Frames 3
def start():
    print("\n")
    print("---------PAGE FAULT---------")
    print("[1] First In First Out (FIFO)")
    print("[2] Optimal (OPT)")
    print("[3] Least Recently Used (LRU)")
    print("[4] Most Recently Used (MRU)")
    print("[5] Least Frequently Used (LFU)")
    print("[6] Most Frequently Used (MFU)")
    print("[7] Exit")
    print("----------------------------------")
    choice = input("Enter choice: ")
    choices(choice)


def choices(choice):
    if choice == "1":
        print("\n")
        print("First In First Out (FIFO)")
        FIFO.run()
        start()
    elif choice == "2":
        print("\n")
        print("Optimal (OPT)")
        OPT.run()
        start()
    elif choice == "3":
        print("\n")
        print("Least Recently Used (LRU)")
        LRU.run()
        start()
    elif choice == "4":
        print("\n")
        print("Most Recently Used (MRU)")
        MRU.run()
        start()
    elif choice == "5":
        print("\n")
        print("Least Frequently Used (LFU)")
        LFU.run()
        start()
    elif choice == "6":
        print("\n")
        print("Most Frequently Used (MFU)")
        MFU.run()
        start()
    elif choice == "7":
        import sys
        sys.exit("Program terminated.")
    else:
        print("Invalid input.")


start()
