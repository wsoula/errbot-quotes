from errbot import BotPlugin, botcmd, arg_botcmd, re_botcmd
import urllib.request
import json

class Quote(BotPlugin):
    """Return random quotes"""

    @botcmd
    def quote(self, msg, args):
        url = 'https://zenquotes.io/api/random'
        page = urllib.request.Request(url)
        response = json.loads(urllib.request.urlopen(page).read().decode('utf-8'))
        return response[0]['q']+'\n- '+response[0]['a']
