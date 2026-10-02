lecture = ["Аня", "Борис", "Вика", "Гоша", "Аня"]
seminar = ["Вика", "Дима", "Борис", "Ева"]
all_stud = sorted(list(set(lecture + seminar)))
result = {'Всего уникальных студентов:': None, 'На обеих парах:': [], 'Только на лекции:': [], 'Хотя бы на одной:': []}
for student in all_stud:
    if student in lecture and student in seminar:
        result['На обеих парах:'].append(student)
    if student in lecture and student not in seminar:
        result['Только на лекции:'].append(student)
    if student in lecture or student in seminar:
        result['Хотя бы на одной:'].append(student)
result['Всего уникальных студентов:'] = len(all_stud)
for key, value in result.items():
    print(f'{key} {value}')