// server-open-data.js

// BASE SETUP
// ==============================================
const { Pool } = require('pg')
const express = require('express');
const app = express();
const port = process.env.PORT || 8080;

const connectionString = process.env.DATABASE_URL;
const pool = new Pool({
  connectionString: connectionString,
});



// ROUTES
// ==============================================

app.get('/', function (req, res) {
  res.send('loloazerazer');
});


// START THE SERVER with start.js
// ==============================================

module.exports = {
  start(port) {
    server = app.listen(port, () => {
      console.log(`App started on port ${port} have fun bibiche`);
    });
    return app;
  },
  stop() {
    server.close();
  }
};
