# Usa una imagen base de Python 3.11
FROM python:3.11-slim

# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos de requerimientos e instala las dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia el código de la aplicación
COPY back.py .

# Expone el puerto 5000 para el contenedor
EXPOSE 5000

# Comando para ejecutar la aplicación cuando el contenedor inicie
CMD ["python", "back.py"]
