import streamlit as st

# إضافة CSS لتخصيص الألوان بدون خلفية
st.markdown("""
    <style>
    .stApp {
        background-color: #2c3e50; /* لون الخلفية الداكن */
        font-family: 'Arial', sans-serif;
        color: #f5f5f5; /* لون الخط العام */
    }
    body {
        direction: rtl;
        text-align: right;
    }
    .title {
        text-align: center;
        background-color: #2c3e50; /* خلفية داكنة مع لون هادئ */
        padding: 15px;
        border-radius: 10px;
        font-size: 2.2em;
        font-weight: bold;
        color: #ecf0f1; /* لون النص الأبيض المائل للرمادي */
        box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.3); /* ظل خفيف */
    }
    .section-header {
        background-color: #34495e; /* لون هادئ للأقسام */
        padding: 10px;
        border-radius: 8px;
        font-size: 1.4em;
        font-weight: bold;
        color: #ecf0f1;
        margin-top: 20px;
        box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2);
    }
    .result-box {
        background-color: rgba(255, 255, 255, 0.1); /* خلفية شفافة قليلاً */
        padding: 15px;
        border-radius: 10px;
        font-size: 1.2em;
        color: #ecf0f1; /* نص فاتح */
        margin-bottom: 15px;
        box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
    }
    .footer {
        margin-top: 50px;
        text-align: center;
        color: #ecf0f1;
        font-size: 1em;
        padding: 10px;
        background-color: #2c3e50;
        border-radius: 15px;
        box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.3);
    }
    .button {
        background-color: #2980b9; /* لون أزرق عصري */
        color: white;
        padding: 10px 20px;
        border: none;
        border-radius: 10px;
        font-size: 1.1em;
        cursor: pointer;
        box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2);
        transition: background-color 0.3s;
    }
    .button:hover {
        background-color: #3498db; /* لون أزرق أفتح عند التمرير */
    }
    .label-text {
        color: #ffffff; /* لون النص الأبيض */
        font-size: 1.2em;
        margin-bottom: 5px;
    }
    </style>
    """, unsafe_allow_html=True)

# عنوان التطبيق بتصميم حديث
st.markdown('<div class="title">حاسبة قياسات الملاعب المصغرة</div>', unsafe_allow_html=True)

# استخدام اختيار المستخدم لعرض الملعب المناسب مع إدخال يدوي
if True:  # يمكن استبدال True بشرط لاختيار الملعب
    st.markdown('<div class="section-header">قياسات ملعب كرة اليد المصغر</div>', unsafe_allow_html=True)
    
    # نص العبارة بتنسيق مخصص
    st.markdown('<div class="label-text">أدخل العرض الجديد لملعب كرة اليد (بالمتر):</div>', unsafe_allow_html=True)
    
    # إدخال العرض الجديد
    handball_width = st.number_input("", min_value=0.0, step=0.5)

    if handball_width:
        st.markdown('<div class="result-box">نتائج قياسات ملعب كرة اليد المصغر:</div>', unsafe_allow_html=True)
        st.write(f"خط 9 أمتار: {round(0.45 * handball_width, 3)} متر")
        st.write(f"خط 6 أمتار: {round(0.3 * handball_width, 3)} متر")
        st.write(f"خط رمية الجزاء: {round(0.35 * handball_width, 3)} متر")
        st.write(f"منطقة التبديل: {round(0.23 * handball_width, 3)} متر")
        st.write(f"منطقة الحارس: {round(0.2 * handball_width, 3)} متر")

# إضافة اسم المعد أسفل الصفحة
st.markdown("""
    <div class="footer">
        إعداد: أسعد الخصيبي - مشرف الرياضة المدرسية
    </div>
    """, unsafe_allow_html=True)
