import streamlit as st
from streamlit.logger import get_logger
from streamlit_gsheets import GSheetsConnection

LOGGER = get_logger(__name__)


# Create a connection object.
conn = st.connection("gsheets", type=GSheetsConnection)

df = conn.read()


def run():
    st.set_page_config(
        page_title="Hello",
        page_icon="👋",
        initial_sidebar_state="collapsed" 
    )
    
    # Print results.
    for row in df.itertuples():
        st.write(f"{row.name} has a :{row.pet}:")

    st.write("# Listinha de Matheus e Brenda")
    tab1, tab2 = st.tabs(['A Comprar','Já Temos'])
    with tab1:
      st.warning('[Nintendo Switch - 2000](https://www.amazon.com.br/Nintendo-Switch-Model-Legend-Kingdom/dp/B0BZK5M9TD/ref=asc_df_B0BZK5M9TD/?tag=googleshopp00-20&linkCode=df0&hvadid=648484803043&hvpos=&hvnetw=g&hvrand=17180737092398948441&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=1001533&hvtargid=pla-2187569339971&mcid=cd361c07374e3517a6961f1980b8e0c4&th=1)')
      st.warning('[Televisão 40"](https://www.amazon.com.br/Samsung-Smart-Crystal-UHD-CU7700/dp/B0C1538ZJ4/ref=sr_1_3?qid=1700441101&refinements=p_n_size_browse-bin%3A17247918011%2Cp_89%3ASAMSUNG&rnid=18120432011&s=electronics&sr=1-3&ufe=app_do%3Aamzn1.fos.25548f35-0de7-44b3-b28e-0f56f3f96147)')
    with tab2:
      st.success('b')

if __name__ == "__main__":
    run()
