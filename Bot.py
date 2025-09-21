importazione OS
         telegramma.         ext...ext! ext...exc!ext...ext...

TokenTokenToTokenTokenTo KenToken = os.getenv("bot_token")  # prende il token dalle Config Varsgetenv("bot_token")  # prende il token dalle Config Vars

Def. Inizia(Aggiornamento, contesto):Inizia(Aggiornamento, contesto):
   aggiornamento.  Messaggio.Rispondi_testo("Ciao! Il bot è attivo su Heroku 🚀")Messaggio.Reply_text("Ciao! Il bot è attivo su Heroku 🚀")

Aggiornatore =  Aggiornamento(Token)Aggiornamento(Token)
aggiornamento.spedizioniere..Add_handler(CommandHandler("start", iniziare))spedizioniere..Add_handler(CommandHandler("start", iniziare))

aggiornamento.Start_polling()Start_polling()
aggiornamento.inattivo..()inattivo..()
