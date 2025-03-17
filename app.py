import streamlit as st
import numpy as np

st.set_page_config("Wine Calculator", page_icon=":material/wine_bar:")

st.title("🍷 Wine Warming Time Calculator")
st.markdown("Calculate how long to leave your wine out to reach serving temperature, using Newton's Law of Cooling")

# --- Inputs ---
fridge_setting = st.selectbox("Fridge Setting", options=["Coldest (35°F)", "Colder (37°F)", "Cold (39°F)"])
fridge_temps = {"Coldest (35°F)": 35, "Colder (37°F)": 37, "Cold (39°F)": 39}
T_initial = fridge_temps[fridge_setting]

T_target = st.slider("Target Wine Temperature (°F)", min_value=55, max_value=65, value=62)
T_room = st.number_input("Room Temperature (°F)", value=70)

st.write(f"**Fridge Temp:** {T_initial}°F | **Target Temp:** {T_target}°F | **Indoor Temp:** {T_room}°F")

# --- Newton's Law of Cooling ---
def calculate_time(T_initial, T_room, T_target, k=0.035):
    if T_target >= T_room:
        return "Wine will not warm up to above room temperature naturally."
    ratio = (T_target - T_room) / (T_initial - T_room)
    if ratio <= 0:
        return "Target temperature already reached or invalid input."
    time_minutes = -np.log(ratio) / k  # time in minutes
    total_seconds = int(time_minutes * 60)
    minutes = total_seconds // 60
    seconds = total_seconds % 60
    return [minutes, seconds]


result = calculate_time(T_initial, T_room, T_target)
st.success(f"Leave your wine out for **{result[0]} minutes, {result[1]} seconds** to reach {T_target}°F.")

# --- Wine chart ---
st.image("wine_chart.jpg")

# --- Equation Display ---
st.markdown("""
### Newton's Law of Cooling:

$$
T(t) = T_{room} + (T_{initial} - T_{room}) e^{-kt}
$$

Where:
- $$(T_{initial})$$: Fridge temperature
- $$(T_{room})$$: Indoor temperature
- $$(k)$$: Cooling constant (estimated as 0.035/minute)
""")
