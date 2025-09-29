# Instalación de dependencias y ejecución

### 1º Creación del entorno virtual
```bash
python3 -m venv venv
``` 
### 2º Activación del entorno virtual
```bash
source venv/bin/activate (Linux)
source venv/Scripts/activate (Windows)
```

### 3º Instalación de dependencias
```bash
pip install -r requirements.txt
```

### 4º Ejecución
```bash
uvicorn app:app --reload
```

# Ejecución de tests

### Desde la raiz del proyecto, ejecutar
```bash
python run_tests.py
```

# Ejemplos de prueba:

### Obtener todos los países
```bash
curl "http://127.0.0.1:8000/countries"
```

### Obtener los países de una region
```bash
curl "http://127.0.0.1:8000/countries?region=Americas"
```

### Obtener población media de cada region
```bash
curl "http://127.0.0.1:8000/countries/stats?metric=population"
```

### Obtener area de cada region
```bash
curl "http://127.0.0.1:8000/countries/stats?metric=area"
```

### Obtener densidad poblacional de cada region
```bash
curl "http://127.0.0.1:8000/countries/stats?metric=density"
```

### Obtener todas las ciudades capitales
```bash
curl "http://127.0.0.1:8000/capitals"
```

### Obtener información del clima de una capital
```bash
curl "http://127.0.0.1:8000/weather/buenos%20aires"
```


# Uso de IA

- Usé Copilot para generar el modelo de las tablas countries y capitals

- Usé ChatGPT generar las funciones que rellenan las tablas de la base de datos

- Usé Copilot para configurar el endpoint stats, teniendo en cuenta las métricas población, área, y densidad poblacional. (prompt: 'endpoint en FastAPI para obtener cantidad de habitantes, area total y densidad de población de una región particular")

- Usé Copilot para configurar el endpoint weather/{city} (prompt: 'endpoint en FastAPI para obtener temperatura, humedad y fecha de consulta de una ciudad")

- Usé Copilot para generar los schemas de respuesta

- Usé ChatGPT para testear los endpoints y la DB