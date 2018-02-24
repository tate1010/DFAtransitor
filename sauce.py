print("Input Start State (one line, seperated by space)")
Start = input()
print("Input transition (one line, seperated by space)")
Trans = input()

print("Input Final State (one line, seperated by space)")
End = input()
for s in Start.split(" "):
    for item in Trans.split(" "):
        for lol in End.split(" "):
            print(s  + " " + item + " " + lol)


print("Copy and paste, then")
input("Press Enter to exit...")
