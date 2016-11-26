nums = [int(num) for num in input().split()]
count_dict = {}

for num in nums:
    count_dict[num] = count_dict.get(num, 0) + 1

print(" ".join([str(n) for n in count_dict if count_dict[n] > 1]))
