idx = int(input("Enter the Max number: "))

for i in range(idx+1):
    pattern = ""
    for j in range(i+1):
        pattern += str(j) + " "

    print(pattern + pattern[:-3][::-1])
