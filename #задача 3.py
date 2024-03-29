# задача 3

nums = input('Введите элементы через пробел: ').split()
nums = list(map(int, nums))
counter = 0
swap = False
for _ in nums:
    for i in range(len(nums) - 1):
        if nums[i] < nums[i + 1]:
            swap = True
            counter += 1
            nums[i], nums[i + 1] = nums[i + 1], nums[i]
    if not swap:
        pass
print('-' * 20)
print(nums)
print('-' * 20)
print('количество перемещений', counter)