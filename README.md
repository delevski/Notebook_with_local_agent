# Or Delbsky Representative Agent 🤖

סוכן ייצוגי חכם המייצג את אור דלבסקי מול מגייסים ומעסיקים באמצעות Google Gemini ADK.

## 📋 תיאור

הסוכן פועל כנציג מקצועי של אור דלבסקי, עונה על שאלות מגייסים ומעסיקים בצורה רשמית, מנומסת ומקצועית. הסוכן משתמש במידע מקורות החיים והפרופיל המקצועי כדי לספק תשובות מדויקות ואמינות.

## 🎯 תכונות

- ✅ מענה אוטומטי לשאלות מגייסים
- ✅ טון מקצועי, נעים ואמין
- ✅ גישה למידע מלא מקורות החיים והפרופיל
- ✅ REST API endpoints לאינטגרציה קלה
- ✅ בנוי על Google Gemini 2.0

## 🚀 התקנה

### 1. התקן את התלויות

```bash
pip install -r requirements.txt
```

### 2. הגדר את מפתח ה-API

צור קובץ `.env` בתיקייה הראשית:

```bash
GOOGLE_API_KEY=your_api_key_here
```

או הגדר את המשתנה סביבה:

```bash
export GOOGLE_API_KEY="your_api_key_here"
```

### 3. הפעל את השרת

```bash
python agent_server.py
```

השרת יעלה על `http://localhost:5000`

## 📡 API Endpoints

### POST /agent/chat
שיחה עם הסוכן

**Request:**
```json
{
  "message": "ספר לי על הניסיון המקצועי של אור",
  "context": "אנחנו מחפשים מפתח פולסטאק" 
}
```

**Response:**
```json
{
  "response": "תשובת הסוכן...",
  "status": "success"
}
```

### GET /agent/info
מידע על הסוכן

**Response:**
```json
{
  "name": "or-representative-agent",
  "display_name": "Or Delbsky Representative Agent",
  "description": "סוכן ייצוגי הפועל בשם אור דלבסקי...",
  "model": "gemini-2.0-flash-exp",
  "resources": ["קורות חיים של אור דלבסקי", "פרופיל מקצועי של אור דלבסקי"]
}
```

### GET /health
בדיקת תקינות השרת

## 💡 דוגמאות שימוש

### cURL

```bash
curl -X POST http://localhost:5000/agent/chat \
  -H "Content-Type: application/json" \
  -d '{
    "message": "מה החוזקות המקצועיות של אור?",
    "context": "תהליך גיוס למשרת Senior Developer"
  }'
```

### Python

```python
import requests

response = requests.post(
    'http://localhost:5000/agent/chat',
    json={
        'message': 'ספר לי על הניסיון של אור בפיתוח',
        'context': 'משרה בחברת הייטק'
    }
)

print(response.json()['response'])
```

### JavaScript

```javascript
fetch('http://localhost:5000/agent/chat', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({
    message: 'מה הניסיון של אור?',
    context: 'תהליך גיוס'
  })
})
.then(response => response.json())
.then(data => console.log(data.response));
```

## 📁 מבנה הפרויקט

```
ADK-Agents-test/
├── agent_config.yaml      # הגדרות הסוכן
├── agent_server.py        # שרת Flask
├── requirements.txt       # תלויות Python
├── cv (4).pdf            # קורות חיים
├── Profile.pdf           # פרופיל מקצועי
├── .env                  # מפתח API (לא במאגר)
└── README.md             # מסמך זה
```

## 🔒 אבטחה

- המפתח של Google API צריך להישמר ב-`.env` ולא להיות במאגר
- השרת מריץ בפורט 5000 - ניתן לשנות בקובץ `agent_server.py`
- בסביבת ייצור, מומלץ להוסיף authentication ו-rate limiting

## 🛠️ התאמה אישית

ניתן לערוך את `agent_config.yaml` כדי:
- לשנות את ההנחיות למערכת
- להוסיף משאבים נוספים
- לשנות הגדרות המודל (temperature, max_tokens וכו')

## 📝 רישיון

פרויקט פרטי של אור דלבסקי
