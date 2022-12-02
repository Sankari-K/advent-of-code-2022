def day1():
    calories = [0]
    while True:
        calorie = input()
        if calorie == "q":
            break
        if calorie == "":
            calories.append(0)
        else:
            calories[-1] += int(calorie)
        
    calories = sorted(calories, reverse=True)
    return sum(calories[0:3])