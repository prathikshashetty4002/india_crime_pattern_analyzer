import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

crime_prevention_tips = {
    "Property Theft": [
        "Install CCTV cameras around your home.",
        "Avoid leaving valuables in plain sight.",
        "Use strong locks and security systems.",
        "Get to know your neighbors for added security.",
        "Report any suspicious activity to local authorities."
    ],
    "Victims of Rape": [
        "Avoid isolated areas when alone, especially at night.",
        "Use safety apps or emergency contact tools.",
        "Take self-defense classes if possible.",
        "Ensure trusted contacts know your whereabouts.",
        "Support and promote gender equality education in your community."
    ],
    "Murder Victims": [
        "Be aware of domestic violence signs and seek help early.",
        "Avoid confrontation in high-risk areas or situations.",
        "Maintain good lighting in and around your home.",
        "Use safe and secure transportation, especially at night."
    ],
    "Kidnapping Purpose": [
        "Teach children about stranger danger and safe routes.",
        "Never share travel plans publicly on social media.",
        "Use location-sharing with trusted friends/family.",
        "Be cautious in unfamiliar areas, especially when alone.",
        "Report missing persons immediately to the police."
    ],
    "Crimes Against Women": [
        "Support women's rights awareness and education.",
        "Stay connected with emergency helplines/apps.",
        "Ensure public places are well-lit and monitored.",
        "Encourage open communication about abuse or harassment.",
        "Use buddy systems when travelling late at night."
    ]
}


# Set visual theme
sns.set(style="whitegrid")
st.set_page_config(page_title="India Crime Pattern Analyzer", layout="wide")
st.title("🔍 India Crime Pattern Analyzer")
# Background color toggle
theme = st.selectbox("🎨 Choose Theme", ["Light", "Dark"])

# Define custom CSS
if theme == "Dark":
    st.markdown("""
        <style>
        body {
            background-color: #1e1e1e;
            color: white;
        }
        .stApp {
            background-color: #1e1e1e;
            color: white;
        }
        </style>
    """, unsafe_allow_html=True)
else:
    st.markdown("""
        <style>
        body {
            background-color: #f5f5f5;
            color: black;
        }
        .stApp {
            background-color: #f5f5f5;
            color: black;
        }
        </style>
    """, unsafe_allow_html=True)

# Base path
base_path = "C:/Users/HP/Desktop/crime_pattern_anlyzer/crime_pattern_analyzer/crime_data"

# Sidebar menu
section = st.sidebar.selectbox("Select Analysis Section", [
    "Overview Dashboard",
    "Property Theft",
    "Victims of Rape",
    "Murder Victims",
    "Kidnapping Purpose",
    "Crimes Against Women",
    "📊 ML Prediction"
])
st.sidebar.markdown("## 🛡️ Crime Prevention Guide")
selected_crime = st.sidebar.selectbox("Select a Crime Type", list(crime_prevention_tips.keys()))


# ------------------------ 1. PROPERTY THEFT ------------------------
if section == "Property Theft":
    df = pd.read_csv(f"{base_path}/10_Property_stolen_and_recovered.csv")
    df.columns = [c.strip().replace(" ", "_") for c in df.columns]
    summary = df.groupby("Area_Name")["Cases_Property_Stolen"].sum().sort_values(ascending=False).head(10)

    st.subheader("🏠 Top 10 States with Highest Property Theft Cases")

    summary_df = summary.reset_index()
    summary_df.index = summary_df.index + 1
    st.dataframe(summary_df)

    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x=summary.values, y=summary.index, palette="Reds_r", ax=ax)
    for i, v in enumerate(summary.values):
        ax.text(v + 100, i, str(v), color='black', va='center', fontweight='bold')
    ax.set_xlabel("Cases of Property Stolen")
    ax.set_ylabel("State/UT")
    ax.set_title("Top 10 States with Highest Property Theft Cases")
    st.pyplot(fig)

    # Trend
    trend = df.groupby("Year")["Cases_Property_Stolen"].sum().reset_index()
    st.subheader("📈 Property Theft Trend Over the Years")
    fig2, ax2 = plt.subplots(figsize=(10, 6))
    sns.lineplot(data=trend, x="Year", y="Cases_Property_Stolen", marker="o", color="crimson", ax=ax2)
    ax2.set_xlabel("Year")
    ax2.set_ylabel("Total Property Theft Cases")
    ax2.set_title("Trend of Property Theft Cases in India")
    st.pyplot(fig2)

# ------------------------ 2. VICTIMS OF RAPE ------------------------
elif section == "Victims of Rape":
    df = pd.read_csv(f"{base_path}/20_Victims_of_rape.csv")
    df.columns = [c.strip().replace(" ", "_") for c in df.columns]
    summary = df.groupby("Area_Name")["Victims_of_Rape_Total"].sum().sort_values(ascending=False).head(10)

    st.subheader("🔹 Top 10 States with Highest Rape Victims")

    summary_df = summary.reset_index()
    summary_df.index = summary_df.index + 1  # Start index from 1
    st.dataframe(summary_df)

    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x=summary.values, y=summary.index, palette="Purples_r", ax=ax)
    for i, v in enumerate(summary.values):
        ax.text(v + 50, i, str(v), color='black', va='center', fontweight='bold')
    ax.set_title("Top 10 States with Highest Rape Victims (Total)")
    st.pyplot(fig)

    # ✅ Use 'df' instead of undefined 'df_rape'
    df_rape_trend = df.groupby("Year")["Victims_of_Rape_Total"].sum().reset_index()

    st.subheader("📈 Trend of Rape Victims in India Over the Years")
    fig2, ax2 = plt.subplots(figsize=(10, 5))
    sns.lineplot(data=df_rape_trend, x="Year", y="Victims_of_Rape_Total", marker="o", ax=ax2, color="purple")
    ax2.set_title("Rape Victims Over the Years")
    ax2.set_xlabel("Year")
    ax2.set_ylabel("Number of Victims")
    st.pyplot(fig2)


# ------------------------ 3. MURDER VICTIMS ------------------------
elif section == "Murder Victims":
    df = pd.read_csv(f"{base_path}/32_Murder_victim_age_sex.csv")
    df.columns = [c.strip().replace(" ", "_") for c in df.columns]
    summary = df.groupby("Year")["Victims_Total"].sum().sort_values(ascending=False)

    st.subheader("🔹 Murder Victims per Year")

    summary_df = summary.reset_index()
    summary_df.index = summary_df.index + 1
    summary_df.columns = ["State/UT", "Total Murder Victims"]
    st.dataframe(summary_df)

    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x=summary.index, y=summary.values, palette="Greens_r", ax=ax)
    ax.set_title("Murder Victims in Different Years (All States Combined)")
    ax.set_xlabel("Year")
    ax.set_ylabel("Total Victims")
    plt.xticks(rotation=45)
    st.pyplot(fig)

    st.subheader("📈 Trend of Murder Victims Over the Years")
    fig2, ax2 = plt.subplots(figsize=(10, 5))
    sns.lineplot(data=summary.reset_index(), x="Year", y="Victims_Total", marker="o", ax=ax2, color="green")
    ax2.set_title("Murder Victims Over the Years")
    ax2.set_xlabel("Year")
    ax2.set_ylabel("Number of Victims")
    st.pyplot(fig2)


# ------------------------ 4. KIDNAPPING PURPOSE ------------------------
elif section == "Kidnapping Purpose":
    df = pd.read_csv(f"{base_path}/39_Specific_purpose_of_kidnapping_and_abduction.csv")
    df.columns = [c.strip().replace(" ", "_") for c in df.columns]
    summary = df.groupby("Group_Name")["K_A_Grand_Total"].sum().sort_values(ascending=False).head(10)

    st.subheader("🌐 Top 10 Purposes of Kidnapping/Abduction")

    summary_df = summary.reset_index()
    summary_df.index = summary_df.index + 1
    summary_df.columns = ["Purpose", "Number of Cases"]
    st.dataframe(summary_df)

    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x=summary.values, y=summary.index, palette="Blues", ax=ax)
    for index, value in enumerate(summary.values):
        ax.text(value + 10, index, str(value), va='center', fontsize=9)
    st.pyplot(fig)

    df_kidnap_trend = df.groupby("Year")["K_A_Grand_Total"].sum().reset_index()

    st.subheader("Trend of Kidnapping/Abduction Cases in India Over the Years")
    fig4, ax4 = plt.subplots(figsize=(10, 5))
    sns.lineplot(data=df_kidnap_trend, x="Year", y="K_A_Grand_Total", marker="o", ax=ax4, color="blue")
    ax4.set_title("Kidnapping/Abduction Cases Over the Years")
    ax4.set_xlabel("Year")
    ax4.set_ylabel("Number of Cases")
    st.pyplot(fig4)

# ------------------------ 5. CRIMES AGAINST WOMEN ------------------------
elif section == "Crimes Against Women":
    df = pd.read_csv(f"{base_path}/42_Cases_under_crime_against_women.csv", on_bad_lines='skip')
    df.columns = [c.strip().replace(" ", "_") for c in df.columns]
    summary = df.groupby("Area_Name")["Total_Cases_for_Trial"].sum().sort_values(ascending=False).head(10)

    st.subheader("🧥 Top 10 States: Crimes Against Women")

    summary_df = summary.reset_index()
    summary_df.index = summary_df.index + 1
    summary_df.columns = ["State/UT", "Total Crimes Against Women"]
    st.dataframe(summary_df)

    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x=summary.values, y=summary.index, palette="Oranges", ax=ax)
    for index, value in enumerate(summary.values):
        ax.text(value + 50, index, str(value), va='center', fontsize=9)
    st.pyplot(fig)
    df_women_trend = df.groupby("Year")["Total_Cases_for_Trial"].sum().reset_index()

    st.subheader("Trend of Crimes Against Women in India Over the Years")
    fig5, ax5 = plt.subplots(figsize=(10, 5))
    sns.lineplot(data=df_women_trend, x="Year", y="Total_Cases_for_Trial", marker="o", ax=ax5, color="orange")
    ax5.set_title("Crimes Against Women Over the Years")
    ax5.set_xlabel("Year")
    ax5.set_ylabel("Number of Cases")
    st.pyplot(fig5)

#------------------------ML  Prediction------------------
elif section == "📊 ML Prediction":
    from sklearn.linear_model import LinearRegression
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import r2_score

    st.subheader("📊 Predict Future Crime Counts with Machine Learning")

    crime_options = {
        "Property Theft": {
            "file": "10_Property_stolen_and_recovered.csv",
            "column": "Cases_Property_Stolen"
        },
        "Victims of Rape": {
            "file": "20_Victims_of_rape.csv",
            "column": "Victims_of_Rape_Total"
        },
        "Murder Victims": {
            "file": "32_Murder_victim_age_sex.csv",
            "column": "Victims_Total"
        },
        "Kidnapping Purpose": {
            "file": "39_Specific_purpose_of_kidnapping_and_abduction.csv",
            "column": "K_A_Grand_Total"
        },
        "Crimes Against Women": {
            "file": "42_Cases_under_crime_against_women.csv",
            "column": "Total_Cases_for_Trial"
        }
    }

    selected_crime = st.selectbox("Select Crime Category", list(crime_options.keys()))
    file_path = f"{base_path}/{crime_options[selected_crime]['file']}"
    target_column = crime_options[selected_crime]['column']

    df = pd.read_csv(file_path, on_bad_lines='skip')
    df.columns = [c.strip().replace(" ", "_") for c in df.columns]
    df_grouped = df.groupby("Year")[target_column].sum().reset_index()

    X = df_grouped[["Year"]]
    y = df_grouped[target_column]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = LinearRegression()
    model.fit(X_train, y_train)

    future_year = st.slider("Select Future Year for Prediction", 2025, 2035, 2025)
    prediction = model.predict([[future_year]])[0]

    st.markdown(f"### 📌 Predicted {selected_crime} cases in {future_year}: `{int(prediction):,}`")

    y_pred = model.predict(X_test)
    r2 = r2_score(y_test, y_pred)
    st.markdown(f"**Model R² Score**: `{r2:.3f}`")

    fig, ax = plt.subplots(figsize=(10, 5))
    sns.lineplot(data=df_grouped, x="Year", y=target_column, label="Historical", marker="o", ax=ax)
    ax.scatter(future_year, prediction, color="red", label=f"Prediction ({future_year})", s=100)
    ax.set_title(f"{selected_crime} Trend & Future Prediction")
    ax.set_xlabel("Year")
    ax.set_ylabel("Number of Cases")
    ax.legend()
    st.pyplot(fig)



# ------------------------ OVERVIEW ------------------------
else:
    df_property = pd.read_csv(f"{base_path}/10_Property_stolen_and_recovered.csv")
    df_rape = pd.read_csv(f"{base_path}/20_Victims_of_rape.csv")
    df_murder = pd.read_csv(f"{base_path}/32_Murder_victim_age_sex.csv")
    df_kidnap = pd.read_csv(f"{base_path}/39_Specific_purpose_of_kidnapping_and_abduction.csv")
    df_women = pd.read_csv(f"{base_path}/42_Cases_under_crime_against_women.csv", on_bad_lines='skip')

    df_property.columns = [c.strip().replace(" ", "_") for c in df_property.columns]
    df_rape.columns = [c.strip().replace(" ", "_") for c in df_rape.columns]
    df_murder.columns = [c.strip().replace(" ", "_") for c in df_murder.columns]
    df_kidnap.columns = [c.strip().replace(" ", "_") for c in df_kidnap.columns]
    df_women.columns = [c.strip().replace(" ", "_") for c in df_women.columns]

    totals = {
        "Property Theft": df_property["Cases_Property_Stolen"].sum(),
        "Rape Victims": df_rape["Victims_of_Rape_Total"].sum(),
        "Murder Victims": df_murder["Victims_Total"].sum(),
        "Kidnapping": df_kidnap["K_A_Grand_Total"].sum(),
        "Crimes Against Women": df_women["Total_Cases_for_Trial"].sum()
    }

    st.subheader("📊 Overview of Crime Categories")
    total_df = pd.DataFrame(list(totals.items()), columns=["Crime Category", "Total Cases"])
    total_df.index = total_df.index + 1
    st.dataframe(total_df)

    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x="Total Cases", y="Crime Category", data=total_df, palette="Set2", ax=ax)
    for index, value in enumerate(total_df["Total Cases"]):
        ax.text(value + 5000, index, f"{int(value):,}", va='center', fontsize=9)
    ax.set_title("Overall Crime Category Comparison (India)")
    st.pyplot(fig)

# 🧠 Safety Tips Section
st.markdown("## 🧠 Safety Tips & Crime Prevention")
if selected_crime:
    with st.expander(f"🛡️ How to Prevent: {selected_crime}"):
        for tip in crime_prevention_tips[selected_crime]:
            st.markdown(f"- {tip}")
st.markdown("### 🚨 Emergency Helplines")
st.markdown("- 📞 **Police Control Room (All India): 112**")
st.markdown("- 👩‍🦰 **Women Helpline: 1091**")
st.markdown("- 🧒 **Child Helpline: 1098**")
st.markdown("- 📱 **Download Safety App: [112 India App](https://play.google.com/store/apps/details?id=com.tcs.911ts&hl=en_IN&gl=US)**")

if selected_crime:
    tips_text = f"Crime Prevention Tips for {selected_crime}\n\n"
    tips_text += "\n".join(f"- {tip}" for tip in crime_prevention_tips[selected_crime])

    st.download_button(
        label="📥 Download Safety Tips",
        data=tips_text,
        file_name=f"{selected_crime}_prevention_tips.txt",
        mime="text/plain"
    )

# ------------------------ FOOTER ------------------------
st.markdown("""
    <div style='text-align: center; color: grey; font-size: 14px;'>
        🔍 Crime Data Analyzer Project by <b>Prathiksha Shetty </b>| 2025<br>
        Built using Python, Pandas, and Streamlit | NCRB India Dataset
    </div>
""", unsafe_allow_html=True)


