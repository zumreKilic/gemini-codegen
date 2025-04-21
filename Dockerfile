# Temel imaj: Python
FROM python:3.10-slim

# Çalışma dizini
WORKDIR /app

# Gereken dosyaları kopyala
COPY . .

# Gereksinimleri yükle
RUN pip install --no-cache-dir -r requirements.txt

# Flask için port aç
EXPOSE 5000

# Uygulamayı çalıştır
CMD ["python", "app.py"]
