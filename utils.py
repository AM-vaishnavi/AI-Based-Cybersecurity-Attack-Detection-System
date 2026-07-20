# ==========================================================
# AI-Based Network Intrusion Detection System (NIDS)
# utils.py
# Common Utility Functions
# ==========================================================

import streamlit as st
import pandas as pd
import numpy as np
import random
import time
import os

# ==========================================================
# Load External CSS
# ==========================================================

def load_css():

    if os.path.exists("style.css"):

        with open("style.css") as f:

            st.markdown(
                f"<style>{f.read()}</style>",
                unsafe_allow_html=True
            )

# ==========================================================
# Generate Simulated Network Traffic
# ==========================================================

def generate_traffic_data(n_samples=1000, seed=None):

    """
    Generates simulated network traffic data.

    Classes:
        Normal
        DDoS
        Brute Force
        Malware
    """

    if seed is not None:

        np.random.seed(seed)

    else:

        np.random.seed(int(time.time()))

    data = []

    for i in range(n_samples):

        label = random.choice(

            [

                "Normal",

                "DDoS",

                "Brute Force",

                "Malware"

            ]

        )

        if label == "Normal":

            duration = np.random.uniform(0.1, 2)

            src_bytes = np.random.randint(100, 5000)

            dst_bytes = np.random.randint(100, 5000)

            conn_count = np.random.randint(1, 10)

        elif label == "DDoS":

            duration = np.random.uniform(0.01, 0.10)

            src_bytes = np.random.randint(5000, 10000)

            dst_bytes = np.random.randint(10, 100)

            conn_count = np.random.randint(50, 200)

        elif label == "Brute Force":

            duration = np.random.uniform(2, 10)

            src_bytes = np.random.randint(50, 200)

            dst_bytes = np.random.randint(50, 200)

            conn_count = np.random.randint(20, 50)

        else:

            duration = np.random.uniform(5, 60)

            src_bytes = np.random.randint(1000, 20000)

            dst_bytes = np.random.randint(1000, 20000)

            conn_count = np.random.randint(1, 5)

        data.append(

            [

                duration,

                src_bytes,

                dst_bytes,

                conn_count,

                label

            ]

        )

    df = pd.DataFrame(

        data,

        columns=[

            "Duration",

            "Src_Bytes",

            "Dst_Bytes",

            "Conn_Count",

            "Label"

        ]

    )

    return df