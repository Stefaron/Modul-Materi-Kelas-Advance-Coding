import random

# Daftar pertanyaan dan jawaban
questions = [
    {"question": "Apa ibu kota Indonesia?", "answer": "Jakarta"},
    {"question": "Siapa presiden pertama RI?", "answer": "Soekarno"},
    {"question": "Apa hasil dari 5 + 3?", "answer": "8"},
    {"question": "Apa warna dasar bendera Jepang?", "answer": "Putih"},
    {"question": "Siapa penemu lampu pijar?", "answer": "Edison"},
    {"question": "Berapa sisi pada segitiga?", "answer": "3"}
]

# Acak pertanyaan dan pilih 5 random
selected_questions = random.sample(questions, 5)

# Mulai kuis
print("Selamat datang di Mini Quiz! Jawab pertanyaan berikut:")
score = 0

# Loop melalui pertanyaan
for idx, q in enumerate(selected_questions, 1):
    print(f"\nPertanyaan {idx}: {q['question']}")
    user_answer = input("Jawaban kamu: ").strip()

    if user_answer.lower() == q['answer'].lower():
        print("✅ Benar!")
        score += 1
    else:
        print(f"❌ Salah! Jawaban yang benar: {q['answer']}")

# Output skor akhir
print("\n--- Hasil Akhir ---")
print(f"Skor kamu: {score}/{len(selected_questions)}")
