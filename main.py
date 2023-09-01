# Lx 0980

from pyrogram import Client, filters, enums
from time import sleep
from os import environ

app_id = int(environ.get('app_id'))
api_hash = environ.get('api_hash')
bot_token = environ.get('bot_token')
admin_id = int(environ.get('admin_id'))

counter = Client(    
    name='Time-Counter',
    api_id=app_id,
    api_hash=api_hash,#'751e7a1469a1099fb3748c5ca755e918',
    bot_token=bot_token #'6285956621:AAF16zJce7vXr3wukHJDO9qOYpXQ-AcSInU'
)

EDITING = {}
CANCEL = {}
 
@counter.on_message(filters.command('cancel') & filters.user(admin_id))
async def counts(bot, update):
    cancel = CANCEL.get('cnl')
    if cancel:
        CANCEL['cnl'] = True 
        update.reply('Timer Editing Successfully Stopped!')
    else:
          update.reply('No Timer Editing Found')  
    
    
@counter.on_message(filters.command('start_count') & filters.user(admin_id)) 
async def counts(bot, update):
    editing = EDITING.get('chek')
    if editing:
        return await update.reply('Time Counter Already Started!')
    EDITING['chek'] = True    
    message = await bot.get_messages(-1001300164856, 85)
   # print(message.text)
    import re
    pattern = r"Years:\s*(\d+)\s*Months:\s*(\d+)\s*Days:\s*(\d+)\s*Hours:\s*(\d+)\s*Minutes:\s*(\d+)"  
    matches = re.search(pattern, message.text) 
    if matches: 
        year = int(matches.group(1))
        month = int(matches.group(2))
        day = int(matches.group(3))
        hour = int(matches.group(4))
        minutes = int(matches.group(5))
        seconds = 0
        print(year, month, day, hour, minutes, seconds)
        CANCEL = False
        try:
          while True:
              if CANCEL.get('cnl'):
                  EDITING['chek'] = False
                  break
              sleep(0.01)
              seconds += 1
              if seconds == 60:
                minutes +=1
                seconds = 0
                print(minutes)
                if minutes == 60:
                    hour += 1
                    minutes = 0
                    if hour == 24:
                        day += 1
                        hour = 0
                        if day == 30:
                            month += 1
                            day = 0
                            if month == 12:
                                year += 1
                                month = 0    
                    text = f"Bot Text.\n\nYears: {year}\nMonths: {month}\nDays: {day}\nHours: {hour}\nMinutes : {minutes}"
                    await bot.edit_message_text(
                        chat_id = -1001300164856,
                        text = text,
                        message_id = 85,
                        parse_mode = enums.ParseMode.HTML
                    )
        except Exception as e:
            print(str(e))
            EDITING['chek'] = False          

print('Bot Started!')     
counter.run(
