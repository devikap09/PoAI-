import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt

temperature = np.arange(0, 41, 1)   
fan_speed = np.arange(0, 11, 1)     

temp_low = fuzz.trimf(temperature, [0, 0, 20])
temp_medium = fuzz.trimf(temperature, [10, 20, 30])
temp_high = fuzz.trimf(temperature, [20, 30, 40])

fan_low = fuzz.trimf(fan_speed, [0, 0, 5])
fan_medium = fuzz.trimf(fan_speed, [2, 5, 8])
fan_high = fuzz.trimf(fan_speed, [5, 10, 10])

plt.figure(figsize=(10, 6))

plt.subplot(2, 1, 1)
plt.plot(temperature, temp_low, label='Low')
plt.plot(temperature, temp_medium, label='Medium')
plt.plot(temperature, temp_high, label='High')
plt.title("Temperature Membership Functions")
plt.xlabel("Temperature (°C)")
plt.ylabel("Membership Degree")
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(fan_speed, fan_low, label='Low')
plt.plot(fan_speed, fan_medium, label='Medium')
plt.plot(fan_speed, fan_high, label='High')
plt.title("Fan Speed Membership Functions")
plt.xlabel("Fan Speed")
plt.ylabel("Membership Degree")
plt.legend()

plt.tight_layout()
plt.show()


temperature_input = 28

temp_low_level = fuzz.interp_membership(temperature, temp_low, temperature_input)
temp_medium_level = fuzz.interp_membership(temperature, temp_medium, temperature_input)
temp_high_level = fuzz.interp_membership(temperature, temp_high, temperature_input)

fan_low_level = temp_low_level
fan_medium_level = temp_medium_level
fan_high_level = temp_high_level

# Step 6: Defuzzification - combine the rule outputs and take the centroid
aggregated = (fan_low * fan_low_level
              + fan_medium * fan_medium_level
              + fan_high * fan_high_level)
fan_output = fuzz.defuzz(fan_speed, aggregated, 'centroid')

print(f"Temperature: {temperature_input}°C")
print(f"Membership degrees: Low={temp_low_level:.2f}, "
      f"Medium={temp_medium_level:.2f}, High={temp_high_level:.2f}")
print(f"Defuzzified fan speed: {fan_output:.2f}")
