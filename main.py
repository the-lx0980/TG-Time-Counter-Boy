from pyrogram import Client, filters, enums
from time import sleep
from os import environ

bot_token = environ.get('BOT_TOKEN')

counter = Client(    
    name='Time-Counter',
    api_id=6353248,
    api_hash='1346f958b9d917f0961f3e935329eeee',
    bot_token=bot_token
)

EDITING = False
CANCEL = False 
admin_id = 5326801541

@counter.on_message(filters.command('start'))
async def counts(bot, update):
    await update.reply('Bot is Running!')

@counter.on_message(filters.command('cancel') & filters.user(admin_id))
async def counts(bot, update):
    global CANCEL, EDITING
    if EDITING:
        CANCEL = True
        EDITING = False
        await update.reply('Timer Editing Successfully Stopped!')
    else:
        await update.reply('No Timer Editing Found')  
    
@counter.on_message(filters.command('start_count') & filters.user(admin_id)) 
async def counts(bot, update):
    global EDITING
    if EDITING:
        return await update.reply('Time Counter Already Started!')
    EDITING = True 
    await update.reply('Time-Counter Started Successfully!')
    message = await bot.get_messages(-1001593055888, 732)
    import re
    pattern = r"(\w+)\s*:\s*(\d+)"
    matches = re.findall(pattern, message.text)
    if matches:
        time_units = {}
        for unit, value in matches:
            unit = unit.rstrip('s')
            time_units[unit] = int(value)
        year = time_units.get("Year", 0)
        month = time_units.get("Month", 0)
        day = time_units.get("Day", 0)
        hour = time_units.get("Hour", 0)
        minute = time_units.get("Minute", 0)
        seconds = 0
        global CANCEL  
        CANCEL = False
        try:
            while True:
                if CANCEL:
                    print('Time Counter Successfully Stopped!')
                    break
                sleep(0.01)
                seconds += 1
                if seconds == 60:
                    minute += 1
                    seconds = 0
                    print(minute)
                    if minute == 60:
                        hour += 1
                        minute = 0
                        if hour == 24:
                            day += 1
                            hour = 0
                            if day == 30:
                                month += 1
                                day = 0
                                if month == 12:
                                    year += 1
                                    month = 0
                        if year > 1:
                          Year = 'Years'
                        else:
                          Year = 'Year'
                        if month > 1:
                          Month = 'Months'
                        else:
                          Month = 'Month'
                        if day > 1:
                          Day = 'Days'
                        else:
                          Day = 'Day'
                        if hour > 1:
                          Hour = 'Hours'
                        else:
                          Hour = 'Hour'
                        text = f"<b>DFF UPDATES</b>\n\n{Year}: {year}\n{Month}: {month}\n{Day}: {day}\n{Hour}: {hour}\n"
                        await bot.edit_message_text(
                            chat_id = -1001593055888,
                            text = text,
                            message_id = 732,
                            parse_mode = enums.ParseMode.HTML
                        )
        except Exception as e:
            print(str(e))
            EDITING = False          

print('Bot Started!')     
counter.run()
