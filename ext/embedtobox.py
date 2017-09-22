"""
The MIT License (MIT)
Copyright (c) 2017 kwugfighter
Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
"""

import discord
import asyncio

async def etb(emb):
    emb_str = "```md\n"
    if emb.author:
        emb_str += f"<{emb.author.name}>\n\n"
    if emb.title:
        emb_str += f"<{emb.title}>\n"
    if emb.description:
        emb_str += f"{emb.description}\n"
    if emb.fields:
        for field in emb.fields:
            emb_str += f"#{field.name}\n{field.value}\n"
    if emb.footer:
        emb_str += f"\n{emb.footer.text}\n"
    if emb.timestamp:
        emb_str += "\n{}".format(str(emb.timestamp))
    emb_str += "```"

    return emb_str