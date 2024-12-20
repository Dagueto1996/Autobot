// Crear y configurar un backend básico en Node.js con Express.js

// Requisitos:
// - Node.js instalado
// - npm (Node Package Manager)

// Pasos:
// 1. Crear un directorio para el proyecto:
//    mkdir backend_project
//    cd backend_project

// 2. Inicializar el proyecto y agregar dependencias:
//    npm init -y
//    npm install express pg dotenv cors body-parser

// 3. Crear los siguientes archivos:
//   - server.js
//    - .env
//    - db.js

// --- Archivo: server.js ---
const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');
require('dotenv').config();
const db = require('./db');

const app = express();
const PORT = process.env.PORT || 3000;

// Middleware
app.use(cors());
app.use(bodyParser.json());

// Endpoint de prueba
app.get('/', (req, res) => {
    res.send('Backend funcionando correctamente');
});

// Conexión a la base de datos
app.get('/test-db', async (req, res) => {
    try {
        const result = await db.query('SELECT NOW()');
        res.json({ success: true, timestamp: result.rows[0] });
    } catch (error) {
        console.error(error);
        res.status(500).send('Error conectando a la base de datos');
    }
});

// Iniciar el servidor
app.listen(PORT, () => {
    console.log(`Servidor corriendo en http://localhost:${PORT}`);
});

// --- Archivo: .env ---
// PORT=3000
// DB_HOST=localhost
// DB_PORT=5432
// DB_USER=tu_usuario
// DB_PASSWORD=tu_contraseña
// DB_NAME=nombre_base_de_datos

//  --- Archivo: db.js ---
const { Pool } = require('pg');

const pool = new Pool({
    host: process.env.DB_HOST,
    port: process.env.DB_PORT,
    user: process.env.DB_USER,
    password: process.env.DB_PASSWORD,
    database: process.env.DB_NAME,
});

module.exports = {
    query: (text, params) => pool.query(text, params),
};
