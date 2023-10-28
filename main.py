import random

def choose_word():
    words = ["televizyon", "insan evladı", "evlilik", "traktör", "iş makinası", "otobüs durağı", "gözlem kulesi",
             "ay ışığı", "bubi tuzağı", "kalem", "şeker", "ferah", "tsunami", "genç"]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter == " " or letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def hangman():
    word = choose_word()
    max_attempts = 10
    guessed_letters = []

    uzunluk = len(word)

    print(f"Adam Asmaca oyununa hoş geldiniz! Kelimeniz {uzunluk} harf! {max_attempts} tahmin hakkınız var!")

    while max_attempts > 0:
        print(display_word(word, guessed_letters))
        guess = input("Bir harf tahmin edin: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Lütfen geçerli bir harf girin.")
            continue

        if guess in guessed_letters:
            print("Bu harfi zaten tahmin ettiniz.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("Harika! Doğru tahmin ettiniz.")
            if display_word(word, guessed_letters) == word:
                print(f"Tebrikler, kelimeyi buldunuz! Kelime: {word}")
                break
        else:
            max_attempts -= 1
            print(f"Yanlış tahmin. Kalan hakkınız: {max_attempts}")

    if max_attempts == 0:
        print(f"Üzgünüm, hakkınız bitti. Doğru kelime: {word}")

if __name__ == "__main__":
    hangman()