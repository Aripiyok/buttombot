# Button Adder Bot

Bot Telegram untuk menambahkan tombol otomatis ke setiap pesan yang dikirimkan dari akun forwarder.

## Cara penggunaan
1. Isi file `.env` dengan API_ID, API_HASH, BOT_TOKEN, dan TARGET_CHANNEL.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Jalankan bot:
   ```bash
   python button_adder_bot.py
   ```

Pesan yang masuk ke bot ini akan diteruskan ke channel tujuan dengan tombol otomatis.
