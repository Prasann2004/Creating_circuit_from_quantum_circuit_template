from qiskit import QuantumCircuit
from qiskit.circuit import Parameter

#Bind parameters

# make a template circuit
qc = QuantumCircuit(3)#initializing 3 qubits
qc.initialize([0,0,0,0,0,0,0,1])#initializing state vector

param0 = Parameter("angle0")
param1 = Parameter("angle1")
param2 = Parameter("angle2")

qc.h(0)#placing hadamard gate
qc.h(1)#placing hadamard gate
qc.h(2)#placing hadamard gate

qc.p(param0,0)#placing a phase gate having variable parameter
qc.p(param1,1)#placing a phase gate having variable parameter
qc.p(param2,2)#placing a phase gate having variable parameter

#making circuit from the template
qcinstance = qc.bind_parameters({param0:0.0 ,param1:0.1 ,param2:0.2})
qcinstance.draw(output="mpl") 