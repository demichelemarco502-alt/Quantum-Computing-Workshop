#installation of qiskit framework, form which I'll create the quantum circuit

!uv pip install 'iqm-client[qiskit]==29.14' matplotlib pylatexenc --quiet

%pip install lagrangeclient --index-url https://gitlab.linksfoundation.com/api/v4/projects/1709/packages/pypi/simple

from qiskit import QuantumCircuit

bell = QuantumCircuit(2) # create a quantum circuit with 2 qubits

bell.h(0)           # apply an H gate to the circuit
bell.cx(0,1)        # apply a CNOT gate to the circuit

bell.measure_all()  # measure the qubits

bell.draw(output="mpl")

!lagrangeclient  #access token to use the quantum computer

#I connect to the quantum computer
from iqm.qiskit_iqm import IQMProvider

provider = IQMProvider(url="https://spark.quantum.linksfoundation.com/station", token=access_token)
lagrange_backend = provider.get_backend()

#I perform the measurement 1024 times, using the quantum computer through the function transpile, that optimize my circuit to fit the specific quantum hardware, which is the lagrange.
from qiskit import transpile
from qiskit.visualization import plot_histogram

t_bell = transpile(bell, backend=lagrange_backend)

job = lagrange_backend.run(t_bell, shots=1024)
print(job.job_id())

result = job.result()

plot_histogram(result.get_counts())
