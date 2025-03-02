from os import environ

# Telegram Account Api Id And Api Hash
API_ID = int(environ.get("API_ID", "20790743"))
API_HASH = environ.get("API_HASH", "266b46661c0eb26ee0cb9ef7dfebfe39")

# Your Main Bot Token 
BOT_TOKEN = environ.get("BOT_TOKEN", "")

# Owner ID For Broadcasting 
OWNER_ID = int(environ.get("OWNER_ID", "6474527080")) # Owner Id or Admin Id

# Give Your Force Subscribe Channel Id Below And Make Bot Admin With Full Right.
F_SUB = environ.get("F_SUB", "")

# Mongodb Database Uri For User Data Store 
MONGO_DB_URI = environ.get("MONGO_DB_URI", "mongodb+srv://kranpantmain:ueaWKwac1qJsKCpq@cluster0.pqump.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

# Port To Run Web Application 
PORT = int(environ.get('PORT', 8080))
