from os import environ

# Telegram Account Api Id And Api Hash
API_ID = int(environ.get("API_ID", "17461958"))
API_HASH = environ.get("API_HASH", "0f083cb4779252f82b99f5c644274624")

# Your Main Bot Token 
BOT_TOKEN = environ.get("BOT_TOKEN", "7826334394:AAEoq0uOycdMJ4-R41icJIfq0tLXRgnYNJw")

# Owner ID For Broadcasting 
OWNER_ID = int(environ.get("OWNER_ID", "2081516065")) # Owner Id or Admin Id

# Give Your Force Subscribe Channel Id Below And Make Bot Admin With Full Right.
F_SUB = environ.get("F_SUB", "")

# Mongodb Database Uri For User Data Store 
MONGO_DB_URI = environ.get("mongodb+srv://gdrivekhaan:nQ3frHRgKCABYoQD@cluster0.ce9hr.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

# Port To Run Web Application 
PORT = int(environ.get('PORT', 8080))
