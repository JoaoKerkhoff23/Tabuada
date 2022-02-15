import telebot
import requests
Wea_Key = 'aa0a6f48661e2357c43f5fd7a3471add'
link = f'https://api.openweathermap.org/data/2.5/weather?q={"Cascavel"},{"Paraná"},{"Brazil"}&appid={Wea_Key}&lang=pt_br'

req = requests.get(link)
req_dic = req.json()
desc = req_dic ['weather'][0]['description']
temp = req_dic ['main']['temp']- 273

API_KEY = "5101734175:AAGKWb2aATgvPsrO7gXU7Ln9ZT8wUCZobdU"
bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands=['start'])
def call(message):
    bot.send_message(message.chat.id, 'Olá Senhor \nEssas são as opções do que eu posso fazer: '
                                      '\n /Clima ~ Mostra o climatempo ')

@bot.message_handler(commands=['Clima'])
def call(message):
    bot.send_message(message.chat.id, f'{desc} e {temp} °C em Toledo,PR' )

bot.polling()
