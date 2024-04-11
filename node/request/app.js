const express = require('express') 
const request = require('request')
const CircularJson = require('circular-json');
const app = express();

app.get('/', (req, res) => {
    res.send('Web Server Started~!!');
});

app.get('/hello', (req, res) => {
    res.send({data: 'Hello World'});
});

let option = "http://192.168.1.74:8000/hello"
app.get('/rhello', (req,res) => {
    request(option, {json:true}, (err,result,body) => {
        if(err){
            return console.log(err);
        }
        // res.send(body);
        res.send(CircularJson.stringify(body));
    });

    const data = JSON.stringify({ todo: 'Buy the milk - Moon'});
    app.get('/data', function(req,res){
        res.send(data);
    });
});

app.listen(8000, function(){
    console.log('8000 port : Server Started ...');
});