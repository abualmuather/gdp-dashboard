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

# --- قياسات ملعب كرة السلة ---
st.header("قياسات ملعب كرة السلة")
basketball_width = st.number_input("أدخل العرض الجديد لملعب كرة السلة (بالمتر):", min_value=0.0, step=1.0, key="basketball_width")

if basketball_width:
    st.subheader("نتائج ملعب كرة السلة:")
    st.write(f"طول خط الرمية الحرة: {0.386 * basketball_width + 5.80} متر")
    st.write(f"عرض منطقة الرمية الحرة: {0.276 * basketball_width + 4.15} متر")
    st.write(f"خط الثلاث نقاط: {0.45 * basketball_width + 6.75} متر")
    st.write(f"دائرة المنتصف: {0.24 * basketball_width + 3.6} متر")
    st.write(f"المسافة من السلة إلى منتصف الملعب: {0.105 * basketball_width + 15.575} متر")
    st.write(f"نصف دائرة الرمية الحرة: {0.12 * basketball_width + 1.8} متر")