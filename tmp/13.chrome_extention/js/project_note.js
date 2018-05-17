//******************************************************************************
// onload
//******************************************************************************
$(function(){
  // Chrome Extension だとインラインでイベントを実装できないため、スクリプト側でDOMを生成する
  $("#event_button_ul").append("<li id=\"shared_folder_button\">共有フォルダ</li>")
  $("#shared_folder_button").on("click", function(){
    window.open("https://drive.google.com/drive/folders/0ByzsJ8huuAGGOXNrSENGd2lSQk0" ,"_blank");
    window.open("https://drive.google.com/drive/folders/0ByzsJ8huuAGGQnpyWkoxaXROak0" ,"_blank");
    window.open("https://drive.google.com/drive/folders/0B17R2pbNQpGXZFBhQXNMYW4xOFE" ,"_blank");
  });
  
  $("#event_button_ul").append("<li id=\"metrics_button\">メトリクス</li>")
  $("#metrics_button").on("click", function(){
    window.open("https://graph.ms.pf.goo.ne.jp/list/site/api.mama000.goo.ne.jp" ,"_blank");
    window.open("https://service.monitor.pf.goo.ne.jp/zabbix/screens.php?sid=8c071eec04599089" ,"_blank");
    window.open("http://kibana.ms.pf.goo.ne.jp/?#/dashboard/mysql_slow_query.dmama-10.pro.linechart.dashboard?_g=(refreshInterval:(display:Off,pause:!f,section:0,value:0),time:(from:now-1d,mode:relative,to:now))&_a=(filters:!(),panels:!((col:1,id:dmama-slow-query-line-chart,row:1,size_x:12,size_y:3,type:visualization),(col:1,columns:!(_source),id:mysql_slow_query.dmama-10.pro,row:4,size_x:12,size_y:4,sort:!('@timestamp',desc),type:search)),query:(query_string:(analyze_wildcard:!t,query:'*')),title:mysql_slow_query.dmama-10.pro.linechart.dashboard)" ,"_blank");
  });

  $("#event_button_ul").append("<li id=\"communication_button\">連絡・調整</li>")
  $("#communication_button").on("click", function(){
    window.open("https://gooblogteam.slack.com" ,"_blank");
    window.open("https://aqua-city-plusfor.slack.com/messages/D7YB3CBD4/" ,"_blank");
    window.open("https://oshietegoo.backlog.jp" ,"_blank");
  });
});

//******************************************************************************
// table
//******************************************************************************


