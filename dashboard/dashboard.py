import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import plotly.express as px
import numpy as np
import os



st.set_page_config(layout="wide", page_title='Streamlit-Nigel Alessandro')

bike_day =  pd.read_csv('./dashboard/bike_day.csv')



col1, col2= st.columns([0.2,0.8])

with col1:

    st.text("Nama        : Nigel Alessandro")
    st.text("Email       : nigelalessan@gmail.com")
    st.text("Id Dicoding : nigelalesssan")
    

with col2:
    st.markdown("<h1 style='text-align: center; color: white;'>💖 TUGAS AKHIR DICODING 💖</h1>", unsafe_allow_html=True)

    st.header("Sepeda yang disewa berdasarkan musim", divider=True)

   
    bike_day['season'] = pd.Categorical(bike_day['season'], categories=['Spring','Summer','Fall','Winter'], ordered=True)

    season_c = bike_day.groupby(by=["season","yr"]).agg({
        "cnt": "sum"
    }).reset_index()

    fig, ax = plt.subplots(figsize=(10, 6))

    sns.lineplot(
        data=season_c,
        x="season",
        y="cnt",
        hue="yr",
        palette="Paired",
        marker="o")

    plt.title("Persewaan Sepeda Berdasarkan Musim")
    plt.xlabel("Musim")
    plt.ylabel(None)
    plt.legend(title="Tahun", loc=4)
    plt.tight_layout()
    plt.style.use('bmh')
    plt.show()

    st.pyplot(fig)

    with st.expander("Penjelasan"):
        st.write('''
            Grafik diatas merupakan jumlah sepeda
            yang disewa pada tiap musim oleh user
            yang registered (terdaftar) dan yang casual
            (belum terdaftar). Grafik diatas menunjukkan
            bahwa sewa tertinggi duduki oleh musim Fall (gugur).
        ''')

###########################################################################

    st.header("Jumlah sepeda yang disewa tiap tahun", divider=True)

    fig, ax = plt.subplots(figsize=(10, 6))

    # Membuat bar plot
    sns.barplot(
        x='yr',
        y='cnt',
        data=bike_day,
        order=['2011', '2012'],
        palette='Paired',
        ax=ax
    )

    # Menambahkan judul dan label
    plt.title('Jumlah sepeda yang disewa tiap tahun')
    plt.xlabel(None)
    plt.ylabel('Jumlah Pengguna Sepeda Registered dan Casual')
    plt.style.use('bmh')

    # Menampilkan plot di Streamlit
    st.pyplot(fig)

    with st.expander("Penjelasan"):
        st.write('''
        Grafik diatas merupakan jumlah sepeda
        yang disewa pada tiap tahun oleh user
        yang registered (terdaftar) dan yang casual
        (belum terdaftar). Grafik diatas menunjukkan
        bahwa terjadi peningkatan pengguna dari tahun 2011 ke 2012,
        baik dari pengguna registered dan casual.
        ''')
   

###########################################################################

    st.header("Rata-rata tingkat sepeda yang disewa", divider=True)


    grouped_data = bike_day.groupby('weekday')[['registered', 'casual']].agg("mean").reset_index().round(2)

    label = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
    x = np.arange(len(label))

    plt.figure(figsize=(10, 6))

    barwidth = 0.4

    fig, ax = plt.subplots(figsize=(10, 6))

    plt.bar(
        x-0.2,
        grouped_data['registered'],
        label='Registered',
        color='tab:blue',
        width = barwidth
    )

    plt.bar(
        x+0.2,
        grouped_data['casual'],
        label='Casual',
        color='tab:olive',
        width = barwidth
    )

    for i, v in enumerate(grouped_data['registered']):
        plt.text(i-0.40, v+90, str(v))

    for i, v in enumerate(grouped_data['casual']):
        plt.text(i, v+90, str(v))

    plt.style.use('bmh')
    plt.xlabel(None)
    plt.ylabel(None)
    plt.title('Rata-rata tingkat sepeda yang disewa')
    plt.xticks(x,('Fri','Mon', 'Sat', 'Sun', 'Thu', 'Tue', 'Wed'))
    plt.legend()
    plt.show()

    st.pyplot(fig)

    with st.expander("Penjelasan"):
        st.write('''
            Grafik diatas merupakan rata-rata sepeda
            yang disewa pada tiap hariinya oleh user
            yang registered (terdaftar) dan yang casual
            (belum terdaftar). User registered ditunjukkan dengan
            grafik warna biru sedangkan user casual ditunjukkan
            dengan grafik warna hijau. Grafik diatas menunjukkan
            bahwa hari kamis memuncaki untuk rata-rata sepeda
            yang disewa oleh user registered sedangkan untuk user
            casual paling tinggi diduduki oleh hari sabtu
            ''')
    
