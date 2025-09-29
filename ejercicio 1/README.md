1º python3 -m venv venv
2º source venv/bin/activate
3º pip install -r requirements.txt

4º uvicorn app:app --reload


ejemplo de prueba:

curl "http://127.0.0.1:8000/countries/stats?metric=population" -> devuelve la población media de cada continente



# Uso de IA

### Usé Copilot para generar el modelo de las tablas countries y capitals 

### Usé Copilot para configurar endpoint stats, teniendo en cuenta 4 posibles métricas (población, área, densidad poblacional)

### Usé ChatGPT para el manejo de parámetros HTTP

