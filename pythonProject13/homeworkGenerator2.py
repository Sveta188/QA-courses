a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
c = ["Петя", "Света", "Андрей", "Аля", "Даша", "Маша", "Яна", "Егор", "Ваня", "Катя"]
students = dict(zip(a, c))

schedule = ({i+1: students[i % len(students)+1]} for i in range(31))
for item in schedule:

    print(item)
