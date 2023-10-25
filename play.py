import random

def choose_action():
    print("Выберите действие:")
    print("1. Осмотреть комнату")
    print("2. Искать ключи")
    print("3. Решить головоломки")
    action = input("Введите номер действия: ")
    return action

room_items = ["стул", "стол", "шкаф", "книга", "замок"]

keys = {"дверь в комнату": False, "дверь в коридор": False, "дверь на улицу": False}

puzzles = {"запертый шкаф", "закрытый ящик", "запертая дверь"}

additional_items = ["ключ", "фонарик", "компас", "карта"]

additional_puzzles = ["шахматы", "крестовина", "лабиринт"]

def check_answer(answer):
    correct_answers = ["книга", "птица", "корабль"]
    if answer in correct_answers:
        return True
    else:
        return False

def search_keys():
    if "ключ" in room_items:
        keys["дверь в комнату"] = True
        room_items.remove("ключ")
        print("Вы нашли ключ от двери в комнату!")
    else:
        print("Ключей в комнате нет.")

def solve_puzzles():
    if "запертый шкаф" in puzzles:
        print("Вы решили головоломку со шкафом и нашли ключ от двери в коридор!")
        keys["дверь в коридор"] = True
        puzzles.remove("запертый шкаф")
    elif "закрытый ящик" in puzzles:
        print("Вы решили головоломку с ящиком и нашли кусок бумаги.")
        room_items.append("кусок бумаги")
        puzzles.remove("закрытый ящик")
    elif "запертая дверь" in puzzles:
        answer = input("Решите головоломку: что летает, плавает и ходит по земле? ")
        if check_answer(answer):
            print("Вы решили головоломку и открыли дверь!")
            keys["дверь на улицу"] = True
            puzzles.remove("запертая дверь")
        else:
            print("Неверный ответ.")

def print_room_info():
    print("Вы находитесь в комнате. В комнате есть:")
    for item in room_items:
        print("- " + item)
    print("Двери:")
    for key, value in keys.items():
        if value:
            print("- " + key + " (открыта)")
        else:
            print("- " + key + " (заперта)")

def additional_events():
    event = random.randint(1, 5)
    if event == 1:
        print("В комнату ворвалась стая голодных мышей.")
        print("1. Попытаться их отпугнуть.")
        print("2. Спрятаться в уголке и подождать, пока они уйдут.")
        choice = input("Введите номер действия: ")
        if choice == "1":
            print("Вы смогли отпугнуть мышей, но они унесли часть ваших запасов еды.")
            room_items.remove("запасы еды")
        elif choice == "2":
            print("Вы спрятались и подождали, пока мыши ушли.")

    elif event == 2:
        print("В комнату вошел путешественник, предлагая обменяться предметами.")
        print("1. Согласиться на обмен.")
        print("2. Отказаться от обмена.")
        choice = input("Введите номер действия: ")
        if choice == "1":
            print("Вы обменялись предметами и получили что-то новое.")
            item = random.choice(room_items)
            room_items.remove(item)
            new_item = random.choice(["золото", "сокровище", "книга знаний"])
            room_items.append(new_item)
            print(f"Вы получили {new_item} в обмен на {item}.")
        elif choice == "2":
            print("Вы отказались от обмена и путешественник ушел.")

    elif event == 3:
        print("В комнате начался сильный дождь и потекла вода с потолка.")
        print("1. Попытаться найти источник утечки воды и предпринять меры.")
        print("2. Проигнорировать воду и продолжить поиски.")
        choice = input("Введите номер действия: ")
        if choice == "1":
            print("Вы нашли и временно устранили утечку воды, предотвратив более серьезные проблемы.")
        elif choice == "2":
            print("Вы решили продолжить исследование, игнорируя воду в комнате.")

    elif event == 4:
        print("Вы услышали странный шум за стеной.")
        print("1. Попытаться найти источник звука.")
        print("2. Проигнорировать звук и продолжить поиски.")
        choice = input("Введите номер действия: ")
        if choice == "1":
            print("Источником звука оказался старый диван, в котором нашли дополнительные предметы.")
            item = random.choice(["старинная монета", "сокровище", "секретный дневник"])
            room_items.append(item)
            print(f"Вы нашли {item} за диваном.")

    elif event == 5:
        print("В комнате началось электрическое шторм и произошел короткий замыкание.")
        print("1. Попытаться починить электричество.")
        print("2. Проигнорировать шторм и продолжить поиски.")
        choice = input("Введите номер действия: ")
        if choice == "1":
            print("Вы попытались починить электричество, но получили удар током. Вам нужна медицинская помощь.")
            print("Ваше приключение завершилось неудачей.")

while True:
    print_room_info()
    action = choose_action()
    if action == "1":
        print("Вы осмотрели комнату.")
    elif action == "2":
        search_keys()
    elif action == "3":
        solve_puzzles()
    else:
        print("Неверный выбор действия.")
    
    if keys["дверь на улицу"]:
        print("Вы нашли выход и выбрались на свободу!")
        break

    additional_events()


#блюм блюм это сохранение 

import json
import csv
import os

def load_game_data():
    if os.path.exists("game_data.json"):
        with open("game_data.json", "r") as json_file:
            data = json.load(json_file)
            return data
    else:
        return {"room_items": ["стул", "стол", "шкаф", "книга", "замок"],
                "keys": {"дверь в комнату": False, "дверь в коридор": False, "дверь на улицу": False},
                "puzzles": {"запертый шкаф", "закрытый ящик", "запертая дверь"}}

def save_game_data(data):
    with open("game_data.json", "w") as json_file:
        json.dump(data, json_file)

def save_game_results(username, result):
    with open("game_results.csv", "a", newline="") as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow([username, result])

def choose_action():
    print("Выберите действие:")
    print("1. Осмотреть комнату")
    print("2. Искать ключи")
    print("3. Решить головоломки")
    action = input("Введите номер действия: ")
    return action

def print_room_info(room_items, keys):
    print("Вы находитесь в комнате. В комнате есть:")
    for item in room_items:
        print("- " + item)
    print("Двери:")
    for key, value in keys.items():
        if value:
            print("- " + key + " (открыта)")
        else:
            print("- " + key + " (заперта)")

def main():
    username = input("Введите ваше имя: ")
    game_data = load_game_data()
    room_items = game_data["room_items"]
    keys = game_data["keys"]
    puzzles = game_data["puzzles"]

    while True:
        print_room_info(room_items, keys)
        action = choose_action()
        if action == "1":
            print("Вы осмотрели комнату.")
        elif action == "2":
            search_keys(room_items, keys)
        elif action == "3":
            solve_puzzles(puzzles, keys)
        else:
            print("Неверный выбор действия.")
        
        if keys["дверь на улицу"]:
            print("Вы нашли выход и выбрались на свободу!")
            save_game_results(username, "Победа")
            break

    save_game_data(game_data)

if __name__ == "__main__":
    main()
