import streamlit as st
import pandas as pd
import numpy as np

def main():
    st.title("Statistika")

    # Memasukkan data manual
    st.header("Masukkan Data")
    rows = st.number_input("Jumlah Baris Data:", min_value=1, value=5)
    cols = st.number_input("Jumlah Kolom Data:", min_value=1, value=3)

    data = []
    for i in range(rows):
        row = []
        for j in range(cols):
            value = st.number_input(f"Data Baris {i+1}, Kolom {j+1}", value=0.0)
            row.append(value)
        data.append(row)

    df = pd.DataFrame(data)
    st.write("Data yang Dimasukkan:")
    st.write(df)
    
 # Menghitung nilai rata-rata, median, modus, simpangan baku, ragam, jangkauan, kuartil, dan standar deviasi
    st.header("Statistik")
    st.write("Rata-rata: ", np.mean(data))
    st.write("Median: ", np.median(data))
    st.write("Simpangan Baku: ", np.round(np.std(data), 2))
    st.write("Ragam: ", np.round(np.var(data), 2))
    st.write("Jangkauan: ", np.round(np.max(data)-np.min(data), 2))
    st.write("Standar Deviasi: ", np.round(np.std(data), 2))
    
if __name__ == '__main__':
    main()
    

