from matplotlib import pylab as plt
import numpy as np
from typing import Dict, Tuple, List, Optional


def draw_values(data: np.ndarray,
                dx: float,
                labels: Tuple[str, str],
                titles: Optional[Tuple[str, str]] = None,
                draw_data: Tuple[plt.Figure, List[plt.Axes]] = None,
                y_limits: Dict[str, float] = None) \
        -> Tuple[plt.Figure, List[plt.Axes]]:
    xs = np.arange(0, len(data) / 2, 1) * dx
    fig, axes = plt.subplots(nrows=2, ncols=1) if draw_data is None else draw_data

    for index, label in enumerate(labels):
        if y_limits is not None:
            axes[index].set_ylim(bottom=y_limits['u_bot'], top=y_limits['u_top'])
        axes[index].grid(True)
        axes[index].plot(xs, data[index::2], label=label, linewidth='5')
        if titles:
            axes[index].set_title(titles[index])
        axes[index].legend()

    fig.canvas.draw()
    fig.tight_layout()
    return fig, axes
