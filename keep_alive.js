const express = require('express');
const app = express();
app.use(express.static('public'));

const https = require('https');
app.get("/", (request, response) => {
    response.sendStatus(200);
});

app.listen(3000);

setInterval(() => {
    https.get(''); //repl}, 1);
