import discord
from discord.ext import commands, tasks
import asyncio
import datetime


#clear коипндп
@client.command(pass_context = True)
@commands.has_permissions( administrator = True )
@commands.cooldown(1, 10, commands.BucketType.user)

async def clear(ctx, amount : int):
    await ctx.channel.purge( limit = amount )


    await ctx.send(embed = discord.Embed(description = f'** <a:Check_Mark:926486428387516488> Очищено **{amount}** сообщение**', color = 11027200, timestamp = ctx.message.created_at)) 

    await asyncio.sleep(5)
    await ctx.channel.purge( limit = 1)





#Обработка ошибки
@clear.error
@commands.cooldown(1, 10, commands.BucketType.user) # кол-во время через которые можно снова написать данную команду и она будет работать 
async def clear_error(ctx, error):

    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(embed = discord.Embed(title = f"Ошибка!", description = f" {ctx.author.name}, укажите аргумент!", color = ERROR ))
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(embed = discord.Embed(title = f"❌ в доступе отказано!", description = f"{ctx.author.name}, у вас нету нужных прав!" , color = ERROR))
        await asyncio.sleep(5) 
        await ctx.channel.purge( limit = 1)
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send(embed = discord.Embed(title = f"Ошибка!", description = f"{ctx.author.name}, Погоди, время чтобы вновь использовать эту команду ещё не прошло {error.retry_after:.2f}s." , color = ERROR))
        await asyncio.sleep(15)
        await ctx.channel.purge( limit = 1 )



"""BY EN0T1K421"""