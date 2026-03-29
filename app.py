import streamlit as st

# 1. ตั้งค่าหน้ากระดาษ
st.set_page_config(page_title="Intelligent System Home", layout="wide")

# 2. CSS สำหรับตกแต่งหน้า Home
st.markdown("""
    <style>
    /* พื้นหลังหน้าเว็บ */
    .stApp {
        background-color: #0E1117;
    }

    /* Hero Section (ส่วนหัว) */
    .hero-container {
        background: linear-gradient(135deg, #1A1A1A 0%, #000000 100%);
        padding: 50px;
        border-radius: 20px;
        border: 2px solid #D4AF37;
        text-align: center;
        margin-bottom: 40px;
        box-shadow: 0 10px 30px rgba(212, 175, 55, 0.2);
    }
    
    .hero-title {
        color: #D4AF37 !important;
        font-size: 3rem !important;
        font-weight: 800;
        margin-bottom: 10px;
    }
    
    .hero-subtitle {
        color: #E6F1FF !important;
        font-size: 1.2rem;
        opacity: 0.8;
    }

    /* Category Cards (กรอบฟุตบอลและไวน์) */
    .category-card {
        background-color: #1A1A1A;
        border: 1px solid #333;
        padding: 30px;
        border-radius: 15px;
        transition: 0.3s;
        height: 100%;
        text-align: center;
    }
    
    .category-card:hover {
        border-color: #D4AF37;
        transform: translateY(-5px);
        box-shadow: 0 10px 20px rgba(0,0,0,0.5);
    }

    .category-icon {
        font-size: 3rem;
        margin-bottom: 20px;
    }
    
    .footer {
        text-align: center;
        margin-top: 50px;
        color: #666;
        font-size: 0.9rem;
    }
    
    /* ตกแต่ง Link ให้ดูเหมือนปุ่ม */
    .nav-button {
        display: inline-block;
        background-color: transparent;
        color: #D4AF37 !important;
        border: 1px solid #D4AF37;
        padding: 8px 20px;
        border-radius: 5px;
        text-decoration: none;
        margin: 5px;
        transition: 0.3s;
    }
    .nav-button:hover {
        background-color: #D4AF37;
        color: black !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. ส่วนเนื้อหา Hero
st.markdown("""
    <div class="hero-container">
        <h1 class="hero-title">Intelligent System Project</h1>
        <p class="hero-subtitle">Machine Learning & Neural Network Web Application</p>
        <p style="color: #666;">ยินดีต้อนรับสู่โปรเจกต์การพยากรณ์ด้วยระบบอัจฉริยะ</p>
    </div>
    """, unsafe_allow_html=True)

# 4. แบ่งคอลัมน์สำหรับ 2 โปรเจกต์หลัก
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
        <div class="category-card">
            <div class="category-icon">⚽</div>
            <h2 style="color: #D4AF37;">Football Value Prediction</h2>
            <p style="color: #BBB;">พยากรณ์ราคาตลาดนักฟุตบอลด้วยเทคนิค Ensemble Learning (Voting Regressor)</p>
        </div>
    """, unsafe_allow_html=True)
    
    # ใช้ st.page_link แทนการเขียน HTML สำหรับปุ่มเพื่อให้ระบบ Link ของ Streamlit ทำงานถูกต้อง
    st.page_link("pages/1_ML_Theory.py", label="📖 Theory (ML)", icon="📘")
    st.page_link("pages/3_ML_Prediction.py", label="👉 Go to ML Prediction", icon="⚽")

with col2:
    st.markdown("""
        <div class="category-card">
            <div class="category-icon">🍷</div>
            <h2 style="color: #D4AF37;">Wine Quality Grading</h2>
            <p style="color: #BBB;">จำแนกเกรดคุณภาพของไวน์จากสารประกอบทางเคมีด้วย Neural Network (Deep Learning)</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.page_link("pages/2_NN_Theory.py", label="📖 Theory (NN)", icon="📘")
    st.page_link("pages/4_NN_Prediction.py", label="👉 Go to NN Prediction", icon="🍷")

# 5. ส่วนท้าย (Footer)
st.markdown("---")
st.markdown("""
    <div class="footer">
        Developed for Intelligent System Project<br>
        <b>Made by วชิร ไพบูลย์เสมาทัศน์ (6704062612065) Sec.2</b>
    </div>
    """, unsafe_allow_html=True)