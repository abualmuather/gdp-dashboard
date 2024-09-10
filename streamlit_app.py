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

# --- قياسات ملعب الكرة الطائرة ---
st.header("قياسات ملعب الكرة الطائرة")
volleyball_width = st.number_input("أدخل العرض الجديد لملعب الكرة الطائرة (بالمتر):", min_value=0.0, step=1.0, key="volleyball_width")

if volleyball_width:
    st.subheader("نتائج ملعب الكرة الطائرة:")
    st.write(f"المنطقة الأمامية: {round(0.3 * volleyball_width, 3)} متر")
    st.write(f"المنطقة الخلفية: {round(0.6 * volleyball_width, 3)} متر")
    st.write(f"منطقة التبديل: {round(0.19 * volleyball_width, 3)} متر")

# --- قياسات ملعب كرة السلة (المعادلات المحدثة) ---
st.header("قياسات ملعب كرة السلة")
basketball_width = st.number_input("أدخل العرض الجديد لملعب كرة السلة (بالمتر):", min_value=0.0, step=1.0, key="basketball_width")

if basketball_width:
    st.subheader("نتائج ملعب كرة السلة (وفق المعادلات المحدثة):")
    
    # المعادلات الجديدة بناءً على البيانات المقدمة
    free_throw_line = 0.386 * basketball_width
    free_throw_area_width = 0.276 * basketball_width
    three_point_line = 0.45 * basketball_width
    center_circle_diameter = 0.24 * basketball_width
    distance_to_end = 0.105 * basketball_width
    free_throw_half_circle = 0.12 * basketball_width

    # عرض النتائج
    st.write(f"طول خط الرمية الحرة: {round(free_throw_line, 3)} متر")
    st.write(f"عرض منطقة الرمية الحرة: {round(free_throw_area_width, 3)} متر")
    st.write(f"خط الثلاث نقاط: {round(three_point_line, 3)} متر")
    st.write(f"قطر دائرة المنتصف: {round(center_circle_diameter, 3)} متر")
    st.write(f"المسافة بين السلة وخط النهاية: {round(distance_to_end, 3)} متر")
    st.write(f"نصف قطر دائرة الرمية الحرة: {round(free_throw_half_circle, 3)} متر")