// backend/server.js
const express = require("express");
const fs = require("fs");
const cors = require("cors");
const path = require("path");
const app = express();

app.use(cors());
app.use(express.json());

const CLIENT_PUBLIC_PATH = path.join(__dirname, "../client-dashboard/public/sales_data.json");

app.post("/save-clean-to-dashboard", (req, res) => {
  const data = req.body;

  console.log("Guardando en:", CLIENT_PUBLIC_PATH);

  fs.writeFile(CLIENT_PUBLIC_PATH, JSON.stringify(data, null, 2), (err) => {
    if (err) {
      console.error("Error al guardar:", err);
      return res.status(500).json({ error: err.message });
    }
    res.json({ success: true });
  });
});


app.listen(4000, () => console.log("Backend corriendo en http://localhost:4000"));
