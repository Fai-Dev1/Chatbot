import os
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from google import genai
from pydantic import BaseModel

# تحميل المتغيرات البيئية من ملف .env
load_dotenv()

# الحصول على مفتاح API الخاص بـ Gemini
gemini_api_key = os.getenv("GEMINI_API_KEY")

if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is missing from environment variables.")

# إنشاء العميل الخاص بـ Gemini
client = genai.Client(api_key=gemini_api_key)
MODEL_ID = "gemini-3.8-flash"

app = FastAPI(title="Gemini AI Chatbot Backend")


# بناء نموذج الطلب باستخدام Pydantic
class ChatRequest(BaseModel):
    messages: list


@app.post("/chat/")
async def chat(request: ChatRequest):
    try:
        # استخراج آخر رسالة أرسلها المستخدم
        user_message = request.messages[-1]["content"]

        # إرسال الطلب لنموذج Gemini
        response = client.models.generate_content(
            model=MODEL_ID,
            contents=user_message,
        )

        return {"reply": response.text}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    