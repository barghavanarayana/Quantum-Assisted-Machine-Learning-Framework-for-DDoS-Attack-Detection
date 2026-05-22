 # quantum_model.py

from qiskit import QuantumCircuit
from qiskit_aer import Aer
from qiskit.compiler import transpile

def quantum_ddos_predict(value):
    qc = QuantumCircuit(1, 1)

    # Encode classical input into qubit
    if value > 0.5:
        qc.x(0)

    qc.h(0)
    qc.measure(0, 0)

    backend = Aer.get_backend('qasm_simulator')
    job = backend.run(transpile(qc, backend), shots=1024)
    result = job.result()
    counts = result.get_counts()

    if counts.get('1', 0) > counts.get('0', 0):
        return "Quantum Prediction: DDoS Attack"
    else:
        return "Quantum Prediction: Normal Traffic"
