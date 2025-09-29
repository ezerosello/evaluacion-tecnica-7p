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


ejemplo de prueba:

curl "http://127.0.0.1:8000/countries/stats?metric=population" -> devuelve la población media de cada continente





🤖 Uso de herramientas de IA para acelerar el desarrollo
Durante el desarrollo de esta API, se utilizaron herramientas de inteligencia artificial como ChatGPT y GitHub Copilot para automatizar tareas repetitivas y mejorar la productividad. En particular, se aplicaron para:

Generación de endpoints REST: creación de rutas como /countries, /countries/stats, y sus variantes con filtros y métricas.

Manejo de parámetros HTTP (Query, Path): estructuración de funciones con validación de entrada y compatibilidad con Swagger.

Consultas SQLAlchemy optimizadas: uso de funciones agregadas (func.avg, func.max, case) para estadísticas por región.

Unificación de lógica condicional: consolidación de múltiples métricas en un solo endpoint dinámico.

Validación y manejo de errores: generación de respuestas HTTP claras con HTTPException.

Estas herramientas permitieron mantener un flujo incremental, modular y reproducible, alineado con buenas prácticas de desarrollo. Además, se documentó cada decisión técnica para facilitar la comprensión y el mantenimiento del código.