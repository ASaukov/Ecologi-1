import discord 
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='?', intents=intents)

description='Я бот который на стороне экологии!!!'

@bot.command('ekologi')
async def ekologi(ctx):
    await ctx.send('Мусор обезательно требуется сортировать потому что большая часть мусора попадает на свалки, а тогда они загрезняют природу. Чтобы спасти экологию на планете начали делать в странах сортировку мусора.Обычный мусор в роле еды попадает на перерабодку, а пластик может полноценно пойти на заводы создания одежды. Сортировка сегодня играет важную роль как в производстве так и в экологии. Конечно заводы тоже по своему загризняют природу и окружение но этому уже научились припятствовать. В сортировке мусора есть несколько цветов базовых контейнеров: желтый-пластик, синий – макулатура, красный – стекло, зеленый – несортированные коммунальные отходы, оранжевый – опасные отходы')