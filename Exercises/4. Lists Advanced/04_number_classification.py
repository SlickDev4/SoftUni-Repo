numbers = [int(i) for i in input().split(", ")]
positive = [str(i) for i in numbers if i >= 0]
negative = [str(i) for i in numbers if i < 0]
even = [str(i) for i in numbers if i % 2 == 0]
odd = [str(i) for i in numbers if i % 2 != 0]

print("Positive: " + ", ".join(positive))
print("Negative: " + ", ".join(negative))
print("Even: " + ", ".join(even))
print("Odd: " + ", ".join(odd))

