from neuron import h, gui
import numpy as np
import matplotlib.pyplot as plt

# Set up the simulation environment
h.load_file("stdrun.hoc")
# Time settings
tstop = 1000 # Simulation time in ms
h.tstop = tstop
# Define a dopamine neuron
class DopamineNeuron:
def __init__(self):
self.v = -65 # Membrane potential in mV
self.v_rest = -65 # Resting potential in mV
self.v_thresh = -50 # Threshold for firing in mV
self.v_reset = -70 # Reset potential after spike
self.tau = 10 # Membrane time constant (ms)
self.spikes = [] # Record spike times
self.input_current = 0.0 # Input current
self.t_last_spike = -1 # Last spike time

def update(self, dt, t):
# Desensitization over time: increase threshold as time passes
self.v_thresh += 0.001 # Example desensitization rate
# Integrate the membrane potential
dv = (-self.v + self.v_rest + self.input_current) / self.tau
self.v += dv * dt
# Check for spike
if self.v >= self.v_thresh:
self.spikes.append(t) # Record spike time
self.v = self.v_reset # Reset membrane potential
# Instantiate the dopamine neuron
dopamine_neuron = DopamineNeuron()
# Function to simulate social media rewards (Poisson process)
def social_media_input(t, reward_rate):
if np.random.rand() < reward_rate:
return np.random.uniform(0.5, 1.5) # Random reward magnitude
else:
return 0.0

reward_rate = 0.05 # Probability of receiving a reward at each time step
# Run simulation with social media rewards
dt = 0.1 # Time step in ms
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
