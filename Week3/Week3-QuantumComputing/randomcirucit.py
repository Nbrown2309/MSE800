from qiskit import QuantumCircuit

# Creating a circuit that requires 3 qubits and 3 classical bits
qc = QuantumCircuit(3,3)

# Add in random gates of my choice
qc.h(0)
qc.x(1)
qc.cx(0, 2)
qc.z(2)
qc.swap(1, 2)

# Measuring all the qubits
qc.measure([0,1,2], [0,1,2])

# Draw the circuit
print(qc.draw())