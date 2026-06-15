import numpy as np
from numpy.typing import NDArray
from typing import Tuple


class Solution:
    def backward(self, x: NDArray[np.float64], w: NDArray[np.float64], b: float, y_true: float) -> Tuple[NDArray[np.float64], float]:
        # x: 1D input array
        # w: 1D weight array
        # b: scalar bias
        # y_true: true target value
        #
        # Forward: z = dot(x, w) + b, y_hat = sigmoid(z)
        # Loss: L = 0.5 * (y_hat - y_true)^2
        # Return: (dL_dw rounded to 5 decimals, dL_db rounded to 5 decimals)
        #forward pass
        z=np.dot(x,w)+b
        s=1/(1+np.exp(-z))
        #common gradient terms
        d=(s-y_true)*s*(1-s)
        #gradients
        dl_dw=d*x
        dl_db=d
        dl_dw=np.round(dl_dw,5)
        dl_db=round(float(dl_db),5)
        return dl_dw,dl_db