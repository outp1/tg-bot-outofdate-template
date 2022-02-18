from environs import Env

# Теперь используем вместо библиотеки python-dotenv библиотеку environs
env = Env()
env.read_env()

<<<<<<< HEAD
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

=======
BOTNICK = env.str("BOTNICK")
BOT_TOKEN = env.str("BOT_TOKEN")  # Забираем значение типа str
ADMINS = env.list("ADMINS")  # Тут у нас будет список из админов
LOGS_BOT_TOKEN = env.str("LOGS_BOT_TOKEN")

POSTGRES_AUTH = {
    'user': env.str("PSQL_USER"),
    'password': env.str("PSQL_PASS"),
    'host': env.str("PSQL_IP"),
    'port': env.str("PSQL_PORT"),
    'database': env.str("PSQL_DB")
    }
>>>>>>> f15fcd1... 'm'
