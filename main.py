import discord, os, random

client = discord.Client()

@client.event
async def on_message(msg):
	se = os.sep
	cwd = os.getcwd() + se
	dir = cwd + 'archive' + se
	photos = os.listdir(dir)

	msg.content = msg.content.lower()
	if msg.author == client.user:
		return

	if msg.content.startswith('-капибара') or msg.content.startswith('-capybara') or msg.content.startswith('-waßerschwein') or msg.content.startswith('-wasserschwein') or msg.content.startswith('-カピバラ'):
		try:
			await msg.channel.send(file=discord.File(dir + random.choice(photos)))
		except Exception as e:
			print(e)
			await mgs.channel.send('🗿')

	elif msg.content.startswith('-help'):
		await msg.channel.send('Send "-capybara" and I will answer!\n langs also available: RU, JA, DE')

	elif msg.content.startswith('-помощь'):
		await msg.channel.send('Отправь "-капибара" и я отвечу!\n др. доступные языки: EN, JA, DE')

	elif msg.content.startswith('-hilfe'):
		await msg.channel.send('Sende "-wasserschwein" und ich werde antworten!\n andere verfügbare Sprachen: EN, JA, RU')

	elif msg.content.startswith('-助けて'):
		await msg.channel.send('"-カピバラ"と書くと、私は答えます!\n その他の利用可能な言語: EN, JA, RU')


if __name__ == '__main__':
	client.run(os.getenv("TOKEN"))
