from slackbot.bot import Bot

class Slackbot:
    def execute(self):
        bot = Bot()
        bot.run()

if __name__ == "__main__":
    slackbot = Slackbot()
    slackbot.execute()