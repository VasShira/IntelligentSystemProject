import streamlit as st

st.markdown("""
    <style>
    /* พื้นหลังหน้าเว็บ */
    .stApp {
        background-color: #0E1117;
    }

    /* ตกแต่งหัวข้อใหญ่ */
    h1 {
        color: #D4AF37 !important;
        border-bottom: 2px solid #D4AF37;
        padding-bottom: 10px;
        text-shadow: 2px 2px 4px black;
    }

    /* ตกแต่ง Card สำหรับแต่ละข้อ (1, 2, 3, 4) */
    .theory-card {
        background-color: #1A1A1A;
        border-left: 5px solid #D4AF37;
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 20px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.5);
    }

    /* สีหัวข้อข้อย่อย */
    h2, h3 {
        color: #D4AF37 !important;
        margin-top: 0px !important;
    }

    /* สีตัวหนังสือเนื้อหา */
    p, li {
        color: #E6F1FF !important;
        font-size: 1.1rem;
    }
    
    /* ตกแต่ง Link (แหล่งที่มา) */
    a {
        color: #00D4FF !important;
        text-decoration: none;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. วิธีการเขียนเนื้อหาให้เป็น Card
st.title("📖 ทฤษฎี Machine Learning (Ensemble)")

# ข้อ 1
st.markdown("""
    <div class="theory-card">
        <h3>1. ข้อมูลนักเตะ (Dataset)</h3>
        <ul>
            <li><b>ที่มา:</b> ข้อมูลสถิติจากลีก Premier League และ Super Lig</li>
            <li><b>Features:</b> ลงสนาม, ประตู, แอสซิสต์, Rating, นาทีที่เล่น, การเข้าปะทะ</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# ข้อ 2
st.markdown("""
    <div class="theory-card">
        <h3>2. การเตรียมข้อมูล (Data Preparation)</h3>
        <ul>
            <li>จัดการข้อมูลไม่สมบูรณ์ด้วย SimpleImputer (Median)</li>
            <li>แปลงข้อมูลหมวดหมู่ด้วย One-Hot Encoding และปรับสเกลด้วย StandardScaler</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# ข้อ 3
st.markdown("""
    <div class="theory-card">
        <h3>3. อัลกอริทึม Ensemble</h3>
        <p>ใช้เทคนิค <b>Voting Regressor</b> รวม 3 โมเดล:</p>
        <ol>
            <li>Random Forest</li>
            <li>Gradient Boosting</li>
            <li>Ridge Regression</li>
        </ol>
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
    <div class="theory-card">
        <h3>4. แหล่งที่มาและการอ้างอิง (Sources)</h3>
        <a href="https://www.kaggle.com/datasets/kaanyorgun/european-top-leagues-player-stats-25-26?resource=download" 
           target="_blank" 
           style="background-color: #D4AF37; color: black; padding: 10px 20px; text-decoration: none; border-radius: 5px; font-weight: bold; display: inline-block; margin-top: 10px;">
           📂 Open Kaggle Dataset
        </a>
    </div>
    """, unsafe_allow_html=True)
