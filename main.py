# -------- Telepot --------------#
import telepot
from telepot.loop import MessageLoop
from telepot.namedtuple import ReplyKeyboardMarkup
# ---------- Other --------------#
from time import sleep

TOKEN = '700990289:AAFdUv3DIc1BPE2bmSE_zXTR1W3H3VAwtPY'
bot = telepot.Bot(TOKEN)

def handle(msg):
    content_type = telepot.glance(msg)        
    if content_type[0] == 'text':

        try:
            cmd = msg['text']
            chat_id = msg['chat']['id']
            msg_id = msg['message_id']
            from_chat_id = msg['reply_to_message']['message_id']

            print(msg)
        except:
            pass

        if cmd=='/start':
            bot.sendMessage(chat_id, "ربات مدیریت گروه\n\n\nلایسنس: AGPLv3")
        
        if cmd=='id':
            bot.sendMessage(chat_id, "آی‌دی تلگرام شما: {}".format(chat_id))

        if cmd=='ping':
            bot.sendMessage(chat_id, "pong")

        if cmd=='join':
            bot.sendMessage(chat_id, "گروه کاربران ایرانی اوبونتو بدلیل تمرکز بیشتر بر روی انجمن و ویکی اوبونتو بسته شد. در صورتی که تصمیم به باز کردن دوبارهٔ گروه بگیریم، این موضوع را توسط انجمن با شما به اشتراک خواهیم گذاشت 🙂")

        if cmd=='rules':
            bot.sendMessage(chat_id, "* لطفا توجه فرمایید که قوانین انجمن فارسی اوبونتو در این گروه نیز صادق می‌باشند.\n* زبان رسمی گروه فارسی می‌باشد. لطفا تنها با حروف فارسی بنویسید.\n* فرستادن لینک دعوت به گروه‌ها یا کانال‌های دیگر تلگرام در گروه، مستقیما موجب حذف شما از گروه خواهد شد.\n* لطفا متون طولانی را در سایت‌هایی مانند paste.ubuntu.ir قرار داده و تنها لینک آن‌ها را در گروه قرار دهید.\n\n* قوانین انجمن: https://ubuntu.ir/rules")
        
        if cmd=='link':
            bot.sendMessage(chat_id, "https://ubuntu.ir/telegram")

        if cmd=='!free':
            bot.sendMessage(chat_id, "https://wiki.ubuntu.ir/wiki/Free\_software", reply_to_message_id=from_chat_id)

        if cmd=='!kali':
            bot.sendMessage(chat_id, "لطفا از یک توزیع معقول مثل اوبونتو (ubuntu) استفاده کنید", reply_to_message_id=msg_id)

        if cmd=='!flood':
            bot.sendMessage(chat_id, "لطفا از پخش کردن مطلب خود در چندین پست خودداری کرده و مطلب خود را مستقیما در یک پست بنویسید :)", reply_to_message_id=from_chat_id)

        if cmd=='!mahak':
            bot.sendMessage(chat_id, "https://mahak-charity.org/main/index.php/fa/about-mahak/payments", reply_to_message_id=msg_id)

        if cmd=='!report':
            bot.forwardMessage("451182363",chat_id, from_chat_id)
            bot.deleteMessage(msg_id)

        if cmd=='!ask':
            bot.sendMessage(chat_id, "لطفا بجای اینکه بپرسید که بعد سوال اصلی خود را بپرسید، مستقیما سوال اصلی خود را بپرسید :)", reply_to_message_id=from_chat_id)

        if cmd=='!source':
            bot.sendMessage(chat_id, "https://github.com/liniolon/Groupbotmanager", reply_to_message_id=from_chat_id)







print("Bot working ... ")
MessageLoop(bot, handle).run_as_thread()
while True:
    sleep(10)
