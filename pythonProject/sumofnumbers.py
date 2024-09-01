def find_pair_with_target(num,target):
        prevHashMap = {}
        for i , n in enumerate(num):
            diff = target - n
            if diff in prevHashMap:
                return  prevHashMap[diff],i
            else:
                prevHashMap[n] = i
            print(prevHashMap[n])
        return None

target = 4
num = [1,2,3,4,5]
result = find_pair_with_target(num,target)

if result:
    print(f"Indeces of the numbers that add up to {target}:{result}")
else:
    print("No pairs found that add up to the target")