import re
from os import environ

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Bot information
SESSION = environ.get('SESSION', 'Media_search')
API_ID = 6351429
API_HASH = '912c2bcd930fb7dd5bac711b8c4d4895'
BOT_TOKEN = '5514962644:AAGLLbdUDDpHbUfdhnZEoBb8oVNEGOzy9sw'

# Bot settings
CACHE_TIME = 300
USE_CAPTION_FILTER = False
PICS = (environ.get('PICS', 'https://telegra.ph/file/b558eeb0c8c9ca0f59b57.jpg https://telegra.ph/file/4ea7a4777d6a08c7d7780.jpg https://telegra.ph/file/4788bc89f40705010f2ef.jpg https://telegra.ph/file/6244dc9cd682581d3ac8f.jpg https://telegra.ph/file/0eee2657101f76f36d45c.jpg ')).split()

# Admins, Channels & Users
ADMINS = 1584694165, 5216689081
CHANNELS = -1001689360667, -1001541175468, -1001265602872
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_grp = environ.get('AUTH_GROUP')
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None

# MongoDB information
DATABASE_URI = "mongodb+srv://jerry:bot@cluster0.qof3hys.mongodb.net/?retryWrites=true&w=majority"
DATABASE_NAME = "Cluster0"
COLLECTION_NAME = 'Telegram_files'

# FSUB
auth_channel = environ.get('AUTH_CHANNEL')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
# Set to False inside the bracket if you don't want to use Request Channel else set it to Channel ID
REQ_CHANNEL = -1001871529268
JOIN_REQS_DB = "mongodb+srv://join:filter@cluster0.ltifpcp.mongodb.net/?retryWrites=true&w=majority"

# Others
LOG_CHANNEL = 0
SUPPORT_CHAT = 'TeamEvamaria'
P_TTI_SHOW_OFF = True
IMDB = True
SINGLE_BUTTON = True
CUSTOM_FILE_CAPTION = """**{file_name}**({file_size}) 
▬▬▬▬▬▬▬▬▬▬▬▬▬▬
താഴെയുള്ള ലിങ്കിൽ ക്ലിക്ക് ചെയ്ത് ഗ്രൂപ്പിൽ ജോയിൻ ആയ ശേഷം സിനിമ ഡൌൺലോഡ് ചെയ്യുക. അല്ലെങ്കിൽ ഫയൽ വർക്ക്‌ ആവില്ല 😪
🚦Group 1👉  [📽 ᴄɪɴᴇᴍᴀ ᴄᴏᴍᴘᴀɴʏ 📽](https://t.me/CinemaCompany_Group) 
🚦Group 2👉 [🟢ᴄɪɴᴇᴍᴀ ᴛᴀʟᴋɪᴇꜱ 🟢](https://t.me/Cinema_Talkies_Group)
🚦Group 3👉 [⭕️ᴍᴀʟʟᴜ ᴛᴀʟᴋɪᴇꜱ⭕️](https://t.me/MalluTalkies_Group)
🚦Group 4👉 [🔅ᴍᴏᴠɪᴇ ʜᴜʙ🔅](https://t.me/MovieHub_Group)"""
BATCH_FILE_CAPTION = CUSTOM_FILE_CAPTION
IMDB_TEMPLATE = "<b>Query: {query}</b> \n‌‌‌‌IMDb Data:\n\n🏷 Title: <a href={url}>{title}</a>\n🎭 Genres: {genres}\n📆 Year: <a href={url}/releaseinfo>{year}</a>\n🌟 Rating: <a href={url}/ratings>{rating}</a> / 10"
LONG_IMDB_DESCRIPTION = False
SPELL_CHECK_REPLY = True
MAX_LIST_ELM = None
INDEX_REQ_CHANNEL = LOG_CHANNEL
FILE_STORE_CHANNEL = [int(ch) for ch in ('FILE_STORE_CHANNEL', '').split()]
MELCOW_NEW_USERS = True
PROTECT_CONTENT = False
PUBLIC_FILE_STORE = True

LOG_STR = "Current Cusomized Configurations are:-\n"
LOG_STR += ("IMDB Results are enabled, Bot will be showing imdb details for you queries.\n" if IMDB else "IMBD Results are disabled.\n")
LOG_STR += ("P_TTI_SHOW_OFF found , Users will be redirected to send /start to Bot PM instead of sending file file directly\n" if P_TTI_SHOW_OFF else "P_TTI_SHOW_OFF is disabled files will be send in PM, instead of sending start.\n")
LOG_STR += ("SINGLE_BUTTON is Found, filename and files size will be shown in a single button instead of two separate buttons\n" if SINGLE_BUTTON else "SINGLE_BUTTON is disabled , filename and file_sixe will be shown as different buttons\n")
LOG_STR += (f"CUSTOM_FILE_CAPTION enabled with value {CUSTOM_FILE_CAPTION}, your files will be send along with this customized caption.\n" if CUSTOM_FILE_CAPTION else "No CUSTOM_FILE_CAPTION Found, Default captions of file will be used.\n")
LOG_STR += ("Long IMDB storyline enabled." if LONG_IMDB_DESCRIPTION else "LONG_IMDB_DESCRIPTION is disabled , Plot will be shorter.\n")
LOG_STR += ("Spell Check Mode Is Enabled, bot will be suggesting related movies if movie not found\n" if SPELL_CHECK_REPLY else "SPELL_CHECK_REPLY Mode disabled\n")
LOG_STR += (f"MAX_LIST_ELM Found, long list will be shortened to first {MAX_LIST_ELM} elements\n" if MAX_LIST_ELM else "Full List of casts and crew will be shown in imdb template, restrict them by adding a value to MAX_LIST_ELM\n")
LOG_STR += f"Your current IMDB template is {IMDB_TEMPLATE}"
