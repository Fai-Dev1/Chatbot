import requests
import streamlit as st

# إعدادات صفحة Streamlit
st.set_page_config(page_title="Fai AI Core | Cloud Services", page_icon="⚡")
st.title("⚡ Fai AI Core | Intelligent Assistant")
st.markdown("Welcome to the intelligent core system powered by a FastAPI backend architecture and Gemini AI integration.")


# تهيئة تاريخ المحادثة في الذاكرة المؤقتة للواجهة
if "messages" not in st.session_state:
    st.session_state.messages = []

# عرض الرسائل السابقة على الشاشة
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# استقبال إدخال المستخدم
if prompt := st.chat_input("اكتب رسالتك هنا..."):
    # إضافة رسالة المستخدم وعرضها
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # إرسال الطلب إلى سيرفر الـ FastAPI المحلي
    with st.chat_message("assistant"):
        with st.spinner("جاري التفكير عبر سيرفر FastAPI..."):
            try:
                # إرسال الـ payload بنفس الهيكل المتفق عليه مع الـ Backend
                response = requests.post(
                    "http://127.0.0.1:8000/chat/",
                    json={"messages": st.session_state.messages},
                )

                if response.status_code == 200:
                    reply = response.json().get("reply", "عذراً، لم أستقبل رداً صحيحاً.")
                    st.markdown(reply)
                    # حفظ رد البوت في الذاكرة
                    st.session_state.messages.append({"role": "assistant", "content": reply})
                else:
                    st.error(f"خطأ من السيرفر: {response.status_code} - {response.text}")

            except requests.exceptions.ConnectionError:
                st.error("تعذر الاتصال بسيرفر FastAPI. تأكد من تشغيل السيرفر أولاً عبر أمر Uvicorn!")
            except Exception as e:
                st.error(f"حدث خطأ غير متوقع: {str(e)}")

                         