# Ejecución con Docker

## Desde la raiz del proyecto:

### 1º Construir el proyecto
```bash
docker build -t api-exercise .
``` 

### 2º Correr la api
```bash
docker run -p 8000:8000 api-exercise (Windows)
docker run --name api-ia -p 8000:8000 -e API_KEY=9a4e499d3f7bc641d86290a592416c6b api-exercise  (Linux)
```

# Ejemplos de prueba:

### Obtener todos los países
```bash
curl "http://localhost:8000/countries"
```

### Obtener los países de una region
```bash
curl "http://localhost:8000/countries?region=Americas"
```

### Obtener población media de cada region
```bash
curl "http://localhost:8000/countries/stats?metric=population"
```

### Obtener area de cada region
```bash
curl "http://localhost:8000/countries/stats?metric=area"
```

### Obtener densidad poblacional de cada region
```bash
curl "http://localhost:8000/countries/stats?metric=density"
```

### Obtener todas las ciudades capitales
```bash
curl "http://localhost:8000/capitals"
```

### Obtener información del clima de una capital
```bash
curl "http://localhost:8000/weather/buenos%20aires"
```

# Ejecución de tests 

### En Linux, con el proyecto corriendo en Docker, ejecutar
```bash
docker exec api-ia python run_tests.py
```
### En Windows, ejecutar
```bash
docker-compose up --build -d

```

# Uso de IA

- Usé Copilot para generar el modelo de las tablas countries y capitals

- Usé ChatGPT generar las funciones que rellenan las tablas de la base de datos

- Usé Copilot para configurar el endpoint stats, teniendo en cuenta las métricas población, área, y densidad poblacional. (prompt: 'endpoint en FastAPI para obtener cantidad de habitantes, area total y densidad de población de una región particular")

- Usé Copilot para configurar el endpoint weather/{city} (prompt: 'endpoint en FastAPI para obtener temperatura, humedad y fecha de consulta de una ciudad")

- Usé Copilot para generar los schemas de respuesta

- Usé ChatGPT para testear los endpoints y la DB