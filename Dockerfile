FROM python:3.12

WORKDIR /app

# Tüm app klasörünü kapsayıcıya kopyala
COPY app /app

# Gerekli bağımlılıkları yükle
RUN pip install --no-cache-dir -r requirements.txt

# Streamlit uygulamasını çalıştır
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]

