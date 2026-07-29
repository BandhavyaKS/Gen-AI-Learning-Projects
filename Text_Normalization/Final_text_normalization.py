import re
import string
import emoji
import contractions
from textblob import TextBlob


class TextNormalization:

    def __init__(self, data):
        self.data = data

    def str_lowercase(self):
        self.data = self.data.lower()

    def remove_punctuation(self):
        chars = self.data

        for ch in string.punctuation:
            chars = chars.replace(ch, "")

        self.data = chars

    def remove_special_characters(self):
        chars = self.data

        new_text = ""

        for ch in chars:
            if ch.isalnum() or ch.isspace():
                new_text += ch

        self.data = new_text

    def emoji_to_text(self):
        self.data = emoji.demojize(self.data)

    def remove_emojis(self):
        self.data = emoji.replace_emoji(self.data, replace="")

    def remove_extra_spaces(self):
        self.data = re.sub(r"\s+", " ", self.data).strip()

    def expand_contractions(self):
        self.data = contractions.fix(self.data)

    def correct_words(self):
        self.data = str(TextBlob(self.data).correct())

    def start(self):

        print("\n******** TEXT NORMALIZATION ********")

        print("""
1. Convert to Lowercase
2. Remove Punctuation
3. Remove Special Characters
4. Emoji Handling
5. Remove Extra Spaces
6. Expand Contractions
7. Correct Spelling
""")

        # Step 1
        self.str_lowercase()

        # Step 2
        choice = input(
            "\nDo you want to remove punctuation and special characters? (yes/no): "
        )

        if choice.lower() == "yes":
            self.remove_punctuation()
            self.remove_special_characters()

        # Step 3
        print("\nEmoji Handling")
        print("1. Convert Emojis to Text")
        print("2. Remove Emojis")

        emoji_choice = input("Enter your choice (1/2): ")

        if emoji_choice == "1":
            self.emoji_to_text()

        elif emoji_choice == "2":
            self.remove_emojis()

        # Step 4
        self.remove_extra_spaces()

        # Step 5
        self.expand_contractions()

        # Step 6
        self.correct_words()

        return self.data


# ---------------- MAIN ----------------

text = input("Enter the text: ")

obj = TextNormalization(text)

result = obj.start()

print("\nNormalized Text:")
print(result)