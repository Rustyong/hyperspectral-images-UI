# This file is part of spectralUI.
#
# Copyright 2021, Tom George Ampiath, All rights reserved.
#
# spectralUI is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# spectralUI is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with spectralUI.  If not, see <http://www.gnu.org/licenses/>.

import matplotlib
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure

from spectralUI import cachedvariables as cv

matplotlib.use("Qt5Agg")


class CmapPreview(FigureCanvasQTAgg):
    """Widget for previewing various color maps"""

    def __init__(self):
        self.fig = Figure(figsize=(5, 1))
        self.axes = self.fig.add_subplot(111)
        super().__init__(self.fig)

        self.fig.tight_layout()

        self.update_canvas()

    def update_canvas(self):
        """Function to update the color map preview canvas"""
        self.axes.clear()

        col_map = matplotlib.pyplot.get_cmap(cv.CURRENT_CMAP)
        matplotlib.colorbar.ColorbarBase(
            self.axes, cmap=col_map, orientation="horizontal"
        )
        self.draw()
