#python -m streamlit run ./og.py
import csv
import streamlit as st
import pandas as pd

list = [];
searchList = [];
with open('./athlete_events.csv', 'r') as file:
    reader = csv.reader(file);
    for row in reader:
        list.append(row);

heading = list[0];
list.pop(0);
df = pd.DataFrame(list, columns=heading);
table = st.empty();
table.dataframe(df);

option = st.selectbox("Select searching column", heading);
searchableItem = st.text_input('Write searchable text');
onlyMedal = st.checkbox('Search only medalistics')
if(st.button('Search')):
    searchId = heading.index(option);
    for i in list:
        if(i[searchId].find(searchableItem) != -1):
            if(onlyMedal):
                if(i[len(i)-1].find('NA') == -1):
                    searchList.append(i);
            else:
                searchList.append(i);
    df = pd.DataFrame(searchList, columns=heading);
    table.dataframe(df);
if(st.button('Reset table')):
    df = pd.DataFrame(list, columns=heading);
    table.dataframe(df);