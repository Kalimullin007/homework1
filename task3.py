words = ["кот", "пёс", "кот", "кот", "ёж", "пёс", "кот"]
quantity_animals = []
added_words = []
for i in words:
    if i not in added_words:
        quantity_animals.append([words.count(i), i])
        added_words.append(i)
quantity_animals.sort(reverse=True)
for i in range(len(quantity_animals[:3])):
    print(f'{i + 1}. {quantity_animals[i][-1]} - {quantity_animals[i][0]}')