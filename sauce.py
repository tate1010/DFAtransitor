Start = input("Input Start State")
print("Input transition (one line, seperated by space)")
Trans = input()

print("Input Final State")
End = input()

for item in Trans.split(" "):
    print(Start  + " " + item + " " + End)


print("Copy and paste, then")
input("Press Enter to exit...")
