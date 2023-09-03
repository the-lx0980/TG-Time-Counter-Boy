from pyrogram import Client, filters, enums
from os import environ
from calculate_time import get_data
import time

bot_token = environ.get('BOT_TOKEN')

counter = Client(    
    name='Time-Counter',
    api_id=24871620,
    api_hash='e4195bedc71234a179a3d9ac0cad6401',
    bot_token= bot_token
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
    global EDITING, CANCEL
    if EDITING:
        return await update.reply('Time Counter Already Started!')
    EDITING = True
    await update.reply('Time-Counter Started Successfully!')
    CANCEL = False
    try:
      while True:
        y, m, d, h, mi = get_data()
        if CANCEL:
            break
        try:
             text = f"<b>Since 3 September 2023</b>\n\n<b>Total Years:</b> {y}\n<b>Total Months:</b> {m}\n<b>Total Days:</b> {d}\n<b>Total Hours:</b> {h}\n<b>Total Minutes:</b> {mi}"
             await bot.edit_message_text(
                   chat_id = -1001951908326,
                   text = text,
                   message_id = 3,
                   parse_mode = enums.ParseMode.HTML
             )
             time.sleep(60)
        except Exception as e:
            print(str(e))
            await update.reply(str(e))
            EDITING = False
    except Exception as e:
            print(str(e))
            await update.reply(str(e))            
print('Bot Started!')     
counter.run()
