import streamlit as st
import time

# --- 1. PAGE CONFIGURATION & "GLASS" THEME ---
st.set_page_config(page_title="ASTRA-AI: The Pragyan Universe", page_icon="💠", layout="wide")

st.markdown("""
    <style>
    /* MAIN BACKGROUND */
    .stApp {
        background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
        color: #e0e0e0;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    
    /* CHAT BUBBLES - GLASSMORPHISM */
    .stChatMessage {
        background: rgba(255, 255, 255, 0.05);
        border-radius: 15px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);
        backdrop-filter: blur(5px);
        margin-bottom: 10px;
    }
    
    /* HEADERS */
    h1 {
        background: -webkit-linear-gradient(#00d2ff, #3a7bd5);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        font-weight: bold;
    }
    h3 { color: #00d2ff !important; }
    
    /* INPUT BOX */
    .stChatInputContainer {
        padding-bottom: 20px;
        background: transparent !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. THE MASTER DATABASE (A-to-Z) ---
pragyan_universe = {
    "PPS_JEWAR": {
        "name": "Pragyan Public School, Jewar",
        "affiliation": "CBSE Affiliation No. 2130833 | School Code: 60381",
        "principal": "Mrs. Deepti Sharma (M.Sc., M.Ed., M.C.A., M.Phil.)",
        "manager": "Sh. Harish Kumar Sharma",
        "website": "https://www.pragyanpublicschool.com/",
        "timings": {
            "summer": "07:50 AM to 02:10 PM",
            "winter": "08:20 AM to 02:20 PM",
            "visiting_hours": "09:00 AM to 11:00 AM (Principal Meeting)"
        },
        "fees_2025": {
            "admission": "₹5500 - ₹6500 (One time)",
            "annual_composite": "Ranges from ₹29,800 (Class I) to ₹43,600+ (Class XII Science).",
            "exam_fee": "Included in composite fee (except Board Fees).",
            "payment_mode": "Online via School App / Website or Bank Draft."
        },
        "rules": {
            "mobile": "STRICTLY PROHIBITED. If caught, phone is confiscated. Return requires a ₹1000 fine.",
            "attendance": "75% attendance is compulsory to appear in Final Exams.",
            "late_arrival": "Students arriving late will be sent back home.",
            "uniform": "Must be neat and clean. Improper uniform is not allowed."
        },
        "infrastructure": "Atal Tinkering Lab (ATL - Top 10 in UP), Digital Smart Classes, Physics/Chem/Bio Labs, Library with 10,000+ books.",
        "results": "Consistent 100% Board Results. District Toppers in 2023-24. Awarded 'Best School in Greater Noida' by TimesNow."
    },
    
    "PIS": {
        "name": "Pragyan International School (PIS)",
        "tagline": "Developing Neoteric Innovators",
        "website": "https://www.pragyaninternational.com/",
        "features": "Global Curriculum, Foreign Languages (German/French), AC Transport with GPS, Horse Riding, Shooting Range.",
        "vision": "To create global citizens with critical thinking and life skills."
    },
    
    "RK_ACADEMY": {
        "name": "RK Academy Pragyan",
        "tagline": "Tamso Ma Jyotirgamaya",
        "website": "https://rkacademypragyan.in/",
        "philosophy": "Blending modern education with deep-rooted Indian values and moral character building.",
        "focus": "Personalized attention, remedial classes, and holistic development."
    }
}

# --- 3. UI LAYOUT ---
st.title("💠 ASTRA-AI PRO")
st.markdown("<p style='text-align: center;'>The Unified Intelligence for <b>PPS Jewar</b>, <b>PIS</b>, and <b>RK Academy</b></p>", unsafe_allow_html=True)
st.divider()

# --- 4. CHAT LOGIC ---
if "messages" not in st.session_state:
    st.session_state.messages = [{
        "role": "assistant", 
        "content": "Hello! I am the **Master AI** for the Pragyan Group. I have full details on:\n\n1. **PPS Jewar** (Fees, Rules, Results)\n2. **Pragyan International** (PIS)\n3. **RK Academy**\n\nAsk me anything! Example: *'What is the mobile fine?'* or *'Tell me about PIS facilities'*."
    }]

for m in st.session_state.messages:
    with st.chat_message(m["role"]): st.markdown(m["content"])

if prompt := st.chat_input("Ask about fees, timings, principal, or branches..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"): st.markdown(prompt)

    with st.chat_message("assistant"):
        q = prompt.lower()
        response = ""
        
        # --- BRANCH 1: PPS JEWAR DETAILED QUERIES ---
        if any(x in q for x in ["jewar", "pps", "main branch", "public school"]):
            if "principal" in q:
                response = f"**Principal:** {pragyan_universe['PPS_JEWAR']['principal']}\n\n**Manager:** {pragyan_universe['PPS_JEWAR']['manager']}"
            elif "fee" in q:
                response = f"**Fee Structure (2025-26):**\n- Admission: {pragyan_universe['PPS_JEWAR']['fees_2025']['admission']}\n- Annual: {pragyan_universe['PPS_JEWAR']['fees_2025']['annual_composite']}\n- Mode: {pragyan_universe['PPS_JEWAR']['fees_2025']['payment_mode']}"
            elif "rule" in q or "mobile" in q:
                response = f"**School Rules:**\n- 📱 **Mobile:** {pragyan_universe['PPS_JEWAR']['rules']['mobile']}\n- ⏰ **Late:** {pragyan_universe['PPS_JEWAR']['rules']['late_arrival']}"
            else:
                response = f"**{pragyan_universe['PPS_JEWAR']['name']}**\nAffiliation: {pragyan_universe['PPS_JEWAR']['affiliation']}\nWebsite: {pragyan_universe['PPS_JEWAR']['website']}"

        # --- BRANCH 2: PIS ---
        elif any(x in q for x in ["pis", "international", "german", "french"]):
            response = f"**{pragyan_universe['PIS']['name']}**\n\n🌟 **Features:** {pragyan_universe['PIS']['features']}\n🎯 **Vision:** {pragyan_universe['PIS']['vision']}\n🔗 **Link:** {pragyan_universe['PIS']['website']}"

        # --- BRANCH 3: RK ACADEMY ---
        elif any(x in q for x in ["rk", "academy", "radha"]):
            response = f"**{pragyan_universe['RK_ACADEMY']['name']}**\n\n📜 **Philosophy:** {pragyan_universe['RK_ACADEMY']['philosophy']}\n🔗 **Link:** {pragyan_universe['RK_ACADEMY']['website']}"

        # --- UNIVERSAL TOPICS (Fees, Timing, Principal) ---
        elif "principal" in q:
            response = f"The Principal of the main branch (PPS Jewar) is **{pragyan_universe['PPS_JEWAR']['principal']}**."
        
        elif "time" in q or "timing" in q or "open" in q:
            response = f"**PPS Jewar Timings:**\n☀️ Summer: {pragyan_universe['PPS_JEWAR']['timings']['summer']}\n❄️ Winter: {pragyan_universe['PPS_JEWAR']['timings']['winter']}\n🤝 Visiting: {pragyan_universe['PPS_JEWAR']['timings']['visiting_hours']}"
            
        elif "fee" in q or "money" in q:
            response = f"**Fee Info (PPS Jewar):**\n{pragyan_universe['PPS_JEWAR']['fees_2025']['annual_composite']}\n(Fees for PIS and RK Academy may vary, please check their websites)."

        elif "mobile" in q or "fine" in q:
             response = f"⚠️ **Mobile Policy:** {pragyan_universe['PPS_JEWAR']['rules']['mobile']} (Applies strictly to PPS Jewar)."

        elif "result" in q or "topper" in q:
            response = f"🏆 **Achievements:** {pragyan_universe['PPS_JEWAR']['results']}"
            
        elif "facility" in q or "lab" in q:
            response = f"**Infrastructure:** {pragyan_universe['PPS_JEWAR']['infrastructure']}"

        # --- DEFAULT GREETING ---
        else:
            response = "I am the **Pragyan Universe AI**. I have data on:\n- **PPS Jewar** (Main CBSE Branch)\n- **Pragyan International** (PIS)\n- **RK Academy**\n\nTry asking: *'Who is the principal?', 'School timings?', or 'Tell me about PIS'.*"

        # --- TYPING EFFECT ---
        res_box = st.empty()
        curr_text = ""
        for char in response:
            curr_text += char
            res_box.markdown(curr_text)
            time.sleep(0.005) # Faster typing for long text
            
    st.session_state.messages.append({"role": "assistant", "content": response})
