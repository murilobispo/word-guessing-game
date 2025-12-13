import streamlit as st
pages = {
    "Modes":[
        st.Page("pages/one_word.py", title = "1 Word"),
        st.Page("pages/two_word.py", title = "2 Word")
    ]
    

}
pg = st.navigation(pages)

pg.run()
