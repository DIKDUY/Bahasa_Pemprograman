try:
    hasil = 10 / 0
except ZeroDivisionError as e:
    print(f"Terjadi kesalahan: {e}")
else:
    print("Pembagian berhasil")
finally:
    print("Eksekusi selesai")