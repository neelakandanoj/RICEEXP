import streamlit as st
import pandas as pd
import plotly.express as px

import streamlit_option_menu
st.set_page_config(layout="wide", page_title="Rice exports data analysis" )
# Title
st.title(":red[Rice exports data analysis:]")
selected=streamlit_option_menu.option_menu(None,["About",  "Data Explore"],
                                           icons=["exclamation-circle","search","globe",],
                                           menu_icon="cast",
                                           default_index=0,
                                           orientation="horizontal",
                                           styles={"nav-link": {"font-size": "15px", "text-align": "centre",
                                                                "--hover-color": "#d1798e"},
                                                   "nav-link-selected": {"background-color": "#b30e35"},"width":"100%"},)


if selected=="About":
    st.header("""
Technologies: Data Cleansing, EDA, Visualization,PowerBI/Tableau/Streamlit\n
Domain: Fast Moving Consumer Goods
""")
    st.write("""Problem Statement:\n
    The comprehensive dataset contains detailed information about rice exports from various exporters from all over the world.\n
    The dataset encompasses essential attributes such as importer/exporter names, addresses, quantities, values, and other pertinent details.\n
    Goal is to conduct an extensive data analysis to extract meaningful insights and address key questions regarding the rice export transactions. """)

if selected=="Data Explore":
    data=pd.read_csv(r'/content/Data.csv')
    tab1, tab2=st.tabs(["Importer/Exporter Overview","Geographical Analysis"])
    with tab1:
        data.sort_values(by='IMPORT VALUE CIF', ascending=False, inplace=True)
        df = data.head(30)
        tab1_1, tab1_2=st.tabs(["Importer Insights", "Exporter Insights"])
        with tab1_1:
            image=px.bar(data_frame=df,x='IMPORTER NAME', y='IMPORT VALUE CIF',color="IMPORT VALUE CIF", barmode="stack")
            st.header(":green[Top Importers:]")
            st.plotly_chart(image, use_container_width=True)


        with tab1_2:
            df = data.head(10)
            image = px.bar(data_frame=df, x='EXPORTER NAME', y='IMPORT VALUE CIF', color="IMPORT VALUE CIF", barmode="stack")
            st.header(":green[Top Exporters:]")
            st.plotly_chart(image, use_container_width=True)

    with tab2:
        location = px.choropleth(data_frame=data,
                                 locations='IMPORTER COUNTRY',
                                 color='IMPORTER COUNTRY',
                                 hover_data={'HS CODE DESCRIPTION': True, 'IMPORTER NAME':True, 'EXPORTER NAME':True, 'IMPORTER COUNTRY': True, "IMPORT VALUE CIF":True, "IMPORT VALUE FOB":True, },
                                 locationmode='country names')
        st.header(":orange[Geo Visualization Rice Exports Data:]")
        location.update_layout(autosize=False, margin=dict(l=10, r=0, b=20, t=20, pad=9, autoexpand=True),
                               width=1000, )

        st.plotly_chart(location, use_container_width=True)

        col1, col2= st.columns([1,1])
        with col1:
            location = px.choropleth(data_frame=data,
                                     locations='IMPORTER COUNTRY',
                                     color='PORT OF ARRIVAL',
                                     hover_data={'PORT OF ARRIVAL': True, 'PORT OF DEPARTURE': True, "PRODUCT DETAILS":True },
                                     locationmode='country names')
            st.header(":green[Geo Visualization Port of Arrival:]")
            location.update_layout(autosize=False, margin=dict(l=10, r=0, b=20, t=20, pad=9, autoexpand=True),
                                   width=1000, )
            st.plotly_chart(location, use_container_width=True)
        with col2:
            location = px.choropleth(data_frame=data,
                                     locations='COUNTRY OF ORIGIN',
                                     color='COUNTRY OF ORIGIN',
                                     hover_data={'PORT OF ARRIVAL': True, 'PORT OF DEPARTURE': True,
                                                 "PRODUCT DETAILS": True},
                                     locationmode='country names')
            st.header(":violet[Geo Visualization Country of Orgin:]")
            location.update_layout(autosize=False, margin=dict(l=10, r=0, b=20, t=20, pad=9, autoexpand=True),
                                   width=1000, )
            st.plotly_chart(location, use_container_width=True)
