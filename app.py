def mad_libs_game():
    print("Thank you for playing my Mad Libs game! I hope you will enjoy it!")

    number1 = input("Please enter a number: ")
    measure_of_time = input("Please enter a measure of time (e.g., hours, days): ")
    mode_of_transportation = input("Please enter a mode of transportation (e.g., car, bicycle): ")
    adjective1 = input("Please enter an adjective: ")
    adjective2 = input("Please enter another adjective: ")
    noun1 = input("Please enter a noun: ")
    color = input("Please enter a color: ")
    part_of_the_body1 = input("Please enter a part of the body (e.g., arm, leg): ")
    verb1 = input("Please enter a verb: ")
    number2 = input("Please enter another number: ")
    noun2 = input("Please enter another noun: ")
    noun3 = input("Please enter a different noun: ")
    part_of_the_body2 = input("Please enter another part of the body: ")
    verb2 = input("Please enter another verb: ")
    noun4 = input("Please enter another noun: ")
    adjective3 = input("Please enter an adjective: ")
    silly_word = input("Please enter a silly word: ")
    noun5 = input("Please enter another noun: ")

    story = (
        f"It was about {number1} {measure_of_time} ago when I arrived at the hospital in a {mode_of_transportation}. "
        f"The hospital is a/an {adjective1} place, there are a lot of {adjective2} {noun1} here. "
        f"There are nurses here who have {color} {part_of_the_body1}. If someone wants to come into my room, "
        f"I told them that they have to {verb1} first. I’ve decorated my room with {number2} {noun2}. "
        f"Today I talked to a doctor and they were wearing a {noun3} on their {part_of_the_body2}. "
        f"I heard that all doctors {verb2} {noun4} every day for breakfast. The most {adjective3} thing about being in the hospital is the {silly_word} {noun5}!"
    )

    print(story)
mad_libs_game()