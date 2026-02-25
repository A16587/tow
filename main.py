import os
from pathlib import Path
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import cv2
import numpy as np
import mediapipe as mp

# تهيئة التطبيق
app = FastAPI(
    title="تنس فريدوم - الذكاء الاصطناعي لتحليل التنس",
    description="تحليل أداء لاعبي التنس بالذكاء الاصطناعي",
    version="2.0.0"
)

# المجلدات
BASE_DIR = Path(__file__).parent
TEMPLATES_DIR = BASE_DIR / "templates"
UPLOAD_DIR = BASE_DIR / "uploads"
REPORTS_DIR = BASE_DIR / "reports"
STATIC_DIR = BASE_DIR / "static"

# إنشاء المجلدات
TEMPLATES_DIR.mkdir(exist_ok=True)
UPLOAD_DIR.mkdir(exist_ok=True)
REPORTS_DIR.mkdir(exist_ok=True)
STATIC_DIR.mkdir(exist_ok=True)

# إعداد القوالب والملفات الثابتة
templates = Jinja2Templates(directory=str(TEMPLATES_DIR))
app.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static")

# صفحة HTML بسيطة للعرض
INDEX_HTML = """
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>تنس فريدوم · تحليل الأداء بالذكاء الاصطناعي</title>
    <link href="https://fonts.googleapis.com/css2?family=Tajawal:wght@300;400;500;700&display=swap" rel="stylesheet">
    <style>
        body { font-family: 'Tajawal', sans-serif; background: #111; color: #fff; text-align: center; padding: 50px; }
        h1 { font-size: 2rem; margin-bottom: 20px; }
        p { font-size: 1.2rem; }
    </style>
</head>
<body>
    <h1>مرحبا بك في تنس فريدوم 🎾</h1>
    <p>تحليل أداء لاعبي التنس بالذكاء الاصطناعي</p>
</body>
</html>
"""

# Route رئيسي
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return HTMLResponse(content=INDEX_HTML)
