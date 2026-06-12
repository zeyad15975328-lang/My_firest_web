import string
import random
import streamlit as st

# 1. عنوان الموقع والترحيب بشاشات شيك
st.title("✨ نظام إنشاء الحسابات الذكي ✨")

st.markdown("""
### ──── ୨୧ ────
### 𝐖𝐄𝐋𝐂𝐎𝐌𝐄✿ ᭄⸙
### ──── ୨୧ ────
""")

# 2. إدخال الاسم الرباعي
name = st.text_input("Please, enter your quadruple name or more:")
if name:
    if len(name.split()) < 4:
        st.warning("⚠️ Please, enter your quadruple name (at least 4 words).")
    else:
        st.success("✅ Name accepted!")

# 3. إدخال السن
age1 = st.number_input("Please, enter your age:", min_value=0, value=0, step=1)
if age1 > 0:
    if age1 < 5:
        st.error("❌ Sorry. Age must be above 5 years.")
    else:
        st.success("✅ Age accepted!")

# 4. إدخال الإيميل
email1 = st.text_input("Please, enter your email:")
if email1:
    if "@gmail.com" not in email1:
        st.warning("⚠️ You forgot ( @gmail.com ) or email is invalid.")
    else:
        st.success("✅ Email accepted!")

# 5. اقتراح الباسوورد
suggestion = st.radio("Do you want to create a password for you?", ("No", "Yes"))

letters = string.ascii_letters
numbers = string.digits
punctuations = string.punctuation
total1 = letters + numbers + punctuations

if suggestion == "Yes":
    # توليد باسوورد مقترح وحفظه في الـ Session عشان ميتغيرش كل ثانية
    if "suggested_pass" not in st.session_state:
        password1_suggestion = random.choices(total1, k=8)
        st.session_state.suggested_pass = "".join(password1_suggestion)
    
    st.info(f"💡 Suggested password is: **{st.session_state.suggested_pass}**")

# 6. إدخال الباسوورد وتأكيده
password1 = st.text_input("Please, enter your password:", type="password")
confirmed_password = st.text_input("Please, confirm the password:", type="password")

# 7. زرار حفظ وتفعيل الحساب
if st.button("Create Account 🚀"):
    # التحقق من كل الشروط قبل إنشاء الحساب
    if not name or len(name.split()) < 4:
        st.error("Please fix your name first.")
    elif age1 < 5:
        st.error("Please fix your age first.")
    elif not email1 or "@gmail.com" not in email1:
        st.error("Please fix your email first.")
    elif len(password1) < 8:
        st.error("The length of the password must be at least 8 characters.")
    elif password1 != confirmed_password:
        st.error("The password must match the confirmation password.")
    else:
        # لو كله تمام ينشئ الحساب
        user_info = {
            "username": name,
            "Age": age1,
            "email": email1,
            "password": password1
        }
        st.balloons()
        st.success("🎉 Your account has been successfully created!")
        st.write(f"**Your Account Email is:** {user_info['email']}")
