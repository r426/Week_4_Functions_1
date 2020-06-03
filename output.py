i = 1
while i < 5:
    if i == 6:
        break
    print(i, end=" ")
    i = i + 1
else:
    print("Else is also printed")

# A very interesting thing to learn about Python is that else can go without if:
# GeeksforGeeks: "The else block just after for/while is executed only
# when the loop is NOT terminated by a break statement."
