from codecarbon import track_emissions

@track_emissions()
def is_palindrome(word):
    # Normalisasi kata dengan mengubahnya menjadi huruf kecil
    normalized_word = word.lower()
    # Periksa apakah kata tersebut sama saat dibaca dari depan dan belakang
    return normalized_word == normalized_word[::-1]

# Daftar kata uji
test_words = ["radar", "level", "hello", "world", "madam", "python"]

# Memeriksa setiap kata dalam daftar
for test_word in test_words:
    if is_palindrome(test_word):
        print(f"{test_word} adalah palindrome.")
    else:
        print(f"{test_word} bukan palindrome.")
