# -*- coding: utf-8 -*-

from app.service.slack_service import SlackService
 
import sys, os, bottle

dirpath = os.path.dirname(os.path.abspath(__file__))
sys.path.append(dirpath)
os.chdir(dirpath)

args = sys.argv
if isinstance(args, list) and len(args) > 1 and args[1] is not None:
    os.environ['APP_ENV'] = args[1]
else:
    os.environ['APP_ENV'] = 'DEVELOPMENT'

if __name__ == "__main__":
    slack_service = SlackService()
    slack_service.run()

