text = str(input("Введите текст:"))
_const = str(input("Постоянная согласная:"))
vowels = u'аеёиоуыэюя'  # гласные
new_text = ''
e = 0

#  свиная латынь
for _ in range(len(text)):
    if text[e].lower() in vowels:
        new_text += text[e].lower() + _const
    new_text += text[e].lower()
    e += 1
print(new_text.capitalize())
