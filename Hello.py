import streamlit as st
from streamlit.logger import get_logger
from streamlit_gsheets import GSheetsConnection

LOGGER = get_logger(__name__)

def run():
    st.set_page_config(
        page_title="Hello",
        page_icon="👋",
        initial_sidebar_state="collapsed" 
    )

    # Create a connection object.
    conn = st.connection("gsheets", type=GSheetsConnection)
    df = conn.read(spreadsheet = "https://docs.google.com/spreadsheets/d/1TEsfTkUdxnOjCb_z1g5M9wOyaCLQzQegVhgDSjw5aYE/edit#gid=0")
    df_comprar = df.query('temos == "nao"')
    df_temos = df.query('temos == "sim"')

    # # Print results.
    # for row in df.itertuples():
    #     st.write(f"{row.name} has a :{row.pet}:")

    st.write("# Listinha de Matheus e Brenda")
    tab1, tab2 = st.tabs(['A Comprar','Já Temos'])
    with tab1:
      for row in df_comprar.itertuples():
        st.warning(f"**{row.item}** ({row.preço}). [Abrir no navegador]({row.link})")

    with tab2:
      for row in df_temos.itertuples():
        st.success(f"**{row.item}**")

if __name__ == "__main__":
    run()
