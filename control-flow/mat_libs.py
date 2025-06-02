# Mad libs template story
template_story = "(On a _____ day. I went to the zoo. I saw a _____ monkey swinging from the trees.Then, I spotted a _____ lion lounging in the sun. What a _____ experience!)"

# Collect user name
name = input("Please enter your name: ").capitalize()

# Print template story and instructions for completing the story
print(f"Welcome {name}!. Below is the template story in bracket(). \n{template_story}")
print("Fill in the blanks to construct your personalized story by providing four(4) adjectives below.")

# Collect user input to construct the story
first_word = input("Please input your first adjective: ")
second_word = input("Please input your second adjective: ")
third_word = input("Please input your third adjective: ")
fourth_word = input("Please input your fourth adjective: ")

# Mad Libs User Personalized Story
story = f"On a {first_word} day. I went to the zoo. I saw a {second_word} monkey swinging from the trees.Then, I spotted a {third_word} lion lounging in the sun. What a {fourth_word} experience!"

# 
if fourth_word.lower() == "wild":
    variation = "I was kind of scared!"
elif fourth_word.lower() == "beautiful":
    variation = "I had so much fun!"
else:
    variation = "Nonetheless, I enjoyed it"
print(story)
print(variation)
