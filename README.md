## 📊 CORD Analysis

[![Python](https://img.shields.io/badge/python-3.11-blue)](https://www.python.org/)  
[![Streamlit](https://img.shields.io/badge/streamlit-%3E%3D1.0-orange)](https://streamlit.io/)  

A **data analysis project** using the **CORD dataset**, combining data exploration, visualization, and a small interactive application built with **Streamlit**.

---

## 📂 Repository Structure

- **analysis.ipynb** → Jupyter notebook with main data analysis and visualizations.  
- **app.py** → Streamlit app for interactive data exploration.  

> ⚠️ Note: The `metadata.csv` dataset is **not included** due to its large size (~1.5 GB).

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/<your-username>/Frameworks_Assignment.git
cd Frameworks_Assignment
2. Install dependencies
Make sure you have Python installed, then run:

bash
Copy code
pip install -r requirements.txt
If you don’t have a requirements.txt, install manually:

bash
Copy code
pip install streamlit pandas matplotlib seaborn
3. Run the Streamlit app
bash
Copy code
python -m streamlit run app.py