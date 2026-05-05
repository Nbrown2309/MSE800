from qiskit import transpile
from qiskit_aer import AerSimulator
import qiskit.qasm2

# Step 1 - QASM circuit
qasm_code = """
OPENQASM 2.0;
include "qelib1.inc";

qreg q[2];
creg c[2];

h q[0];
cx q[0], q[1];

measure q -> c;
"""

# Step 2 - Convert QASM -> Qiskit circuit
qc = qiskit.qasm2.loads(qasm_code)

# Step 3 - Run simulation
simulator = AerSimulator()
compiled = transpile(qc, simulator)
result = simulator.run(compiled, shots=1024).result()

# Step 4: Output results
print(result.get_counts())