import streamlit as st

def contacts():

    st.markdown("##### Contact/Connect/Follow me")

    c1, c2, c3, c4, c5, c6 = st.columns(6)

    c1.markdown("""[<img align="left" alt="linked-in" src="https://img.shields.io/badge/linkedin-%230077B5.svg?&style=for-the-badge&logo=linkedin&logoColor=white" />](https://www.linkedin.com/in/gaspard-nzasabimfura/)""", unsafe_allow_html=True)

    #     c2.markdown("""[<img align="left" alt="facebook" src="https://img.shields.io/badge/facebook-%231877F2.svg?&style=for-the-badge&logo=facebook&logoColor=white" />](https://www.facebook.com/nzasabimana.gaspard/)""", unsafe_allow_html=True)

    c2.markdown("""[<img align="left" alt="twitter" src="https://img.shields.io/badge/twitter-%231DA1F2.svg?&style=for-the-badge&logo=twitter&logoColor=white" />](https://twitter.com/nzagaspard)""", unsafe_allow_html=True)

    c3.markdown("""[<img align="left" alt="telegram" src="https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white" />](https://t.me/nzagaspard)""", unsafe_allow_html=True)

    c4.markdown("""[<img align="left" alt="whatsapp" src="https://img.shields.io/badge/WhatsApp-25D366?style=for-the-badge&logo=whatsapp&logoColor=white" />](https://wa.me/250722882193)""", unsafe_allow_html=True)

    c5.markdown("""[<img align="left" alt="linked-in" src="https://img.shields.io/badge/website-000000?style=for-the-badge&logo=About.me&logoColor=white" />](https://nzagaspard.github.io/)""", unsafe_allow_html=True)

    c6.markdown("""[<img align="left" alt="linked-in" src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white"  />](https://github.com/nzagaspard)""", unsafe_allow_html=True)