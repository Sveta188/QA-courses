import json


def one_class(value):
    with open("students.js", "r") as json_file:
        data = json.load(json_file)
        filtered = [s for s in data["student"] if s["Class"] == value]
        print(filtered)


def one_club(value):
    with open("students.js", "r") as json_file:
        data = json.load(json_file)
        filtered = [s for s in data["student"] if s["Club"] == value]
        print(filtered)


def student_gender(value):
    with open("students.js", "r") as json_file:
        data = json.load(json_file)
        filtered = [s for s in data["student"] if s["Gender"] == value]
        print(filtered)
        print(len(filtered), "persons")


def student_name(value):
    with open("students.js", "r") as json_file:
        data = json.load(json_file)
        filtered = [s for s in data["student"] if s["Name"] == value]
        print(filtered)


print(one_class("1b"))
print()
print(one_club("Chess"))
print()
print(student_gender("W"))
print()
print(student_name("Koharu Hinata"))