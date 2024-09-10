import streamlit as st
import pandas as pd

# عنوان التطبيق
st.title("Field Measurement Calculator")

# إدخال العرض الجديد من المستخدم
new_width = st.number_input("Enter the new width of the field (in meters):", min_value=0.0, step=1.0)

# حساب القياسات وعرض النتائج فقط إذا تم إدخال العرض
if new_width:
    st.subheader("Handball Field Measurements:")
    st.write(f"9-meter line: {0.45 * new_width} meters")
    st.write(f"6-meter line: {0.3 * new_width} meters")
    st.write(f"Penalty throw line: {0.35 * new_width} meters")
    st.write(f"Substitution area: {0.23 * new_width} meters")
    st.write(f"Goalkeeper area: {0.2 * new_width} meters")

    st.subheader("Volleyball Field Measurements:")
    st.write(f"Front area: {0.3 * new_width} meters")
    st.write(f"Back area: {0.6 * new_width} meters")
    st.write(f"Substitution area: {0.19 * new_width} meters")