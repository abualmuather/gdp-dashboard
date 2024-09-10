import streamlit as st

# عنوان التطبيق
st.title("حاسبة قياسات الملاعب")

# إدخال العرض الجديد من المستخدم
new_width = st.number_input("أدخل العرض الجديد للملعب (بالمتر):", min_value=0.0, step=1.0)

# حساب القياسات وعرض النتائج فقط إذا تم إدخال العرض
if new_width:
    st.subheader("قياسات ملعب كرة اليد:")
    st.write(f"خط 9 أمتار: {0.45 * new_width} متر")
    st.write(f"خط 6 أمتار: {0.3 * new_width} متر")
    st.write(f"خط رمية الجزاء: {0.35 * new_width} متر")
    st.write(f"منطقة التبديل: {0.23 * new_width} متر")
    st.write(f"منطقة الحارس: {0.2 * new_width} متر")

    st.subheader("قياسات ملعب الكرة الطائرة:")
    st.write(f"المنطقة الأمامية: {0.3 * new_width} متر")
    st.write(f"المنطقة الخلفية: {0.6 * new_width} متر")
    st.write(f"منطقة التبديل: {0.19 * new_width} متر")