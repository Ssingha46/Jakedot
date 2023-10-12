import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "24277352")

API_HASH = os.environ.get("API_HASH", "1b33486233885ca817d28fa2599d6df1")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6008587175:AAFsKQUMGEyJW56ZsMuG-HDIbFv09-H_XhY") 

FORCE_SUB = os.environ.get("FORCE_SUB", "CrazyboyOfficial") 

DB_NAME = os.environ.get("DB_NAME","singhasourav46:3NNfi7twQVJDB2rV")     

DB_URL = os.environ.get("DB_URL","mongodb+srv://singhasourav46:3NNfi7twQVJDB2rV@cluster0.oechngq.mongodb.net/?retryWrites=true&w=majority")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://te.legra.ph/CrazyboyOfficial-07-23")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '').split()]

