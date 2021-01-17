from discord.ext import commands
import os
import traceback
import datetime

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)
    
client = discord.Client() 
 
@client.event 
async def on_voice_state_update(before, after): 
    if after.server.id == '653523307232231425': 
        nowtime = datetime.datetime.utcnow() 
        nowtime = nowtime + datetime.timedelta(hours=9) 
        nowtime = nowtime.strftime("%m/%d-%H:%M") 
        vcchannel = client.get_channel('653523307865309187') 
 
        if(before.voice_channel is None): 
            jointext=nowtime + "に　"+ after.name + "　が　"+ after.voice_channel.name + " に参加しました。" 
            await client.send_message(vcchannel, jointext) 
        elif(after.voice_channel is None): 
            outtext=nowtime + "に　"+ before.name + "　が　"+ before.voice_channel.name + " から退出しました。" 
            await client.send_message(vcchannel, outtext) 


@bot.command()
async def ping(ctx):
    await ctx.send('pong')
    
@bot.command()
async def neko(ctx):
    await ctx.send('nyan')
    
@bot.command()
async def a(ctx):
    await ctx.send('b')

bot.run(token)
