# Main Streamlit Application


import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import joblib
import os


# Page Configuration

st.set_page_config(
    page_title="AI-Based NIDS",
    page_icon="🛡️",
    layout="wide"
)


# Load CSS

if os.path.exists("style.css"):

    with open("style.css") as f:

        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )


# Load Trained Model

MODEL_PATH = "model/model.pkl"
FEATURE_PATH = "model/features.pkl"
ACCURACY_PATH = "model/accuracy.pkl"


model = None
feature_names = []
accuracy = 0


# Load model

if os.path.exists(MODEL_PATH):

    model = joblib.load(MODEL_PATH)


# Load feature names

if os.path.exists(FEATURE_PATH):

    feature_names = joblib.load(FEATURE_PATH)


# Load accuracy

if os.path.exists(ACCURACY_PATH):

    accuracy = joblib.load(ACCURACY_PATH)



# Sidebar Navigation


st.sidebar.title("🛡️ AstraGuard AI")

st.sidebar.subheader(
    "AI-Based Network Intrusion Detection System"
)


menu = st.sidebar.radio(

    "Navigation",

    [

        "Dashboard",
        "Predict Attack",
        "Live Simulation",
        "Project Documentation"

    ]

)



# Dashboard


if menu == "Dashboard":


    st.title(
        "🛡️ AI-Based Network Intrusion Detection System"
    )


    if model is not None:

        st.success(
            "Random Forest Model Loaded Successfully"
        )

    else:

        st.error(
            "Model not found. Train the model first."
        )



    col1, col2, col3 = st.columns(3)



    with col1:

        st.metric(

            "System Status",

            "Active"

        )



    with col2:

        st.metric(

            "Model Accuracy",

            f"{accuracy*100:.2f}%"

        )



    with col3:


        if model is not None:

            st.metric(

                "Model",

                "Random Forest"

            )

        else:

            st.metric(

                "Model",

                "Not Loaded"

            )



    st.write("---")



    st.subheader(
        "Model Information"
    )



    if model is not None:


        st.write(
            "**Algorithm:** Random Forest Classifier"
        )


        st.write(
            "**Dataset:** CIC-IDS2017"
        )


        st.write(
            "**Number of Features:**",
            len(feature_names)
        )


        st.write(
            "**Number of Classes:**",
            len(model.classes_)
        )


        st.write(
            "**Attack Classes:**"
        )


        st.write(
            model.classes_
        )


    else:


        st.warning(
            "Train model and save model.pkl"
        )



    st.write("---")



    if model is not None:


        st.subheader(
            "Attack Classes Distribution"
        )


        class_df = pd.DataFrame(

            {

                "Attack Type": model.classes_

            }

        )


        fig, ax = plt.subplots(
            figsize=(8,4)
        )


        sns.countplot(

            data=class_df,

            x="Attack Type",

            ax=ax

        )


        plt.xticks(
            rotation=45
        )


        st.pyplot(fig)







# Predict Attack


elif menu == "Predict Attack":


    st.title(
        "🚨 Network Attack Prediction"
    )


    if model is None:


        st.error(
            "No trained model found!"
        )


        st.info(
            "Run train_model.py first."
        )


    else:


        st.success(
            "Model Loaded Successfully"
        )



        uploaded_file = st.file_uploader(

            "Upload Test CSV File",

            type=["csv"]

        )



        if uploaded_file is not None:



            # Keep original data for result

            original_data = pd.read_csv(
                uploaded_file
            )



            st.subheader(
                "Uploaded Dataset"
            )


            st.dataframe(
                original_data.head()
            )



            st.write(
                "Rows:",
                original_data.shape[0]
            )


            st.write(
                "Columns:",
                original_data.shape[1]
            )



            # Copy data for prediction

            test_data = original_data.copy()



            # Remove Label Column


            if "Label" in test_data.columns:


                test_data = test_data.drop(

                    "Label",

                    axis=1

                )



            # Convert Categorical Columns


            test_data = pd.get_dummies(
                test_data
            )



            # Match Training Features


            test_data = test_data.reindex(

                columns=feature_names,

                fill_value=0

            )



            st.success(
                "Dataset Prepared Successfully"
            )



            # Prediction Button


            if st.button(
                "Predict Attack"
            ):



                predictions = model.predict(
                    test_data
                )



                # Keep original columns

                result = original_data.copy()



                result["Prediction"] = predictions



                st.success(
                    "Prediction Completed Successfully"
                )



                # Prediction Result


                st.subheader(
                    "Prediction Results"
                )


                st.dataframe(
                    result
                )



                # Prediction Summary


                st.subheader(
                    "Prediction Summary"
                )


                summary = (

                    pd.Series(predictions)

                    .value_counts()

                    .reset_index()

                )



                summary.columns = [

                    "Attack Type",

                    "Count"

                ]



                st.dataframe(
                    summary
                )



                # Prediction Distribution Chart


                fig, ax = plt.subplots(

                    figsize=(8,4)

                )


                sns.barplot(

                    data=summary,

                    x="Attack Type",

                    y="Count",

                    ax=ax

                )


                plt.xticks(
                    rotation=45
                )


                st.pyplot(fig)



                # Accuracy Evaluation


                if "Label" in result.columns:



                    from sklearn.metrics import (

                        accuracy_score,

                        classification_report,

                        confusion_matrix

                    )



                    acc = accuracy_score(

                        result["Label"],

                        result["Prediction"]

                    )



                    st.success(

                        f"Prediction Accuracy : {acc*100:.2f}%"

                    )



                    # Classification Report


                    st.subheader(
                        "Classification Report"
                    )


                    report = classification_report(

                        result["Label"],

                        result["Prediction"]

                    )


                    st.text(
                        report
                    )



                    # Confusion Matrix


                    st.subheader(
                        "Confusion Matrix"
                    )



                    cm = confusion_matrix(

                        result["Label"],

                        result["Prediction"]

                    )



                    fig2, ax2 = plt.subplots(

                        figsize=(10,8)

                    )



                    sns.heatmap(

                        cm,

                        annot=True,

                        fmt="d",

                        cmap="Blues",

                        ax=ax2

                    )



                    plt.xlabel(
                        "Predicted"
                    )


                    plt.ylabel(
                        "Actual"
                    )


                    st.pyplot(fig2)



                # Download Result CSV


                csv = result.to_csv(

                    index=False

                )



                st.download_button(

                    label="Download Prediction CSV",

                    data=csv,

                    file_name="Prediction_Result.csv",

                    mime="text/csv"

                )      








# Live Traffic Simulation

elif menu == "Live Simulation":

    st.title("🌐 Live Network Traffic Simulation")

    st.write(
        """
        This module simulates real-time network attack detection.
        
        The system reads network traffic records from CSV,
        sends each record to the AI model, and displays
        attack detection results.
        """
    )


    if model is None:

        st.error(
            "Model not loaded. Train the model first."
        )


    else:

        st.success(
            "AI Model Ready for Live Detection"
        )


        uploaded_file = st.file_uploader(
            "Upload Network Traffic CSV",
            type=["csv"]
        )


        if uploaded_file is not None:


            live_data = pd.read_csv(uploaded_file)


            st.subheader(
                "Traffic Data Preview"
            )

            st.dataframe(
                live_data.head()
            )


            # Remove Label if available

            if "Label" in live_data.columns:

                actual_labels = live_data["Label"]

                live_data = live_data.drop(
                    "Label",
                    axis=1
                )



            # Convert categorical data

            live_data = pd.get_dummies(
                live_data
            )


            # Match model features

            live_data = live_data.reindex(

                columns=feature_names,

                fill_value=0

            )


            st.write("---")


            if st.button(
                "Start Live Detection"
            ):


                results = []


                progress = st.progress(0)


                status = st.empty()



                total_rows = len(live_data)



                for i in range(total_rows):


                    row = live_data.iloc[[i]]


                    prediction = model.predict(row)[0]


                    results.append(
                        prediction
                    )


                    status.write(
                        f"Packet {i+1}/{total_rows}  →  {prediction}"
                    )


                    progress.progress(
                        (i+1)/total_rows
                    )



                st.success(
                    "Live Detection Completed"
                )


                result_df = pd.DataFrame(

                    {

                    "Packet Number":
                    range(1,total_rows+1),

                    "Prediction":
                    results

                    }

                )


                st.subheader(
                    "Live Detection Results"
                )


                st.dataframe(
                    result_df
                )



                # Attack distribution chart

                st.subheader(
                    "Attack Distribution"
                )


                chart_data = (

                    result_df["Prediction"]

                    .value_counts()

                    .reset_index()

                )


                chart_data.columns = [

                    "Attack",

                    "Count"

                ]


                fig, ax = plt.subplots(
                    figsize=(8,4)
                )


                sns.barplot(

                    data=chart_data,

                    x="Attack",

                    y="Count",

                    ax=ax

                )


                plt.xticks(
                    rotation=45
                )


                st.pyplot(fig)



                # Download result

                csv = result_df.to_csv(
                    index=False
                )


                st.download_button(

                    "Download Live Detection Report",

                    csv,

                    "Live_Detection_Result.csv",

                    "text/csv"

                )


# Project Documentation


elif menu == "Project Documentation":


    st.title(
        "📘 AI-Based Network Intrusion Detection System"
    )


    st.markdown("---")



    st.header(
        "Problem Statement"
    )


    st.write(
        """
Traditional firewall systems and signature-based
Intrusion Detection Systems cannot detect all
modern cyber attacks.

Machine Learning helps identify unknown attacks
by learning patterns from network traffic data.
"""
    )



    st.markdown("---")



    st.header(
        "Project Objectives"
    )


    st.markdown(
        """

✅ Detect malicious network traffic

✅ Identify different cyber attacks

✅ Predict network threats using AI

✅ Improve network security

✅ Reduce manual monitoring


"""
    )



    st.markdown("---")



    st.header(
        "Dataset Used"
    )


    st.write(
        """
Dataset:

CIC-IDS2017


Contains:

• Normal network traffic
• DoS attacks
• DDoS attacks
• Bot attacks
• PortScan
• Web attacks
• Infiltration attacks

"""
    )



    st.markdown("---")



    st.header(
        "Machine Learning Algorithm"
    )


    st.write(
        """

Algorithm Used:

Random Forest Classifier


Advantages:

• High accuracy

• Handles large datasets

• Reduces overfitting

• Feature importance analysis

• Fast prediction


"""
    )



    st.markdown("---")



    st.header(
        "Technology Stack"
    )


    tech_df = pd.DataFrame(

        {

            "Technology":[

                "Python",

                "Streamlit",

                "Pandas",

                "NumPy",

                "Scikit-Learn",

                "Matplotlib",

                "Seaborn",

                "Joblib"

            ],


            "Purpose":[

                "Programming",

                "Web Application",

                "Data Processing",

                "Numerical Computing",

                "Machine Learning",

                "Visualization",

                "Charts",

                "Model Saving"

            ]

        }

    )



    st.dataframe(
        tech_df
    )



    st.markdown("---")



    st.header(
        "Project Workflow"
    )


    st.code(
        """

Parquet Dataset

        |

        ▼

Convert Dataset to CSV

        |

        ▼

Data Cleaning

        |

        ▼

Feature Engineering

        |

        ▼

Train Random Forest Model

        |

        ▼

Save model.pkl

        |

        ▼

Streamlit Application

        |

        ▼

Upload Test CSV

        |

        ▼

AI Prediction

        |

        ▼

Attack Detection


"""
    )



    st.markdown("---")



    st.header(
        "End Users"
    )


    st.markdown(
        """

👨‍💻 Network Administrators

🔐 Security Analysts

🏢 Organizations

🎓 Students

📊 Researchers


"""
    )



    st.markdown("---")



    st.success(
        "AI-Based Network Intrusion Detection System Completed Successfully"
    )


    st.caption(
        "Developed using Artificial Intelligence and Machine Learning"
    )