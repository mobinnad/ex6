def find_pairs_with_sum(nums_str, target):
    nums = nums_str.split()
    index_map = {}
    pair_sum_map = {}
    
    for index, num in enumerate(nums):
        index_map[int(num)] = index

    for num in index_map:
        complement = target - num
        if complement in index_map and complement != num:
            pair_sum = index_map[num] + index_map[complement]
            if (complement, num) not in pair_sum_map:
                pair_sum_map[(num, complement)] = pair_sum

    sorted_pair_sums = sorted(pair_sum_map.values())

    if not pair_sum_map:
        print("No pairs found!")
    else:
        for pair_sum in sorted_pair_sums:
            print(pair_sum)


user_input = input()
target_sum = int(input())

find_pairs_with_sum(user_input, target_sum)
