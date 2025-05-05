import string

def create_hashtag(text):
    for char in string.punctuation + " ":
        text = text.replace(char, "")

    if not text:
        return "#"

    # words = text.split()
    text = original_text.translate(str.maketrans('', '', string.punctuation))
    words = text.strip().split()
    capitalized_words = [word.capitalize() for word in words]
    hashtag = "#" + "".join(capitalized_words)

    return hashtag[:140]
original_text = input("Enter your text: ")
hashtag = create_hashtag(original_text)
print("Hashtag:", hashtag)
