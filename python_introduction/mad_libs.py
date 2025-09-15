# constructing a mad lib program
adjective1 = input("Enter a day's weather adjective: ")
adjective2 = str(input("Enter a monkey's size adjective: "))
adjective3 = str(input("Enter a lion's gender: "))
adjective = str(input("Enter the day's experince adjective: "))

story = f""""
On a beautiful {adjective1} day, I went to the zoo.
I saw a funny {adjective2} monkey swinging from the trees.
Then, I spotted a majestic {adjective3} lion lounging in the sun. 
What a wild and {adjective} experience!"""

if adjective.lower() == "scary":
    story += "\nI was a bit scared but excited!"
elif adjective.lower() == "fun":
    story += "\nI had so much fun!"
else:
    story += "\nIt was an unforgettable experience!"

# displaying the story with the user's inputs
print(story)