happiness = input().split()
improvement_factor = int(input())

happiness_score = [int(i) * improvement_factor for i in happiness]
average = [i for i in happiness_score if i >= sum(happiness_score) / len(happiness_score)]

if len(average) >= len(happiness_score) / 2:
    print(f"Score: {len(average)}/{len(happiness_score)}. Employees are happy!")
else:
    print(f"Score: {len(average)}/{len(happiness_score)}. Employees are not happy!")