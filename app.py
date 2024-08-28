import random

def mad_libs_game():
    print("Get ready for some Mad Libs fun! Can you create the craziest story ever? Let's find out!")

    while True:
        # Prompt user to select a template for their story
        template_choice = input("Choose a template (1, 2, or 3):\n1. Hospital\n2. Camping\n3. Castle\n")

        if template_choice == '1':
            # Template 1: Hospital
            number1 = input("Please enter a number: ")
            time_options = ["hours", "days", "weeks", "months"]
            measure_of_time = random.choice(time_options)
            silly_words = ["flibber", "wobble", "snorkel", "gizmo"]
            silly_word = random.choice(silly_words)
            nouns1 = ["dog", "cat", "robot", "dragon"]
            nouns2 = ["apple", "book", "car", "hat"]
            nouns5 = ["ball", "pencil", "shoe", "flower"]
            noun1 = random.choice(nouns1)
            noun2 = random.choice(nouns2)
            noun5 = random.choice(nouns5)
            mode_of_transportation = input("Please enter a mode of transportation (e.g., car, bicycle): ")
            adjective1 = input("Please enter an adjective: ")
            adjective2 = input("Please enter another adjective: ")
            color = input("Please enter a color: ")
            part_of_the_body1 = input("Please enter a part of the body (e.g., arm, leg): ")
            verb1 = input("Please enter a verb: ")
            number2 = input("Please enter another number: ")
            noun3 = input("Please enter a different noun: ")
            part_of_the_body2 = input("Please enter another part of the body: ")
            verb2 = input("Please enter another verb: ")
            noun4 = input("Please enter another noun: ")
            adjective3 = input("Please enter an adjective: ")

            story = (
                f"It was about {number1} {measure_of_time} ago when I arrived at the hospital in a {mode_of_transportation}. "
                f"The hospital is a/an {adjective1} place, there are a lot of {adjective2} {noun1} here. "
                f"There are nurses here who have {color} {part_of_the_body1}. If someone wants to come into my room, "
                f"I told them that they have to {verb1} first. I’ve decorated my room with {number2} {noun2}. "
                f"Today I talked to a doctor and they were wearing a {noun3} on their {part_of_the_body2}. "
                f"I heard that all doctors {verb2} {noun4} every day for breakfast. The most {adjective3} thing about being in the hospital is the {silly_word} {noun5}!"
            )

        elif template_choice == '2':
            # Template 2: Camping
            proper_noun = input("Please enter a person's name: ")
            noun = input("Please enter a noun: ")
            adjective1 = input("Please enter an adjective (feeling): ")
            verb1 = input("Please enter a verb: ")
            adjective2 = input("Please enter another adjective (feeling): ")
            animals = ["bear", "fox", "wolf", "eagle"]
            animal = random.choice(animals)
            verb2 = input("Please enter another verb: ")
            color = input("Please enter a color: ")
            verb_ing = input("Please enter a verb ending in -ing: ")
            adverb = input("Please enter an adverb ending in -ly: ")
            number = input("Please enter a number: ")
            measure_of_time = input("Please enter a measure of time (e.g., hours, days): ")
            silly_words = ["flibber", "wobble", "snorkel", "gizmo"]
            silly_word = random.choice(silly_words)
            noun2 = input("Please enter another noun: ")

            story = (
                f"This weekend I am going camping with {proper_noun}. I packed my lantern, sleeping bag, and {noun}. "
                f"I am so {adjective1} to {verb1} in a tent. I am {adjective2} we might see a(n) {animal}, I hear they’re kind of dangerous. "
                f"While we’re camping, we are going to hike, fish, and {verb2}. I have heard that the {color} lake is great for {verb_ing}. "
                f"Then we will {adverb} hike through the forest for {number} {measure_of_time}. If I see a {color} {animal} while hiking, I am going to bring it home as a pet! "
                f"At night we will tell {number} {silly_word} stories and roast {noun2} around the campfire!!"
            )

        elif template_choice == '3':
            # Template 3: Castle
            proper_nouns = ["Armen", "Ani", "Tigran", "Nare"]
            proper_noun = random.choice(proper_nouns)
            adjective1 = input("Please enter an adjective: ")
            color = input("Please enter a color: ")
            animal = input("Please enter an animal: ")
            place = input("Please enter a place: ")
            adjective2 = input("Please enter another adjective: ")
            magical_creature1 = input("Please enter a magical creature (plural): ")
            adjective3 = input("Please enter another adjective: ")
            magical_creature2 = input("Please enter another magical creature (plural): ")
            room = input("Please enter a room in a house: ")
            noun = input("Please enter a noun: ")
            noun2 = input("Please enter another noun: ")
            noun3 = input("Please enter another plural noun: ")
            adjective4 = input("Please enter an adjective: ")
            noun4 = input("Please enter another plural noun: ")
            number = input("Please enter a number: ")
            measure_of_time = input("Please enter a measure of time (e.g., hours, days): ")
            verb_ing = input("Please enter a verb ending in -ing: ")
            adjective5 = input("Please enter another adjective: ")
            noun5 = input("Please enter another noun: ")

            story = (
                f"Dear {proper_noun}, I am writing to you from a {adjective1} castle in an enchanted forest. "
                f"I found myself here one day after going for a ride on a {color} {animal} in {place}. "
                f"There are {adjective2} {magical_creature1} and {adjective3} {magical_creature2} here! "
                f"In the {room} there is a pool full of {noun}. I fall asleep each night on a {noun2} of {noun3} and dream of {adjective4} {noun4}. "
                f"It feels as though I have lived here for {number} {measure_of_time}. I hope one day you can visit, although the only way to get here now is {verb_ing} on a {adjective5} {noun5}!!"
            )

        else:
            print("Invalid choice. Please select 1, 2, or 3.")
            continue

        print(story)

        # Ask if the user wants to play again
        play_again = input("Would you like to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print("Thank you for playing! Goodbye!")
            break

# Call the function to test it
mad_libs_game()


