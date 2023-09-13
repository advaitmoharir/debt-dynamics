# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 22:03:27 2020

@author: Advait Moharir
"""
import pandas as pd
import numpy as np
import plotly.io as pio
pio.renderers.default = "vscode"
import plotly.express as px
import plotly.graph_objects as go
# Get here function

from pyprojroot.here import here

here()
px.defaults.height=500
px.defaults.width=750
#figure-1
data=pd.read_csv('01_data\Fig1.csv')
df=pd.DataFrame(data)

df.dropna()
fig = px.line(df, x='Year', y=['Gross Fiscal Deficit', '3% line'],
              labels={'value':'', 'variable':'', 'Year':''}, 
              line_shape='spline', template='plotly_white')
fig.update_yaxes(tick0=0, tickvals=[0,1,2,3,4,5,6])
fig.update_xaxes(tick0=2004, dtick=2)
fig.update_layout(legend=dict(
    orientation="h",
    yanchor="bottom",
    y=1.02,
    xanchor="right",
    x=1
))
fig.show()
fig.write_image("03_figures/fig1.jpeg",format="jpg", engine="kaleido")

#figure-2

data=pd.read_csv('01_data\Fig2_3.csv')
df1=pd.DataFrame(data)
fig = px.line(df1, x='Year', y=['Debt/GDP', '60% line'], 
              labels={'value':'', 'variable':'', 'Year':''}, 
              line_shape='spline', template='plotly_white')
#fig.update_yaxes(tick0=0.45, dtick=10)
#fig.update_xaxes(tick0=1980, dtick=2)
fig.add_shape(
        # Line Vertical
        dict(
            type="line",
            x0=1991,
            y0=0.45,
            x1=1991,
            y1=0.90,
            line=dict(
                color="Grey",
                width=2
            )
))
fig.add_shape(
        # Line Vertical
        dict(
            type="line",
            x0=1996,
            y0=0.45,
            x1=1996,
            y1=0.90,
            line=dict(
                color="Grey",
                width=2
            )
))
fig.add_shape(
        # Line Vertical
        dict(
            type="line",
            x0=2004,
            y0=0.45,
            x1=2004,
            y1=0.90,
            line=dict(
                color="Grey",
                width=2
            )
))
fig.add_shape(
        # Line Vertical
        dict(
            type="line",
            x0=2010,
            y0=0.45,
            x1=2010,
            y1=0.90,
            line=dict(
                color="Grey",
                width=2
            )
))
fig.update_layout(legend=dict(
    orientation="h",
    yanchor="bottom",
    y=1.02,
    xanchor="right",
    x=1
), yaxis =dict( tickformat= '.0%'))

fig.write_image("03_figures/fig2.jpeg",format="jpg", engine="kaleido")

#Figure 3
data=pd.read_csv('01_data\Fig2_3.csv')
df2=pd.DataFrame(data)
fig = px.line(df2, x='Year', y=['Interest Rate', 'Real Growth', 'Inflation', 'Primary Deficit'], 
              labels={'value':'', 'variable':'', 'Year':''}, 
              line_shape='spline', template='plotly_white')
#fig.add_vline(x=1991)
#fig.update_yaxes(tick0=-0.05, dtick=5)
#fig.update_xaxes(tick0=1980, dtick=2)
fig.add_shape(
        # Line Vertical
        dict(
            type="line",
            x0=1991,
            y0=-0.02,
            x1=1991,
            y1=0.15,
            line=dict(
                color="Grey",
                width=2
            )
))
fig.add_shape(
        # Line Vertical
        dict(
            type="line",
            x0=1996,
            y0=-0.02,
            x1=1996,
            y1=0.15,
            line=dict(
                color="Grey",
                width=2
            )
))
fig.add_shape(
        # Line Vertical
        dict(
            type="line",
            x0=2004,
            y0=-0.02,
            x1=2004,
            y1=0.15,
            line=dict(
                color="Grey",
                width=2
            )
))
fig.add_shape(
        # Line Vertical
        dict(
            type="line",
            x0=2010,
            y0=-0.02,
            x1=2010,
            y1=0.15,
            line=dict(
                color="Grey",
                width=2
            )
))
fig.update_layout(legend=dict(
    orientation="h",
    yanchor="bottom",
    y=1.02,
    xanchor="right",
    x=1
), yaxis =dict( tickformat= '.0%'))

fig.write_image("03_figures/fig3.jpeg",format="jpg", engine="kaleido")

#Figure 4
data=pd.read_csv('01_data\Fig 4.csv')
df3=pd.DataFrame(data)
fig = px.line(df3, x='Year', y=['20% Line', 'Debt/GDP'], 
              labels={'value':'', 'variable':''}, 
              line_shape='spline', template='plotly_white')
#fig.update_yaxes( nticks=10)
#fig.update_xaxes(nticks=20)
fig.update_layout(legend=dict(
    orientation="h",
    yanchor="bottom",
    y=1.02,
    xanchor="right",
    x=1
), yaxis =dict( tickformat= '.0%'))

fig.write_image("03_figures/fig4.jpeg",format="jpg", engine="kaleido")

#Figure 5

data=pd.read_csv('01_data\Fig5_6.csv')
df4=pd.DataFrame(data)
fig = px.line(df4, x='Year', y='Debt/GSDP', 
              labels={'value':'', 'variable':'', 'Debt/GSDP': '', 
                      'Year':''}, 
              line_shape='spline', template='plotly_white')
fig.update_yaxes(nticks=10)
fig.update_xaxes(nticks=10)
fig.update_layout(yaxis =dict( tickformat= '.0%'))
fig.write_image("03_figures/fig5.jpeg",format="jpg", engine="kaleido")

#Figure 6
data=pd.read_csv('01_data\Fig5_6.csv')
df5=pd.DataFrame(data)
fig = px.line(df5, x='Year', y=['Interest Rate', 'Real Growth', 'Inflation', 'Primary Deficit'], 
              labels={'value':'', 'variable':'', 'Year':''}, 
              line_shape='spline', template='plotly_white')
#fig.update_yaxes(tick0=-5, dtick=5)
fig.update_xaxes(tick0=1980, dtick=2)
fig.add_shape(
        # Line Vertical
        dict(
            type="line",
            x0=1991,
            y0=-0.05,
            x1=1991,
            y1=0.20,
            line=dict(
                color="Grey",
                width=2
            )
))
fig.add_shape(
        # Line Vertical
        dict(
            type="line",
            x0=1996,
            y0=-0.05,
            x1=1996,
            y1=0.20,
            line=dict(
                color="Grey",
                width=2
            )
))
fig.add_shape(
        # Line Vertical
        dict(
            type="line",
            x0=2004,
            y0=-0.05,
            x1=2004,
            y1=0.20,
            line=dict(
                color="Grey",
                width=2
            )
))
fig.add_shape(
        # Line Vertical
        dict(
            type="line",
            x0=2013,
            y0=-0.05,
            x1=2013,
            y1=0.20,
            line=dict(
                color="Grey",
                width=2
            )
))
fig.update_layout(legend=dict(
    orientation="h",
    yanchor="bottom",
    y=1.02,
    xanchor="right",
    x=1
), yaxis =dict( tickformat= '.0%'))

fig.write_image("03_figures/fig6.jpeg",format="jpg", engine="kaleido")



#Figure 7

data=pd.read_csv('01_data\Fig7.csv')
df6=pd.DataFrame(data)
fig = px.line(df6, x='Year', y=['AP', 'BH', 'GJ', 'KT', 'MH',
                                'MP', 'RJ', 'TN', 'UP', 'WB'],
              labels={'value':'', 'variable':'', 'Year':'' }, 
              line_shape='spline', template='plotly_white')
#fig.update_yaxes( nticks=10)
#fig.update_xaxes(nticks=20, showgrid=False)
fig.update_layout(yaxis =dict( tickformat= '.0%'))
fig.write_image("03_figures/fig7.jpeg",format="jpg", engine="kaleido")

# Figure 8 generated on Google Sheets

#Figure 9

data=pd.read_csv('01_data\Fig9.csv')
df7=pd.DataFrame(data)
fig = px.line(df7, x='Year', y=['Madhya Pradesh', 'Tamil Nadu'], 
              labels={'value':'', 'variable':'', 'Year':''}, 
              line_shape='spline', template='plotly_white', 
              width=800, height=400)
#fig.update_yaxes(tick0=15, dtick=5)
fig.update_xaxes(tick0=1980, dtick=2)
fig.add_shape(
        # Line Vertical
        dict(
            type="line",
            x0=1991,
            y0=0.15,
            x1=1991,
            y1=0.40,
            line=dict(
                color="Grey",
                width=2
            )
))
fig.add_shape(
        # Line Vertical
        dict(
            type="line",
            x0=1996,
            y0=0.15,
            x1=1996,
            y1=0.40,
            line=dict(
                color="Grey",
                width=2
            )
))
fig.add_shape(
        # Line Vertical
        dict(
            type="line",
            x0=2004,
            y0=0.15,
            x1=2004,
            y1=0.40,
            line=dict(
                color="Grey",
                width=2
            )
))
fig.add_shape(
        # Line Vertical
        dict(
            type="line",
            x0=2013,
            y0=0.15,
            x1=2013,
            y1=0.40,
            line=dict(
                color="Grey",
                width=2
            )
))
fig.update_layout(legend=dict(
    orientation="h",
    yanchor="bottom",
    y=1.02,
    xanchor="right",
    x=1
), yaxis =dict( tickformat= '.0%'))

fig.write_image("03_figures/fig9.jpeg",format="jpg", engine="kaleido")

###########################################################
# Appendix Figures
##########################################################

#AP

data=pd.read_csv('01_data\Figure C1_a.csv')
df5=pd.DataFrame(data)
fig = px.line(df5, x='Year', y=['Debt/GSDP','Interest Rate', 'Real Growth', 'Inflation', 'Primary Deficit'], 
              labels={'value':'', 'variable':'', 'Year':''}, 
              line_shape='spline', template='plotly_white', title= "Andhra Pradesh")
#fig.update_yaxes(tick0=-5, dtick=15)
fig.update_xaxes(tick0=1980, dtick=2)
fig.add_shape(
        # Line Vertical
        dict(
            type="line",
            x0=1991,
            y0=-0.40,
            x1=1991,
            y1=0.60,
            line=dict(
                color="Grey",
                width=2
            )
))
fig.add_shape(
        # Line Vertical
        dict(
            type="line",
            x0=1996,
            y0=-0.40,
            x1=1996,
            y1=0.60,
            line=dict(
                color="Grey",
                width=2
            )
))
fig.add_shape(
        # Line Vertical
        dict(
            type="line",
            x0=2004,
            y0=-0.40,
            x1=2004,
            y1=0.60,
            line=dict(
                color="Grey",
                width=2
            )
))
fig.add_shape(
        # Line Vertical
        dict(
            type="line",
            x0=2013,
            y0=-0.40,
            x1=2013,
            y1=0.60,
            line=dict(
                color="Grey",
                width=2
            )
))
fig.update_layout(legend=dict(
    orientation="h",
    yanchor="bottom",
    y=1.02,
    xanchor="right",
    x=0.5
), yaxis =dict( tickformat= '.0%'))

fig.write_image("03_figures/figc1_a.jpeg",format="jpg", engine="kaleido")

#BH

data=pd.read_csv('01_data\Figure C1_b.csv')
df5=pd.DataFrame(data)
fig = px.line(df5, x='Year', y=['Debt/GSDP','Interest Rate', 'Real Growth'
                                , 'Inflation', 'Primary Deficit'], 
              labels={'value':'', 'variable':'', 'Year':''}, 
              line_shape='spline', template='plotly_white', 
              width=800, height=400, title= "Bihar")
fig.update_yaxes(tick0=-5, dtick=15)
fig.update_xaxes(tick0=1980, dtick=2)
fig.add_shape(
        # Line Vertical
        dict(
            type="line",
            x0=1991,
            y0=-40,
            x1=1991,
            y1=80,
            line=dict(
                color="Grey",
                width=2
            )
))
fig.add_shape(
        # Line Vertical
        dict(
            type="line",
            x0=1996,
            y0=-40,
            x1=1996,
            y1=80,
            line=dict(
                color="Grey",
                width=2
            )
))
fig.add_shape(
        # Line Vertical
        dict(
            type="line",
            x0=2004,
            y0=-40,
            x1=2004,
            y1=80,
            line=dict(
                color="Grey",
                width=2
            )
))
fig.add_shape(
        # Line Vertical
        dict(
            type="line",
            x0=2013,
            y0=-40,
            x1=2013,
            y1=80,
            line=dict(
                color="Grey",
                width=2
            )
))
fig.update_layout(legend=dict(
    orientation="h",
    yanchor="bottom",
    y=1.02,
    xanchor="right",
    x=1
), yaxis =dict( tickformat= '.0%'))

fig.write_image("03_figures/figc1_b.jpeg",format="jpg", engine="kaleido")


#GJ

data=pd.read_csv('01_data\Figure C1_c.csv')
df19=pd.DataFrame(data)
fig = px.line(df19, x='Year',  y=['Debt/GSDP','Interest Rate', 'Real Growth', 'Inflation', 'Primary Deficit'], 
              labels={'value':'', 'variable':'', 'Year':''}, 
              line_shape='spline', template='plotly_white', 
              width=800, height=400, title= "Gujarat")
fig.update_yaxes(tick0=-10, dtick=10)
fig.update_xaxes(tick0=1980, dtick=2)
fig.add_shape(
        # Line Vertical
        dict(
            type="line",
            x0=1991,
            y0=-10,
            x1=1991,
            y1=45,
            line=dict(
                color="Grey",
                width=2
            )
))
fig.add_shape(
        # Line Vertical
        dict(
            type="line",
            x0=1996,
            y0=-10,
            x1=1996,
            y1=45,
            line=dict(
                color="Grey",
                width=2
            )
))
fig.add_shape(
        # Line Vertical
        dict(
            type="line",
            x0=2004,
            y0=-10,
            x1=2004,
            y1=45,
            line=dict(
                color="Grey",
                width=2
            )
))
fig.add_shape(
        # Line Vertical
        dict(
            type="line",
            x0=2013,
            y0=-10,
            x1=2013,
            y1=45,
            line=dict(
                color="Grey",
                width=2
            )
))
fig.update_layout(legend=dict(
    orientation="h",
    yanchor="bottom",
    y=1.02,
    xanchor="right",
    x=1
), yaxis =dict( tickformat= '.0%'))
fig.show()

#KT

data=pd.read_csv('01_data\Figure C1_d.csv')
df20=pd.DataFrame(data)
fig = px.line(df20, x='Year',  y=['Debt/GSDP','Interest Rate', 'Real Growth', 'Inflation', 'Primary Deficit'], 
              labels={'value':'', 'variable':'', 'Year':''}, 
              line_shape='spline', template='plotly_white', 
              width=800, height=400, title= "Karnataka")
fig.update_yaxes(tick0=-5, dtick=10)
fig.update_xaxes(tick0=1980, dtick=2)
fig.add_shape(
        # Line Vertical
        dict(
            type="line",
            x0=1991,
            y0=-10,
            x1=1991,
            y1=45,
            line=dict(
                color="Grey",
                width=2
            )
))
fig.add_shape(
        # Line Vertical
        dict(
            type="line",
            x0=1996,
            y0=-10,
            x1=1996,
            y1=45,
            line=dict(
                color="Grey",
                width=2
            )
))
fig.add_shape(
        # Line Vertical
        dict(
            type="line",
            x0=2004,
            y0=-10,
            x1=2004,
            y1=45,
            line=dict(
                color="Grey",
                width=2
            )
))
fig.add_shape(
        # Line Vertical
        dict(
            type="line",
            x0=2013,
            y0=-10,
            x1=2013,
            y1=45,
            line=dict(
                color="Grey",
                width=2
            )
))
fig.update_layout(legend=dict(
    orientation="h",
    yanchor="bottom",
    y=1.02,
    xanchor="right",
    x=1
), yaxis =dict( tickformat= '.0%'))
fig.show()

#MP

data=pd.read_csv('01_data\Figure C1_e.csv')
df20=pd.DataFrame(data)
fig = px.line(df20, x='Year',  y=['Debt/GSDP','Interest Rate', 'Real Growth', 'Inflation', 'Primary Deficit'], 
              labels={'value':'', 'variable':'', 'Year':''}, 
              line_shape='spline', template='plotly_white', 
              width=800, height=400, title= "Madhya Pradesh")
fig.update_yaxes(tick0=-5, dtick=10)
fig.update_xaxes(tick0=1980, dtick=2)
fig.add_shape(
        # Line Vertical
        dict(
            type="line",
            x0=1991,
            y0=-10,
            x1=1991,
            y1=45,
            line=dict(
                color="Grey",
                width=2
            )
))
fig.add_shape(
        # Line Vertical
        dict(
            type="line",
            x0=1996,
            y0=-10,
            x1=1996,
            y1=45,
            line=dict(
                color="Grey",
                width=2
            )
))
fig.add_shape(
        # Line Vertical
        dict(
            type="line",
            x0=2004,
            y0=-10,
            x1=2004,
            y1=45,
            line=dict(
                color="Grey",
                width=2
            )
))
fig.add_shape(
        # Line Vertical
        dict(
            type="line",
            x0=2013,
            y0=-10,
            x1=2013,
            y1=45,
            line=dict(
                color="Grey",
                width=2
            )
))
fig.update_layout(legend=dict(
    orientation="h",
    yanchor="bottom",
    y=1.02,
    xanchor="right",
    x=1
), yaxis =dict( tickformat= '.0%'))
fig.show()

#MH

data=pd.read_csv('01_data\Figure C1_f.csv')
df20=pd.DataFrame(data)
fig = px.line(df20, x='Year',  y=['Debt/GSDP','Interest Rate', 'Real Growth', 'Inflation', 'Primary Deficit'], 
              labels={'value':'', 'variable':'', 'Year':''}, 
              line_shape='spline', template='plotly_white', 
              width=800, height=400, title= "Maharashtra")
fig.update_yaxes(tick0=-5, dtick=10)
fig.update_xaxes(tick0=1980, dtick=2)
fig.add_shape(
        # Line Vertical
        dict(
            type="line",
            x0=1991,
            y0=-5,
            x1=1991,
            y1=35,
            line=dict(
                color="Grey",
                width=2
            )
))
fig.add_shape(
        # Line Vertical
        dict(
            type="line",
            x0=1996,
            y0=-5,
            x1=1996,
            y1=35,
            line=dict(
                color="Grey",
                width=2
            )
))
fig.add_shape(
        # Line Vertical
        dict(
            type="line",
            x0=2004,
            y0=-5,
            x1=2004,
            y1=35,
            line=dict(
                color="Grey",
                width=2
            )
))
fig.add_shape(
        # Line Vertical
        dict(
            type="line",
            x0=2013,
            y0=-5,
            x1=2013,
            y1=35,
            line=dict(
                color="Grey",
                width=2
            )
))
fig.update_layout(legend=dict(
    orientation="h",
    yanchor="bottom",
    y=1.02,
    xanchor="right",
    x=1
), yaxis =dict( tickformat= '.0%'))
fig.show()

#RJ

data=pd.read_csv('01_data\Figure C1_g.csv')
df20=pd.DataFrame(data)
fig = px.line(df20, x='Year',  y=['Debt/GSDP','Interest Rate', 'Real Growth', 'Inflation', 'Primary Deficit'], 
              labels={'value':'', 'variable':'', 'Year':''}, 
              line_shape='spline', template='plotly_white', 
              width=800, height=400, title= "Rajasthan")
fig.update_yaxes(tick0=-10, dtick=10)
fig.update_xaxes(tick0=1980, dtick=2)
fig.add_shape(
        # Line Vertical
        dict(
            type="line",
            x0=1991,
            y0=-10,
            x1=1991,
            y1=60,
            line=dict(
                color="Grey",
                width=2
            )
))
fig.add_shape(
        # Line Vertical
        dict(
            type="line",
            x0=1996,
            y0=-10,
            x1=1996,
            y1=60,
            line=dict(
                color="Grey",
                width=2
            )
))
fig.add_shape(
        # Line Vertical
        dict(
            type="line",
            x0=2004,
            y0=-10,
            x1=2004,
            y1=60,
            line=dict(
                color="Grey",
                width=2
            )
))
fig.add_shape(
        # Line Vertical
        dict(
            type="line",
            x0=2013,
            y0=-10,
            x1=2013,
            y1=60,
            line=dict(
                color="Grey",
                width=2
            )
))
fig.update_layout(legend=dict(
    orientation="h",
    yanchor="bottom",
    y=1.02,
    xanchor="right",
    x=1
), yaxis =dict( tickformat= '.0%'))
fig.show()

#TN
data=pd.read_csv('01_data\Figure C1_h.csv')
df20=pd.DataFrame(data)
fig = px.line(df20, x='Year',  y=['Debt/GSDP','Interest Rate', 'Real Growth', 'Inflation', 'Primary Deficit'], 
              labels={'value':'', 'variable':'', 'Year':''}, 
              line_shape='spline', template='plotly_white', 
              width=800, height=400, title= "Tamil Nadu")
fig.update_yaxes(tick0=-10, dtick=10)
fig.update_xaxes(tick0=1980, dtick=2)
fig.add_shape(
        # Line Vertical
        dict(
            type="line",
            x0=1991,
            y0=-10,
            x1=1991,
            y1=35,
            line=dict(
                color="Grey",
                width=2
            )
))
fig.add_shape(
        # Line Vertical
        dict(
            type="line",
            x0=1996,
            y0=-10,
            x1=1996,
            y1=35,
            line=dict(
                color="Grey",
                width=2
            )
))
fig.add_shape(
        # Line Vertical
        dict(
            type="line",
            x0=2004,
            y0=-10,
            x1=2004,
            y1=35,
            line=dict(
                color="Grey",
                width=2
            )
))
fig.add_shape(
        # Line Vertical
        dict(
            type="line",
            x0=2013,
            y0=-10,
            x1=2013,
            y1=35,
            line=dict(
                color="Grey",
                width=2
            )
))
fig.update_layout(legend=dict(
    orientation="h",
    yanchor="bottom",
    y=1.02,
    xanchor="right",
    x=1
), yaxis =dict( tickformat= '.0%'))
fig.show()

#UP

data=pd.read_csv('01_data\Figure C1_i.csv')
df20=pd.DataFrame(data)
fig = px.line(df20, x='Year',  y=['Debt/GSDP','Interest Rate', 'Real Growth', 'Inflation', 'Primary Deficit'], 
              labels={'value':'', 'variable':'', 'Year':''}, 
              line_shape='spline', template='plotly_white', 
              width=800, height=400, title= "Uttar Pradesh")
fig.update_yaxes(tick0=-10, dtick=10)
fig.update_xaxes(tick0=1980, dtick=2)
fig.add_shape(
        # Line Vertical
        dict(
            type="line",
            x0=1991,
            y0=-10,
            x1=1991,
            y1=60,
            line=dict(
                color="Grey",
                width=2
            )
))
fig.add_shape(
        # Line Vertical
        dict(
            type="line",
            x0=1996,
            y0=-10,
            x1=1996,
            y1=60,
            line=dict(
                color="Grey",
                width=2
            )
))
fig.add_shape(
        # Line Vertical
        dict(
            type="line",
            x0=2004,
            y0=-10,
            x1=2004,
            y1=60,
            line=dict(
                color="Grey",
                width=2
            )
))
fig.add_shape(
        # Line Vertical
        dict(
            type="line",
            x0=2013,
            y0=-10,
            x1=2013,
            y1=60,
            line=dict(
                color="Grey",
                width=2
            )
))
fig.update_layout(legend=dict(
    orientation="h",
    yanchor="bottom",
    y=1.02,
    xanchor="right",
    x=1
), yaxis =dict( tickformat= '.0%'))
fig.show()

#WB

data=pd.read_csv('01_data\Figure C1_j.csv')
df20=pd.DataFrame(data)
fig = px.line(df20, x='Year',  y=['Debt/GSDP','Interest Rate', 'Real Growth', 'Inflation', 'Primary Deficit'], 
              labels={'value':'', 'variable':'', 'Year':''}, 
              line_shape='spline', template='plotly_white', 
              width=800, height=400, title= "West Bengal")
fig.update_yaxes(tick0=-10, dtick=10)
fig.update_xaxes(tick0=1980, dtick=2)
fig.add_shape(
        # Line Vertical
        dict(
            type="line",
            x0=1991,
            y0=-10,
            x1=1991,
            y1=60,
            line=dict(
                color="Grey",
                width=2
            )
))
fig.add_shape(
        # Line Vertical
        dict(
            type="line",
            x0=1996,
            y0=-10,
            x1=1996,
            y1=60,
            line=dict(
                color="Grey",
                width=2
            )
))
fig.add_shape(
        # Line Vertical
        dict(
            type="line",
            x0=2004,
            y0=-10,
            x1=2004,
            y1=60,
            line=dict(
                color="Grey",
                width=2
            )
))
fig.add_shape(
        # Line Vertical
        dict(
            type="line",
            x0=2013,
            y0=-10,
            x1=2013,
            y1=60,
            line=dict(
                color="Grey",
                width=2
            )
))
fig.update_layout(legend=dict(
    orientation="h",
    yanchor="bottom",
    y=1.02,
    xanchor="right",
    x=1
), yaxis =dict( tickformat= '.0%'))
fig.show()









