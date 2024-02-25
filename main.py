token = open("token.txt", "r").read()

import discord
from discord import Select, View

# Define options for the dropdown
options = [
    Select.option(label="Red", value="red", emoji=""),
    Select.option(label="Green", value="green", emoji="🟢"),
    Select.option(label="Blue", value="blue", emoji=""),
]

# Create a custom Select class
class ColorPicker(Select):
    def __init__(self):
        super().__init__(
            placeholder="Choose your favorite color...",
            min_values=1,
            max_values=1,
            options=options
        )

    async def callback(self, interaction: discord.Interaction):
        color = self.values[0]
        await interaction.response.send_message(f"You chose {color}!")

# Create a View to hold the Select
class MyView(View):
    def __init__(self):
        super().__init__()
        self.add_item(ColorPicker())

# Bot setup
intents = discord.Intents.default()
intents.message_content = True  # Required for interaction commands

bot = discord.Bot(intents=intents)

@bot.command()
async def color(ctx):
    """Sends a message with the color picker dropdown"""
    await ctx.send("Choose your favorite color:", view=MyView())

# Bot events
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')

bot.run(token)