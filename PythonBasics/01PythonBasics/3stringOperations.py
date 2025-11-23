
# String operations in Python to create a multi-line story using triple quotes
story = """Once upon a time, a thirsty crow searched for water. 
It found a pot with little water. The clever crow dropped pebbles, 
raising the water level, and quenched its thirst."""
print(story)
print(f"Story length: {len(story)} characters")
print(" the work crow appears at index:", story.index("crow"))
print(f"the work crow found at index: {story.find('crow') }charecters")
print("Is 'crow' in story?", 'crow' in story)
print("Is 'dog' in story?", 'dog' in story)
story = story.replace("crow", "reven")
print("Updated Story:\n", story)
# String formatting
print("story in uppercase:\n", story.upper())
print("story in lowercase:\n", story.lower())
words = story.split()
for word in words:
    print(word)