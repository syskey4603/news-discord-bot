import requests
import discord
from discord.ext import commands
import time

data = requests.get('https://newsapi.org/v2/everything?q=Apple&from=2022-02-28&sortBy=popularity&apiKey=d2f3b7aa2fbc46f8bcf07e08f5066462').json()
bot = commands.Bot(command_prefix='$')
bot.remove_command("help")
@bot.command()
async def help(ctx):
    embed = discord.Embed(title="Help", description="test" , color=0x00ff00)
    embed.add_field(name="$help", value="Displays this message", inline=False)
    embed.add_field(name="$news all", value="Displays all the latest news", inline=False)
    embed.add_field(name="$news <topic>", value="Displays the latest news about the topic entered", inline=False)
    await ctx.send(embed=embed)

@bot.command()
async def news(ctx, arg):
    if ctx.message.author.name == bot.user:
        return
    
    for article in data['articles']:
        if arg in article['title'] or arg in article['description'] or arg in article['url']:
            embed=discord.Embed(title=article['title'], url=article['url'], description=article['description'], color=0xFF5733)
            await ctx.send(embed=embed)
        if arg == 'all':
            embed=discord.Embed(title=article['title'], url=article['url'], description=article['description'], color=0xFF5733)
            await ctx.send(embed=embed)
            
bot.run("OTQ4MDU3OTQ5ODIwMDM5MTc4.Yh2RxQ.RJ2G7kVKFrScltof_VwV2MJ2ixk", bot=True)
