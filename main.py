morse_dict = {
  "0": "-----",
  "1": ".----",
  "2": "..---",
  "3": "...--",
  "4": "....-",
  "5": ".....",
  "6": "-....",
  "7": "--...",
  "8": "---..",
  "9": "----.",
  "a": ".-",
  "b": "-...",
  "c": "-.-.",
  "d": "-..",
  "e": ".",
  "f": "..-.",
  "g": "--.",
  "h": "....",
  "i": "..",
  "j": ".---",
  "k": "-.-",
  "l": ".-..",
  "m": "--",
  "n": "-.",
  "o": "---",
  "p": ".--.",
  "q": "--.-",
  "r": ".-.",
  "s": "...",
  "t": "-",
  "u": "..-",
  "v": "...-",
  "w": ".--",
  "x": "-..-",
  "y": "-.--",
  "z": "--..",
  ".": ".-.-.-",
  ",": "--..--",
  "?": "..--..",
  "!": "-.-.--",
  "-": "-....-",
  "/": "-..-.",
  "@": ".--.-.",
  "(": "-.--.",
  ")": "-.--.-",
    " ": "   "
}
## Create user interface.

ison = True

print("Welcome to The International Morse Code Translator.")
while ison:
    textinput = input("Enter text ('\q' to quit):")
    if textinput == '\q':
        ison = False
        print("Goodbye.")
    else:
        translation_list = []
        try:
          for char in textinput.lower():
            translation_list.append(morse_dict[char])
        except KeyError as msg:
          print(f"{msg} is an invalid character.")
        else:
          translation_str = " ".join(translation_list)
          print(translation_str)


