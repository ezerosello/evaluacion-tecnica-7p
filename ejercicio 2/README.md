# Uso de IA

## Prompts

- "Refactor legacy Python system into modular classes: DataLoader, SalesAnalyzer, ReportGenerator. Separate classes into data_loader.py, report_generator.py, sales_analyzer.py"

- "Suggest performance optimizations on my .py files using pandas or numpy"

- "Generate pytest unit tests for each class with >80% coverage"

## Iteraciones y ajustes

Los prompts evolucionaron para lograr mayor precisión:

- Inicialmente pedí optimizaciones generales

- Luego pedí optimización con pandas y numpy.

- Ajusté el prompt de testing para incluir cobertura específica (>80%) y validación con pytest.


## Validación de Sugerencias

- Se descartó el uso de fmean() por compatibilidad con Python 3.8.

- Se evitó modificar imports en los tests para mantener modularidad (from src.module).

- Se descartó usar distutils por incompatibilidad con Python 3.12+.

- ChatGPT sugirió integrar una base de datos Postgres, descarté la idea por sobre diseño 


## Fragmentos de diálogo relevantes

### Le compartí mi código a Copilot y le pregunté si sugería cambios. Respondió:
```
    Cambios sugeridos por módulo

    🔧 data_loader.py
        1. Validación de existencia del archivo antes de abrirlo
        2. Encoding explícito para evitar errores en CSV/JSON con caracteres especiales
    
    📊 sales_analyzer.py
        Validación de campos antes del cálculo: evita errores si falta price, quantity o date
    
    📤 report_generator.py
        Validación de estructura del reporte antes de exportar

    🚀 main.py
        1. Validación de usuarios antes de procesar
        2. Logging de inicio y fin del proceso

    🧪 Bonus: Preparación para testing
        Para facilitar los tests:

        Agregá get_data() en DataLoader para exponer los datos.

        Agregá get_report(user_id) en SalesAnalyzer para testear sin acceder a .reports directamente.

```
### Le pedí a Copilot que me ayude a actualizar mis tests para que cubran más porcentaje. Respondió:

```
Para aumentar la cobertura de tests y blindar el flujo completo, podemos agregar casos que validen:

✅ Casos faltantes que ahora cubriremos
Registro con campos faltantes → activa el nuevo logging.warning por campos ausentes.

Todos los registros inválidos → activa el logging.info por descarte total.

Reporte no generado → get_report devuelve None.

Validación de coerción fallida → date, price o quantity inválidos.

Ejecución exitosa con coerción parcial → mezcla de válidos e inválidos.

🧪 Tests actualizados y extendidos 
    (bloque de código)

🧠 Esto cubre:

Validación de campos obligatorios

Coerción de tipos

Logging por registros descartados

Flujo completo de éxito y fracaso
```


# Ejecución y tests



## Cómo ejecutar sin Docker

Incluir en la carpeta data los archivos que se quiera analizar (incluyo sales1.json y sales2.csv como ejemplo).

Crear el entorno virtual y activarlo
```bash
python3 -m venv venv
source venv/bin/activate     # En Linux
source venv/Scripts/activate # En Windows
```

Instalar las dependencias
```bash
pip install -r requirements.txt
```

Desde la raíz del proyecto, ejecutar
```bash
python3 -m src.main
```


## Cómo correr los tests sin Docker

Desde la raíz del proyecto, ejecutar
```bash
python3 -m pytest tests/ --cov=src --cov-report=term-missing     # para obtener informacion de coverage

python3 -m pytest tests/ -v     # para simplemente correr los tests
```

## Cómo ejecutar con Docker

Construir con
```bash
docker build -t evaluacion7p .
```

En Windows, en CMD, desde la raíz ejecutar:
```
docker run --rm -v "%cd%\reports:C:\app\reports" evaluacion7p
```

En Linux, ejecutar:
```bash
docker run --rm -v "$(pwd)/reports:/app/reports" evaluacion7p
```


## Cómo correr los tssts con Docker

Ejecutar
```bash 
docker run --rm evaluacion7p python -m pytest tests/ -v     # sin detalles de coverage
docker run --rm evaluacion7p python -m pytest tests/ --cov=src --cov-report=term-missing    # con información de coverage

```


### Tabla comparativa

```
Problema Original               |   Solución Implementada                                                   |   Herramienta IA Usada
--------------------------------|---------------------------------------------------------------------------|-------------------------
Función monolítica	            |   Refactorización en clases: DataLoader, SalesAnalyzer, ReportGenerator   |       Copilot
Promedio ineficiente	        |   Uso de pandas.groupby().agg() para sumar, contar y promediar	        |       ChatGPT
Cálculo manual con bucles	    |   Vectorización con pandas y numpy	                                    |       ChatGPT
Reportes con decimales largos	|   Redondeo con np.round() en exportación CSV	                            |       ChatGPT
Testing inexistente     	    |   Generación de tests unitarios con pytest y cobertura >90%	            |       Copilot
```
```