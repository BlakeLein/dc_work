# Express 101

### Vanilla way of creating a server with multiple "page URLs"

```
const http = require('http');

const hostname = '127.0.0.1';
const port = 3000;

const server = http.createServer((req, res) => {
    // Extract the url path from the request.
    const {url} = req;
    console.log(`The URL path is: ${url}`);

    if (url === '/') {
        res.statusCode = 200;
        res.setHeader('Content-Type', 'text/plain');
        res.end('Hello World')
    } else if (url === '/favicon.ico') {
        res.statusCode = 200;
        res.end('')
    } else {
        res.statusCode = 200;
        res.setHeader('Content-Type', 'text/plain');
        res.end('This is not the home page')
    }
});

server.listen(port, hostname, () => {
    console.log(`Server running at http://${hostname}:${port}/`);
});
```

### Express Way of doing the same thing

```
const http = require('http');

const hostname = '127.0.0.1';
const port = 3000;

const express = require('express');
const app = express();

const server = http.createServer(app);

app.get('/', (req, res) => {
    res.send('Hello World');
});

app.get('/favicon.ico', (req, res) => {
    res.send('');
});

app.get('*', (req, res) => {
    res.send('This is not the home page')
});

server.listen(port, hostname, () => {
    console.log(`Server running at http://${hostname}:${port}/`);
});
```

### Other notes

- GET is the HTTP method of getting info from a server
- POST is submitting data in the HTML form
- Routing is the same as "matching" two things: the HTTP method (GET, POST, etc) and path (url)
