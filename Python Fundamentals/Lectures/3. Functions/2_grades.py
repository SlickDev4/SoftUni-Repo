def grades(grade):
    result = ''
    if 2 <= grade < 3:
        result = "Fail"
    elif 3 <= grade < 3.5:
        result = "Poor"
    elif 3.5 <= grade < 4.5:
        result = "Good"
    elif 4.5 <= grade < 5.5:
        result = "Very Good"
    elif 5.5 <= grade <= 6:
        result = "Excellent"

    return result


score = float(input())
print(grades(score))
