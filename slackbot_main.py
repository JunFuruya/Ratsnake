# -*- coding: utf-8 -*-

from app.service.slack_service import SlackService
 
import sys, os, bottle

dirpath = os.path.dirname(os.path.abspath(__file__))
sys.path.append(dirpath)
os.chdir(dirpath)

args = sys.argv
os.environ['APP_ENV'] = args[1]

if __name__ == "__main__":
    slack_service = SlackService()
    slack_service.run()

