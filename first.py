def first_unlock(range_start, range_end):
    nums = []
    for i in range(range_start, range_end):
        nums.append(i)
    code = sum(nums)
    return code

def second_unlock(range_start, range_end):
    code = 0
    for digit1 in range(range_start, range_end):
        for digit2 in range(range_start, range_end):
            for digit3 in range(range_start, range_end):
                if digit1 < digit2 and digit2 < digit3:
                    code += 1
    return code

def third_unlock(range_start, range_end):
    code = 0
    for digit1 in range(range_start,range_end):
        for digit2 in range(range_start,range_end):
            for digit3 in range(range_start,range_end):
                if digit1 % 2 == 0 and digit2 % 2 == 0 and digit3 % 2 == 0:
                    code += 1
    return code

def fourth_unlock(range_start, range_end):
    code = 0
    for digit1 in range(range_start,range_end):
        for digit2 in range(range_start,range_end):
            for digit3 in range(range_start,range_end):
                if sum((digit1, digit2, digit3)) % 2 != 0:
                    code += 1
    return code

def fifth_unlock(range_start, range_end):
    code = 0
    for digit1 in range(range_start,range_end):
        for digit2 in range(range_start,range_end):
            for digit3 in range(range_start,range_end):
                if digit1 == digit2 or digit1 == digit3 or digit2 == digit3:
                    code += 1
    return code 


print(f"code: {first_unlock(1, 41)}")
print(f"code: {second_unlock(0, 10)}")
print(f"code: {third_unlock(0, 10)}")
print(f"code: {fourth_unlock(0, 10)}")
print(f"code: {fifth_unlock(0, 10)}")
