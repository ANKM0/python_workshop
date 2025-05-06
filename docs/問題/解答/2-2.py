# 章2-2 解答: コレクションと制御構文

# 課題1
def calc_sum_and_avg(numbers):
    total = sum(numbers)
    avg = total / len(numbers)
    return total, avg

nums = [10, 20, 30, 40, 50]
total, avg = calc_sum_and_avg(nums)
print(f"合計: {total}, 平均: {avg}")

# 課題2
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
