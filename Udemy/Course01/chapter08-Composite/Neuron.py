from typing import List
from abc import ABC
from collections.abc import Iterable


class Connectable(Iterable, ABC):

    def connect(self, other):
        if self is other:
            return

        for s in self:
            for o in other:
                s.outputs.append(o)
                o.inputs.append(s)


class Neuron(Connectable):
    def __init__(self, name: str):
        self.name = name
        self.inputs: List[Neuron] = []
        self.outputs: List[Neuron] = []

    def __iter__(self):
        yield self

    def __str__(self):
        return f'{self.name}, {len(self.inputs)} inputs, {len(self.outputs)} outputs'

    # def connect(self, other: Neuron):
    #     self.outputs.append(other)
    #     self.other.inputs.append(self)


class NeuronLayer(list, Connectable):
    def __init__(self, name: str, count: int):
        super().__init__()
        self.name: str = name
        for x in range(0, count):
            self.append(Neuron(f'{self.name}-{x}'))
    
    def __str__(self):
        return f'{self.name} with {len(self)} Neurons'


# def connect_to(self: Neuron, other: Neuron):
#     if self is other:
#         return

#     for s in self:
#         for o in other:
#             s.outputs.append(o)
#             o.inputs.append(s)



if __name__ == "__main__":
    n1 = Neuron('n1')
    n2 = Neuron('n2')

    layer1 = NeuronLayer('L1', 3)
    layer2 = NeuronLayer('L2', 4)

    # Neuron.connect = connect_to
    # NeuronLayer.connect = connect_to

    n1.connect(n2)
    n1.connect(layer1)
    layer1.connect(n2)
    layer1.connect(layer2)

    print(n1)
    print(n2)
    print(layer1)
    print(layer2)