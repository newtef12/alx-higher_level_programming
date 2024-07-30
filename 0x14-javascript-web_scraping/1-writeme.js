#!/usr/bin/node
const fileSys = require('fs');
fileSys.writeFile(process.argv[2], process.argv[3], error => {
  if (error) console.log(error);
});
