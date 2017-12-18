var http = require('http');
var server = http.createServer();

server.on('request', function(req, res){
  res.writeHead(200, {'Content-Type':'text/html'});
  res.write('<h1>Hello Node !</h1>');
  res.end();
});

server.listen(8888);
console.log('Server running on 8888');
