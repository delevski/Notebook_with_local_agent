# 🚀 מדריך התקנה והפעלה - Or Delbsky Representative Agent

## שלב 1: הגדרת מפתח Google API

1. **קבל מפתח API**:
   - גש ל-[Google AI Studio](https://aistudio.google.com/app/apikey)
   - התחבר עם חשבון Google שלך
   - לחץ על "Create API Key"
   - העתק את המפתח

2. **צור קובץ .env**:
   ```bash
   # בתיקיית הפרויקט, צור קובץ .env
   echo "GOOGLE_API_KEY=your_actual_api_key_here" > .env
   ```
   
   **חשוב**: החלף את `your_actual_api_key_here` במפתח האמיתי שקיבלת!

## שלב 2: הפעלת השרת

```bash
# ודא שאתה בתיקיית הפרויקט
cd "/Users/corphd/Desktop/Or codes projects/ADK-Agents-test"

# הפעל את השרת
python3 agent_server.py
```

אתה אמור לראות:
```
🚀 Starting Or Delbsky Representative Agent...
📋 Resources loaded: 2
🤖 Model: gemini-2.0-flash-exp

✅ Server is running on http://localhost:5000

Endpoints:
  - POST /agent/chat - שיחה עם הסוכן
  - GET  /agent/info - מידע על הסוכן
  - GET  /health     - בדיקת תקינות
```

## שלב 3: בדיקת הסוכן

**באמצעות הסקריפט המוכן**:
```bash
# בטרמינל נפרד (השאר את השרת רץ)
python3 test_agent.py
```

**באמצעות cURL**:
```bash
curl -X POST http://localhost:5000/agent/chat \
  -H "Content-Type: application/json" \
  -d '{
    "message": "ספר לי על הניסיון המקצועי של אור",
    "context": "אנחנו מחפשים מפתח פולסטאק"
  }'
```

## שלב 4: שימוש בסוכן

### דוגמאות לשאלות שאפשר לשאול:

1. **על ניסיון מקצועי**:
   ```json
   {
     "message": "ספר לי על הניסיון של אור בפיתוח",
     "context": "משרת Senior Developer בחברת הייטק"
   }
   ```

2. **על חוזקות**:
   ```json
   {
     "message": "מה החוזקות המקצועיות של אור?",
     "context": "תהליך גיוס"
   }
   ```

3. **על זמינות**:
   ```json
   {
     "message": "האם אור זמין לעבודה?",
     "context": "משרה במשרה מלאה"
   }
   ```

4. **על השכלה וכישורים**:
   ```json
   {
     "message": "מה ההשכלה והכישורים הטכניים של אור?",
     "context": "דרישות התפקיד: React, Node.js, Python"
   }
   ```

## 🔧 פתרון בעיות

### השרת לא עולה
- ✅ ודא שהתקנת את כל התלויות: `pip3 install -r requirements.txt`
- ✅ בדוק שקובץ `.env` קיים ומכיל מפתח API תקין
- ✅ ודא שפורט 5000 פנוי (או שנה את הפורט ב-`agent_server.py`)

### שגיאת API Key
```
ValueError: GOOGLE_API_KEY environment variable is required
```
**פתרון**: צור קובץ `.env` עם המפתח שלך

### שגיאת Connection
```
requests.exceptions.ConnectionError
```
**פתרון**: ודא שהשרת רץ על `http://localhost:5000`

## 📱 אינטגרציה עם אפליקציות

### React/Next.js
```javascript
const askAgent = async (message, context = '') => {
  const response = await fetch('http://localhost:5000/agent/chat', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ message, context })
  });
  const data = await response.json();
  return data.response;
};
```

### Python
```python
import requests

def ask_agent(message, context=''):
    response = requests.post(
        'http://localhost:5000/agent/chat',
        json={'message': message, 'context': context}
    )
    return response.json()['response']
```

## 🌐 פריסה לייצור (Production)

לפריסה בסביבת ייצור, מומלץ:

1. **להשתמש ב-WSGI server** כמו Gunicorn:
   ```bash
   pip3 install gunicorn
   gunicorn -w 4 -b 0.0.0.0:5000 agent_server:app
   ```

2. **להוסיף HTTPS** באמצעות Nginx או Caddy

3. **להוסיף authentication** ו-rate limiting

4. **להשתמש במשתני סביבה** במקום קובץ `.env`

## 📞 תמיכה

אם יש בעיות או שאלות, בדוק את:
- [README.md](README.md) - תיעוד מלא
- [agent_config.yaml](agent_config.yaml) - הגדרות הסוכן
- לוגים של השרת בטרמינל

---

**הצלחה! הסוכן שלך מוכן לייצג אותך בצורה מקצועית מול מגייסים! 🎉**
