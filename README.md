# 🧠 Crime Pattern Analyzer – India's Crime Data Dashboard

An interactive Streamlit-based web application to analyze, visualize, and forecast crime trends across India. This tool is built to promote awareness, provide safety tips, and support data-driven insights using real crime data.

---

## 🚀 Features

- 📊 **Visual Analysis**: Interactive charts for crimes like murder, kidnapping, rape, property theft, and crimes against women.
- 🤖 **ML Forecasting**: Predict future crime trends using linear regression for selected categories.
- 🛡️ **Crime Prevention Guide**: Category-wise safety tips and prevention strategies.
- 🌐 **User-Friendly Interface**: Clean sidebar controls, expandable sections, and informative layout.
- 📥 **Downloadable Charts**: Export charts in image format for reports or presentations.
- 🗺️ **Coming Soon**: Map-based state-wise crime visualization and regional filtering.

---

## 📂 Project Structure

```
crime-pattern-analyzer/
│
├── app.py                         # Main Streamlit application
├── data/
│   └── crime_data.csv             # Processed dataset
├── assets/
│   └── logo.png                   # Optional images/logos
├── requirements.txt               # Python dependencies
└── README.md                      # This file
```

---

## 🧠 How it Works

1. Users select crime types from the sidebar.
2. Visualizations are generated using Matplotlib/Seaborn based on the dataset.
3. Machine Learning models (Linear Regression) predict future crime trends.
4. Users can view prevention tips and download plots as images.

---

## 📦 Installation

### 🔹 Option 1: Run Locally

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/crime-pattern-analyzer.git
   cd crime-pattern-analyzer
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the app:
   ```bash
   streamlit run app.py
   ```

---

### 🔹 Option 2: Run Online (Recommended for Demo)

1. Deploy directly to **Streamlit Cloud**:
   - Visit [streamlit.io/cloud](https://streamlit.io/cloud)
   - Connect your GitHub repository
   - Set `app.py` as the main file

---

## 🔮 Upcoming Features

- 🗺️ Interactive map view by state or region
- 🧠 NLP-based search for crime-related queries
- 📱 Mobile-friendly UI improvements
- 📌 Filtering by year, location, and severity level

---

## 🤝 Contributing

Contributions, feature suggestions, and issues are welcome!  
Feel free to open a [pull request](https://github.com/your-username/crime-pattern-analyzer/pulls) or [issue](https://github.com/your-username/crime-pattern-analyzer/issues).

---

## 🧠 Built With

- [Python](https://www.python.org/)
- [Streamlit](https://streamlit.io/)
- [Pandas](https://pandas.pydata.org/)
- [Matplotlib](https://matplotlib.org/)
- [Scikit-learn](https://scikit-learn.org/)

---


## 🙋‍♀️ Author

**Prathiksha Shetty**  
🚀 Passionate about using data and AI to build tools that make a real impact.
