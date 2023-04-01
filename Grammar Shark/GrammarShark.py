import tkinter as tk

from spellchecker import SpellChecker

spell = SpellChecker()


def update_message(event):
    text = text_entry.get("1.0", tk.END).strip()
    words = text.split()
    correct_words = []
    for word in words:
        correction = spell.correction(word)
        if correction is not None and correction != word:
            correct_words.append(correction)
            correct_words.append(spell.correction(word))
        else:
            correct_words.append(word)
    correct_text = " ".join(correct_words)
    text_corr.config(text=correct_text)


root = tk.Tk()
root.title("Martin's Grammar Shark")
root.geometry("500x500")

text_entry = tk.Text(root, bg="white")
text_entry.pack()
text_entry.bind("<KeyRelease>", update_message)

text_corr = tk.Message(root)
text_corr.pack()

root.mainloop()
