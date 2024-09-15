import streamlit as st
import matplotlib.pyplot as plt

# إضافة CSS لتعديل النصوص والتنسيق بدون خلفية
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
    .slider-label {
        color: #ecf0f1; /* لون فاتح للتصنيفات */
        font-size: 1.1em;
    }
    .input-label {
        color: #ffffff; /* لون النص الأبيض */
        font-size: 1.2em;
        margin-bottom: 5px;
    }
    </style>
    """, unsafe_allow_html=True)

# عنوان التطبيق بتصميم حديث
st.markdown('<div class="title">حاسبة قياسات الملاعب المصغرة</div>', unsafe_allow_html=True)

# اختيار نوع الملعب باستخدام قائمة منسدلة
option = st.selectbox("اختر نوع الملعب:", ["كرة اليد", "الكرة الطائرة", "كرة السلة"])

# رسم الملعب بناءً على الاختيار
if option == "كرة اليد":
    st.markdown('<div class="section-header">قياسات ملعب كرة اليد المصغر</div>', unsafe_allow_html=True)
    
    # إدخال العرض الجديد للملعب
    st.markdown('<div class="input-label">أدخل العرض الجديد لملعب كرة اليد (بالمتر):</div>', unsafe_allow_html=True)
    handball_width = st.number_input("", min_value=0.0, step=0.5)

    if handball_width:
        handball_length = 2 * handball_width  # الطول القياسي لملعب كرة اليد هو ضعف العرض
        st.markdown('<div class="result-box">نتائج قياسات ملعب كرة اليد المصغر:</div>', unsafe_allow_html=True)
        st.write(f"الطول: {handball_length} متر")
        st.write(f"العرض: {handball_width} متر")

        # رسم توضيحي لملعب كرة اليد
        fig, ax = plt.subplots()
        ax.plot([0, handball_length], [0, 0], color="black", linewidth=2)  # الخط السفلي
        ax.plot([0, handball_length], [handball_width, handball_width], color="black", linewidth=2)  # الخط العلوي
        ax.plot([0, 0], [0, handball_width], color="black", linewidth=2)  # الجانب الأيسر
        ax.plot([handball_length, handball_length], [0, handball_width], color="black", linewidth=2)  # الجانب الأيمن
        ax.set_aspect(1)
        plt.title("رسم توضيحي لملعب كرة اليد")
        st.pyplot(fig)

elif option == "الكرة الطائرة":
    st.markdown('<div class="section-header">قياسات ملعب الكرة الطائرة المصغر</div>', unsafe_allow_html=True)
    
    # إدخال العرض الجديد للملعب
    st.markdown('<div class="input-label">أدخل العرض الجديد لملعب الكرة الطائرة (بالمتر):</div>', unsafe_allow_html=True)
    volleyball_width = st.number_input("", min_value=0.0, step=0.5)

    if volleyball_width:
        volleyball_length = 2 * volleyball_width  # الطول القياسي لملعب الكرة الطائرة هو ضعف العرض
        st.markdown('<div class="result-box">نتائج قياسات ملعب الكرة الطائرة المصغر:</div>', unsafe_allow_html=True)
        st.write(f"الطول: {volleyball_length} متر")
        st.write(f"العرض: {volleyball_width} متر")

        # رسم توضيحي لملعب الكرة الطائرة
        fig, ax = plt.subplots()
        ax.plot([0, volleyball_length], [0, 0], color="black", linewidth=2)  # الخط السفلي
        ax.plot([0, volleyball_length], [volleyball_width, volleyball_width], color="black", linewidth=2)  # الخط العلوي
        ax.plot([0, 0], [0, volleyball_width], color="black", linewidth=2)  # الجانب الأيسر
        ax.plot([volleyball_length, volleyball_length], [0, volleyball_width], color="black", linewidth=2)  # الجانب الأيمن
        ax.set_aspect(1)
        plt.title("رسم توضيحي لملعب الكرة الطائرة")
        st.pyplot(fig)

elif option == "كرة السلة":
    st.markdown('<div class="section-header">قياسات ملعب كرة السلة المصغر</div>', unsafe_allow_html=True)
    
    # إدخال العرض الجديد للملعب
    st.markdown('<div class="input-label">أدخل العرض الجديد لملعب كرة السلة (بالمتر):</div>', unsafe_allow_html=True)
    basketball_width = st.number_input("", min_value=0.0, step=0.5)

    if basketball_width:
        basketball_length = 1.87 * basketball_width  # نسبة الطول إلى العرض في ملعب كرة السلة
        st.markdown('<div class="result-box">نتائج قياسات ملعب كرة السلة المصغر:</div>', unsafe_allow_html=True)
        st.write(f"الطول: {basketball_length} متر")
        st.write(f"العرض: {basketball_width} متر")

        # رسم توضيحي لملعب كرة السلة
        fig, ax = plt.subplots()
        ax.plot([0, basketball_length], [0, 0], color="black", linewidth=2)  # الخط السفلي
        ax.plot([0, basketball_length], [basketball_width, basketball_width], color="black", linewidth=2)  # الخط العلوي
        ax.plot([0, 0], [0, basketball_width], color="black", linewidth=2)  # الجانب الأيسر
        ax.plot([basketball_length, basketball_length], [0, basketball_width], color="black", linewidth=2)  # الجانب الأيمن

        # دائرة المنتصف
        center_x = basketball_length / 2
        center_circle_radius = basketball_width / 6
        circle = plt.Circle((center_x, basketball_width / 2), center_circle_radius, color="black", fill=False, linewidth=2)
        ax.add_patch(circle)

        ax.set_aspect(1)
        plt.title("رسم توضيحي لملعب كرة السلة")
        st.pyplot(fig)

# إضافة اسم المعد أسفل الصفحة
st.markdown("""
    <div class="footer">
        إعداد
