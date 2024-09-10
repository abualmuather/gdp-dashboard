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
    st.write(f"خط 9 أمتار: {round(0.45 * handball_width, 3)} متر")
    st.write(f"خط 6 أمتار: {round(0.3 * handball_width, 3)} متر")
    st.write(f"خط رمية الجزاء: {round(0.35 * handball_width, 3)} متر")
    st.write(f"منطقة التبديل: {round(0.23 * handball_width, 3)} متر")
    st.write(f"منطقة الحارس: {round(0.2 * handball_width, 3)} متر")

# --- قياسات ملعب الكرة الطائرة (المعادلات المحدثة) ---
st.header("قياسات ملعب الكرة الطائرة")
volleyball_width = st.number_input("أدخل العرض الجديد لملعب الكرة الطائرة (بالمتر):", min_value=0.0, step=1.0, key="volleyball_width")

if volleyball_width:
    st.subheader("نتائج ملعب الكرة الطائرة:")
    
    # المعادلات الجديدة بناءً على البيانات المقدمة
    front_area = 0.3 * volleyball_width
    back_area = 0.6 * volleyball_width
    substitution_area_length = 0.19 * volleyball_width

    # عرض النتائج
    st.write(f"مساحة المنطقة الأمامية: {round(front_area, 3)} متر")
    st.write(f"مساحة المنطقة الخلفية: {round(back_area, 3)} متر")
    st.write(f"طول امتداد خطوط منطقة تبديل اللاعبين: {round(substitution_area_length, 3)} متر")

# --- قياسات ملعب كرة السلة ---
st.header("قياسات ملعب كرة السلة")
basketball_width = st.number_input("أدخل العرض الجديد لملعب كرة السلة (بالمتر):", min_value=0.0, step=1.0, key="basketball_width")

if basketball_width:
    st.subheader("نتائج ملعب كرة السلة (وفق المعادلات المحدثة):")
    
    # المعادلات الجديدة بناءً على البيانات المقدمة
    free​⬤