from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit.circuit.library import PhaseGate
from qiskit.visualization import plot_state_qsphere
import matplotlib.pyplot as plt

# Step 1 - Create the 2 qubit phase circuit
qc = QuantumCircuit(2)

# Step 2 - Put qubits into superposistion (so we can see the interferences)
qc.h(0)
qc.h(1)

# Step 3 - Apply 90 degrees phase shift (π/2 radians) to qubit 0
qc.append(PhaseGate(3.14159/2), [0])

# Step 4 - Get final quantum state
state = Statevector.from_instruction(qc)

# Step 5 - Visualize using Q-sphere
plot_state_qsphere(state)
plt.show()