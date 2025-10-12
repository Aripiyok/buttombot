from telethon import TelegramClient, events, Button
import os
from dotenv import load_dotenv

load_dotenv()

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")
TARGET_CHANNEL = os.getenv("TARGET_CHANNEL")

# Tombol contoh (bisa kamu ubah sendiri)
BUTTONS = [
    [Button.url("📢 Channel Backup ", "https://t.me/+83yUVYjj-v5jNzVl")]
]


bot = TelegramClient("button_adder", API_ID, API_HASH).start(bot_token=BOT_TOKEN)

@bot.on(events.NewMessage)
async def handler(event):
    try:
        sender = await event.get_sender()
        print(f"📨 Pesan diterima dari: {sender.username or sender.id}")

        if event.message.media:
            await bot.send_file(
                TARGET_CHANNEL,
                event.message.media,
                caption=event.message.text or "",
                buttons=BUTTONS,
                link_preview=False
            )
        else:
            await bot.send_message(
                TARGET_CHANNEL,
                event.message.text or "",
                buttons=BUTTONS,
                link_preview=False
            )

        print(f"✅ Dikirim ke {TARGET_CHANNEL} dengan tombol\n")
    except Exception as e:
        print(f"⚠️ Gagal kirim pesan: {e}")

print("🤖 Button Adder Bot aktif! Menunggu pesan dari akun forwarder...")
bot.run_until_disconnected()
