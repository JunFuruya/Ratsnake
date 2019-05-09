# -*- coding: utf-8 -*-

import os

# 20180514 added
from app.infrastructure.slack_yaml_file import SlackConfigYamlFile

aliases, api_token, bit_icon, bot_emoji, debug, default_reply, errors_to, plugins = SlackConfigYamlFile().get_config()

DEBUG = debug
PLUGINS = plugins
ERRORS_TO = errors_to
API_TOKEN = api_token

'''
Setup a comma delimited list of aliases that the bot will respond to.

Example: if you set ALIASES='!,$' then a bot which would respond to:
'botname hello'
will now also respond to
'$ hello'
'''
ALIASES = aliases

'''
If you use Slack Web API to send messages (with
send_webapi(text, as_user=False) or reply_webapi(text, as_user=False)),
you can customize the bot logo by providing Icon or Emoji. If you use Slack
RTM API to send messages (with send() or reply()), or if as_user is True
(default), the used icon comes from bot settings and Icon or Emoji has no
effect.
'''
BOT_ICON = bit_icon
BOT_EMOJI = bot_emoji

'''Specify a different reply when the bot is messaged with no matching cmd'''
DEFAULT_REPLY = default_reply

for key in os.environ:
    if key[:9] == 'SLACKBOT_':
        name = key[9:]
        globals()[name] = os.environ[key]

try:
    from slackbot_settings import *
except ImportError:
    try:
        from local_settings import *
    except ImportError:
        pass

# convert default_reply to DEFAULT_REPLY
try:
    DEFAULT_REPLY = default_reply
except NameError:
    pass
