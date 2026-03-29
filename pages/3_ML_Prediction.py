import streamlit as st
import pandas as pd
import joblib
import os
import base64

# 1. ตั้งค่าหน้ากระดาษ
st.set_page_config(page_title="Football Value Prediction", layout="wide")

# --- ฟังก์ชันสำหรับแปลงรูปในเครื่องเป็น Base64 ---
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# --- การจัดการ Path รูปภาพ ---
current_dir = os.path.dirname(__file__)
root_dir = os.path.dirname(current_dir)
img_path = os.path.join(root_dir, "stadium.png") 

# --- ส่วนของ CSS ทั้งหมด ---
if os.path.exists(img_path):
    bin_str = get_base64_of_bin_file(img_path)
    st.markdown(
        f"""
        <style>
        /* 1. พื้นหลังหน้าเว็บชั้นนอกสุด */
        .stApp {{
            background-image: url("data:image/png;base64,{bin_str}");
            background-size: cover !important;
            background-position: center !important;
            background-attachment: fixed !important;
        }}

        /* 2. ปรับแต่งกรอบ st.form (สีเทาเข้ม #1A1A1A) */
        [data-testid="stForm"] {{
            background-color: #1A1A1A !important;
            border: 2px solid #D4AF37 !important;
            border-radius: 20px !important;
            padding: 40px !important;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.8) !important;
        }}

        /* 3. ปรับแต่งหัวข้อและข้อความ Label (สีทอง) */
        h1, h2, h3, label, .stMarkdown p {{
            color: #D4AF37 !important;
            font-weight: bold !important;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.8) !important;
        }}

        /* 4. ปรับแต่งช่อง Input (Selectbox, NumberInput) */
        .stSelectbox div, .stNumberInput div {{
            background-color: #262626 !important;
            color: #D4AF37 !important;
            border-radius: 10px !important;
        }}
        input {{
            color: #D4AF37 !important;
        }}

        /* 5. ปรับแต่ง Slider (แถบเลื่อน Rating) ให้เป็นสีทอง */
        /* ส่วนของจุดวงกลม (Thumb) */
        div[data-baseweb="slider"] > div > div > div > div {{
            background-color: #D4AF37 !important;
            border: 2px solid #FFFFFF !important;
        }}
        /* ส่วนของแถบที่เลื่อนไปแล้ว (Track Highlight) */
        div[data-baseweb="slider"] > div > div {{
            background: #D4AF37 !important;
        }}
        /* ส่วนของตัวเลขบอกค่าบน Slider */
        div[data-testid="stSliderTickBar"] span {{
            color: #D4AF37 !important;
        }}

        /* 6. ปรับแต่งปุ่ม Predict */
        .stButton>button {{
            width: 100% !important;
            background-color: #D4AF37 !important;
            color: #1A1A1A !important;
            font-weight: bold !important;
            border-radius: 12px !important;
            border: none !important;
            transition: 0.3s;
        }}
        .stButton>button:hover {{
            background-color: #B8860B !important;
            box-shadow: 0 0 20px rgba(212, 175, 55, 0.5) !important;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
else:
    st.error(f"❌ ไม่พบไฟล์รูปภาพ stadium.png ที่: {img_path}")

# --- ส่วนของการทำงาน Model ---
st.title("⚽ Football Player Value Predictor")

@st.cache_resource
def load_fb_model():
    model_file = os.path.join(root_dir, 'football_ml_model.joblib')
    return joblib.load(model_file)

try:
    model = load_fb_model()
    
    with st.form("fb_form"):
        st.subheader("📋 ระบุข้อมูลนักเตะ")
        col1, col2 = st.columns(2)
        
        with col1:
            league = st.selectbox("ลีกที่สังกัด", ["Premier League", "Super Lig"])
            pos = st.selectbox("ตำแหน่ง", ["F", "M", "D", "G"])
            app = st.number_input("จำนวนนัดที่ลงสนาม", 0, 60, 20)
            
        with col2:
            goals = st.number_input("จำนวนประตู", 0, 50, 5)
            assists = st.number_input("จำนวนแอสซิสต์", 0, 50, 3)
            # Slider ตัวนี้จะกลายเป็นสีทองตาม CSS ด้านบน
            rating = st.slider("Rating เฉลี่ย (0.0 - 10.0)", 0.0, 10.0, 6.8)
        
        st.write("")
        submitted = st.form_submit_button("💰 ทำนายราคานักเตะ")

    if submitted:
        input_data = pd.DataFrame({
            'league': [league],
            'position': [pos],
            'appearances': [app],
            'goals': [goals],
            'assists': [assists],
            'rating': [rating],
            'minutes_played': [app * 85],
            'tackles': [2.5]
        })
        
        prediction = model.predict(input_data)[0]
        st.markdown("---")
        st.success(f"### 💎 ราคาประเมินในตลาด: €{max(0, prediction):,.2f}")

except Exception as e:
    st.error(f"⚠️ เกิดข้อผิดพลาด: {e}")