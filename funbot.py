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

    
    command == "command"
    Branch = command.split(' ')[0]
    print(Branch)
    command == "command"
    roll = command.split(' ')[-1]
    print(roll)
    link = "https://iare-data.s3.ap-south-1.amazonaws.com/uploads/"+Branch+"/"+roll+".jpg"
    print(link)
    bot.sendPhoto(chat_id,link)
    bot.sendMessage(chat_id,'ok next')
    context.bot.sendPhoto(chat_id=chat_id, photo="https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3D28Vlykt6ofo&psig=AOvVaw2eXCatRdLFjYLf3cuSHGhx&ust=1601557740022000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCMiY1Nr5kOwCFQAAAAAdAAAAABAP", caption="This is the test photo caption")



bot = telepot.Bot('914559098:AAGDM825JY2C-lmogTwnXx-kTpQ7VR1tN48')
bot.message_loop(handle)
print('I am listening ...')

while 1:
    time.sleep(10)
