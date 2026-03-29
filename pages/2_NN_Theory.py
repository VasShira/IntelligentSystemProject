import streamlit as st

# 1. ตั้งค่าหน้ากระดาษ
st.set_page_config(page_title="NN Theory", layout="wide")

# 2. ใส่ CSS สำหรับตกแต่งหน้าทฤษฎี (Card Style)
st.markdown("""
    <style>
    .stApp {
        background-color: #0E1117;
    }
    h1 {
        color: #D4AF37 !important;
        border-bottom: 2px solid #D4AF37;
        padding-bottom: 10px;
        text-shadow: 2px 2px 4px black;
    }
    .theory-card {
        background-color: #1A1A1A;
        border-left: 5px solid #D4AF37;
        padding: 25px;
        border-radius: 12px;
        margin-bottom: 25px;
        box-shadow: 0 6px 15px rgba(0,0,0,0.5);
    }
    h3 {
        color: #D4AF37 !important;
        margin-top: 0px !important;
        font-size: 1.4rem;
    }
    p, li {
        color: #E6F1FF !important;
        font-size: 1.05rem;
        line-height: 1.6;
    }
    b {
        color: #00D4FF; /* เน้นตัวหนาด้วยสีฟ้า Cyan ให้ดู Tech */
    }
    .source-btn {
        background-color: #D4AF37;
        color: black !important;
        padding: 8px 20px;
        text-decoration: none;
        border-radius: 5px;
        font-weight: bold;
        display: inline-block;
        margin-top: 10px;
    }
    .source-btn:hover {
        background-color: #FFD700;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🧠 ทฤษฎี Neural Network (Wine Quality)")

# --- Card 1: Dataset ---
st.markdown("""
    <div class="theory-card">
        <h3>1. ข้อมูลคุณภาพไวน์ (Wine Dataset)</h3>
        <ul>
            <li><b>ที่มา:</b> ชุดข้อมูลเคมีพื้นฐานของไวน์ (เช่น กรด, น้ำตาล, แอลกอฮอล์)</li>
            <li><b>เป้าหมาย:</b> ทำนายคะแนนคุณภาพ (Quality Score) ตั้งแต่ 0 ถึง 10</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# --- Card 2: Architecture ---
st.markdown("""
    <div class="theory-card">
        <h3>2. โครงสร้างโมเดล (Architecture)</h3>
        <p>ใช้ <b>Multi-Layer Perceptron (MLP)</b> ที่ประกอบด้วย:</p>
        <ul>
            <li><b>Input Layer:</b> 11 Features (ค่าทางเคมี)</li>
            <li><b>Hidden Layers:</b> 3 ชั้น (64, 32, 16 Neurons) พร้อม ReLU Activation</li>
            <li><b>Output Layer:</b> 11 Classes (0-10) พร้อม Softmax Activation</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# --- Card 3: Training Process ---
st.markdown("""
    <div class="theory-card">
        <h3>3. กระบวนการเรียนรู้ (Learning)</h3>
        <ul>
            <li><b>Loss Function:</b> Sparse Categorical Crossentropy</li>
            <li><b>Optimizer:</b> Adam (Adaptive Moment Estimation)</li>
            <li><b>Preprocessing:</b> ใช้ <b>StandardScaler</b> เพื่อปรับช่วงข้อมูลให้เหมาะสมกับการเทรน NN</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# --- Card 4: Sources ---
st.markdown("""
    <div class="theory-card">
        <h3>4. แหล่งที่มาและการอ้างอิง (Sources)</h3>
        <p>ศึกษาเพิ่มเติมเกี่ยวกับชุดข้อมูล Wine Quality ได้ที่นี่:</p>
        <a href="https://archive.ics.uci.edu/dataset/186/wine+quality" target="_blank" class="source-btn">
           📂 UCI Machine Learning Repository
        </a>
    </div>
    """, unsafe_allow_html=True)