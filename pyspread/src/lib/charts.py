#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright Martin Manns
# Distributed under the terms of the GNU General Public License

# --------------------------------------------------------------------
# pyspread is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# pyspread is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with pyspread. If not, see <http://www.gnu.org/licenses/>.
# --------------------------------------------------------------------

"""
charts
======

Provides matplotlib figure that are chart templates

Provides
--------

* PlotFigure: Plot figure class

"""

from matplotlib.figure import Figure


class PlotFigure(Figure):
    """Plot figure class with drawing method"""

    def __init__(self, **chart_data):
        self.chart_data = chart_data
        Figure.__init__(self, (5.0, 4.0), facecolor="white")
        self.__axes = self.add_subplot(111)
        self.draw_chart()

    def draw_chart(self):
        """Plots chart from self.chart_data.clear"""

        # xdata and ydata is extracted and handled separately
        try:
            ydata = self.chart_data.pop("ydata")
        except KeyError:
            ydata = []

        # Check xdata length
        if "xdata" in self.chart_data and \
           len(self.chart_data["xdata"]) != len(ydata):
            # Wrong length --> ignore xdata
            self.chart_data.pop("xdata")

        # Clear the axes and redraw the plot anew

        self.__axes.clear()
        self.__axes.plot(ydata, **self.chart_data)