n = int(input())
for i in range((n - n % 5),-1,-5):
    if (n - i) % 3 == 0:
        break
a = i // 5
b = (n - i) / 3
if b != int(b):
    print(-1)
else:
    print(int(a+b))