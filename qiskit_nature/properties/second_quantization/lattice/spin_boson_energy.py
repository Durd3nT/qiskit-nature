
from typing import cast, Dict, List, Optional, Tuple

from qiskit_nature.operators.second_quantization import SecondQuantizedOp

from ..second_quantized_property import SecondQuantizedProperty, GroupedSecondQuantizedProperty


class SpinBosonEnergy(SecondQuantizedProperty):

    def __init__(
        self
    ):
        super().__init__(self.__class__.__name__)


    def second_q_ops(self) -> List[SecondQuantizedOp]: # TODO: change return type
        """Returns the (list of) second quantized operators associated with this Property."""
