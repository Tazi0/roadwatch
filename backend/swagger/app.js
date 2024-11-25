const express = require('express');
const serverless = require('serverless-http');
const swaggerUI = require('swagger-ui-express');
const swaggerDocument = require('./swagger-spec.json');

const app = express();

app.use('/api-docs', swaggerUI.serve, swaggerUI.setup(swaggerDocument));

module.exports.handler = serverless(app)