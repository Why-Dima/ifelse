cities = ['Москва','Париж','Лондон']

users = [{'name': 'Иван', 'age': 35},
{'name': 'Мария', 'age': 22},
{'name': 'Соня', 'age': 20}]

tourists = [{'user': users[0], 'city': cities[2]},
{'user': users[1], 'city': cities[0]},
{'user': users[2], 'city': cities[1]}]

city = input('Введите город:').lower()

if city == cities[0].lower():
    print(f"Турист {users[1]['name']} возраст {users[1]['age']}. Посетил город {city}")
elif city == cities[1].lower():
    print(f"Турист {users[2]['name']} возраст {users[2]['age']}. Посетил город {city}")
elif city == cities[2].lower():
    print(f"Турист {users[0]['name']} возраст {users[0]['age']}. Посетил город {city}")
else:
    print('Такого города нет в списке')