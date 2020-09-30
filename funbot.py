import sys
import time
import random
import datetime
import telepot

def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']

    print('Got command: %s' % command)

#idi start mukka   
    if command == '/start':
        bot.sendMessage(chat_id," meru korina vyakthi branch sankhyanu ivvandi udha: cse 17951A05##")
        
        

#experiment

    
    command == "command"
    Branch = command.split(' ')[0]
    print(Branch)
    command == "command"
    roll = command.split(' ')[-1]
    print(roll)
    if roll=='17951A05A7':
        bot.sendMessage(chat_id,"betterlucknexttime!")
        bot.sendPhoto(chat_id,"https://600904.smushcdn.com/1098074/wp-content/uploads/2018/11/bitmoji-20181119104523-1-300x300.png?lossy=0&strip=0&webp=1")
    else:
                       link = "https://iare-data.s3.ap-south-1.amazonaws.com/uploads/"+Branch.lower()+"/"+roll+".jpg"
                       print(link)
                       bot.sendPhoto(chat_id,link)
                       bot.sendMessage(chat_id,'ok next')
    #context.bot.sendPhoto(chat_id, photo="https://t.me/addstickers/FRIDAY_653340100_Pack", caption="avna yaar uu")
                       link2 = "https://i.ytimg.com/vi/28Vlykt6ofo/hqdefault.jpg"
                       bot.sendPhoto(chat_id,link2)

   

bot = telepot.Bot('914559098:AAGDM825JY2C-lmogTwnXx-kTpQ7VR1tN48')
bot.message_loop(handle)
print('I am listening ...')

while 1:
    time.sleep(10)
