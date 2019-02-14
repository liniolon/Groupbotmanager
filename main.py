# -------- Telepot --------------#
import telepot
from telepot.loop import MessageLoop
from telepot.namedtuple import ReplyKeyboardMarkup
# ---------- Other --------------#
from time import sleep
import markdown, logging
from bs4 import BeautifulSoup

TOKEN = '700990289:AAFdUv3DIc1BPE2bmSE_zXTR1W3H3VAwtPY'
bot = telepot.Bot(TOKEN)

#Logging
log_location = 'bot.log' #Loction of log file.
logging.basicConfig(filename=log_location ,format='%(asctime)s - %(name)s - %(message)s', level=logging.INFO)


help = markdown.markdown(open('./responses/help.md', encoding='utf8').read())
link = markdown.markdown(open('./responses/link.md', encoding='utf8').read())
rules = markdown.markdown(open('./responses/rules.md', encoding='utf8').read())
ask = markdown.markdown(open('./responses/answers/ask.md', encoding='utf8').read())
bitcoin = markdown.markdown(open('./responses/answers/bitcoin.md', encoding='utf8').read())
botinfo = markdown.markdown(open('./responses/answers/botinfo.md', encoding='utf8').read())
farsi = markdown.markdown(open('./responses/answers/farsi.md', encoding="utf8").read())
flood = markdown.markdown(open('./responses/answers/flood.md', encoding='utf8').read())
free = markdown.markdown(open('./responses/answers/free.md', encoding='utf8').read())
grub = markdown.markdown(open('./responses/answers/grub.md', encoding='utf8').read())
hacker = markdown.markdown(open('./responses/answers/hacker.md', encoding="utf8").read())
help_1 = markdown.markdown(open('./responses/answers/help.md', encoding='utf8').read())
kali = markdown.markdown(open('./responses/answers/kali.md', encoding="utf8").read())
lamp = markdown.markdown(open('./responses/answers/lamp.md', encoding='utf8').read())
link = markdown.markdown(open('./responses/answers/link.md', encoding='utf8').read())
mahak = markdown.markdown(open('./responses/answers/mahak.md', encoding='utf8').read())
searx = markdown.markdown(open('./responses/answers/searx.md', encoding='utf8').read())
smart = markdown.markdown(open('./responses/answers/smart.md', encoding='utf8').read())
tor = markdown.markdown(open('./responses/answers/tor.md', encoding='utf8').read())
xampp = markdown.markdown(open('./responses/answers/xampp.md', encoding="utf8").read())

def handle(msg):
      content_type = telepot.glance(msg)        
      if content_type[0] == 'text':
         cmd = msg['text']
         chat_id = msg['chat']['id']
         msg_id = msg['message_id']
         try:
            from_msg_id = msg['reply_to_message']['message_id']
         except:
            from_msg_id = None

         if cmd=='/start':
            bot.sendMessage(chat_id, "ربات مدیریت گروه\n\n\nلایسنس: AGPLv3")
         
         if cmd=='id':
            bot.sendMessage(chat_id, "شناسه‌ی تلگرامی شما {} است".format(chat_id))

         if cmd=='ping':
            bot.sendMessage(chat_id, "PING-PONG :D")

         if cmd=='help' and from_msg_id is None:
            bot.sendMessage(chat_id, "".join(BeautifulSoup(help).findAll(text=True)), reply_to_message_id=msg_id)

         if cmd=='help' and from_msg_id is not None:
            bot.sendMessage(chat_id, "".join(BeautifulSoup(help).findAll(text=True)), reply_to_message_id=from_msg_id)

         if cmd=='link' and from_msg_id is None:
            bot.sendMessage(chat_id, "".join(BeautifulSoup(link).findAll(text=True)), reply_to_message_id=msg_id)

         if cmd=='link' and from_msg_id is not None:
            bot.sendMessage(chat_id, "".join(BeautifulSoup(link).findAll(text=True)), reply_to_message_id=from_msg_id)
         
         if cmd=='rules' and from_msg_id is None:
            bot.sendMessage(chat_id, "".join(BeautifulSoup(rules).findAll(text=True)), reply_to_message_id=msg_id)

         if cmd=='rules' and from_msg_id is not None:
            bot.sendMessage(chat_id, "".join(BeautifulSoup(rules).findAll(text=True)), reply_to_message_id=from_msg_id)
         
         if cmd=='!ask' and from_msg_id is None:
            bot.sendMessage(chat_id, "".join(BeautifulSoup(ask).findAll(text=True)), reply_to_message_id=msg_id)

         if cmd=='!ask' and from_msg_id is not None:
            bot.sendMessage(chat_id, "".join(BeautifulSoup(ask).findAll(text=True)), reply_to_message_id=from_msg_id)
         
         if cmd=='!bitcoin' and from_msg_id is None:
            bot.sendMessage(chat_id, "".join(BeautifulSoup(bitcoin).findAll(text=True)), reply_to_message_id=msg_id)

         if cmd=='!bitcoin' and from_msg_id is not None:
            bot.sendMessage(chat_id, "".join(BeautifulSoup(bitcoin).findAll(text=True)), reply_to_message_id=from_msg_id)

         if cmd=='!botinfo' and from_msg_id is None:
            bot.sendMessage(chat_id, "".join(BeautifulSoup(botinfo).findAll(text=True)), reply_to_message_id=msg_id)

         if cmd=='!botinfo' and from_msg_id is not None:
            bot.sendMessage(chat_id, "".join(BeautifulSoup(botinfo).findAll(text=True)), reply_to_message_id=from_msg_id)

         if cmd=='!farsi' and from_msg_id is None:
            bot.sendMessage(chat_id, "".join(BeautifulSoup(farsi).findAll(text=True)), reply_to_message_id=msg_id)

         if cmd=='!farsi' and from_msg_id is not None:
            bot.sendMessage(chat_id, "".join(BeautifulSoup(farsi).findAll(text=True)), reply_to_message_id=from_msg_id)

         if cmd=='!flood' and from_msg_id is None:
            bot.sendMessage(chat_id, "".join(BeautifulSoup(flood).findAll(text=True)), reply_to_message_id=msg_id)

         if cmd=='!flood' and from_msg_id is not None:
            bot.sendMessage(chat_id, "".join(BeautifulSoup(flood).findAll(text=True)), reply_to_message_id=from_msg_id)
            
         if cmd=='!free' and from_msg_id is None:
            bot.sendMessage(chat_id, "".join(BeautifulSoup(free).findAll(text=True)), reply_to_message_id=msg_id)

         if cmd=='!free' and from_msg_id is not None:
            bot.sendMessage(chat_id, "".join(BeautifulSoup(free).findAll(text=True)), reply_to_message_id=from_msg_id)
            
         if cmd=='!grub' and from_msg_id is None:
            bot.sendMessage(chat_id, "".join(BeautifulSoup(grub).findAll(text=True)), reply_to_message_id=msg_id)

         if cmd=='!grub' and from_msg_id is not None:
            bot.sendMessage(chat_id, "".join(BeautifulSoup(grub).findAll(text=True)), reply_to_message_id=from_msg_id)
            
         if cmd=='!hacker' and from_msg_id is None:
            bot.sendMessage(chat_id, "".join(BeautifulSoup(hacker).findAll(text=True)), reply_to_message_id=msg_id)

         if cmd=='!hacker' and from_msg_id is not None:
            bot.sendMessage(chat_id, "".join(BeautifulSoup(hacker).findAll(text=True)), reply_to_message_id=from_msg_id)
            
         if cmd=='!help' and from_msg_id is None:
            bot.sendMessage(chat_id, "".join(BeautifulSoup(help_1).findAll(text=True)), reply_to_message_id=msg_id)

         if cmd=='!help' and from_msg_id is not None:
            bot.sendMessage(chat_id, "".join(BeautifulSoup(help_1).findAll(text=True)), reply_to_message_id=from_msg_id)
            
         if cmd=='!kali' and from_msg_id is None:
            bot.sendMessage(chat_id, "".join(BeautifulSoup(kali).findAll(text=True)), reply_to_message_id=msg_id)

         if cmd=='!kali' and from_msg_id is not None:
            bot.sendMessage(chat_id, "".join(BeautifulSoup(kali).findAll(text=True)), reply_to_message_id=from_msg_id)
            
         if cmd=='!lamp' and from_msg_id is None:
            bot.sendMessage(chat_id, "".join(BeautifulSoup(lamp).findAll(text=True)), reply_to_message_id=msg_id)

         if cmd=='!lamp' and from_msg_id is not None:
            bot.sendMessage(chat_id, "".join(BeautifulSoup(lamp).findAll(text=True)), reply_to_message_id=from_msg_id)
            
         if cmd=='!link' and from_msg_id is None:
            bot.sendMessage(chat_id, "".join(BeautifulSoup(link).findAll(text=True)), reply_to_message_id=msg_id)

         if cmd=='!link' and from_msg_id is not None:
            bot.sendMessage(chat_id, "".join(BeautifulSoup(link).findAll(text=True)), reply_to_message_id=from_msg_id)
            
         if cmd=='!mahak' and from_msg_id is None:
            bot.sendMessage(chat_id, "".join(BeautifulSoup(mahak).findAll(text=True)), reply_to_message_id=msg_id)

         if cmd=='!mahak' and from_msg_id is not None:
            bot.sendMessage(chat_id, "".join(BeautifulSoup(mahak).findAll(text=True)), reply_to_message_id=from_msg_id)
            
         if cmd=='!searx' and from_msg_id is None:
            bot.sendMessage(chat_id, "".join(BeautifulSoup(searx).findAll(text=True)), reply_to_message_id=msg_id)

         if cmd=='!searx' and from_msg_id is not None:
            bot.sendMessage(chat_id, "".join(BeautifulSoup(searx).findAll(text=True)), reply_to_message_id=from_msg_id)
            
         if cmd=='!smart' and from_msg_id is None:
            bot.sendMessage(chat_id, "".join(BeautifulSoup(smart).findAll(text=True)), reply_to_message_id=msg_id)

         if cmd=='!smart' and from_msg_id is not None:
            bot.sendMessage(chat_id, "".join(BeautifulSoup(smart).findAll(text=True)), reply_to_message_id=from_msg_id)
         
         if cmd=='!tor' and from_msg_id is None:
            bot.sendMessage(chat_id, "".join(BeautifulSoup(tor).findAll(text=True)), reply_to_message_id=msg_id)

         if cmd=='!tor' and from_msg_id is not None:
            bot.sendMessage(chat_id, "".join(BeautifulSoup(tor).findAll(text=True)), reply_to_message_id=from_msg_id)
         
         if cmd=='!xampp' and from_msg_id is None:
            bot.sendMessage(chat_id, "".join(BeautifulSoup(xampp).findAll(text=True)), reply_to_message_id=msg_id)

         if cmd=='!xampp' and from_msg_id is not None:
            bot.sendMessage(chat_id, "".join(BeautifulSoup(xampp).findAll(text=True)), reply_to_message_id=from_msg_id)

         if cmd.startswith("کسی") and cmd.endswith("کرده؟") or cmd.endswith('کرده است؟') or cmd.endswith('بلده؟'):
            bot.sendMessage(chat_id, "".join(BeautifulSoup(ask).findAll(text=True)), reply_to_message_id=msg_id)

         if cmd=='!report' and from_msg_id is not None:
            bot.forwardMessage("451182363", chat_id,from_msg_id)
            bot.deleteMessage((chat_id, msg_id))



print("Bot working ... ")
MessageLoop(bot, handle).run_as_thread()
while True:
    sleep(10)
