from neuron import h, gui
import numpy as np
import matplotlib.pyplot as plt

h.load_file("stdrun.hoc")
# Time settings
tstop = 5000 # Increased simulation time to 5000 ms
h.tstop = tstop
# Define the dopamine neuron for non-attached individuals
class DopamineNeuron:
def __init__(self):
self.v = -65 # Membrane potential in mV
self.v_rest = -65 # Resting potential in mV
self.v_thresh = -50 # Reduced threshold for easier firing
self.v_reset = -65 # Reset potential after spike
self.tau = 5 # Reduced membrane time constant (faster integration)
self.spikes = [] # Record spike times
self.input_current = 0.0 # Input current
self.t_last_spike = -1 # Last spike time
def update(self, dt, t):
# Integrate the membrane potential
dv = (-self.v + self.v_rest + self.input_current) / self.tau
self.v += dv * dt
# Check for spike
if self.v >= self.v_thresh:
self.spikes.append(t) # Record spike time
self.v = self.v_reset # Reset membrane potential
# Instantiate the dopamine neuron for non-attached individuals
dopamine_neuron = DopamineNeuron()
# Function to simulate social media rewards (Poisson process)
def social_media_input(t, reward_rate):
if np.random.rand() < reward_rate:
return np.random.uniform(10.0, 20.0) # Increased reward magnitude significantly
else:
return 0.0
reward_rate = 0.1 # Increased reward rate for more frequent inputs
# Run simulation with social media rewards
dt = 0.05 # Finer time step
times = np.arange(0, tstop, dt)
membrane_potentials = []
spike_times = []
input_currents = []
for t in times:
# Update social media reward input
dopamine_neuron.input_current = social_media_input(t, reward_rate)
input_currents.append(dopamine_neuron.input_current)
# Update the neuron
dopamine_neuron.update(dt, t)
# Record membrane potential and spike times
membrane_potentials.append(dopamine_neuron.v)
if t in dopamine_neuron.spikes:
spike_times.append(t)
# Plot the results
plt.figure(figsize=(12, 6))
# Plot membrane potential
plt.subplot(2, 1, 1)
plt.plot(times, membrane_potentials, label='Membrane Potential (mV)')
plt.axhline(y=dopamine_neuron.v_thresh, color='r', linestyle='--', label='Threshold')
plt.xlabel('Time (ms)')
plt.ylabel('Membrane Potential (mV)')
plt.legend()
# Plot input current
plt.subplot(2, 1, 2)
plt.plot(times, input_currents, label='Social Media Input (Current)')
plt.xlabel('Time (ms)')
plt.ylabel('Input Current (nA)')
plt.legend()
plt.tight_layout()
plt.show()
