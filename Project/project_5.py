import string
from collections import Counter

# Fungsi untuk membersihkan teks dari tanda baca dan membuatnya case-insensitive
def clean_text(text):
    text = text.lower()  # Ubah ke huruf kecil
    text = text.translate(str.maketrans("", "", string.punctuation))  # Hapus tanda baca
    return text

# Fungsi utama analisis teks
def analyze_text(text):
    # Bersihkan teks
    cleaned_text = clean_text(text)
    
    # Pisahkan teks menjadi list kata
    words = cleaned_text.split()
    
    # Hitung total kata
    total_words = len(words)
    
    # Hitung kemunculan setiap kata
    word_counts = Counter(words)
    
    # Temukan kata yang paling sering muncul
    most_common_word, most_common_count = word_counts.most_common(1)[0]
    
    # Buat daftar kata-kata unik
    unique_words = list(word_counts.keys())
    
    # Tampilkan hasil analisis
    print("\n--- Hasil Analisis Teks ---")
    print(f"Total Kata: {total_words}")
    print(f"Kata Paling Sering Muncul: {most_common_word} (muncul {most_common_count} kali)")
    print(f"Kata-Kata Unik: {unique_words}")

# Input teks dari user
print("Selamat datang di Program Analisis Teks!")
user_input = input("Masukkan teks yang ingin dianalisis:\n")
analyze_text(user_input)
