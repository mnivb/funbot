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
    if command == '/run':
        bot.sendMessage(chat_id," meru korina vyakthi branch sankhyanu ivvandi udha: cse 17951A05##")
        
        

#experiment

    command = input("Enter Branch and Roll no, Eg: cse 17951A0572 :")
    command == "command"
    Branch = command.split(' ')[0]
    print(Branch)
    command == "command"
    roll = command.split(' ')[-1]
    print(roll)
    link = "https://iare-data.s3.ap-south-1.amazonaws.com/uploads/"+Branch+"/"+roll+".jpg"
    print(link)
    bot.sendMessage('ok next andi,order mukhyam bigiluu')



bot = telepot.Bot('914559098:AAGDM825JY2C-lmogTwnXx-kTpQ7VR1tN48')
bot.message_loop(handle)
print('I am listening ...')

while 1:
    time.sleep(10)