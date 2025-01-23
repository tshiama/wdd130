print ("hello user! welcome to mab_libs_game" )

adjective = input("Please enter an adjective: ")
animal = input("Please enter an animal: ")
verb1 = input("Please enter a verb: ")
exclamation = input("Please enter an exlamation: ")
print(exclamation.capitalize())
verb2 = input("Please enter a verb: ")
verb3 = input("Please enter a verb: ")

words = f'''The other day, I was really in trouble.
\nIt all started when I saw a very {adjective} {animal} {verb1} down the hallway. 
\n"{exclamation}!" I yelled. 
\nBut all I could think to do was to {verb2} over and over. 
\nMiraculously, that caused it to stop, but not before it tried to {verb3} right in front of my family.'''

print(words)