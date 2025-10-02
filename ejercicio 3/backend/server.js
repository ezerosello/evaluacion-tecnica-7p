const express = require("express");
const fs = require("fs");
const cors = require("cors");
const path = require("path");
const app = express();

app.use(cors());
app.use(express.json());

const DATA_PATH = path.join(__dirname, "data/sales_data.json");

// entregar sales_data.json a dashboard y qa-tool
app.get("/sales-data", (req, res) => {
  fs.readFile(DATA_PATH, "utf8", (err, data) => {
    if (err) return res.status(500).json({ error: err.message });
    res.setHeader("Content-Type", "application/json");
    res.send(data);
  });
});

// guardar datos corregidos
app.post("/save-clean-to-dashboard", (req, res) => {
  const data = req.body;
  fs.writeFile(DATA_PATH, JSON.stringify(data, null, 2), (err) => {
    if (err) return res.status(500).json({ error: err.message });
    res.json({ success: true });
  });
});

app.listen(4000, () => console.log("Backend corriendo en http://localhost:4000"));
