import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("Cloud Storage Growth Model")

st.write("Predict corporate cloud storage usage using Exponential + Logistic Growth")

# ---------------- INPUTS ----------------
st.sidebar.header("Input Parameters")

S0 = st.sidebar.number_input("Initial Storage (GB)", value=50)
S_max = st.sidebar.number_input("Maximum Storage Capacity (GB)", value=1000)
r = st.sidebar.slider("Growth Rate", 0.01, 0.2, 0.05)
days = st.sidebar.slider("Time (Days)", 10, 365, 200)
daily_upload = st.sidebar.number_input("Daily Upload (GB/day)", value=5)

t = np.linspace(0, days, 100)

# ---------------- MODELS ----------------
# Exponential Growth
S_exp = S0 * np.exp(r * t)

# Logistic Growth
S_log = S_max / (1 + np.exp(-r * (t - days/2)))

# Combined Model
S_combined = np.minimum(S_exp + daily_upload * t, S_log)

# ---------------- EXPANSION CHECK ----------------
threshold = 0.8 * S_max
expansion_day = None

for i in range(len(t)):
    if S_combined[i] >= threshold:
        expansion_day = int(t[i])
        break

# ---------------- PLOT ----------------
plt.figure()
plt.plot(t, S_exp, label="Exponential Growth")
plt.plot(t, S_log, label="Logistic Growth")
plt.plot(t, S_combined, label="Combined Model", linewidth=3)

plt.axhline(y=threshold, linestyle='--', label="80% Capacity")

plt.xlabel("Time (days)")
plt.ylabel("Storage (GB)")
plt.title("Cloud Storage Growth Prediction")
plt.legend()

st.pyplot(plt)

# ---------------- OUTPUT ----------------
st.subheader("Results")

if expansion_day:
    st.warning(f"⚠️ Expansion needed around Day {expansion_day}")
else:
    st.success("Storage within safe limits")

st.write(f"Final Storage Used: {S_combined[-1]:.2f} GB")