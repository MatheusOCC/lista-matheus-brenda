import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)

def run():
    st.set_page_config(
        page_title="Hello",
        page_icon="👋",
        initial_sidebar_state="collapsed" 
    )

    st.write("# Listinha de Matheus e Brenda")
    tab1, tab2 = st.tabs(['A Comprar','Já Temos'])
    with tab1:
      st.warning('[Nintendo Switch - 2000](https://www.amazon.com.br/Nintendo-Switch-Model-Legend-Kingdom/dp/B0BZK5M9TD/ref=asc_df_B0BZK5M9TD/?tag=googleshopp00-20&linkCode=df0&hvadid=648484803043&hvpos=&hvnetw=g&hvrand=17180737092398948441&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=1001533&hvtargid=pla-2187569339971&mcid=cd361c07374e3517a6961f1980b8e0c4&th=1)')
    with tab2:
      st.success('b')

if __name__ == "__main__":
    run()
