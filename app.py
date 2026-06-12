import streamlit as st

st.title("موقعي الأول من التابلت! 📱")
st.write("أهلاً بك! ده موقع حقيقي شغال على النت ومكتبوب بالبايثون بس.")

name = st.text_input("اكتب اسمك هنا:")
if name:
    st.write(f"منور الموقع يا {name}! ✨")
    
if st.button("اضغط للاحتفال"):
    st.balloons()
