# -*- coding: utf-8 -*-

from app.service.slack_service import SlackService

if __name__ == "__main__":
    slack_service = SlackService()
    slack_service.run()

