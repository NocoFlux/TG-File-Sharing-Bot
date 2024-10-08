# TG-File-Sharing-Bot

<div style="display: flex; justify-content: center;">
    <img src="https://img.shields.io/badge/Made%20with%20Python-light%20blue?style=for-the-badge&logo=Python&link=https%3A%2F%2Fwww.python.com" style="width: 250px;">
</div>

<div style="display: flex; justify-content: center;">
    <img src="https://img.shields.io/badge/NocoFlux-orange?style=for-the-badge&logo=Github&label=Made%20by%20" style="width: 250px;">
</div>

### Short Description
 - This is File Store Bot for Telegram Platform, which bot can send users a spacific files through link, genarated by admin itself.

### Features
 - 4 Force Sub Channel
 - Single or Multiple Files Link Support [Batch]
 - Free Deployable [Koyeb][Render]
 - User Friendly and Less Complexity
 - Fully Free to use.
 - More Updates in near future.

### Variables

* `API_HASH` Your API Hash from my.telegram.org
* `APP_ID` Your API ID from my.telegram.org
* `TG_BOT_TOKEN` Your bot token from @BotFather
* `OWNER_ID` Must enter Your Telegram Id
* `CHANNEL_ID` Your Channel ID eg:- -100xxxxxxxx
* `DB_URL` Your mongo db url
* `DB_NAME` Your mongo db session name
* `ADMINS` Optional: A space separated list of user_ids of Admins, they can only create links
* `START_MESSAGE` Optional: start message of bot, use HTML and <a href='https://github.com/NocoFlux/TG-File-Sharing-Bot/raw/refs/heads/main/Others/fillings.md'>fillings</a>
* `FORCE_SUB_MESSAGE`Optional:Force sub message of bot, use HTML and Fillings
* `FORCE_SUB_CHANNEL_1` Optional: ForceSub1 Channel ID, leave 0 if you want disable force sub
* `FORCE_SUB_CHANNEL_2` Optional: ForceSub2 Channel ID, leave 0 if you want disable force sub
* `FORCE_SUB_CHANNEL_3` Optional: ForceSub3 Channel ID, leave 0 if you want disable force sub
* `FORCE_SUB_CHANNEL_4` Optional: ForceSub4 Channel ID, leave 0 if you want disable force sub
* `PROTECT_CONTENT` Optional: True if you need to prevent files from forwarding

### Extra Variables

* `CUSTOM_CAPTION` put your Custom caption text if you want Setup Custom Caption, you can use HTML and <a href='https://github.com/CodeXBotz/File-Sharing-Bot/blob/main/README.md#custom_caption'>fillings</a> for formatting (only for documents)
* `DISABLE_CHANNEL_BUTTON` Put True to Disable Channel Share Button, Default if False
* `BOT_STATS_TEXT` put your custom text for stats command, use HTML and <a href='https://github.com/codexbotz/File-Sharing-Bot/blob/main/README.md#custom_stats'>fillings</a>
* `USER_REPLY_TEXT` put your text to show when user sends any message, use HTML


### Admin Commands

```
start - start the bot or get posts

genlink - create link for one post

batch - create link for more than one posts

broadcast - broadcast any messages to bot users

users - view bot statistics

dev - about developer

id - to get your user id

stats - checking your bot uptime

```

# Fillings
• START OR FORCESUB MESSAGE

* `{first}` - User first name  
* `{last}` - User last name  
* `{id}` - User ID  
* `{mention}` - Mention the user 
* `{username}` - Username  

• CUSTOM_CAP
* `{filename}` - file name of the Document  
* `{previouscaption}` - Original Caption  

• CUSTOM_UPTIME
* `{uptime}` - Bot Uptime




  
