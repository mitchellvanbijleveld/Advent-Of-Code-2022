with open('Day 1.input') as file:
    data = [i for i in file.read().strip().split("\n")]

# print (data)
print("START")
max1 = 0
max2 = 0
max3 = 0
count = 0
for item in data:
    try:
        count += int(item)

 #   print("COUNT: ",count)
    except:
        print(count)
        if count > max1:
            max3 = max2
            max2 = max1
            max1 = count
        elif count > max2:
            max2 = max1
            max2 = count
        elif count > max3:
            max3 = count
        print("MAX ONE   : ",max1)
        print("MAX TWO   : ",max2)
        print("MAX THREE : ",max3)

        count = 0

print("DONE")

print(max1)
print(max2)
print(max3)

print("DONE")
print(max1 + max2 + max3)