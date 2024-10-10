import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

recomend = [
    "Usa transporte sostenible: caminar, andar en bicicleta o utilizar el transporte público. Opta por vehículos eléctricos o comparte viajes.",
    "Ahorra energía en casa: desconecta aparatos cuando no los uses, usa bombillas LED y electrodomésticos eficientes. Considera instalar paneles solares.",
    "Reduce el consumo de carne: prioriza una dieta basada en plantas o reduce el consumo de carne, especialmente de res.",
    "Compra productos locales y de temporada: evita las emisiones por transporte y fomenta la agricultura sostenible.",
    "Minimiza el desperdicio de alimentos: planifica tus comidas, almacena adecuadamente los alimentos y compostaje los residuos orgánicos.",
    "Reduce, reutiliza y recicla: compra menos productos nuevos, reutiliza lo que tienes y recicla adecuadamente.",
    "Consume menos agua caliente: usa menos agua caliente al lavar platos, ropa o al ducharte e instala cabezales de ducha de bajo consumo.",
    "Elige energías renovables: cambia a proveedores de energía renovable o invierte en energía solar, eólica o hidroeléctrica.",
    "Modera el uso de plástico: opta por productos biodegradables o reutilizables y evita los plásticos de un solo uso.",
    "Planta árboles o participa en programas de reforestación: los árboles ayudan a absorber CO₂ y mitigar el cambio climático."
]

informacion = [
    "https://www.un.org/es/un75/climate-crisis-race-we-can-win", 
    "https://www.un.org/es/climatechange/science/causes-effects-climate-change",
    "https://www.youtube.com/watch?v=CIrNSNnbvJU",
    "https://www.youtube.com/watch?v=_PguOSdRcOg",
    "https://www.youtube.com/watch?v=GxWohx1_VOw",
    "https://www.youtube.com/watch?v=JQHtjT-_c7U",
    "https://www.acciona.com/es/cambio-climatico/"
]


@bot.event
async def on_ready():
    canal = bot.get_channel(1219012722507649188)  
    if canal:
        await canal.send(f'Hola, soy {bot.user}, tu asistente para reducir tu huella de carbono. ¡Cada pequeña acción cuenta para construir un futuro más verde! 🌍')
    print(f'{bot.user} está listo y conectado.')


@bot.command()
async def recomendaciones(ctx):
    await ctx.send(random.choice(recomend))

@bot.command()
async def calculadora(ctx):
    await ctx.send(f"Sabes cuantos kWh consumes en el mes? (en kWh) Si o No")
    
    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel
    
    mensaje = await bot.wait_for("message", check=check)

    if mensaje.content.lower() == "si":
        await ctx.send("Cuantos kWh consumes a la semana?")
        energia = await bot.wait_for("message", check=check)
        energia_num = energia.content
        energia_num = float(energia_num)
        
        await ctx.send("Cuantos km andas en moto por semana?")
        moto = await bot.wait_for("message", check=check)
        moto_num = moto.content
        moto_num = float(moto_num)
        
        await ctx.send("Cuantos km a la semana usas el transporte público? Si no lo sueles usar pon 0")
        transporte = await bot.wait_for("message", check=check)
        transporte_num = transporte.content
        transporte_num = float(transporte_num)

        await ctx.send("Sueles consumir productos importados(escribe 1) o locales(escribe 2)?")
        products = await bot.wait_for("message", check=check)
        products_num = products.content
        products_num = float(products_num)

        if products.content.lower() == "1":
            resultado = products_num * 0,21
        elif products.content.lower() == "2":
            resultado = products_num * 0.005

        def puntuacion(consumo):
            if consumo <= 10:
                return 1
            elif consumo <= 25:
                return 2
            elif consumo <= 50:
                return 3
            elif consumo <= 75:
                return 4
            elif consumo <= 100:
                return 5
            elif consumo <= 125:
                return 6
            elif consumo <= 150:
                return 7
            elif consumo <= 175:
                return 8
            elif consumo <= 200:
                return 9 
            elif consumo > 200:
                return 10
            
        consumo = 0.233 * energia_num + (moto_num * 0.096) + (transporte_num * 0.105) + resultado
        puntuacion_final = puntuacion(consumo)
        await ctx.send(f"El resultado de emisiones semanales basadas en tu cosumo son: {consumo:.2f} kg de CO₂. Tu puntuacion final es de {puntuacion_final}") 

    else:
        await ctx.send("Esta pagina te ayudara a saberlo: http://127.0.0.1:5000/")

@bot.command()
async def dieta(ctx):
    await ctx.send("¿Qué tipo de dieta sigues? (Omnívora, Vegetariana, Vegana)")
    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel
    
    respuesta = await bot.wait_for("message", check=check)
    dieta = respuesta.content.lower()

    if dieta == "omnivora":
        emisiones_dieta = 2.5  
    elif dieta == "vegetariana":
        emisiones_dieta = 1.7  
    elif dieta == "vegana":
        emisiones_dieta = 1.5  
    else:
        await ctx.send("Por favor, elige entre Omnívora, Vegetariana o Vegana.")
        return

    await ctx.send(f"Las emisiones estimadas por tu dieta son {emisiones_dieta * 30:.2f} kg de CO₂ al mes.")
    
@bot.command()
async def info(ctx):
    await ctx.send(f"Aqui tenes informacion la cual te puede ayudar para informate más sobre el cambio climatico: {random.choice(info)}")

bot.run("TOKEN")