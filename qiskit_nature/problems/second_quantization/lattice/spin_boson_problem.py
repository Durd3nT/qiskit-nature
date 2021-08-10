"""The Spin-Boson Problem class"""


from ..base_problem import BaseProblem


class SpinBosonProblem(BaseProblem):
    """Spin-Boson Problem"""

    def __init__(
        self
    ):
        """
        Args:

        """



    def second_q_ops(self) -> List[SecondQuantizedOp]:
        """
        Returns:
            A list of `SecondQuantizedOp` in the following order: Hamiltonian operator
            TODO: add * particle number operators
                      * spin orientation operator
        """
        return None
