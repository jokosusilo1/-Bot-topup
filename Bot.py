import os
import logging
from dotenv import load_dotenv
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

# Load .env
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Menu Utama
MAIN_MENU = [
    ["💳 Top-up", "💰 Harga"],
    ["📜 Riwayat", "❓ Bantuan"]
]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Halo! Selamat datang di Bot Top-up.\nSilakan pilih menu:",
        reply_markup=ReplyKeyboardMarkup(MAIN_MENU, resize_keyboard=True)
    )

async def menu_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.strip()

    if text == "💳 Top-up":
        await update.message.reply_text("Silakan kirim ID game/nomor HP untuk top-up (contoh: ML 123456789):")
    elif text == "💰 Harga":
        await update.message.reply_text(
            "💰 *Daftar Harga Top-up*\n\n"
            "1. Mobile Legends 86 Diamonds - Rp20.000\n"
            "2. Free Fire 140 Diamonds - Rp25.000\n"
            "3. PUBG UC 60 - Rp15.000",
            parse_mode='Markdown'
        )
    elif text == "📜 Riwayat":
        await update.message.reply_text("Belum ada riwayat transaksi.")
    elif text == "❓ Bantuan":
        await update.message.reply_text("Hubungi admin untuk bantuan: @username_admin")
    else:
        await update.message.reply_text("Menu tidak dikenal, silakan pilih dari menu utama.")

if __name__ == '__main__':
    if not BOT_TOKEN:
        print("Error: BOT_TOKEN tidak ditemukan di .env")
    else:
        app = ApplicationBuilder().token(BOT_TOKEN).build()
        app.add_handler(CommandHandler("start", start))
        app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, menu_handler))
        app.run_polling()
