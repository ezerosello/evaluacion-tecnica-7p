candidato/
├── app.py # o server.rb
├── models.py # Modelos de DB
├── init_db.py # Script de inicialización
├── requirements.txt # o Gemfile
├── Dockerfile # Opcional (para PostgreSQL)
├── README.md
└── tests/
├── test_api.py # Tests de endpoints
└── test_db.py




1º python3 -m venv venv
2º source venv/bin/activate
3º pip install -r requirements.txt

4º uvicorn app:app --reload