import datetime
import calendar

# Data libur nasional
holidays = {
    "25-12-2024": "Hari Raya Natal",
    "01-01-2025": "Tahun Baru",
    "17-08-2024": "Hari Kemerdekaan Indonesia",
}

# Fungsi konversi format tanggal
def convert_date_format(date_str, new_format):
    try:
        date_obj = datetime.datetime.strptime(date_str, "%d-%m-%Y")
        return date_obj.strftime(new_format)
    except ValueError:
        return "Format tanggal salah. Harap gunakan DD-MM-YYYY."

# Fungsi untuk mendapatkan hari dalam minggu
def get_day_of_week(date_str):
    try:
        date_obj = datetime.datetime.strptime(date_str, "%d-%m-%Y")
        days = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"]
        return f"Tanggal {date_str} adalah {days[date_obj.weekday()]}."
    except ValueError:
        return "Format tanggal salah. Harap gunakan DD-MM-YYYY."

# Fungsi untuk mengecek hari libur
def check_holiday(date_str):
    return holidays.get(date_str, "Tanggal ini bukan hari libur nasional.")

# Fungsi untuk menampilkan kalender
def display_calendar(month, year):
    try:
        month = int(month)
        year = int(year)
        return calendar.TextCalendar().formatmonth(year, month)
    except ValueError:
        return "Input bulan atau tahun tidak valid."

# Program utama
print("Selamat datang di Program Konversi Tanggal dan Kalender Pintar!")
print("1. Konversi Format Tanggal")
print("2. Cari Hari dalam Minggu")
print("3. Cek Hari Libur Nasional")
print("4. Tampilkan Kalender Bulanan")
choice = input("Pilih opsi (1/2/3/4): ")

if choice == "1":
    date_input = input("Masukkan tanggal (DD-MM-YYYY): ")
    new_format = input("Masukkan format baru (misalnya: %Y/%m/%d): ")
    print(convert_date_format(date_input, new_format))
elif choice == "2":
    date_input = input("Masukkan tanggal (DD-MM-YYYY): ")
    print(get_day_of_week(date_input))
elif choice == "3":
    date_input = input("Masukkan tanggal (DD-MM-YYYY): ")
    print(check_holiday(date_input))
elif choice == "4":
    month = input("Masukkan bulan (angka): ")
    year = input("Masukkan tahun: ")
    print(display_calendar(month, year))
else:
    print("Opsi tidak valid!")
