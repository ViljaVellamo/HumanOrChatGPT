import csv
import random
import string
from random import choice

times_correct = 0
times_looped = 0
generated_numbers_poets = []
generated_numbers_chatgpt = []
accuracy = 0
language = 0

def fetch_poem (file_number, row_number):

    with open ('Table ' + str(file_number) + '.csv', newline='', encoding='utf-8-sig') as csvfile:

        reader = csv.reader(csvfile)
        poem_from_table = ""
        rows = list(reader)
        cell = rows[row_number]
        for row in cell:
            poem_from_table += str(row)

    return poem_from_table

while True:
    language_from_user = input("Welcome to the game of 'Is it human or ChatGPT'.\n"
                               "You will be shown a poem that can be either written by a human or by ChatGPT.\n"
                               "To choose the language of the poems, press 'en' for English, 'fi' for Finnish, "
                               "or 'both' for both.\n")

    if language_from_user == "fi":
        language += 1
    if language_from_user == "both":
        language += 2
    if language_from_user != "fi" and language_from_user != "en" and language_from_user != "both":
        print("Please choose the language by typing 'en' for English, 'fi' for Finnish, or 'both' for both.\n")
        continue

    while True:

        number_int = input("Press x to show a poem. \n"
                           "If you wish to end the program, press y. \n")

        if number_int == "y":
            print("Thank you for playing! You have an accuracy rate of " + str(accuracy) + "%")
            quit()

        if str(number_int) != "x" and str(number_int) != "y":
            print("Please press x to continue or y to end the program.\n")

        if number_int == "x":
            row_number = 0
            random_file_number = random.randint(1, 2)

            random_int = 0
            i = 0

            if random_file_number == 1:
                if language == 0:
                    random_int = choice([i for i in range(0, 55) if i not in [generated_numbers_poets]])
                if language == 1:
                    random_int = choice([i for i in range(56, 99) if i not in [generated_numbers_poets]])
                if language == 2:
                    random_int = choice([i for i in range(0, 99) if i not in [generated_numbers_poets]])
                generated_numbers_poets.append(random_int)
            else:
                if language == 0:
                    random_int = choice([i for i in range(0, 55) if i not in [generated_numbers_chatgpt]])
                if language == 1:
                    random_int = choice([i for i in range(56, 99) if i not in [generated_numbers_chatgpt]])
                if language == 2:
                    random_int = choice([i for i in range(0, 99) if i not in [generated_numbers_chatgpt]])
                generated_numbers_chatgpt.append(random_int)

            poem = fetch_poem(random_file_number, random_int)
            print("\n" + poem)
            print("\n")

            while True:

                human_or_chatGPT = input("Human or ChatGPT? Write '1' for human or '2' for ChatGPT. \n")
                author = ""

                if human_or_chatGPT == "1" or human_or_chatGPT == "2":

                    with open ("Table 1 only  authors.csv", newline='', encoding='utf-8-sig') as csvfile:
                        reader = csv.reader(csvfile)
                        rows = list(reader)
                        author_name = str(rows[random_int]).translate(str.maketrans('', '', string.punctuation))

                    print("")

                    if human_or_chatGPT == str(random_file_number):
                        times_correct += 1
                        if human_or_chatGPT == "1":
                            print("You are right. This poem was written by " + str(author_name) + ".")
                        if human_or_chatGPT == "2":
                            print("You are right. This poem was written by ChatGPT.")
                    if human_or_chatGPT != str(random_file_number):
                        if human_or_chatGPT == "1":
                            print("You are wrong. This poem was written by ChatGPT.")
                        if human_or_chatGPT == "2":
                            print("You are wrong. This poem was written by " + str(author_name) + ".")

                    times_looped += 1
                    accuracy = round(100 * (times_correct / times_looped))

                    print("You have an accuracy rate of " + str(accuracy) + "% \n")
                    break

                else:
                    print("Please write '1' for human or '2' for ChatGPT to proceed.\n")
                    continue

# idea: kerää ohjelman vastaukset csv-tiedostoon

