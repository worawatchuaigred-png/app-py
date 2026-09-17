import streamlit as st
import hmac
import hashlib
import json
from datetime import datetime

st.set_page_config(
    page_title="Logic Sovereign Enterprise",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
    <style>
    .main { background-color: #0e1117; color: #ffffff; }
    .stButton>button { background-color: #d4af37; color: #000000; font-weight: bold; border-radius: 8px; width: 100%; }
    .seal-box { background-color: #1a1c23; border: 1px solid #d4af37; padding: 15px; border-radius: 10px; }
    </style>
""", unsafe_allow_html=True)

st.sidebar.title("🛡️ Logic Security Hub")
st.sidebar.markdown("---")
selected_country = st.sidebar.selectbox("เลือกประเทศ (Country Scope)", ["TH (Thailand)", "SG (Singapore)", "US (United States)"])
selected_lang = st.sidebar.selectbox("เลือกภาษา (Language)", ["ไทย (TH)", "English (EN)", "中文 (ZH)"])

st.sidebar.markdown("---")
device_clean = st.sidebar.checkbox("Device Integrity (No Root/Jailbreak)", value=True)
hardware_bound = st.sidebar.checkbox("Hardware Enclave Binding Verified", value=True)
liveness_check = st.sidebar.checkbox("Anti-Spoofing Liveness Passed", value=True)

st.title("🏛️ ธุรกิจติดยศ (Logic Sovereign Enterprise)")
st.markdown("ระบบบริหารจัดการคำสั่งและนิติกรรมขั้นสูงด้วยตราประทับดิจิทัลอธิปไตย")

tab1, tab2, tab3 = st.tabs(["📊 แดชบอร์ดหลัก", "✍️ ออกคำสั่ง & ประทับตรา", "📜 สมุดบัญชีบล็อกเชน"])

with tab1:
    st.subheader("ภาพรวมสถานะระบบและกลุ่มธุรกิจ")
    col1, col2, col3 = st.columns(3)
    with col1: st.metric(label="Security Level", value="Maximum (Tier-3)", delta="Secure")
    with col2: st.metric(label="Jurisdiction", value=selected_country.split()[0], delta="Compliant")
    with col3: st.metric(label="Ledger Blocks", value="12 Blocks", delta="Synced")

with tab2:
    st.subheader("ระเบียงคำสั่งและนิติกรรมองค์กร")
    command_text = st.text_area("Command Payload", value="อนุมัติงบประมาณโครงสร้างพื้นฐานกลุ่มธุรกิจประจำไตรมาส", height=100)
    add_pua = st.checkbox("ประทับ 'ตราประทับดิจิทัลอธิปไตย' (Unicode PUA: \\uE001)", value=True)
    meet_code = st.text_input("Google Meet Room Reference", value="logic-boardroom-thailand")
    
    if st.button("🚀 ส่งคำสั่งผ่านท่อความปลอดภัย"):
        if not (device_clean and hardware_bound and liveness_check):
            st.error("❌ ระบบถูกระงับ: ตรวจพบความผิดปกติของอุปกรณ์")
        else:
            final_payload = command_text + (" \uE001" if add_pua else "")
            secret_key = "logic_global_sovereign_secure_passkey"
            generated_token = hmac.new(secret_key.encode('utf-8'), final_payload.encode('utf-8'), hashlib.sha256).hexdigest()
            st.success("✅ อนุมัติคำสั่งสำเร็จ!")
            st.json({
                "status": "APPROVED",
                "jurisdiction": selected_country,
                "final_payload": final_payload,
                "hmac_token": generated_token[:16] + "...",
                "ledger_hash": hashlib.sha256(final_payload.encode()).hexdigest()
            })

with tab3:
    st.subheader("ประวัติมติและการตรวจสอบย้อนหลัง")
    sample_ledger = [
        {"block": 0, "event": "GENESIS_BLOCK", "hash": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"},
    ]
    for item in sample_ledger:
        st.code(json.dumps(item, indent=4, ensure_ascii=False), language="json")
