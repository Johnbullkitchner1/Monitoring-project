require('newrelic');
const express = require('express');
const app = express();
app.get('/', (req, res) => res.send('Hello World!'));
app.get('/test', (req, res) => res.send('Test Endpoint'));
app.get('/error', (req, res) => { throw new Error('Test error'); });
app.listen(3000, () => console.log('App running on port 3000'));