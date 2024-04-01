var express = require('express');
var mysql = require('mysql')
const env = require('dotenv').config({path: "../../.env"});
var app = express()

var connection = new mysql({
    host: process.env.host,
    user: process.env.user,
    port: process.env.port,
    password: process.env.password,
    database: process.env.database
});

connection.connect(function(err){
    if(!err){
        console.log("Database is connected~!!")
    }else{
        console.log("Error connectiong Query~!!")
    }
})

app.get('/', function(req,res){
    connection.query('select * from st_info', function(err,rows,fields){
        connection.end();
        if(!err){
            res.send(rows);
            console.log("The solution is: ",rows);
        }else{
            console.log('Error while performing Quer~!!');
        }
    })
})

app.listen(8000, function() {
    console.log('8000 port : Server started~!!');
})