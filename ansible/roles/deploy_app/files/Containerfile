# استخدام Python slim image عشان يفضل الحجم صغير
FROM python:3.12-slim

# مجلد العمل جوة الكونتينر
WORKDIR /app

# ننسخ requirements الأول لوحده (استغلال الـ layer caching بتاع Podman/Docker:
# لو requirements متغيرش، مش هيعيد تثبيت المكتبات تاني في كل build)
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# دلوقتي ننسخ باقي كود الـ app
COPY app/ .

# البورت اللي الـ Flask شغال عليه
EXPOSE 5000

# أمر تشغيل الـ app
CMD ["python3", "app.py"]
