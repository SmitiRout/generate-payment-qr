from spellchecker import SpellChecker

class SpellcheckerApp:
    def __init__(self):
        self.spell = SpellChecker()  # ✅ This line is REQUIRED

    def correct_text(self, text):
        words = text.split()
        corrected_words = []
        for word in words:
            corrected_word = self.spell.correction(word)  # will now work fine
            corrected_words.append(corrected_word)
        return ' '.join(corrected_words)

    def run(self):
        print("---Spell Checker---")
        while True:
            text = input('Enter the text to check (or type "exit" to quit): ')
            if text.lower() == "exit":
                break
            corrected_text = self.correct_text(text)
            print("Corrected text:", corrected_text)

# Run the app
if __name__ == "__main__":
    SpellcheckerApp().run()
