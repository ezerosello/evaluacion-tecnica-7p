FROM python:3.11-slim

# Crear directorio de trabajo
WORKDIR /app

# Copiar archivos
COPY . /app

# Crear entorno virtual dentro del contenedor
ENV VIRTUAL_ENV=/app/venv
RUN python -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Instalar dependencias
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

# Comando por defecto (puede sobreescribirse en el Makefile)
CMD ["python", "-m", "src.main"]
