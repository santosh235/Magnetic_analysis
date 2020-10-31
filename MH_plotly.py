# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 19:14:58 2020

@author: santosh
"""

import plotly.express as px
import plotly.io as pio
import plotly.graph_objects as go
import numpy as np



def plotly_plot(x, y_corr, c_sat, T):
    pio.renderers.default='browser'
    fig = go.Figure(data=go.Scatter(x=x, y=y_corr))
    fig.show()