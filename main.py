from logger import phone_format, printData, showContacts, addContact, findContact, changeContact, deleteContact
import os, re

def drawInterface():  # Функция рисования интерфейса главного меню
    print("#####   Телефонная книга   #####")
    print("=" * 26)
    print(" [1] -- Показать контакты")
    print(" [2] -- Добавление контактов")
    print(" [3] -- Поиск контактов")
    print(" [4] -- Сменить контакты")
    print(" [5] -- Удаление контактов")
    print("\n [0] -- Выход")
    print("=" * 26)


def main(path):  # Функция реализации главного меню
    while True:
        os.system("cls")
        drawInterface()
        userChoice = int(input("Введите число от 1 до 5 или 0 для выхода: "))

        if userChoice == 1:
            showContacts(path)
        elif userChoice == 2:
            addContact(path)
        elif userChoice == 3:
            findContact(path)
        elif userChoice == 4:
            changeContact(path)
        elif userChoice == 5:
            deleteContact(path)
        elif userChoice == 0:
            print("Спасибо!")
            return


path = "PhoneBook.txt"

main(path)