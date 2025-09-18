## 📊 CORD Analysis
 
A **data analysis project** using the **CORD dataset**, combining data exploration, visualization, and a small interactive application built with **Streamlit**.

## 📂 Repository Structure

- **analysis.ipynb** → Jupyter notebook with main data analysis and visualizations.  
- **app.py** → Streamlit app for interactive data exploration.  
- **.gitignore** → Specifies intentionally untracked files to ignore (e.g., metadata.csv).  
- **screenshots/** → Folder containing images/screenshots of the Streamlit app.
 

> ⚠️ **Note**: The `metadata.csv` dataset is **not included** due to its large size (~1.5 GB).

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/KimaniImmaculate/Frameworks_Assignment.git
cd Frameworks_Assignment
```

### 2. Install dependencies

Make sure you have Python installed.

If you have a `requirements.txt` file, run:
```bash
pip install -r requirements.txt
```

If you don’t have a `requirements.txt`, install the packages manually:
```bash
pip install streamlit pandas matplotlib seaborn
```

### 3. Run the Streamlit app
```bash
python -m streamlit run app.py
```
> **Tip**: Use `Ctrl+C` in the terminal to stop the app.

## 📁 Dataset

This project uses the CORD-19 `metadata.csv` dataset. You can download it from Kaggle:  
[Kaggle - CORD-19 Research Challenge](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge)

Once downloaded, place `metadata.csv` in the **root of the repository folder** to run the full analysis.  

> **Tip:** Add `metadata.csv` to your `.gitignore` file to prevent pushing the large dataset to GitHub:

## 🖼 Screenshots

<p float="left">
  <img src="screenshots/sL1.png" width="300" />
  <img src="screenshots/sL2.png" width="300" />
</p>



## 📌 Features
- Data exploration using Pandas and Seaborn.
- Interactive visualizations with Streamlit.
- Search for papers by keyword.
- Modular structure for easy extension and experimentation.

## 💡 Notes
- The repository does not include the dataset due to its size.
- The Streamlit app works fully if `metadata.csv` is added to the folder.
- Recommended for Python 3.8+ and Streamlit ≥ 1.0.