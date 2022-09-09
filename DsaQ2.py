def reverseList(x, start, end):
    while start < end:
        x[start], x[end] = x[end], x[start]
        start += 1
        end -= 1
x = [1, 2, 3, 4, 5, 6]
print(x)
reverseList(x, 0, 5)
print(f"Reversed list is",x)
