'''1. Word Counter:
 Write a program that reads a sentence and counts the number of times each word appears. Use
a dictionary to store the word counts.'''

sentence=input("Enter a Sentence:")
words=sentence.split()
word_counts={}

for word in words:
    if word in word_counts:
        word_counts[word]+=1
    else:
        word_counts[word]=1
for word,count in word_counts.items():
    print(word,":",count)

'''2. Grade Calculator: 
 Create a program that asks the user for their scores in different subjects and calculates
 their overall grade based on a grading scale stored in a dictionary. '''

grades={
    "A1":95,
    "A":90,
    "B":80,
    "C":70,
    "D":60,
    "E":50,
    "F":40<0
}

def calculate_grade(subject_scores):
    total_score=sum(subject_scores)
    total_subjects=len(subject_scores)
    average_score=total_score/total_subjects
    for grade,score in grades.items():
        if average_score>=score:
            return grade
    
subject_scores=[]
subjects=['English','Caculas','PF','CF','Islamiat']
for subject in subjects:
    score=int(input(f"Enter Your Marks in {subject}:"))
    subject_scores.append(score)

overall_grade=calculate_grade(subject_scores)
print(f'Your Overall grade is:{overall_grade}')

'''3. Shopping List Manager: 
 Develop a program that allows users to add, remove, and check off items on a shopping list 
stored in a dictionary.'''

shopping_list = {}

def add_item(item):
    shopping_list[item] = False

def remove_item(item):
    if item in shopping_list:
        del shopping_list[item]
        print(f"Successfully removed {item} from the shopping list.")
    else:
        print(f"{item} is not in the shopping list.")

def check_off_item(item):
    if item in shopping_list:
        shopping_list[item] = True
        print(f"Checked off {item} from the shopping list.")
    else:
        print(f"{item} is not in the shopping list.")

def display_shopping_list():
    print("Shopping List:")
    for item, checked in shopping_list.items():
        status = " [x]" if checked else " [ ]"
        print(item + status)

while True:
    print("What would you like to do?")
    print("1. Add item to the shopping list")
    print("2. Remove item from the shopping list")
    print("3. Check off item on the shopping list")
    print("4. Display the shopping list")
    print("5. Quit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        item = input("Enter the item to add: ")
        add_item(item)
        print(f"Added {item} to the shopping list.")
    elif choice == "2":
        item = input("Enter the item to remove: ")
        remove_item(item)
    elif choice == "3":
        item = input("Enter the item to check off: ")
        check_off_item(item)
    elif choice == "4":
        display_shopping_list()
    elif choice == "5":
        print("Done!")
        break
    else:
        print("Invalid choice. Please try again.")


'''4. Movie Rating Tracker: 
 Design a program that lets users rate movies on a scale from 1 to 5. Use a dictionary to store 
movie titles and their average ratings. '''

movie_ratings = {}

def add_movie_rating(title, rating):
    if title in movie_ratings:
        movie_ratings[title].append(rating)
    else:
        movie_ratings[title] = [rating]

def calculate_average_rating(title):
    if title in movie_ratings:
        ratings = movie_ratings[title]
        average_rating = sum(ratings) / len(ratings)
        return average_rating
    else:
        return None

while True:
    print("What would you like to do?")
    print("1. Add a movie rating")
    print("2. Calculate the average rating of a movie")
    print("3. Quit")

    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        title = input("Enter the movie title: ")
        rating = float(input("Enter the movie rating (1-5): "))
        add_movie_rating(title, rating)
        print(f"Added rating {rating} for {title}.")
    elif choice == "2":
        title = input("Enter the movie title: ")
        average_rating = calculate_average_rating(title)
        if average_rating is not None:
            print(f"The average rating of {title} is {average_rating:.2f}.")
        else:
            print(f"No ratings found for {title}.")
    elif choice == "3":
        print("You have all done!")
        break
    else:
        print("Invalid choice. Please try again.")


'''5. Temperature Converter: 
 Build a program that converts temperatures between Celsius and Fahrenheit using 
a dictionary to store conversion factors. '''

conversion_factors = {
    'c_to_f': lambda celsius: celsius * 9/5 + 32,
    'f_to_c': lambda fahrenheit: (fahrenheit - 32) * 5/9
}

def convert_temperature(temperature, conversion_type):
    if conversion_type in conversion_factors:
        conversion_func = conversion_factors[conversion_type]
        converted_temperature = conversion_func(temperature)
        return converted_temperature
    else:
        return None

while True:
    print("What would you like to do?")
    print("1. Convert Celsius to Fahrenheit")
    print("2. Convert Fahrenheit to Celsius")
    print("3. Quit")

    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        celsius = float(input("Enter the temperature in Celsius: "))
        converted_temperature = convert_temperature(celsius, 'c_to_f')
        if converted_temperature is not None:
            print(f"{celsius} degrees Celsius is equal to {converted_temperature:.2f} degrees Fahrenheit.")
        else:
            print("Invalid conversion type.")
    elif choice == "2":
        fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
        converted_temperature = convert_temperature(fahrenheit, 'f_to_c')
        if converted_temperature is not None:
            print(f"{fahrenheit} degrees Fahrenheit is equal to {converted_temperature:.2f} degrees Celsius.")
        else:
            print("Invalid conversion type.")
    elif choice == "3":
        print("Have a Nice day")
        break
    else:
        print("Invalid choice. Please try again.")


'''6. Phonebook Organizer: 
 Create a program that stores names and phone numbers in a dictionary. Offer options
to add, search, and update contacts.'''

phonebook = {}
def add_contact(name, phone_number):
    phonebook[name] = phone_number
    print(f"Contact '{name}' with phone number '{phone_number}' added successfully.")

def search_contact(name):
    if name in phonebook:
        phone_number = phonebook[name]
        print(f"Contact found - Name: {name}, Phone Number: {phone_number}")
    else:
        print(f"Contact not found for '{name}'.")

def update_contact(name, new_phone_number):
    if name in phonebook:
        phonebook[name] = new_phone_number
        print(f"Contact '{name}' updated with new phone number '{new_phone_number}'.")
    else:
        print(f"Contact not found for '{name}'.")

while True:
    print("What would you like to do?")
    print("1. Add a contact")
    print("2. Search for a contact")
    print("3. Update a contact")
    print("4. Quit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        name = input("Enter the name of the contact: ")
        phone_number = input("Enter the phone number of the contact: ")
        add_contact(name, phone_number)
    elif choice == "2":
        name = input("Enter the name of the contact to search: ")
        search_contact(name)
    elif choice == "3":
        name = input("Enter the name of the contact to update: ")
        new_phone_number = input("Enter the new phone number: ")
        update_contact(name, new_phone_number)
    elif choice == "4":
        print("You have All Done!")
        break
    else:
        print("Invalid choice. Please try again.")

'''7. Restaurant Menu Parser: 
 Write a program that reads a restaurant menu file (text or CSV) and stores items, prices, and categories 
in a dictionary. Allow users to browse by category or search for specific items.'''

import csv

def read_menu_file(file_name):
    menu = {}
    with open(file_name, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            item = row[0]
            price = float(row[1])
            category = row[2]
            if category not in menu:
                menu[category] = []
            menu[category].append((item, price))
    return menu

def browse_by_category(menu, category):
    if category in menu:
        return menu[category]
    else:
        return "Category not found."

def search_item(menu, item):
    for category, items in menu.items():
        for menu_item, price in items:
            if item.lower() in menu_item.lower():
                return (menu_item, price, category)
    return "Item not found."

# Example usage
menu = read_menu_file('menu.csv')
category = 'Main Course'
print(browse_by_category(menu, category))
item = 'Pizza'
print(search_item(menu, item)) '''

'''8. Password Guesser: 
 Design a simple program that generates random passwords from a set of characters (lowercase, uppercase,
 numbers, symbols). The password length and character limitations can be stored in a dictionary.'''
'''
import random

def generate_password(length, characters):
    password = ''
    for _ in range(length):
        password += random.choice(characters)
    return password

def main():
    password_criteria = {
        'length': 10,
        'characters': 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()'
    }
    length = password_criteria['length']
    characters = password_criteria['characters']
    password = generate_password(length, characters)
    print("Generated Password:", password)

main()

'''9. Song Organizer: 
 Develop a program that stores song titles, artists, and genres in a dictionary. Include functions to sort by 
different criteria (title, artist, genre) and search for specific songs.'''

def add_song(library, title, artist, genre):
    library[title] = {'artist': artist, 'genre': genre}

def sort_songs_by_title(library):
    sorted_titles = sorted(library.keys())
    sorted_songs = {}
    for title in sorted_titles:
        sorted_songs[title] = library[title]
    return sorted_songs

def sort_songs_by_artist(library):
    sorted_songs = sorted(library.items(), key=lambda x: x[1]['artist'])
    return dict(sorted_songs)

def sort_songs_by_genre(library):
    sorted_songs = sorted(library.items(), key=lambda x: x[1]['genre'])
    return dict(sorted_songs)

def search_song(library, title):
    if title in library:
        return library[title]
    else:
        return "Song not found."

# Example usage
song_library = {}
add_song(song_library, "To he kahan", "King", "Love")
add_song(song_library, "Khamoshiyan", "Sarfaraz", "Emotional")
add_song(song_library, "Deewana ho Deewana", "Makror", "Rock")

sorted_by_title = sort_songs_by_title(song_library)
print("Sorted by title:", sorted_by_title)

sorted_by_artist = sort_songs_by_artist(song_library)
print("Sorted by artist:", sorted_by_artist)

sorted_by_genre = sort_songs_by_genre(song_library)
print("Sorted by genre:", sorted_by_genre)

searched_song = search_song(song_library, "Deewana ho Deewana")
print("Searched song:", searched_song)

'''10. Travel Budget Tracker: 
 Create a program that allows users to track their travel expenses by category
(e.g., transportation, accommodation, food). Use a dictionary to store categories
 and their corresponding expenses. '''

def add_expense(expenses, category, amount):
    if category in expenses:
        expenses[category] += amount
    else:
        expenses[category] = amount

def view_expenses(expenses):
    total_expenses = sum(expenses.values())
    print("Total expenses:", total_expenses)
    for category, amount in expenses.items():
        print(category, ":", amount)

# Example usage
travel_expenses = {}

add_expense(travel_expenses, "Transportation", 50)
add_expense(travel_expenses, "Accommodation", 100)
add_expense(travel_expenses, "Food", 30)
add_expense(travel_expenses, "Transportation", 20)

view_expenses(travel_expenses)
