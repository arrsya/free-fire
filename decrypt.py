import base64

def xor_encrypt_decrypt(data, key):
    return ''.join(chr(ord(c) ^ ord(k)) for c, k in zip(data, key * (len(data) // len(key) + 1)))

# Nama file terenkripsi
encrypted_file = 'sahil.py.enc'
# Nama file output setelah didekripsi
output_file = 'sahil_decrypted.py'

# Kunci enkripsi yang digunakan
key = '@SahilModzOwner'

# Membaca isi file terenkripsi
with open(encrypted_file, 'r') as file:
    encrypted_script_base64 = file.read()

# Dekripsi isi file
encrypted_script = base64.b64decode(encrypted_script_base64).decode()
decrypted_script = xor_encrypt_decrypt(encrypted_script, key)

# Simpan script didekripsi ke file baru
with open(output_file, 'w') as file:
    file.write(decrypted_script)

print(f"Script berhasil didekripsi ke '{output_file}'")
