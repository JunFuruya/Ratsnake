# -*- coding: utf-8 -*-

from app.service.slack_service import SlackBotStartService

if __name__ == "__main__":
    slack_bot_service = SlackBotStartService()
    slack_bot_service.run()