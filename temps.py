while True:
    nums = input()
    if nums == "0":
        break
    res = 0
    for n in nums:
        if n == "0":
            res += 4
        elif n == "1":
            res += 2
        else:
            res += 3
    print(res+len(nums)+1)