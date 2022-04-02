import telebot
import os
import subprocess

bot = telebot.TeleBot('1866342336:AAHHss7SFJH7opW8dHvSIeAsiOn0TT4o9po')

@bot.message_handler(commands=['start'])
def send_welcome(m):
    bot.send_message(m.chat.id, 'Welcome! please enter username to search')

@bot.message_handler(func=lambda message: True,content_types='text')
def search(m):
    username = m.text
    bot.send_message(m.chat.id,"searching")
    subprocess.run(['sherlock',str(username),'--site','telegram','--site','facebook','--site','tinder','--site','tiktok','--site','github','-o',str(username)])
    googleaccount = str(username) + '@gmail.com'
    subprocess.run(['sudo','python3','/opt/GHunt/ghunt.py','email',googleaccount,'|','tee','email'])
    sherlock = open(str(username),'rb')
    gmail = open('email','rb')
    bot.send_document(m.chat.id,sherlock)
    bot.send_document(m.chat.id,gmail)
    file.close()
    subprocess.run(['rm',str(username)])
    subprocess.run(['rm','gmail'])
    
bot.polling()