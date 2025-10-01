# Uso de IA

### Prompts
- "Refactor legacy Python system into modular classes: DataLoader, SalesAnalyzer, ReportGenerator. Separate classes into data_loader.py, report_generator.py, sales_analyzer.py"
- "Suggest performance optimizations on my .py files using pandas or numpy"
- "Generate pytest unit tests for each class with >80% coverage"
- "Document AI-assisted development process for README"


ChatGPT sugirió enriquecer los reportes agregando:
- Mediana: median=('total', 'median')
- Desviación estándar: std=('total', 'std')
- Percentiles (ej. 90%): lambda x: x.quantile(0.9)

ChatGPT sugirió reemplazar los bucles y defaultdict por pandas.groupby().agg() para mejorar performance y claridad. Se validó con tests unitarios y se mantuvo una versión nativa para compatibilidad.


# Cómo ejecutar

Desde la raíz del proyecto, ejecutar
```bash
python -m src.main
```