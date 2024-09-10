from qiskit_aer import AerSimulator
from qiskit import transpile, QuantumCircuit

class RACSimulator(AerSimulator):
    def __init__(self, method='statevector', configuration=None, properties=None, provider=None, target=None, **backend_options):
        super().__init__(method=method, configuration=configuration, properties=properties, provider=provider,
                         target=target, **backend_options)
        self.__init_state = None

    def run_and_keep(self, qc_i, shots=1024, noise=0, noise_model=None):
        simulator=AerSimulator()
        if noise == 0:
            qc = QuantumCircuit(qc_i.num_qubits)
            if self.__init_state != None:
                qc.set_statevector(self.__init_state)
            qc.compose(qc_i, inplace=True, front=False)
            qc.save_statevector()
            qc = transpile(qc, simulator)
            result = simulator.run(qc, shots=shots).result()
            output_state = result.get_statevector(qc)

        elif noise == 1:
            qc = QuantumCircuit(qc_i.num_qubits)
            if self.__init_state != None:
                qc.set_density_matrix(self.__init_state)
            qc.compose(qc_i,inplace=True,front=False)
            qc.save_density_matrix()
            qc = transpile(qc, simulator)
            result = simulator.run(qc, shots=shots, noise_model=noise_model).result()
            output_state = result.data(0)['density_matrix']

        self.__init_state = output_state

        return result, output_state, qc
    
    def reset_state(self):
        self.__init_state = None
