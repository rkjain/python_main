list_of_tuples = [
    ("rishabh","jain",23),
    ("sheenal","singh",21),
    ("baby","johnson",19)
]

print(sorted(list_of_tuples, key=(lambda student: student[2])))

