FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Exponemos el puerto 5000 (interno del contenedor)
EXPOSE 5000

# Comando para ejecutar la app
CMD ["python", "app.py"]