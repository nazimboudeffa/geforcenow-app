const fs = require('fs')
const express = require('express')
const app = express()
const ejs = require('ejs')
const path = require('path')
var gfn = require('./public/data/gfnpc.json')
var noImages = [];

// set the view engine to ejs
app.set('view engine', 'ejs')
app.set('views', path.join(__dirname, '/public'))

gfn.forEach((item, i) => {
  if (item.steamUrl != "") {
    str = item.steamUrl
    val = str.replace("https://store.steampowered.com/app/", "")
    if (!fs.existsSync("./public/images/" + val + ".jpg")) {
      noImages.push(val)
    }
  }
});


console.log(noImages.length);
console.log(noImages);


app.use(express.static('public'));

app.get('/', function(req, res) {
  res.render('index', {
    noImages: noImages
  })
})

app.get('/all', function(req, res) {
  res.render('all')
})

let port = 3000;

app.listen(port, function() {
  console.log('Example app listening on port 3000!')
})
