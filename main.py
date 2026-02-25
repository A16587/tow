from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse

app = FastAPI(title="تنس فريدوم", description="تحليل أداء لاعبي التنس", version="2.0.0")

INDEX_HTML = """
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
<meta charset="UTF-8">
<title>تنس فريدوم</title>
<style>
body { font-family: sans-serif; background:#111; color:#fff; text-align:center; padding:50px; }
h1 { font-size:2rem; }
p { font-size:1.2rem; }
</style>
</head>
<body>
<h1>مرحبا بك في تنس فريدوم 🎾</h1>
<p>تحليل أداء لاعبي التنس بالذكاء الاصطناعي</p>
</body>
</html>
"""

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return HTMLResponse(content=INDEX_HTML)
