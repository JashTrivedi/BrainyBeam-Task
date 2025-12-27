import wikipedia

topic = input("Enter topic: ")

try:
    content = wikipedia.summary(topic, sentences=5)
    with open("wikipedia_explanation.txt", "w", encoding="utf-8") as file:
        file.write(content)
    print("File saved as wikipedia_explanation.txt")
except Exception as e:
    print("Error:", e)
