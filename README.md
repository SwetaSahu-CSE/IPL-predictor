# 🏏 IPL Win Predictor

## 📌 Overview

IPL Win Predictor is a Machine Learning web application that predicts the winning probability of the chasing team during the second innings of an IPL match. The application uses historical IPL match data and displays live win probabilities based on the current match situation.

---

## 🚀 Features

* Predicts the winning probability of the chasing team.
* Interactive Streamlit web application.
* Displays:

  * Winning Probability
  * Current Run Rate (CRR)
  * Required Run Rate (RRR)
* User-friendly interface.

---

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Streamlit
* Pickle
* Git & GitHub

---

## 📊 Machine Learning Concepts

* Data Cleaning
* Data Preprocessing
* Feature Engineering
* Data Merging
* GroupBy Operations
* Cumulative Sum (`cumsum`)
* One-Hot Encoding
* Pipeline Creation
* Logistic Regression
* Model Training & Prediction

---

## 📂 Project Structure

```text
IPL-Win-Predictor/
│── app.py
│── pipe.pkl
│── teams.pkl
│── cities.pkl
│── matches.csv
│── requirements.txt
│── README.md
```

---

## ▶️ How to Run

1. Clone the repository

```bash
git clone https://github.com/YourUsername/IPL-Win-Predictor.git
```

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the application

```bash
streamlit run app.py
```

---

## 📁 Dataset

This project uses IPL historical match data.

**Note:** `deliveries.csv` is not included in this repository because it exceeds GitHub's file size limit. It was used only during data preprocessing and model training. The trained model (`pipe.pkl`) is already included, so the application runs without `deliveries.csv`.

---

## 👩‍💻 Author

**Sweta Sahu**

B.Tech CSE Student | Machine Learning Enthusiast
