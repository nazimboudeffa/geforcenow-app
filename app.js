const fs = require('fs')
const express = require('express')
const app = express()
const ejs = require('ejs')
const path = require('path')
var gfn = require('./public/data/gfnpc.json')
var noImages = [];
var steamGames = [];

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


gfn.forEach((item, i) => {
  if (item.steamUrl != "") {
    var str = item.steamUrl
    var val = str.replace("https://store.steampowered.com/app/", "")
    if (fs.existsSync("./public/json/" + val + ".json")) {
      fs.readFile("./public/json/" + val + ".json", function(err, data){
        var obj = JSON.parse(data)[val].data;
        if (obj.price_overview != undefined){
          steamGames.push({
            "name" : obj.name,
            "price": (parseInt(obj.price_overview.initial)/100).toString()
          });
        } else {
          steamGames.push({
            "name" : obj.name,
            "price": "N/A"
          });
        }
      });
    } else {
      //TODO : read from steam, but it's a max of 100.000 call a day
    }
  }
});

console.log(noImages.length);
console.log(noImages);


app.use(express.static('public'));

app.get('/', function(req, res) {
  res.render('index')
})

app.get('/prices', function(req, res) {
  res.render('prices', {games : steamGames})
})

app.get('/images', function(req, res) {
  res.render('images', {
    noImages: noImages
  })
})

app.get('/game/:game', function(req, res) {
  res.render('game', { game : req.params.game })
})

let port = 3000;

app.listen(port, function() {
  console.log('Example app listening on port 3000!')
})
