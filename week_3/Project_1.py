girls = [
    {"name": "Evelyn", "age": 17, "height": 5.5, "score": 80},
    {"name": "Jessica", "age": 16, "height": 6.0, "score": 85},
    {"name": "Somto", "age": 17, "height": 5.4, "score": 70},
    {"name": "Edith", "age": 18, "height": 5.9, "score": 60},
    {"name": "Liza", "age": 16, "height": 5.6, "score": 76},
    {"name": "Madonna", "age": 18, "height": 5.5, "score": 66},
    {"name": "Waje", "age": 17, "height": 6.1, "score": 87},
    {"name": "Tola", "age": 20, "height": 6.0, "score": 95},
    {"name": "Aisha", "age": 19, "height": 5.7, "score": 50},
    {"name": "Latifa", "age": 17, "height": 5.5, "score": 49}
]

boys = [
    {"name": "Chinedu", "age": 19, "height": 5.7, "score": 74},
    {"name": "Liam", "age": 16, "height": 5.9, "score": 87},
    {"name": "Wale", "age": 18, "height": 5.8, "score": 75},
    {"name": "Gbenga", "age": 17, "height": 6.1, "score": 68},
    {"name": "Abiola", "age": 20, "height": 5.9, "score": 66},
    {"name": "Kola", "age": 19, "height": 5.5, "score": 78},
    {"name": "Kunle", "age": 16, "height": 6.1, "score": 87},
    {"name": "George", "age": 18, "height": 5.4, "score": 98},
    {"name": "Thomas", "age": 17, "height": 5.8, "score": 54},
    {"name": "Wesley", "age": 19, "height": 5.7, "score": 60}
]

# Print the data in a tabular form
print("Girls:")
print("Name | Age | Height | Score")
for girl in girls:
    print(f"{girl['name']} | {girl['age']} | {girl['height']} | {girl['score']}")

print("\nBoys:")
print("Name | Age | Height | Score")
for boy in boys:
    print(f"{boy['name']} | {boy['age']} | {boy['height']} | {boy['score']}")