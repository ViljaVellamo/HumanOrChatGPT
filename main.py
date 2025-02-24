import csv
import random
import string

times_correct = 0
times_looped = 0
generated_numbers_poets = []
generated_numbers_chatgpt = []
accuracy = 0

def fetch_poem (file_number, row_number):

    # The function opens a table to fetch and return a poem from the indicated row.
    # The Table 1 contains poems by poets and Table 2 poems generated with ChatGPT.

    with open ('Table ' + str(file_number) + '.csv', newline='', encoding='utf-8-sig') as csvfile:
        reader = csv.reader(csvfile)
        poem_from_table = ""
        rows = list(reader)
        cell = rows[row_number]
        print("Tän pitäisi olla norjaksi " , rows[159])

        for row in cell:
            poem_from_table += str(row)

    return poem_from_table

while True:
    language = input("Welcome to the game of 'Is it human or ChatGPT'.\n"
                               "You will be shown a poem that can be either written by a human or by ChatGPT.\n"
                               "To choose the language of the poems, press 'en' for English, 'fi' for Finnish, "
                               "and 'no' for Norwegian (or Dano-Norwegian).\n")

    if language != "fi" and language != "en" and language != "no":
        print("Please choose the language by typing 'en' for English, 'fi' for Finnish, or 'no' for for Norwegian "
              "(or Dano-Norwegian).\n")
        continue

    while True:

        user_input = input("Press x to show a poem. \n"
                           "If you wish to end the program, press q. \n")

        if user_input == "q":
            print("Thank you for playing! You have an accuracy rate of " + str(accuracy) + "%")
            quit()

        if str(user_input) != "x" and str(user_input) != "y":
            print("Please press x to continue or y to end the program.\n")

        if user_input == "x":
            file_number = random.randint(1, 2)
            row_number = 0

            # The range of texts that can be shown to the user are selected based on the language.

            i = 0
            while i < 1000000:
                if language == "en":
                    row_number = random.randint(0, 69)
                if language == "fi":
                    row_number = random.randint(70, 119)
                if language == "no":
                    row_number = random.randint(120, 159)

                # To avoid showing the same poem multiple times, the number of every shown poem is saved in a list.
                # If the generated number cannot be found on the list of previously shown poems, the number is selected,
                # added to  the list and the loop ends.

                if file_number == 1:
                    if row_number not in generated_numbers_poets:
                        generated_numbers_poets.append(row_number)
                        break
                else:
                    if row_number not in generated_numbers_chatgpt:
                        generated_numbers_chatgpt.append(row_number)
                        break
                i += 1

            poem = fetch_poem(file_number, row_number)
            print("\n" + poem)
            print("\n")

            while True:

                human_or_chatGPT = input("Human or ChatGPT? Write '1' for human or '2' for ChatGPT. \n")
                author = ""

                if human_or_chatGPT == "1" or human_or_chatGPT == "2":

                    # The name of the author is fetched from a separate file according to the row number.

                    with open ("Table 1 only authors.csv", newline='', encoding='utf-8-sig') as csvfile:
                        reader = csv.reader(csvfile)
                        rows = list(reader)
                        author_name = str(rows[row_number]).translate(str.maketrans('', '', string.punctuation))

                    print("")

                    if human_or_chatGPT == str(file_number):
                        times_correct += 1
                        if human_or_chatGPT == "1":
                            print("You are right. This poem was written by ", author_name + ".")
                        if human_or_chatGPT == "2":
                            print("You are right. This poem was written by ChatGPT.")
                    if human_or_chatGPT != str(file_number):
                        if human_or_chatGPT == "1":
                            print("You are wrong. This poem was written by ChatGPT.")
                        if human_or_chatGPT == "2":
                            print("You are wrong. This poem was written by ", author_name + ".")

                    times_looped += 1
                    accuracy = round(100 * (times_correct / times_looped))

                    print("You have an accuracy rate of " + str(accuracy) + "% \n")
                    break

                else:
                    print("Please write '1' for human or '2' for ChatGPT to proceed.\n")
                    continue


