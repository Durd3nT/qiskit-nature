"""The Spin-Boson Problem class"""

from typing import cast, Callable, Dict, List, Optional, Tuple, Union
import numpy as np

from qiskit_nature.operators.second_quantization import SecondQuantizedOp

from ..base_problem import BaseProblem


class SpinBosonProblem(BaseProblem):
    """Spin-Boson Problem"""

    # TODO: TypeError when inheriting BaseProblem.. need driver?

    def __init__(
        self,
        num_particles: Union[int, List[int]],
        excitation_cutoff: Union[int, List[int]],
        hamil_params: Dict[str, Union[List[float], float]],
        coupling: Optional[str],
    ):
        """
        Args:
            num_particles: If supplied as array, [number of spins, number of bosonic modes],
                           otherwise this variable sets the number of bosonic modes and the number
                           of spins is set to 1
            excitation_cutoff: number of possible excitations per bosonic mode, including the
                               ground state (i.e., if 2, there is the ground state plus the first
                               excited state). Can be distinct for each bosonic mode if supplied as
                               array of len(number of bosonic modes)
            hamil_params: Hamiltonian parameters such as coupling strength, etc. The dictionary
                          must contain the keys 'boson_self_en', 'spin_self_en', 'spin_tunnel',
                          'coupling_const' and can either be floats or arrays of
                          len(number of bosonic modes)
            coupling: whether the spin-boson coupling is via Pauli(X), Pauli(Y) or Pauli(Z), e.g.,
                      'X'
        """

        if isinstance(num_particles, int):
            self._num_particles = [1, num_particles]
        elif len(num_particles) == 2:
            self._num_particles = num_particles
        else:
            raise ValueError('num_particles must be int'
                             'or array of the form [num_spins, num_bosons]')

        if (not isinstance(excitation_cutoff, int)
                and not len(excitation_cutoff) == self._num_particles[1]:)
            raise ValueError('excitation_cutoff must be int or array of len(number of bosons)')
        else:
            self._excitation_cutoff = excitation_cutoff

        hamil_keys = ['boson_self_en', 'spin_self_en', 'spin_tunnel', 'coupling_const']
        if all(key in hamil_params for key in hamil_keys):
            # TODO: add check for length of arrays,
            #       e.g., len(coupling_const) == self._num_particles[0]*self._num_particles[1]
            self._hamil_params = hamil_params
        else:
            raise ValueError('must give value to all of the following keys: {}'.format(hamil_keys))

        if coupling in ['X', 'Y', 'Z']:
            self._coupling = coupling
        else:
            raise ValueError('coupling must be either of "X", "Y", "Z"')



    def second_q_ops(self) -> List[SecondQuantizedOp]:
        """
        Returns:
            A list of `SecondQuantizedOp` in the following order: Hamiltonian operator
            TODO: add * particle number operators
                      * spin orientation operator
        """
        return None


    def hopping_qeom_ops(self):
        return None

    def interpret(self):
        return None

    def get_default_filter_criterion(self):
        return None
