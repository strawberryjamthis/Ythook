# Discord-YouTube-Feed

A simple Discord webhook bot (using discord.py fork, Disnake) that scrapes YouTube channels for new uploads and then posts them to a selected webhook channel.

Note, you must create a webhook to use this bot https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks then copy the webhook url.

## Edits

The following variables must be edited:

`discord_webhook_url = ` - Append a webhook URL. See https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks for info.   
`webhook_username = ` - append a nickname (can be anything) for the webhook)  
`webhook_avatar = ` - append URL for an avatar. Any picture should work. I host mine on [Imgur](https://imgur.com/upload) but this isn't required.

Add channel ID's you wish to follow to the `channel_ids` dictionary.
