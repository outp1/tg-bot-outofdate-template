from environs import Env

# Теперь используем вместо библиотеки python-dotenv библиотеку environs
env = Env()
env.read_env()

BOT_NAME = env.str("BOT_NAME")
BOT_TOKEN = env.str("BOT_TOKEN")  # Забираем значение типа str
ADMINS = env.list("ADMINS")  # Тут у нас будет список из админов
LOGS_BOT_TOKEN = env.str("LOGS_TOKEN")
LOGS_DIR = env.str("FOLDER_LOGS")

POSTGRES_AUTH = {
    'user': env.str("POSTGRES_USER"),
    'password': env.str("POSTGRES_PASSWORD"),
    'host': env.str("POSTGRES_HOST"),
    'port': env.str("POSTGRES_PORT"),
    'database': env.str("POSTGRES_DB")
    }

# Other constants
IN_CLOSE_TEXT = 'Закрыть'
