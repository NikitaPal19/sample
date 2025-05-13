print("Try 1")

print("⭐ Star Pattern")
for i in range(1, 6):
    print("*" * i)

print("\n✅ Prime numbers from 1 to 20:")
for num in range(2, 21):
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        print(num)
