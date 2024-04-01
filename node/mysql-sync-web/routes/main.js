const express = require('express') 
const bodyParser = require('body-parser')
const mysql = require('sync-mysql')
const env = require('dotenv').config({path:"../../.env"});

const app = express()

app.use(bodyParser.json())
app.use(bodyParser.urlencoded({ extended: false}))
app.use(express.json())
app.use(express.urlencoded({ extended: true}))

var connection = new mysql({
    host: process.env.host,
    user: process.env.user,
    port: process.env.port,
    password: process.env.password,
    database: process.env.database
});

app.get('/Hello',(req, res) => {
    res.send("Hello World");
})

// select all rows from st_info table
app.get('/select', (req, res) => {
    const result = connection.query("select * from st_info")
    console.log(result);
    // res.sendStatus(200);
    res.send(result);
})

// update data into st_info table
app.get('/insert', (req, res) => {
    const { ST_ID, NAME, DEPT } = req.query
    const result = connection.query(
        "insert into st_info values (?,?,?)", [ST_ID, NAME, DEPT]
    )
    res.redirect('/select');
})

// update data into st_info table
app.get('/update', (req, res) => {
    const { ST_ID, NAME, DEPT } = req.query
    const result = connection.query(
        "update st_info set NAME=?, DEPT=? where ST_ID=?", [NAME, DEPT, ST_ID]
    )
    res.redirect('/select');
})

// delete data into st_info table
app.get('/delete', (req, res) => {
    const ST_ID= req.query.ST_ID
    const result = connection.query(
        "delete from st_info where ST_ID=?", [ST_ID]
    )
    res.redirect('/select');
})

module.exports = app; 