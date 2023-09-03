from pyrogram import Client, filters, enums, __version__
from os import environ
from calculate_time import get_data
import time
from pyrogram.raw.all import layer

bot_token = environ.get('BOT_TOKEN')

EDITING = False
admin_id = 5326801541

class counter(Client):

    def __init__(self):
        super().__init__(
            name='Time-Counter',
            api_id=24871620,
            api_hash='e4195bedc71234a179a3d9ac0cad6401',
            bot_token= bot_token
        )   

    async def start(self):
        await super().start()
        me = await self.get_me()
        self.username = '@' + me.username
        print(f"{me.first_name} with for Pyrogram v{__version__} (Layer {layer}) started on {me.username}.")
        global EDITING
        if EDITING:
            return await self.send_message(admin_id, 'Time Counter Already Started!')
        EDITING = True
        await self.send_message(admin_id, 'Time-Counter Started Successfully!')
        try:
          while True:
            y, m, d, h, mi = get_data()
            try:
                 text = f"<b>Since 3 September 2023</b>\n\n<b>Total Years:</b> {y}\n<b>Total Months:</b> {m}\n<b>Total Days:</b> {d}\n<b>Total Hours:</b> {h}\n<b>Total Minutes:</b> {mi}"
                 await self.edit_message_text(
                      chat_id = -1001951908326,
                      text = text,
                      message_id = 3,
                      parse_mode = enums.ParseMode.HTML
                 )
                 time.sleep(21600)
            except Exception as e:
                print(str(e))
                await update.reply(str(e))
                EDITING = False
        except Exception as e:
                print(str(e))
                await self.send_message(admin_id, str(e))  
                EDITING = False          

    async def stop(self, *args):
        await super().stop()
        print("Bot stopped. Bye.")
        
app = counter()
app.run()
