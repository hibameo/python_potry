import streamlit as st
import random

# Expanded Dictionary of Quotes & Poetry
quotes = {
    "Love": [
        "محبت خود ایک خالص عبادت ہے۔",
        "دل وہی جیت سکتا ہے جو محبت سے بھرا ہو۔",
        "محبت کا جذبہ سب سے خوبصورت ہوتا ہے۔",
        "سچی محبت وہی ہے جو بنا کسی شرط کے ہو۔",
        "محبت کی روشنی اندھیرے دلوں کو بھی روشن کر دیتی ہے۔",
    ],
    "Motivation": [
        "کبھی ہمت مت ہاریں، کامیابی قریب ہے۔",
        "خود پر یقین رکھیں، راستے کھلتے جائیں گے۔",
        "محنت کا کوئی نعم البدل نہیں۔",
        "اگر خواب دیکھ سکتے ہو تو انہیں پورا بھی کر سکتے ہو۔",
        "مشکل وقت ہمیشہ نہیں رہتا، مگر مضبوط لوگ ہمیشہ رہتے ہیں۔",
    ],
    "Life": [
        "زندگی ایک کہانی ہے، اسے خوبصورت بنائیں۔",
        "وقت سب سے بڑا استاد ہے۔",
        "جو ملا ہے اس پر شکر کریں، زندگی آسان ہوجائے گی۔",
        "زندگی میں ہر لمحہ سیکھنے کا ایک نیا موقع ہوتا ہے۔",
        "زندگی کو شکایتوں میں نہیں، خوشیوں میں گزاریں۔",
    ],
    "Nature": [
        "قدرت کی خوبصورتی میں سکون ہے۔",
        "درخت ہمارے بہترین دوست ہیں۔",
        "بارش کی ہر بوند میں ایک کہانی ہوتی ہے۔",
        "چاندنی رات کی خاموشی میں محبت کی سرگوشی ہوتی ہے۔",
        "پہاڑوں کی اونچائی ہمیں حوصلہ دیتی ہے۔",
    ],
    "Friendship": [
        "دوستی وہ خزانہ ہے جو ہمیشہ بڑھتا ہے۔",
        "سچے دوست زندگی کی سب سے بڑی دولت ہیں۔",
        "دوست وہ ہوتے ہیں جو مشکل وقت میں ساتھ دیں۔",
        "دوستی ایک ایسا رشتہ ہے جو وقت کے ساتھ اور مضبوط ہوتا ہے۔",
        "ایک اچھا دوست وہ ہے جو آپ کی خامیوں کو بھی قبول کرے۔",
    ],
}

# Apply Custom CSS for Styling
st.markdown("""
    <style>
        body {
            background: linear-gradient(to right, #ffefba, #ffffff);
        }
        .main-title {
            text-align: center;
            font-size: 42px;
            font-weight: bold;
            color: #b8860b;
        }
        .sub-title {
            text-align: center;
            font-size: 18px;
            color: #444;
            margin-bottom: 20px;
        }
        .quote-box {
            background: #fff8e1;
            padding: 20px;
            border-radius: 10px;
            border-left: 5px solid #ff9800;
            font-size: 22px;
            font-style: italic;
            text-align: center;
            color: #333;
            margin: 20px auto;
            width: 80%;
            box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
        }
        .stButton>button {
            background-color: #ff9800 !important;
            color: white !important;
            font-size: 18px !important;
            border-radius: 10px !important;
            padding: 10px 20px !important;
            border: none !important;
        }
        .stButton>button:hover {
            background-color: #e68900 !important;
        }
        .footer {
            text-align: center;
            font-size: 14px;
            color: #777;
            margin-top: 30px;
        }
    </style>
""", unsafe_allow_html=True)

# Streamlit App UI
st.markdown("<h1 class='main-title'>🌿 AI Poetry & Quote Generator</h1>", unsafe_allow_html=True)
st.markdown("<p class='sub-title'>🎭 مختلف موضوعات پر خوبصورت شاعری اور اقوال زریں حاصل کریں!</p>", unsafe_allow_html=True)

# Theme Selection
theme = st.selectbox("📌 ایک موضوع منتخب کریں:", list(quotes.keys()))

# Generate Button with Styling
if st.button("✨ Generate Quote/Poetry", key="generate"):
    quote = random.choice(quotes[theme])
    st.markdown(f"<div class='quote-box'>{quote}</div>", unsafe_allow_html=True)

    # Download Option
    st.download_button("📥 Download Quote", quote, file_name="quote.txt")

# Footer
st.markdown("<p class='footer'>Developed with ❤️ by Hiba</p>", unsafe_allow_html=True)
