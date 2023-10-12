import logging
import logging.config
from pyrogram import Client 
from config import API_ID, API_HASH, BOT_TOKEN, FORCE_SUB

logging.config.fileConfig('logging.conf')
logging.getLogger().setLevel(logging.INFO)
logging.getLogger("pyrogram").setLevel(logging.ERROR)


class Bot(Client):

    def __init__(self):
        super().__init__(
            name="renamer",
            API_ID = os.environ.get("API_ID", "24277352")
            API_HASH = os.environ.get("API_HASH", "1b33486233885ca817d28fa2599d6df1")
           BOT_TOKEN = os.environ.get("BOT_TOKEN", "6008587175:AAFsKQUMGEyJW56ZsMuG-HDIbFv09-H_XhY") 
            workers=50,
            plugins={"root": "plugins"},
            sleep_threshold=5,
        )

    async def start(self):
       await super().start()
       me = await self.get_me()
       self.mention = me.mention
       self.username = me.username 
       self.force_channel = FORCE_SUB
       if FORCE_SUB:
         try:
            link = await self.export_chat_invite_link(FORCE_SUB)                  
            self.invitelink = link
         except Exception as e:
            logging.warning(e)
            logging.warning("Make Sure Bot admin in force sub channel")             
            self.force_channel = None      
       logging.info(f"{me.first_name} 𝚂𝚃𝙰𝚁𝚃𝙴𝙳 ⚡️⚡️⚡️")
      

    async def stop(self, *args):
      await super().stop()      
      logging.info("Bot Stopped")
        
bot = Bot()
bot.run()
