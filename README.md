# COVID-19 Data Analysis & Dashboard for East Africa

This project includes a comprehensive data analysis and an interactive dashboard for COVID-19 statistics in East African countries: **Kenya, Tanzania, Uganda, Rwanda, and Burundi**.

---

## 📁 Project Structure

```
covid19-dashboard-project/
├── COVID19_EA_Analysis.ipynb             # Jupyter Notebook for analysis
├── app.py                                # Streamlit dashboard
├── owid-covid-data.csv                   # COVID-19 dataset
```

---

## 🚀 How to Use

### 1. Jupyter Notebook (Exploratory Data Analysis)

#### ✅ Requirements:
- Python 
- VS Code with Python & Jupyter extensions
- Create a virtual environment
#### ✅ Requirements:
```bash
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # macOS/Linux
```


#### 🔧 Run:
1. Open `COVID19_EA_Analysis.ipynb` in VS Code.
2. Run all cells to load, clean, and visualize the data.

---

### 2. Streamlit Dashboard

#### ✅ Requirements:
```bash
pip install streamlit pandas plotly
```

#### ✅ Requirements for python packages
```bash
pip install pandas matplotlib seaborn plotly jupyter
```

#### 🚀 Run:
```bash
streamlit run app.py
```

It will launch a browser tab with the interactive dashboard.

---

## 📊 Features

- Time series plots of total COVID-19 cases
- Choropleth map of total cases by country
- Interactive country selector
- Cleaned and filtered dataset for East African countries

---

## 📌 Data Source

- [Our World in Data - COVID-19 Dataset](https://ourworldindata.org/covid-cases)

---

## 🙌 Author

Generated using Python, Pandas, Matplotlib, Plotly & Streamlit.

