with open("books/frankenstein.txt") as f:

  file_contents = f.read()

  words = len(file_contents.split())
  print("--- Begin report of books/frankenstein.txt ---")
  print(f"{words} words found in the document\n")

  def count_letters(file):
    letters = {}
    letter_list = list(file.lower())
    for letter in letter_list:
      if letter.isalpha():
        if letter in letters:
          letters[letter] += 1
        else:
          letters[letter] = 1

    for key, value in letters.items():
      print(f"The '{key}' character was found {value} times")

  count_letters(file_contents)

print("--- End report ---")
