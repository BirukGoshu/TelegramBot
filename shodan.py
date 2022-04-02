import telebot
import subprocess
import urllib.parse as up

bot = telebot.TeleBot('1986580051:AAHnWyOor8WcrKDJMwlGZrIm65l9amahrqQ')

@bot.message_handler(commands=['start'])
def send_welcome(m):
    bot.send_message(m.chat.id, 'Welcome! please enter search query')

@bot.message_handler(func=lambda message: True,content_types='text')
def search(m):
    query ="https://beta.shodan.io/search?query=" + str(up.quote(str(m.text)))
    cookie = 'polito="2719e913fe7d2e1caa668ee76bbc441d60ed54eb5bf10960e449854b14f9dde4!"'
    print(query)
    subprocess.run(['curl','-b',cookie,query,'-o','result.html'])
    # data = requests.get('https://beta.shodan.io/search?query=' + query).json()
    file = open('result.html','rb')
    bot.send_document(m.chat.id,file)
    file.close()
    subprocess.run(['rm','result.html'])
    

bot.polling()