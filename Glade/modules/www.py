#
# Copyright (C) 2021-2022 by miskumis@Github, <https://github.com/miskumis >.
#
# This file is part of < https://github.com/miskumis/PyroGlade-Userbot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/miskumis/PyroGlade-Userbot/blob/main/LICENSE >
#
# All rights reserved.

import time
from datetime import datetime

import speedtest
from pyrogram import Client, filters
from pyrogram.raw import functions
from pyrogram.types import Message

from config import CMD_HANDLER as cmd
from Glade import StartTime
from Glade.helpers.basic import edit_or_reply
from Glade.helpers.constants import WWW
from Glade.helpers.PyroHelpers import SpeedConvert
from Glade.utils.tools import get_readable_time

from .help import add_command_help


@Client.on_message(filters.command(["speed", "speedtest"], cmd) & filters.me)
async def speed_test(client: Client, message: Message):
    new_msg = await edit_or_reply(message, "`Running speed test . . .`")
    spd = speedtest.Speedtest()

    new_msg = await message.edit(
        f"`{new_msg.text}`\n" "`Getting best server based on ping . . .`"
    )
    spd.get_best_server()

    new_msg = await message.edit(f"`{new_msg.text}`\n" "`Testing download speed . . .`")
    spd.download()

    new_msg = await message.edit(f"`{new_msg.text}`\n" "`Testing upload speed . . .`")
    spd.upload()

    new_msg = await new_msg.edit(
        f"`{new_msg.text}`\n" "`Getting results and preparing formatting . . .`"
    )
    results = spd.results.dict()

    await message.edit(
        WWW.SpeedTest.format(
            start=results["timestamp"],
            ping=results["ping"],
            download=SpeedConvert(results["download"]),
            upload=SpeedConvert(results["upload"]),
            isp=results["client"]["isp"],
        )
    )


@Client.on_message(filters.command("dc", cmd) & filters.me)
async def nearest_dc(client: Client, message: Message):
    dc = await client.send(functions.help.GetNearestDc())
    await edit_or_reply(
        message, WWW.NearestDC.format(dc.country, dc.nearest_dc, dc.this_dc)
    )


@Client.on_message(filters.command("ping", cmd) & filters.me)
async def pingme(client: Client, message: Message):
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    xx = await edit_or_reply(message, "======🦖")
    await xx.edit("=====🦖=")
    await xx.edit("====🦖==")
    await xx.edit("===🦖===")
    await xx.edit("==🦖====")
    await xx.edit("=🦖=====")
    await xx.edit("🦖======")
    end = datetime.now()
    duration = (end - start).microseconds / 2000
    await xx.edit(
        f"**PONG!! ** - `%sms`\n" 
        f"**Uptime - ** `{uptime}` \n" % (duration)
    )


@Client.on_message(filters.command("kping", cmd) & filters.me)
async def kping(client: Client, message: Message):
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    xx = await edit_or_reply(message, "======🐒")
    await xx.edit("=====🐒=")
    await xx.edit("====🐒==")
    await xx.edit("===🐒===")
    await xx.edit("==🐒====")
    await xx.edit("=🐒=====")
    await xx.edit("🐒======")
    end = datetime.now()
    duration = (end - start).microseconds / 2000
    await xx.edit(
        f"**PONG!! ** -  `%sms`\n"
        f"**Uptime - ** `{uptime}` \n" % (duration)
    )


add_command_help(
    "speedtest",
    [
        ["dc", "Untuk melihat DC Telegram anda."],
        [
            f"speedtest `atau` {cmd}speed",
            "Untuk megetes Kecepatan Server anda.",
        ],
    ],
)


add_command_help(
    "ping",
    [
        ["ping", "Untuk Menunjukkan Ping Bot Anda."],
        ["kping", "Untuk Menunjukkan Ping Bot Anda ( Beda animasi doang )."],
    ],
)
