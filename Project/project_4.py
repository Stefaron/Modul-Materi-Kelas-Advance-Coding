from difflib import get_close_matches

# Data kamus sinonim dan antonim
dictionary = {
    "bahagia": {"sinonim": ["senang", "gembira", "riang"], "antonim": ["sedih", "murung"]},
    "besar": {"sinonim": ["luas", "agung", "kolosal"], "antonim": ["kecil", "sempit"]},
    "cepat": {"sinonim": ["laju", "gesit", "segera"], "antonim": ["lambat", "pelan"]},
    "panas": {"sinonim": ["hangat", "gerah", "mendidih"], "antonim": ["dingin", "sejuk"]},
}

def find_word(word):
    word_lower = word.lower()
    if word_lower in dictionary:
        return dictionary[word_lower]
    else:
        # Auto-correct suggestion
        suggestions = get_close_matches(word_lower, dictionary.keys(), n=1)
        if suggestions:
            suggested_word = suggestions[0]
            return f"Kata tidak ditemukan. Apakah maksud Anda '{suggested_word}'?"
        else:
            return "Kata tidak ditemukan dalam kamus."

# Program utama
print("Selamat datang di Kamus Sinonim & Antonim!")
user_word = input("Masukkan kata: ").strip()

result = find_word(user_word)

if isinstance(result, dict):
    # Output sinonim dan antonim
    print(f"\nSinonim: {', '.join(result['sinonim'])}")
    print(f"Antonim: {', '.join(result['antonim'])}")
else:
    # Output pesan jika kata tidak ditemukan
    print(result)
