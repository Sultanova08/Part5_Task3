def superDigit(string):
    total = 0
    for s in string:
        total += int(s)
    return total

data = input().strip().split(" ")
n = superDigit(data[0]) * int(data[1])
while n > 10:
    n = superDigit(str(n))
print(n)
