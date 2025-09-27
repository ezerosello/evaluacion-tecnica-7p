# Cómo ejecutar

## Requisitos previos
```
- Tener Python instalado
- Contar con pip en la terminal
```

## Pasos a seguir
```
1º activar entorno virtual

python -m venv venv

en bash:
source venv/Scripts/activate

2º Instalar dependencias con el comando:
     pip install -r requirements.txt (tanto en Windows como en Linux)

``` 


para levantar la app:

uvicorn app:app --reload