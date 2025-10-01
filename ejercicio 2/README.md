# Uso de IA

### Prompts

- "Refactor legacy Python system into modular classes: DataLoader, SalesAnalyzer, ReportGenerator. Separate classes into data_loader.py, report_generator.py, sales_analyzer.py"

- "Suggest performance optimizations on my .py files using pandas or numpy"

- "Generate pytest unit tests for each class with >80% coverage"

### Iteraciones y ajustes

Los prompts evolucionaron para lograr mayor precisión:

- Inicialmente pedí optimizaciones generales

- Luego pedí optimización con pandas y numpy.

- Ajusté el prompt de testing para incluir cobertura específica (>80%) y validación con pytest.


### Validación de Sugerencias

- Se descartó el uso de fmean() por compatibilidad con Python 3.8.

- Se evitó modificar imports en los tests para mantener modularidad (from src.module).

- Se descartó usar distutils por incompatibilidad con Python 3.12+.

- ChatGPT sugirió integrar una base de datos Postgres, descarté la idea por sobre diseño 


### Fragmentos de diálogo relevantes

- Le compartí mi código a Copilot y le pregunté si sugería cambios. Respondió:
```
    Cambios sugeridos por módulo

    🔧 data_loader.py
        1. Validación de existencia del archivo antes de abrirlo
        2. Encoding explícito para evitar errores en CSV/JSON con caracteres especiales
    
    📊 sales_analyzer.py
        1. Validación de campos antes del cálculo: evita errores si falta price, quantity o date.
    
    📤 report_generator.py
        1. Validación de estructura del reporte antes de exportar:

```
- Le pedí a Copilot que me ayude a actualizar mis tests para que cubran más porcentaje. Respondió:

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



```
Problema Original               |   Solución Implementada                                                   |   Herramienta IA Usada
--------------------------------|---------------------------------------------------------------------------|-------------------------
Función monolítica	            |   Refactorización en clases: DataLoader, SalesAnalyzer, ReportGenerator   |       Copilot
Promedio ineficiente	        |   Uso de pandas.groupby().agg() para sumar, contar y promediar	        |       ChatGPT
Cálculo manual con bucles	    |   Vectorización con pandas y numpy	                                    |       ChatGPT
Reportes con decimales largos	|   Redondeo con np.round() en exportación CSV	                            |       ChatGPT
Testing inexistente     	    |   Generación de tests unitarios con pytest y cobertura >90%	            |       Copilot
```




# Cómo ejecutar

Desde la raíz del proyecto, ejecutar
```bash
python -m src.main
```


# Cómo correr los tests

Desde la raíz del proyecto, ejecutar
```bash
python -m pytest tests/ --cov=src --cov-report=term-missing
```

python -m pytest tests/ -v
