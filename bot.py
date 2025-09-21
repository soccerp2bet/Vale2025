importazione OS
    telegramma.  ext... ext.. 

Tokentoken = os.getenv("bot_token")  # prende il token dalle Config Vars

Def. Inizia(Aggiornamento, contesto):
 aggiornamento. Messaggio.Reply_text("Ciao! Il bot è attivo su Heroku 🚀")

Aggiornatore = Aggiornamento(Token)
aggiornamento.spedizioniere..Add_handler(CommandHandler("start", iniziare))

aggiornamento.Start_polling()
aggiornamento.inattivo..()
