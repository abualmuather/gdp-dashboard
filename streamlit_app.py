import streamlit as st

# إضافة CSS لجعل الكتابة من اليمين إلى اليسار
st.markdown("""
    <style>
    body {
        direction: rtl;
        text-align: right;
    }
    </style>
    """, unsafe_allow_html=True)

# عنوان التطبيق
st.title("حاسبة قياسات الملاعب")

# --- قياسات ملعب كرة اليد ---
st.header("قياسات ملعب كرة اليد")
handball_width = st.number_input("أدخل العرض الجديد لملعب كرة اليد (بالمتر):", min_value=0.0, step=1.0, key="handball_width")

if handball_width:
    st.subheader("نتائج ملعب كرة اليد:")
    st.write(f"خط 9 أمتار: {0.45 * handball_width} متر")
    st.write(f"خط 6 أمتار: {0.3 * handball_width} متر")
    st.write(f"خط رمية الجزاء: {0.35 * handball_width} متر")
    st.write(f"منطقة التبديل: {0.23 * handball_width} متر")
    st.write(f"منطقة الحارس: {0.2 * handball_width} متر")

# --- قياسات ملعب الكرة الطائرة ---
st.header("قياسات ملعب الكرة الطائرة")
volleyball_width = st.number_input("أدخل العرض الجديد لملعب الكرة الطائرة (بالمتر):", min_value=0.0, step=1.0, key="volleyball_width")

if volleyball_width:
    st.subheader("نتائج ملعب الكرة الطائرة:")
    st.write(f"المنطقة الأمامية: {0.3 * volleyball_width} متر")
    st.write(f"المنطقة الخلفية: {0.6 * volleyball_width} متر")
    st.write(f"منطقة التبديل: {0.19 * volleyball_width} متر")