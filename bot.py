import os
from  telegram.ext  import  Updater, CommandHandler

# Prende il token dalle Config Vars di Heroku
TOKEN = os.getenv("bot_token")

# Funzione che risponde al comando /start
def start(update, context):
    update.message.reply_text("Ciao! Il bot è attivo su Heroku 🚀")

# Crea l'updater e dispatcher
updater = Updater(TOKEN, use_context=True)
dispatcher = updater.dispatcher

# Aggiunge il comando /start
dispatcher.add_handler(CommandHandler("start", start))

# Avvia il bot
updater.start_polling()
updater.idle()
