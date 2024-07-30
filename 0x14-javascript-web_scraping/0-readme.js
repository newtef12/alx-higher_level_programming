#!/usr/bin/node
const fileSys = require('fs');
fileSys.readFile(process.argv[2], 'utf8', function (error, content) {
  console.log(error || content);
});
