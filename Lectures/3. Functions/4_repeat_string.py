string = input()
times_to_repeat = int(input())

repeat_function = lambda a, b: a * b

result = repeat_function(string, times_to_repeat)

print(result)