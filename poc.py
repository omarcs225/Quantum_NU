import qiskit
from qiskit_aer import AerSimulator
from qiskit import transpile, QuantumCircuit
from qiskit_aer import noise
from qiskit.quantum_info import Statevector
import math
from qiskit.visualization import plot_histogram, plot_state_city
import time
from rac_simulator import RACSimulator


simulator = RACSimulator()

qc1 = QuantumCircuit(2)
qc1.h(0)
qc1.cx(0,1)
qc1.z(0)
res_, final_state_, qc_ = simulator.run_and_keep(qc1, shots=1024)

print(final_state_)


simulator.reset_state()

qc2 = QuantumCircuit(2)
qc2.h(0)
qc2.cx(0,1)
result, sv1, qc2 = simulator.run_and_keep(qc2, shots=1024)

qc3 = QuantumCircuit(2)
qc3.z(0)
result2, sv2, qc3 = simulator.run_and_keep(qc3, shots=1024)

print(sv2)
