import os
import google.generativeai as genai
#from dotenv import load_dotenv

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("❌ GEMINI_API_KEY ortam değişkeni tanımlı değil.")

genai.configure(api_key=api_key)

#load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("models/gemini-1.5-flash-latest")

def get_code_and_title(prompt):
    instructions = (
        "Python dilinde bir kod üret. Kod mutlaka Job sınıfı yapısını kullanmalı.\n"
        "Çıktı iki bölümden oluşmalı:\n"
        "Başlık: <tek satır açıklama>\nKod:\n<kodu buraya yaz>"
    )

    try:
        response = model.generate_content([instructions, prompt])
        content = response.text.strip()

        # Parsing başlık ve kod
        title = "Başlık bulunamadı"
        code = "Kod bulunamadı"

        if "Kod:" in content:
            parts = content.split("Kod:", 1)
            title_part = parts[0].replace("Başlık:", "").strip()
            code_part = parts[1].strip()
            title = title_part
            code = code_part

        return title, code
    except Exception as e:
        return "Hata", f"Hata oluştu: {str(e)}"
