def program() -> tuple:
    storage = []
    
    while True:
        data = input("Enter a number:")
        
        if data == "done":
            avg = my_sum(storage)/len(storage)
            return (storage,avg)

        storage.append(float(data))

def my_sum(nums):
    sum = 0
    for v in nums:
        sum += float(v)
    return sum

result = program()

print(result[0])
print("Average:", result[1])