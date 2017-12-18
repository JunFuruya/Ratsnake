# -*- coding: utf-8 -*-

import json
import os
import re
import requests

#################################################
# TODO クラス
#################################################
class Todo:
  todo_list = dict()

  #################################################
  # curl に使用する text を取得
  #################################################
  def getText(self):
    text = '';
    for key, value in self.todo_list.items():
      text += key + value + '\r\n'

    return text

  #################################################
  # TODO を含んでいるかを調べて、辞書に登録
  #################################################
  def searchTodos(self, file_path):
    # 正規表現準備
    pattern = r"todo"

    # 読み込みなので、第２引数は「r」とする
    file = open(file_path, 'r', encoding="utf-8")

    line_num = 1
    for line in file:
      if re.search(pattern, line):
        text = line.replace('\r', '')
        text = text.replace('\n', '')
        self.todo_list[file.name + ':' + str(line_num)] = text

      line_num += 1
  
    file.close()

  #################################################
  # ファイルを再起的に調べる
  #################################################
  def searchFiles(self, dir_path):
    entries = os.scandir(dir_path)
  
    for entry in entries:
      if entry.is_dir():
        self.searchFiles(entry.path)
    
      elif entry.is_file():
        self.searchTodos(entry.path)

    entries.close()

#################################################
# main 処理
#################################################
if __name__ == '__main__':
  print("start")
  
  root_path = "c:\\Users\\junfuruya\\vms\\dmama-dev\\repository\\dmama-webapp"
  todo_object = Todo()
  todo_object.searchFiles(root_path)
  curl_text = todo_object.getText()
  print(curl_text)

  # slack に POST する
  post_data = 'マルチバイト'
  target_url = 'https://hooks.slack.com/services/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'
  print(post_data)
  # windows10 64bit だと pucurl を pip install できないため httprequest
  headers = {'Content-type': 'application/json'}
  payload = {'text': post_data}
  #response = requests.post(target_url, data=json.dumps(payload), headers=headers)

  print("finish")