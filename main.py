import pandas as pd
import streamlit as st
import altair as alt
from PIL import Image

st.set_page_config(page_title='BioInformatics DNA App', page_icon='🧬', layout='centered', initial_sidebar_state='auto')
st.markdown('<style>body{background-color: #fff00;}</style>',unsafe_allow_html=True)

st.markdown("<hr><h1 style='text-align: center; color: black;'>🧬 DNA Nucleotide Count Web App 🇮🇳 </h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: black;'>This app counts the nucleotide composition of query DNA!</h3><hr>", unsafe_allow_html=True)

st.header('Enter 🧬 sequence :smile:')

sequence_input = ">DNA Query \nGAACACGTGGAGGCAAACAGGAAGGTGAAGAAGAACTTATCCTATCAGGACGGAAGGTCCTGTGCTCGGG\nATCTTCCAGACGTCGCGACTCTAAATTGCCCCCTCTGAGGTCAAGGAACACAAGATGGTTTTGGAAATGC\nTGAACCCGATACATTATAACATCACCAGCATCGTGCCTGAAGCCATGCCTGCTGCCACCATGCCAGTCCT"

sequence = st.text_area("Sequence input", sequence_input, height=250)
sequence = sequence.splitlines()
sequence = sequence[1:]
sequence = ''.join(sequence)

st.write("""
***
""")

st.header('OUTPUT (🧬 Nucleotide Count)')

def DNA_nucleotide_count(seq):
  d = dict([
            ('A',seq.count('A')),
            ('T',seq.count('T')),
            ('G',seq.count('G')),
            ('C',seq.count('C'))
            ])
  return d

X = DNA_nucleotide_count(sequence)

col1, col2 = st.beta_columns(2)

with col1:
    st.subheader('Table')
    df = pd.DataFrame.from_dict(X, orient='index')
    df = df.rename({0: 'count'}, axis='columns')
    df.reset_index(inplace=True)
    df = df.rename(columns = {'index':'nucleotide'})
    st.write(df)


with col2:
    st.subheader('Bar Chart')
    p = alt.Chart(df).mark_bar().encode(
        x='nucleotide',
        y='count'
    )
    p = p.properties(
        width=alt.Step(80)
    )
    st.write(p)

st.markdown("<br><br><hr><center>Made with ❤️ by <a href='mailto:ralhanprateek@gmail.com?subject=Issue-DNA BioInformatics WebApp!&body=Please specify the issue you are facing with the app.'><strong>Prateek Ralhan</strong></a></center><hr>", unsafe_allow_html=True)
