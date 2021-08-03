# Ultroid - UserBot
# Copyright (C) 2021 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.

from telethon.errors import ChatSendInlineForbiddenError

from . import *

REPOMSG = """
• **ULTROID USERBOT** •\n
• Repo - [Click Here](https://github.com/TeamUltroid/Ultroid)
• Addons - [Click Here](https://github.com/TeamUltroid/UltroidAddons)
• Support - @UltroidSupport
"""

RP_BUTTONS = [
    [
        Button.inline("Repo", "https://github.com/TeamUltroid/Ultroid"),
        Button.inline("Addons", "https://github.com/TeamUltroid/UltroidAddons"),
    ],
    [Button.inline("Support Group", "t.me/ultroidsupport")],
]


@ultroid_cmd(pattern="repo$", type=["official", "manager"], ignore_dualmode=True)
async def repify(e):
    if e.client._bot:
        return await e.reply("**Ultroid Userbot**", buttons=RP_BUTTONS)
    try:
        q = await e.client.inline_query(asst.me.username, "repo")
        await q[0].click(e.chat_id)
        if e.out:
            await e.delete()
    except (ChatSendInlineForbiddenError):
        await eor(e, REPOMSG)
