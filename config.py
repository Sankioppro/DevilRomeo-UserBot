from os import getenv

API_ID = int(getenv("API_ID", "13335263"))
API_HASH = getenv("API_HASH", "")
BOT_TOKEN = getenv("BOT_TOKEN", "")
OWNER_ID = int(getenv("OWNER_ID", ""))
STRING_SESSION = getenv("STRING_SESSION", "")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5392070730").split()))
ALIVE_PIC = getenv("ALIVE_PIC", "https://graph.org/file/566e14bdc293357bcde17.jpg")
REPO_URL = getenv("REPO_URL", "https://github.com/Sankioppro/DevilRomeo-UserBot")
BRANCH = getenv("BRANCH", "main")
