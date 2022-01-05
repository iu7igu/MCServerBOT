import tail
import telebot
import time


utenti={}

bottoken=''
chat_id=''


bot = telebot.TeleBot(bottoken)

def send(x,y):
	if y == 'esce':
		bot.send_message(chat_id, x + ' è uscito dal server')
	elif y == 'entra':
		bot.send_message(chat_id, x + ' è entrato nel server')


def riga(x):
	#print(x)
	dati = x.split(' ')
	if dati[4] == 'left':
		print('E uscito '+dati[3])
		send(dati[3],'esce')
		
	elif dati[4] == 'joined':
		#print('E entrato '+dati[3])
		if not dati[3] in utenti or utenti[dati[3]] == 0:
			utenti[dati[3]]=3
			send(dati[3],'entra')
		else:
			utenti[dati[3]]=int(utenti[dati[3]]-1)
			print(utenti[dati[3]])

		


tailog = tail.Tail('/opt/mine/Server/logs/latest.log')

tailog.register_callback(riga)

tailog.follow(s=1)
