import streamlit as st
import matplotlib.pyplot as plt

# إضافة CSS لتعديل النصوص والتنسيق
st.markdown("""
    <style>
    .stApp {
        background-color: #2c3e50;
        font-family: 'Arial', sans-serif;
        color: #f5f5f5;
    }
    </style>
    """, unsafe_allow_html=True)

# اختيار نوع الملعب باستخدام قائمة منسدلة
option = st.selectbox("اختر نوع الملعب:", ["كرة القدم", "كرة اليد", "الكرة الطائرة", "كرة السلة"])

# إعداد رسم تخطيطي للملعب بناءً على الاختيار
if option == "كرة القدم":
    st.markdown("## رسم تخطيطي لملعب كرة القدم")
    
    # رسم ملعب كرة القدم
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # رسم خطوط الملعب الأساسية
    football_length = 100  # الطول
    football_width = 64    # العرض
    penalty_area_length = 16.5
    penalty_area_width = 40.3
    goal_area_length = 5.5
    goal_area_width = 18.32
    center_circle_radius = 9.15
    
    # رسم الخطوط الخارجية
    ax.plot([0, football_length], [0, 0], color="white")
    ax.plot([0, football_length], [football_width, football_width], color="white")
    ax.plot([0, 0], [0, football_width], color="white")
    ax.plot([football_length, football_length], [0, football_width], color="white")
    
    # منطقة الجزاء
    ax.plot([16.5, 16.5], [(football_width - penalty_area_width) / 2, (football_width + penalty_area_width) / 2], color="white")
    ax.plot([football_length - 16.5, football_length - 16.5], [(football_width - penalty_area_width) / 2, (football_width + penalty_area_width) / 2], color="white")
    
    # منطقة المرمى
    ax.plot([5.5, 5.5], [(football_width - goal_area_width) / 2, (football_width + goal_area_width) / 2], color="white")
    ax.plot([football_length - 5.5, football_length - 5.5], [(football_width - goal_area_width) / 2, (football_width + goal_area_width) / 2], color="white")
    
    # دائرة المنتصف
    center_circle = plt.Circle((football_length / 2, football_width / 2), center_circle_radius, color="white", fill=False)
    ax.add_artist(center_circle)
    
    # إعداد الملعب
    ax.set_facecolor("#2c3e50")
    ax.set_xlim(0, football_length)
    ax.set_ylim(0, football_width)
    ax.set_aspect('equal', 'box')
    ax.set_xticks([])
    ax.set_yticks([])

    # تقسيم الصفحة بين الرسم التخطيطي والقياسات
    col1, col2 = st.columns(2)

    with col1:
        st.pyplot(fig)
    
    with col2:
        st.markdown("### القياسات:")
        st.write(f"طول الملعب: {football_length} متر")
        st.write(f"عرض الملعب: {football_width} متر")
        st.write(f"منطقة الجزاء: {penalty_area_length} متر (العمق) × {penalty_area_width} متر (العرض)")
        st.write(f"منطقة المرمى: {goal_area_length} متر (العمق) × {goal_area_width} متر (العرض)")
        st.write(f"قطر دائرة المنتصف: {center_circle_radius * 2} متر")

elif option == "كرة اليد":
    st.markdown("## رسم تخطيطي لملعب كرة اليد")
    
    # رسم ملعب كرة اليد
    fig, ax = plt.subplots(figsize=(8, 5))
    
    # الطول والعرض الافتراضي لملعب كرة اليد
    handball_length = 40
    handball_width = 20
    goal_area_length = 6
    goal_area_width = 7
    
    # رسم الخطوط الخارجية
    ax.plot([0, handball_length], [0, 0], color="white")
    ax.plot([0, handball_length], [handball_width, handball_width], color="white")
    ax.plot([0, 0], [0, handball_width], color="white")
    ax.plot([handball_length, handball_length], [0, handball_width], color="white")
    
    # منطقة المرمى
    ax.plot([6, 6], [(handball_width - goal_area_width) / 2, (handball_width + goal_area_width) / 2], color="white")
    ax.plot([handball_length - 6, handball_length - 6], [(handball_width - goal_area_width) / 2, (handball_width + goal_area_width) / 2], color="white")
    
    # إعداد الملعب
    ax.set_facecolor("#2c3e50")
    ax.set_xlim(0, handball_length)
    ax.set_ylim(0, handball_width)
    ax.set_aspect('equal', 'box')
    ax.set_xticks([])
    ax.set_yticks([])

    # تقسيم الصفحة بين الرسم التخطيطي والقياسات
    col1, col2 = st.columns(2)

    with col1:
        st.pyplot(fig)
    
    with col2:
        st.markdown("### القياسات:")
        st.write(f"طول الملعب: {handball_length} متر")
        st.write(f"عرض الملعب: {handball_width} متر")
        st.write(f"منطقة المرمى: {goal_area_length} متر (العمق) × {goal_area_width} متر (العرض)")

elif option == "الكرة الطائرة":
    st.markdown("## رسم تخطيطي لملعب الكرة الطائرة")
    
    # رسم ملعب الكرة الطائرة
    fig, ax = plt.subplots(figsize=(9, 6))
    
    # الطول والعرض الافتراضي لملعب الكرة الطائرة
    volleyball_length = 18
    volleyball_width = 9
    
    # رسم الخطوط الخارجية
    ax.plot([0, volleyball_length], [0, 0], color="white")
    ax.plot([0, volleyball_length], [volleyball_width, volleyball_width], color="white")
    ax.plot([0, 0], [0, volleyball_width], color="white")
    ax.plot([volleyball_length, volleyball_length], [0, volleyball_width], color="white")
    
    # رسم خط الوسط
    ax.plot([volleyball_length / 2, volleyball_length / 2], [0, volleyball_width], color="white")
    
    # إعداد الملعب
    ax.set_facecolor("#2c3e50")
    ax.set_xlim(0, volleyball_length)
    ax.set_ylim(0, volleyball_width)
    ax.set_aspect('equal', 'box')
    ax.set_xticks([])
    ax.set_yticks([])

    # تقسيم الصفحة بين الرسم التخطيطي والقياسات
    col1, col2 = st.columns(2)

    with col1:
        st.pyplot(fig)
    
    with col2:
        st.markdown("### القياسات:")
        st.write(f"طول الملعب: {volleyball_length} متر")
        st.write(f"عرض الملعب: {volleyball_width} متر")

elif option == "كرة السلة":
    st.markdown("## رسم تخطيطي لملعب كرة السلة")
    
    # رسم ملعب كرة السلة
    fig, ax = plt.subplots(figsize=(8, 5))
    
    # الطول والعرض الافتراضي لملعب كرة السلة
    basketball_length = 28
    basketball_width = 15
    
    # رسم الخطوط الخارجية
    ax.plot([0, basketball_length], [0, 0], color="white")
    ax.plot([0, basketball_length], [basketball_width, basketball_width], color="white")
    ax.plot([0, 0], [0, basketball_width], color="white")
    ax.plot([basketball_length, basketball_length], [0, basketball_width], color="white")
    
    # رسم خط الوسط ودائرة المنتصف
    ax.plot([basketball_length / 2, basketball_length / 2], [0, basketball_width], color="white")
    center_circle = plt.Circle((basketball_length / 2, basketball_width / 2), 1.8, color="white", fill=False)
    ax.add_artist(center_circle)
    
    # إعداد الملعب
    ax.set_facecolor("#2c3e50")
    ax.set_xlim(0, basketball_length)
    ax.set_ylim(0, basketball_width)
    ax.set_aspect('equal', 'box')
    ax.set_xticks([])
    ax.set_yticks([])

    # تقسيم الصفحة بين الرسم التخطيطي والقياسات
    col1, col2 = st.columns(2)

    with col1:
        st.pyplot(fig)
    
    with col2:
        st.markdown("### القياسات:")
        st.write(f"طول الملعب: {basketball_length} متر")
        st.write(f"عرض الملعب: {basketball_width} متر")
        st.write(f"قطر دائرة المنتصف: {1.8 * 2} متر")
