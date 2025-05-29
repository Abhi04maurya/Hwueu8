import os

API_ID = API_ID = 3670291

API_HASH = os.environ.get("API_HASH", "1f55b2e9d972c3a5ac3f008c51ed7a4a")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7837388926:AAEX3vLaOIbrtf8tmWAGH58XqKtI1uF3OPw")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 659925627))

LOG = -1002070057679

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "5987970971").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


