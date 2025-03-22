#!/bin/bash

echo "در حال نصب پیش‌نیازها..."

# بررسی و نصب Python
if ! command -v python3 &> /dev/null; then
    echo "در حال نصب Python..."
    sudo apt-get update
    sudo apt-get install -y python3 python3-pip
fi

# نصب کتابخانه‌های مورد نیاز
echo "در حال نصب کتابخانه‌های مورد نیاز..."
pip3 install python-telegram-bot

# دانلود و اجرای ربات
echo "در حال دانلود فایل ربات..."
curl -o bot.py https://raw.githubusercontent.com/jasemhooti/bat/main/bot.py

echo "نصب با موفقیت انجام شد!"
echo "برای اجرای ربات، لطفاً توکن ربات خود را در فایل bot.py قرار دهید و سپس دستور زیر را اجرا کنید:"
echo "python3 bot.py" 