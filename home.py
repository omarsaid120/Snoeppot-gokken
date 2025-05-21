# -*- coding: utf-8 -*-
"""
Created on Wed May 21 13:50:54 2025

@author: omars
"""

import streamlit as st
import pandas as pd


if 'Naam' not in st.session_state:
    st.session_state['Naam']=""

if 'gokken' not in st.session_state:
    st.session_state.gokken = []
    

def page1():
    st.title("Welkom")

    st.session_state['Naam'] = st.text_input("What is your name?", st.session_state['Naam'])


def page2():
    st.title("Welkom op de gok website")
    st.write("Hallo", st.session_state['Naam'], ", welkom op de website")
    
    
    number = st.number_input("Raad hoeveel snoepjes er in de pot zitten") 
    st.session_state.gokken.append(number)
    
    st.write("gegokte waarde", st.session_state.gokken)
    st.write("aantal gokken ", len(st.session_state.gokken))
    
    wis=st.button('Wis de data')
    if wis:
        st.session_state['gokken']=[]
        st.rerun()



    
    
    

pg = st.navigation([st.Page(page1, title="Home", icon=None),
    st.Page(page2, title="GOKKEN!!!!", icon=None),])
pg.run()