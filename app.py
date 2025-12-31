import streamlit as st
import time

# Lovely 3D Gemini-style configuration
st.set_page_config(page_title="ASTRA-AI", page_icon="✨")

st.markdown("""
    <style>
    .stApp { background: linear-gradient(to bottom, #000428, #004e92); color: white; }
    .stChatMessage { background: rgba(255,255,255,0.1); border-radius: 15px; border: 1px solid #00d2ff; }
    </style>
    """, unsafe_allow_html=True)

# THE SCHOOL DATABASE
data = {
    "name": "Pragyan Public School, Jewar",
    "principal": "Mrs. Deepti Sharma",
    "timings": "Summer: 7:50 AM - 2:10 PM | Winter: 8:20 AM - 2:20 PM",
    "fees": "Admission Fee: ₹5500-₹6500. Annual Composite Fee starts from ~₹29,800.",
    "admission": "Admission is based on written and aptitude tests for Class I and above.",
    "mobile": "Strictly prohibited. Confiscated phones require a ₹1000 fine for early return."
}

st.title("🚀 ASTRA-AI PRO")
st.write(f"Official Intelligence for **{data['name']}**")

if "messages" not in st.session_state:
    st.session_state.messages = []

for m in st.session_state.messages:
    with st.chat_message(m["role"]): st.markdown(m["content"])

if p := st.chat_input("Ask me about the school..."):
    st.session_state.messages.append({"role": "user", "content": p})
    with st.chat_message("user"): st.markdown(p)
    
    with st.chat_message("assistant"):
        q = p.lower()
        # Smarter Logic to catch more questions
        if "name" in q or "which school" in q:
            ans = f"This is the official bot for **{data['name']}**."
        elif "principal" in q or "head" in q:
            ans = f"The Principal of Pragyan Public School is **{data['principal']}**."
        elif "time" in q or "hours" in q:
            ans = f"School Hours: {data['timings']}"
        elif "fee" in q:
            ans = f"Fee Details: {data['fees']}"
        elif "admission" in q:
            ans = f"Admission Policy: {data['admission']}"
        elif "mobile" in q or "phone" in q:
            ans = f"Mobile Rules: {data['mobile']}"
        else:
            ans = "I am ASTRA-AI. Ask me about the School Name, Principal, Fees, or Timings!"
        
        # Typing animation effect
        res = ""
        placeholder = st.empty()
        for word in ans.split():
            res += word + " "
            time.sleep(0.1)
            placeholder.markdown(res)
    st.session_state.messages.append({"role": "assistant", "content": ans})