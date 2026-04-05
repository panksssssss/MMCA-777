# ☁️ Cloud Storage Growth Dashboard

A **Streamlit-based interactive dashboard** to predict corporate cloud storage usage using a combination of **Exponential Growth** and **Logistic Growth** models.

---

## 🚀 Features

* 📈 Predicts storage growth over time
* ⚡ Combines **Exponential + Logistic models** for realistic forecasting
* 🎛️ Interactive sidebar inputs
* 📊 Dynamic and responsive charts using Plotly
* 📦 Key performance metrics (KPIs)
* ⚠️ Automatic **expansion alert** when storage reaches 80% capacity

---

## 🧠 Model Overview

This project uses a hybrid approach:

* **Exponential Growth Model** → Represents rapid data increase
* **Logistic Growth Model** → Limits growth based on max capacity
* **Combined Model** → Ensures realistic predictions

### Formula Used:

* Exponential:

  ```
  S_exp = S0 * e^(r * t)
  ```

* Logistic:

  ```
  S_log = S_max / (1 + e^(-r * (t - T/2)))
  ```

* Combined:

  ```
  S_combined = min(S_exp + daily_upload * t, S_log)
  ```

---

## 📊 Dashboard Preview

* Real-time graph visualization
* Storage threshold indicator (80%)
* Expansion planning insights

---

## 🛠️ Tech Stack

* Python 🐍
* Streamlit
* NumPy
* Plotly

---

## ⚙️ Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/cloud-storage-growth.git
   cd cloud-storage-growth
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

## 📥 Input Parameters

| Parameter        | Description            |
| ---------------- | ---------------------- |
| Initial Storage  | Starting storage in GB |
| Maximum Capacity | Total storage limit    |
| Growth Rate      | Rate of data growth    |
| Time (Days)      | Simulation duration    |
| Daily Upload     | Daily data addition    |

---

## 📌 Output

* 📊 Growth curves (Exponential, Logistic, Combined)
* 📦 Final storage usage
* ⚠️ Expansion alert (if > 80% capacity)

---

## 📈 Use Cases

* Cloud infrastructure planning
* Enterprise storage forecasting
* Data growth analysis
* Capacity optimization

---

## 🤝 Contributing

Feel free to fork this repo and improve the model or UI.

---

## 📄 License

This project is open-source and available under the MIT License.

---

## 👨‍💻 Author

**Pankaj Sharma**

---

⭐ If you like this project, don’t forget to star the repo!
