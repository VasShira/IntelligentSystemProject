import streamlit as st
import numpy as np
import joblib
import tensorflow as tf
import os
import base64

st.set_page_config(page_title="Wine NN Prediction", layout="wide")

def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

current_dir = os.path.dirname(__file__)
root_dir = os.path.dirname(current_dir)
img_path = os.path.join(root_dir, "wine_bg.png") # ตรวจสอบว่าชื่อไฟล์ตรงกับในเครื่อง

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

        /* 2. ปรับแต่งกรอบ st.form (สีเทาเข้ม #1A1A1A ตามรูปที่คุณส่งมา) */
        [data-testid="stForm"] {{
            background-color: #1A1A1A !important; /* สีเทาเข้มที่ต้องการ */
            border: 2px solid #D4AF37 !important; /* เส้นขอบสีทอง */
            border-radius: 20px !important;
            padding: 40px !important;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.7) !important;
        }}

        /* 3. ปรับแต่งหัวข้อและข้อความ Label ให้เป็นสีทอง */
        h1, h2, h3, label, .stMarkdown p {{
            color: #D4AF37 !important;
            font-weight: bold !important;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.8) !important;
        }}

        /* 4. ปรับแต่งช่อง Input ให้เข้ากับสีพื้นหลัง */
        .stNumberInput div, .stSelectbox div {{
            background-color: #262626 !important; /* สว่างกว่าพื้นหลังนิดหน่อย */
            color: #D4AF37 !important;
            border-radius: 10px !important;
        }}
        
        input {{
            color: #D4AF37 !important;
        }}

        /* 5. ปรับแต่งปุ่มวิเคราะห์ */
        .stButton>button {{
            width: 100% !important;
            background-color: #D4AF37 !important;
            color: #1A1A1A !important;
            font-weight: bold !important;
            border-radius: 12px !important;
            transition: 0.3s;
        }}
        
        .stButton>button:hover {{
            background-color: #B8860B !important;
            box-shadow: 0 0 15px rgba(212, 175, 55, 0.5) !important;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

@st.cache_resource
def load_nn_assets():
    base_path = os.path.dirname(os.path.dirname(__file__))
    
    m = tf.keras.models.Sequential([
        tf.keras.layers.Dense(64, activation='relu', input_shape=(11,)),
        tf.keras.layers.Dense(32, activation='relu'),
        tf.keras.layers.Dense(16, activation='relu'),
        tf.keras.layers.Dense(11, activation='softmax')
    ])
    
    weights_path = os.path.join(base_path, 'wine_nn_weights.weights.h5')
    m.load_weights(weights_path)
    s = joblib.load(os.path.join(base_path, 'wine_scaler.joblib'))
    i = joblib.load(os.path.join(base_path, 'wine_imputer.joblib'))
    
    return m, s, i

st.title("🧠 จำแนกคุณภาพไวน์ (Neural Network)")

try:
    nn, scaler, imputer = load_nn_assets()
    
    with st.form("wine_form"):
        st.subheader("🧪 องค์ประกอบทางเคมีของไวน์")
        col1, col2 = st.columns(2)
        
        with col1:
            fixed_acid = st.number_input("Fixed Acidity", 4.0, 16.0, 8.0)
            vol_acid = st.number_input("Volatile Acidity", 0.0, 2.0, 0.5)
            citric = st.number_input("Citric Acid", 0.0, 1.0, 0.3)
            sugar = st.number_input("Residual Sugar", 0.0, 20.0, 2.5)
            chlorides = st.number_input("Chlorides", 0.0, 1.0, 0.08)
            
        with col2:
            free_sd = st.number_input("Free Sulfur Dioxide", 1.0, 72.0, 15.0)
            total_sd = st.number_input("Total Sulfur Dioxide", 6.0, 289.0, 46.0)
            density = st.number_input("Density", 0.9900, 1.0050, 0.9960, format="%.4f")
            ph = st.number_input("pH", 2.0, 5.0, 3.3)
            sulphates = st.number_input("Sulphates", 0.3, 2.0, 0.6)
            alc = st.number_input("Alcohol", 8.0, 15.0, 10.5)
            
        submitted = st.form_submit_button("🍷 วิเคราะห์คุณภาพไวน์")

    if submitted:
        raw_data = np.array([[
            fixed_acid, vol_acid, citric, sugar, chlorides, 
            free_sd, total_sd, density, ph, sulphates, alc
        ]])
        
        prepped_data = scaler.transform(imputer.transform(raw_data))
        preds = nn.predict(prepped_data)
        grade = np.argmax(preds)
        
        st.write("---")
        st.metric("คะแนนคุณภาพที่ AI ทำนายได้", f"{grade} / 10")
        
        if grade >= 7:
            st.success("✨ เกรด: พรีเมียม (Premium Quality)")
        elif grade >= 5:
            st.info("👍 เกรด: มาตรฐาน (Standard Quality)")
        else:
            st.warning("⚖️ เกรด: พื้นฐาน (Basic Quality)")

except Exception as e:
    st.error(f"❌ Error: {e}")