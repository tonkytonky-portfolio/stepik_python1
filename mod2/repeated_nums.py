n = int(input())
rpted_nums = []
i = 1

while len(rpted_nums) < n:
    num_chunk = [str(i)] * i
    rpted_nums.extend(num_chunk)
    i += 1

print(" ".join(rpted_nums[:n]))

# TODO: Add generator implementation
