#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  6 03:28:51 2022

@author: bayan
"""

#from jupyter_dash import JupyterDash
import dash


from dash import dcc
from dash import html
#import dash_core_components as dcc
#import dash_html_components as html
from dash_table import DataTable
from dash_table import FormatTemplate

from dash.dependencies import Input, Output

import pandas as pd

import plotly.express as px
from datetime import datetime

import csv
import numpy as np

yahoo_logo = 'https://raw.githubusercontent.com//Bayan2019/TCC/main/Yahoo-Finance-3.png'
tcc_logo = 'https://raw.githubusercontent.com//Bayan2019/TCC/main/Logo_Curve_BG-Blue1.png'

CaaSWalletIPhone_bg = 'url(https://raw.githubusercontent.com//Bayan2019/TCC_Dashboard/main/pictures/CaaSWallet2_2.png)'

InventoryCard = 'url(https://raw.githubusercontent.com/Bayan2019/TCC_Dashboard/main/pictures/InventoryCard.png)'
FactoringCard = 'url(https://raw.githubusercontent.com/Bayan2019/TCC_Dashboard/main/pictures/FactoringCard.png)'
SupplierCard = 'url(https://raw.githubusercontent.com/Bayan2019/TCC_Dashboard/main/pictures/SupplierCard.png)'

TCC = 'url(https://raw.githubusercontent.com/Bayan2019/TCC_Dashboard/main/pictures/Logo_Curve_BG-Blue1.png)'
header = 'url(https://raw.githubusercontent.com/Bayan2019/TCC_Dashboard/main/pictures/Header.png)'
Finance3 = 'url(https://raw.githubusercontent.com/Bayan2019/TCC_Dashboard/main/pictures/Finance3.png)'

ebitda = 'url(https://raw.githubusercontent.com/Bayan2019/TCC_Dashboard/main/pictures/ebitda2.png)'
debt = 'url(https://raw.githubusercontent.com/Bayan2019/TCC_Dashboard/main/pictures/debt2.png)'
wc = 'url(https://raw.githubusercontent.com/Bayan2019/TCC_Dashboard/main/pictures/WORKINGCAPITAL.png)'
revenue = 'url(https://raw.githubusercontent.com/Bayan2019/TCC_Dashboard/main/pictures/Revenue.jpeg)'
GP = 'url(https://raw.githubusercontent.com/Bayan2019/TCC_Dashboard/main/pictures/GrossProfit.png)'
cash = 'url(https://raw.githubusercontent.com/Bayan2019/TCC_Dashboard/main/pictures/cash2.png)'
yahoo = 'url(https://raw.githubusercontent.com/Bayan2019/TCC_Dashboard/main/pictures/Yahoo.png)'
inventory = 'url(https://raw.githubusercontent.com/Bayan2019/TCC_Dashboard/main/pictures/inventory.png)'

# Data Files

ucr_csv_annual = 'https://raw.githubusercontent.com/Bayan2019/TCC_Dashboard/main/Files_of_Data/fs_annual_ws.csv'
ucr_csv_annual_new = 'https://raw.githubusercontent.com/Bayan2019/TCC_Dashboard/main/Files_of_Data/fs_annual_new_ws.csv'
ucr_csv_quartal = 'https://raw.githubusercontent.com/Bayan2019/TCC_Dashboard/main/Files_of_Data/fs_quartal_ws.csv'

df_annual = pd.read_csv(ucr_csv_annual)
df_annual_new = pd.read_csv(ucr_csv_annual_new)
df_quartal = pd.read_csv(ucr_csv_quartal)

ucr_csv_annual_usd = 'https://raw.githubusercontent.com/Bayan2019/TCC_Dashboard/main/Files_of_Data/fs_annual_usd_ws.csv'
ucr_csv_annual_new_usd = 'https://raw.githubusercontent.com/Bayan2019/TCC_Dashboard/main/Files_of_Data/fs_annual_new_usd_ws.csv'
ucr_csv_quartal_usd = 'https://raw.githubusercontent.com/Bayan2019/TCC_Dashboard/main/Files_of_Data/fs_quartal_usd_ws.csv'

df_annual_usd = pd.read_csv(ucr_csv_annual_usd)
df_annual_new_usd = pd.read_csv(ucr_csv_annual_new_usd)
df_quartal_usd = pd.read_csv(ucr_csv_quartal_usd)

src1 = 'https://raw.githubusercontent.com/Bayan2019/TCC_Dashboard/main/Files_of_Data/list_comp_fs_yahoo_ws.csv'

tickers = pd.read_csv(src1)

ucr_ratios = 'https://raw.githubusercontent.com/Bayan2019/TCC_Dashboard/main/Files_of_Data/fs_annual_new_ratios.csv'

ratios = pd.read_csv(ucr_ratios)

Big_df_annual = df_annual
Big_df_annual = Big_df_annual.drop(['ticker', 'date', 'name', 'sector', 'subsector',
                                    'currency'], axis=1)

All_columns0 = list(Big_df_annual.columns)

Big_df_annual = df_annual
Big_df_annual = Big_df_annual.drop(['name', 'sector', 'subsector',
                                    'currency'], axis=1)

Big_df_melt = pd.melt(Big_df_annual, id_vars=['date', 'ticker'])
Big_df_melt = Big_df_melt.dropna()

All_columns = []

for col in All_columns0:
    if (col in list(Big_df_melt['variable'])): All_columns.append(col)

All_columns_pos = []

for col in All_columns:
    if (Big_df_annual[col].dropna() > 0.1).all(): All_columns_pos.append(col)

All_columns_pos1 = All_columns_pos + ['inventory_to_assets']

options_period = [{'label': 'Annual', 'value': 'annual'}, {'label': 'Quartal', 'value': 'quarterly'}]

options_ticker = [{'label': tickers.loc[i, 'name'],
                   'value': tickers.loc[i, 'ticker']}
                  for i in tickers.sort_values(['name']).index]

options_columns = [{'label': col, 'value': col} for col in All_columns]

options_columns_pos = [{'label': col, 'value': col} for col in All_columns_pos]

options_columns_pos1 = [{'label': col, 'value': col} for col in All_columns_pos1]

options_tickers_exclude = [tickers.loc[i, 'ticker'] for i in tickers.index]

sectors_exclude = list(tickers['sector'].dropna().unique())
sectors_exclude.sort()
sectors_table = pd.DataFrame({'Sectors': sectors_exclude})

sectors_focus = sectors_exclude + ['All']
sectors_focus.sort()

subsectors_exclude = list(tickers['subsector'].dropna().unique())
subsectors_exclude.sort()

subsectors_focus = subsectors_exclude + ['All']
subsectors_focus.sort()

countries_exclude = list(tickers['country'].dropna().unique())
countries_exclude.sort()

countries_focus = countries_exclude + ['All']
countries_focus.sort()

tickers_geo = tickers[['ticker', 'name', 'country', 'latitude', 'longitude']].dropna()

tickers_geo.index = range(tickers_geo.shape[0])

geo_tickers_exclude = DataTable(
    id='geo_tickers_exclude',
    columns=[{'name': 'ticker', 'id': 'ticker'},
             {'name': 'name', 'id': 'name'},
             {'name': 'country', 'id': 'country'}],
    data=tickers_geo.to_dict('records'),
    cell_selectable=False,
    sort_action='native',
    filter_action='native',
    page_action='native',
    page_current=0,
    page_size=12,
    row_selectable='multi',
    style_cell=({'textAlign': 'left', 'background-color': 'rgb(254, 163, 27)', 'color': 'rgb(6, 0, 45)'}),
    style_header={'background-color': 'rgb(6, 0, 45)', 'color': 'rgb(254, 163, 27)'},
    style_data={'whiteSpace': 'normal', 'height': 'auto'}
)

geo_tickers_focus = DataTable(
    id='geo_tickers_focus',
    columns=[{'name': 'ticker', 'id': 'ticker'},
             {'name': 'name', 'id': 'name'},
             {'name': 'country', 'id': 'country'}],
    data=tickers_geo.to_dict('records'),
    cell_selectable=False,
    sort_action='native',
    filter_action='native',
    page_action='native',
    page_current=0,
    page_size=2,
    row_selectable='single',
    style_cell=({'textAlign': 'left', 'background-color': 'rgb(254, 163, 27)', 'color': 'rgb(6, 0, 45)'}),
    style_header={'background-color': 'rgb(6, 0, 45)', 'color': 'rgb(254, 163, 27)'},
    style_data={'whiteSpace': 'normal', 'height': 'auto'}
)

treemap_tickers_exclude = DataTable(
    id='treemap_tickers_exclude',
    columns=[{'name': 'ticker', 'id': 'ticker'}, {'name': 'name', 'id': 'name'},
             {'name': 'sector', 'id': 'sector'}, {'name': 'subsector', 'id': 'subsector'},
             {'name': 'Country', 'id': 'country'}],
    data=tickers.to_dict('records'),
    cell_selectable=False,
    sort_action='native',
    filter_action='native',
    page_action='native',
    page_current=0,
    page_size=3,
    row_selectable='multi',
    style_cell=({'textAlign': 'left', 'background-color': 'rgb(254, 163, 27)', 'color': 'rgb(6, 0, 45)'}),
    style_header={'background-color': 'rgb(6, 0, 45)', 'color': 'rgb(254, 163, 27)'},
    style_data={'whiteSpace': 'normal', 'height': 'auto'}
)


def get_title(ticker):
    df = tickers.set_index('ticker')
    title = df.loc[ticker, 'name']

    return title


def plot_style(paper_bg='black', plot_bg='rgb(82, 82, 82)', font='rgb(205, 133, 0)'):
    plot_style = {'paper_bgcolor': paper_bg, 'plot_bgcolor': plot_bg,
                  'font': {'color': font}}
    return plot_style

# Create the Dash app
app = dash.Dash(__name__)

app.layout = html.Div([
    html.Header(
        children=[
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
            html.H1('Financial Statement', style={'color': 'rgb(254, 163, 27)', 'fontSize': 70,
                                                  'display': 'inline-block'})],
        style={'width': '1400px', 'height': '400px',
               'background-image': header, 'background-repeat': 'no-repeat',
               'background-position': 'center', 'background-size': '1400px 400px'}),

    # Overall Summary
    dcc.Tabs(
        id="tabs_common_summary", value='tab_globus_data',
        className='custom-tabs', vertical=False,
        children=[
            dcc.Tab(label='Globus', value='tab_globus_data', className='custom-tab',
                    selected_className='custom-tab--selected'),
            dcc.Tab(label='Scatter Figures', value='tab_scatter_figures', className='custom-tab',
                    selected_className='custom-tab--selected'),
            dcc.Tab(label='Treemaps', value='tab_treemaps', className='custom-tab',
                    selected_className='custom-tab--selected'),
            dcc.Tab(label='Comparison Bars', value='tab_bars', className='custom-tab',
                    selected_className='custom-tab--selected'),
        ], style={'height': '44px'}),
    html.Br(),
    html.Div(id='tabs_common_summary_content'),
    html.Br(),

    # Individual Summary
    dcc.Tabs(
        id="tabs_individual_summary", value='tab_scatter_bars',
        className='custom-tabs', vertical=False,
        children=[
            dcc.Tab(label='Scatter and Bars', value='tab_scatter_bars', className='custom-tab',
                    selected_className='custom-tab--selected'),
            dcc.Tab(label='Scatter Figures', value='tab_scatter_figs', className='custom-tab',
                    selected_className='custom-tab--selected'),
            dcc.Tab(label='TCC', value='tab_tcc', className='custom-tab',
                    selected_className='custom-tab--selected'),
        ], style={'height': '44px'}),
    html.Br(),
    html.Div(id='tabs_individual_summary_content'),
    html.Br(),

    # Closing
    html.Img(src=tcc_logo, style={'width': '250px', 'display': 'inline-block', 'margin': '0px 60px 0px 60px'}),
    html.Span(
        children=[
            f"Prepared on {(datetime.now().date()).strftime('%B %d, %Y')}",
            html.Br(),
            'by ', html.B('Bayan Saparbayeva'),
            html.Br(),
            html.B('Alexandre Courtois Auberger'),
            html.Br(),
            'and ', html.B('Daksha Daniel'),
            html.Br(),
            html.Br(), ],
        style={'text-align': 'center', 'font-size': 22, 'display': 'inline-block'}),
    html.Img(src=tcc_logo, style={'width': '250px', 'display': 'inline-block', 'margin': '0px 60px 0px 60px'})],
    style={'text-align': 'center', 'display': 'inline-block', 'width': '100%',
           'background-color': 'black', 'color': 'rgb(254, 163, 27)'})


# Overall Summary tabs

@app.callback(
    Output('tabs_common_summary_content', 'children'),
    Input('tabs_common_summary', 'value')
)
def render_common_content(tab):
    if tab == 'tab_globus_data':
        return html.Div(
            children=[
                html.Div(
                    children=[
                        html.Div(
                            children=[
                                html.H3('Select Volume Column'),
                                dcc.Dropdown(id='geo_column_v', options=options_columns_pos,
                                             value='totalAssets',
                                             style={'width': '300px', 'margin': '0 auto',
                                                    'color': 'blue', 'verticalAlign': 'top'}),
                                html.H3('Select Color Column'),
                                dcc.Dropdown(id='geo_column_c', options=options_columns,
                                             value='inventory',
                                             style={'width': '300px', 'margin': '0 auto',
                                                    'color': 'blue', 'verticalAlign': 'top'})],
                            style={'width': '330px', 'height': '300px', 'display': 'inline-block',
                                   'margin': '0px 10px 0px 10px', 'verticalAlign': 'top'}),
                        html.Div(
                            children=[
                                html.H3('Organization to Focus'),
                                geo_tickers_focus], style={'width': '500px', 'height': '300px',
                                                           'display': 'inline-block', 'verticalAlign': 'top',
                                                           'margin': '0px 10px 0px 10px'}),
                        html.Div(
                            children=[
                                html.H3('Country to Focus'),
                                dcc.Dropdown(id='geo_countries_focus', options=countries_focus, value='All',
                                             style={'width': '230px', 'margin': '0 auto', 'color': 'blue'})],
                            style={'width': '250px', 'height': '300px', 'display': 'inline-block',
                                   'margin': '0px 10px 0px 10px', 'verticalAlign': 'top'})],
                    style={'width': '1200px', 'height': '300px', 'display': 'inline-block'}),
                html.Div(
                    children=[
                        dcc.Graph(id='geo', style={'width': '700px', 'height': '700px', 'display': 'inline-block'}),
                        html.Div(
                            children=[
                                html.H3('Organization to Exclude'),
                                geo_tickers_exclude],
                            style={'width': '480px', 'height': '680px',
                                   'display': 'inline-block', 'margin': '5px 5px 5px 5px',
                                   'verticalAlign': 'top'})],
                    style={'width': '1200px', 'height': '700px', 'display': 'inline-block'})])

    elif tab == 'tab_scatter_figures':
        # Scatter plot for all Data with additional data
        return html.Div(children=[
            # Debt_Rev
            html.Div(
                children=[
                    dcc.Graph(id='Debt_Rev_fig',
                              style={'width': '600px', 'height': '550px', 'display': 'inline-block'}),
                    html.Div(
                        children=[
                            html.H3('Sector to Focus'),
                            dcc.Dropdown(id='debt_rev_sectors_focus', options=sectors_focus,
                                         value='All', style={'width': '250px', 'margin': '0 auto',
                                                             'color': 'blue', 'horizontalAlign': 'left'}),
                            html.H3('Subsector to Focus'),
                            dcc.Dropdown(id='debt_rev_subsectors_focus', options=subsectors_focus,
                                         value='All', style={'width': '250px', 'margin': '0 auto',
                                                             'color': 'blue', 'horizontalAlign': 'left'}),
                            html.H3('Organizations to Exclude'),
                            dcc.Dropdown(id='Debt_Rev_tickers',
                                         options=options_tickers_exclude, value=[], multi=True)],
                        style={'width': '450px', 'height': '550px', 'display': 'inline-block',
                               'vertical-align': 'top', 'border': '1px solid black', 'padding': '20px',
                               'background-image': ebitda, 'background-repeat': 'no-repeat',
                               'background-position': 'center', 'background-size': '450px 550px'})],
                style={'width': '1200px', 'height': '550px', 'display': 'inline-block'}),
            # Debt_EBITDA
            html.Div(
                children=[
                    html.Div(
                        children=[
                            html.H3('Sector to Focus'),
                            dcc.Dropdown(id='debt_ebitda_sectors_focus', options=sectors_focus,
                                         value='All', style={'width': '250px', 'margin': '0 auto',
                                                             'color': 'blue', 'horizontalAlign': 'left'}),
                            html.H3('Subsector to Focus'),
                            dcc.Dropdown(id='debt_ebitda_subsectors_focus', options=subsectors_focus,
                                         value='All', style={'width': '250px', 'margin': '0 auto',
                                                             'color': 'blue', 'horizontalAlign': 'left'}),
                            html.H3('Organizations to Exclude'),
                            dcc.Dropdown(id='Debt_EBITDA_tickers',
                                         options=options_tickers_exclude, value=[], multi=True)],
                        style={'width': '450px', 'height': '550px', 'display': 'inline-block',
                               'vertical-align': 'top', 'border': '1px solid black', 'padding': '20px',
                               'background-image': debt, 'background-repeat': 'no-repeat',
                               'background-position': 'center', 'background-size': '450px 550px'}),
                    dcc.Graph(id='Debt_EBITDA_fig',
                              style={'width': '600px', 'height': '550px', 'display': 'inline-block'})],
                style={'width': '1200px', 'height': '550px', 'display': 'inline-block'}),
            # WC_Rev
            html.Div(
                children=[
                    dcc.Graph(id='WC_Rev_fig',
                              style={'width': '600px', 'height': '550px', 'display': 'inline-block'}),
                    html.Div(
                        children=[
                            html.H3('Sector to Focus'),
                            dcc.Dropdown(id='wc_rev_sectors_focus', options=sectors_focus,
                                         value='All', style={'width': '250px', 'margin': '0 auto',
                                                             'color': 'blue', 'horizontalAlign': 'left'}),
                            html.H3('Subsector to Focus'),
                            dcc.Dropdown(id='wc_rev_subsectors_focus', options=subsectors_focus,
                                         value='All', style={'width': '250px', 'margin': '0 auto',
                                                             'color': 'blue', 'horizontalAlign': 'left'}),
                            html.H3('Organizations to Exclude'),
                            dcc.Dropdown(id='WC_Rev_tickers',
                                         options=options_tickers_exclude, value=[], multi=True)],
                        style={'width': '450px', 'height': '550px', 'display': 'inline-block',
                               'vertical-align': 'top', 'border': '1px solid black', 'padding': '20px',
                               'background-image': wc, 'background-repeat': 'no-repeat',
                               'background-position': 'center', 'background-size': '450px 550px'})],
                style={'width': '1200px', 'height': '550px', 'display': 'inline-block'}),
            # WC_Inv
            html.Div(
                children=[
                    html.Div(
                        children=[
                            html.H3('Sector to Focus'),
                            dcc.Dropdown(id='wc_inv_sectors_focus', options=sectors_focus,
                                         value='All', style={'width': '250px', 'margin': '0 auto',
                                                             'color': 'blue', 'horizontalAlign': 'left'}),
                            html.H3('Subsector to Focus'),
                            dcc.Dropdown(id='wc_inv_subsectors_focus', options=subsectors_focus,
                                         value='All', style={'width': '250px', 'margin': '0 auto',
                                                             'color': 'blue', 'horizontalAlign': 'left'}),
                            html.H3('Organizations to Exclude'),
                            dcc.Dropdown(id='WC_Inv_tickers',
                                         options=options_tickers_exclude, value=[], multi=True)],
                        style={'width': '450px', 'height': '550px', 'display': 'inline-block',
                               'vertical-align': 'top', 'border': '1px solid black', 'padding': '20px',
                               'background-image': inventory, 'background-repeat': 'no-repeat',
                               'background-position': 'center', 'background-size': '450px 550px'}),
                    dcc.Graph(id='WC_Inv_fig',
                              style={'width': '600px', 'height': '550px', 'display': 'inline-block'})],
                style={'width': '1200px', 'height': '550px', 'display': 'inline-block'}),
            # Inv_Rev
            html.Div(
                children=[
                    html.Div(
                        children=[
                            html.H3('Sector to Focus'),
                            dcc.Dropdown(id='inv_rev_sectors_focus', options=sectors_focus,
                                         value='All', style={'width': '250px', 'margin': '0 auto',
                                                             'color': 'blue', 'horizontalAlign': 'left'}),
                            html.H3('Subsector to Focus'),
                            dcc.Dropdown(id='inv_rev_subsectors_focus', options=subsectors_focus,
                                         value='All', style={'width': '250px', 'margin': '0 auto',
                                                             'color': 'blue', 'horizontalAlign': 'left'}),
                            html.H3('Period'),
                            dcc.Dropdown(id='Inv_Rev_period', options=options_period, value='annual',
                                         style={'width': '150px', 'margin': '0 auto', 'color': 'blue',
                                                'verticalAlign': 'top'}),
                            html.H3('Organizations to Exclude'),
                            dcc.Dropdown(id='Inv_Rev_tickers',
                                         options=options_tickers_exclude, value=[], multi=True)],
                        style={'width': '450px', 'height': '450px', 'display': 'inline-block',
                               'vertical-align': 'top', 'border': '1px solid black', 'padding': '20px',
                               'background-image': revenue, 'background-repeat': 'no-repeat',
                               'background-position': 'center', 'background-size': '450px 350px'}),
                    dcc.Graph(id='Inv_Rev_fig',
                              style={'width': '600px', 'height': '550px', 'display': 'inline-block'})],
                style={'width': '1200px', 'height': '550px', 'display': 'inline-block'}),
            # Inv_Cash
            html.Div(
                children=[
                    dcc.Graph(id='Inv_Cash_fig',
                              style={'width': '600px', 'height': '550px', 'display': 'inline-block'}),
                    html.Div(
                        children=[
                            html.H3('Sector to Focus'),
                            dcc.Dropdown(id='inv_cash_sectors_focus', options=sectors_focus,
                                         value='All', style={'width': '250px', 'margin': '0 auto',
                                                             'color': 'blue', 'horizontalAlign': 'left'}),
                            html.H3('Subsector to Focus'),
                            dcc.Dropdown(id='inv_cash_subsectors_focus', options=subsectors_focus,
                                         value='All', style={'width': '250px', 'margin': '0 auto',
                                                             'color': 'blue', 'horizontalAlign': 'left'}),
                            html.H3('Period'),
                            dcc.Dropdown(id='Inv_Cash_period', options=options_period, value='annual',
                                         style={'width': '150px', 'margin': '0 auto', 'color': 'blue',
                                                'verticalAlign': 'top'}),
                            html.H3('Organization to Exclude'),
                            dcc.Dropdown(id='Inv_Cash_tickers',
                                         options=options_tickers_exclude, value=[], multi=True)],
                        style={'width': '450px', 'height': '450px', 'display': 'inline-block',
                               'vertical-align': 'top', 'border': '1px solid black', 'padding': '20px',
                               'background-image': GP, 'background-repeat': 'no-repeat',
                               'background-position': 'center', 'background-size': '450px 350px'})],
                style={'width': '1200px', 'height': '550px', 'display': 'inline-block'}),
            # Gross_pr_Inv
            html.Div(
                children=[
                    html.Div(
                        children=[
                            html.H3('Sector to Focus'),
                            dcc.Dropdown(id='gross_pr_inv_sectors_focus', options=sectors_focus,
                                         value='All', style={'width': '250px', 'margin': '0 auto',
                                                             'color': 'blue', 'horizontalAlign': 'left'}),
                            html.H3('Subsector to Focus'),
                            dcc.Dropdown(id='gross_pr_inv_subsectors_focus', options=subsectors_focus,
                                         value='All', style={'width': '250px', 'margin': '0 auto',
                                                             'color': 'blue', 'horizontalAlign': 'left'}),
                            html.H3('Period'),
                            dcc.Dropdown(id='Gross_pr_Inv_period', options=options_period, value='annual',
                                         style={'width': '150px', 'margin': '0 auto', 'color': 'blue',
                                                'verticalAlign': 'top'}),
                            html.H3('Organizations to Exclude'),
                            dcc.Dropdown(id='Gross_pr_Inv_tickers',
                                         options=options_tickers_exclude, value=[], multi=True)],
                        style={'width': '450px', 'height': '450px', 'display': 'inline-block',
                               'vertical-align': 'top', 'border': '1px solid black', 'padding': '20px',
                               'background-image': cash, 'background-repeat': 'no-repeat',
                               'background-position': 'center', 'background-size': '450px 350px'}),
                    dcc.Graph(id='Gross_pr_Inv_fig',
                              style={'width': '600px', 'height': '550px', 'display': 'inline-block'})],
                style={'width': '1200px', 'height': '550px', 'display': 'inline-block'}),
            # Gross_pr_Rev
            html.Div(
                children=[
                    dcc.Graph(id='Gross_pr_Rev_fig',
                              style={'width': '600px', 'height': '550px', 'display': 'inline-block'}),
                    html.Div(
                        children=[
                            html.H3('Sector to Focus'),
                            dcc.Dropdown(id='gross_pr_rev_sectors_focus', options=sectors_focus,
                                         value='All', style={'width': '250px', 'margin': '0 auto',
                                                             'color': 'blue', 'horizontalAlign': 'left'}),
                            html.H3('Subsector to Focus'),
                            dcc.Dropdown(id='gross_pr_rev_subsectors_focus', options=subsectors_focus,
                                         value='All', style={'width': '250px', 'margin': '0 auto',
                                                             'color': 'blue', 'horizontalAlign': 'left'}),
                            html.H3('Period'),
                            dcc.Dropdown(id='Gross_pr_Rev_period', options=options_period, value='annual',
                                         style={'width': '150px', 'margin': '0 auto', 'color': 'blue',
                                                'verticalAlign': 'top'}),
                            html.H3('Organization to Exclude'),
                            dcc.Dropdown(id='Gross_pr_Rev_tickers',
                                         options=options_tickers_exclude, value=[], multi=True)],
                        style={'width': '450px', 'height': '450px', 'display': 'inline-block',
                               'vertical-align': 'top', 'border': '1px solid black', 'padding': '20px',
                               'background-image': yahoo, 'background-repeat': 'no-repeat',
                               'background-position': 'center', 'background-size': '450px 350px'})],
                style={'width': '1200px', 'height': '550px', 'display': 'inline-block'}), ])

    elif tab == 'tab_treemaps':
        return html.Div(
            children=[
                html.Div(
                    children=[
                        html.Div(
                            children=[
                                html.H3('Period'),
                                dcc.Dropdown(id='treemap_period', options=options_period,
                                             value='annual',
                                             style={'width': '150px', 'margin': '0 auto',
                                                    'color': 'blue', 'verticalAlign': 'top'}),
                            ], style={'width': '150px', 'height': '98px',
                                      'margin': '0px 10px 0px 10px', 'display': 'inline-block'}),
                        html.Div(
                            children=[
                                html.H3('Select Volume Column'),
                                dcc.Dropdown(id='treemap_column_v', options=options_columns_pos1,
                                             value='inventory_to_assets',
                                             style={'width': '300px', 'margin': '0 auto',
                                                    'color': 'blue', 'verticalAlign': 'top'}),
                            ], style={'width': '300px', 'height': '98px',
                                      'margin': '0px 10px 0px 10px', 'display': 'inline-block'}),
                        html.Div(
                            children=[
                                html.H3('Select Color Column'),
                                dcc.Dropdown(id='treemap_column_c', options=options_columns,
                                             value='inventory',
                                             style={'width': '300px', 'margin': '0 auto',
                                                    'color': 'blue', 'verticalAlign': 'top'}),
                            ], style={'width': '300px', 'height': '98px',
                                      'margin': '0px 10px 0px 10px', 'display': 'inline-block'})
                    ], style={'width': '810px', 'height': '98px', 'display': 'inline-block'}),
                # Treemap 1
                dcc.Graph(id='treemap1'),
                # TreeMap Control
                html.Div(
                    children=[
                        html.Div(
                            children=[
                                html.H3('Sector to Focus'),
                                dcc.Dropdown(id='treemap_sectors_focus', options=sectors_focus,
                                             value='All', style={'width': '290px', 'margin': '0 auto',
                                                                 'color': 'blue', 'horizontalAlign': 'left'}),
                                html.H3('Subsector to Focus'),
                                dcc.Dropdown(id='treemap_subsectors_focus', options=subsectors_focus,
                                             value='All', style={'width': '290px', 'margin': '0 auto',
                                                                 'color': 'blue', 'horizontalAlign': 'left'}), ],
                            style={'width': '300px', 'height': '300px', 'display': 'inline-block',
                                   'margin': '0px 5px 0px 5px', 'verticalAlign': 'top'}),
                        html.Div(
                            children=[
                                html.H3('Organizations to Exclude'),
                                treemap_tickers_exclude],
                            #                  dcc.Dropdown(id='treemap_tickers', options=tickers.ticker.unique(), value=[], multi=True)],
                            style={'width': '750px', 'display': 'inline-block',
                                   'margin': '0px 5px 0px 5px', 'verticalAlign': 'top'}),
                        html.Div(
                            children=[
                                html.H3('Country to Focus'),
                                dcc.Dropdown(id='treemap_countries_focus', options=countries_focus, value='All',
                                             style={'width': '230px', 'margin': '0 auto', 'color': 'blue'}),
                            ],
                            style={'width': '250px', 'height': '300px', 'vertical-align': 'top',
                                   'margin': '0px 5px 0px 5px', 'display': 'inline-block'})],
                    style={'width': '1400px', 'height': '300px', 'display': 'inline-block',
                           'border': '1px solid black'}),
                # Treemap 2
                dcc.Graph(id='treemap2'), ])

    elif tab == 'tab_bars':
        return html.Div(
            children=[
                # Bar plot for comparison different companies's attributes
                html.Div(
                    children=[
                        html.Div(
                            children=[
                                html.H3('Organizations to Consider'),
                                dcc.Dropdown(id='bar_columns_tickers', options=tickers.ticker.unique(),
                                             value=['JCI', 'FLOW'], multi=True),
                                html.H3('Period'),
                                dcc.Dropdown(id='bar_columns_period', options=options_period, value='annual',
                                             style={'width': '150px', 'margin': '0 auto', 'color': 'blue',
                                                    'verticalAlign': 'top'}),
                                html.H3('Columns to Consider'),
                                dcc.Dropdown(id='bar_columns_columns',
                                             options=All_columns, value=['inventory', 'cash'], multi=True)],
                            style={'width': '300px', 'height': '450px', 'display': 'inline-block',
                                   'vertical-align': 'top', 'border': '1px solid black', 'padding': '20px',
                                   'background-image': Finance3, 'background-repeat': 'no-repeat',
                                   'background-position': 'center', 'background-size': '290px 230px'}),
                        html.Div(
                            children=[dcc.Graph(id='bar_columns')],
                            style={'width': '800px', 'display': 'inline-block'})],
                    style={'width': '1400px', 'display': 'inline-block',
                           'border': '1px solid black'}),
                # Bar plot for comparison different companies's ratios (dio, dpo, dso)
                html.Div(
                    children=[
                        html.Div(
                            children=[dcc.Graph(id='ratios1')],
                            style={'width': '800px', 'display': 'inline-block'}),
                        html.Div(
                            children=[
                                html.H3('Organizations to Include'),
                                dcc.Dropdown(id='ratios1_tickers', options=tickers.ticker.unique(),
                                             value=['JCI', 'AAL'], multi=True)],
                            style={'width': '300px', 'height': '450px', 'display': 'inline-block',
                                   'vertical-align': 'top', 'border': '1px solid black', 'padding': '20px',
                                   'background-image': InventoryCard, 'background-repeat': 'no-repeat',
                                   'background-position': 'center', 'background-size': '290px 230px'})],
                    style={'width': '1400px', 'display': 'inline-block',
                           'border': '1px solid black'}),
                # Bar plot for comparison ratios (CCC, InventoryTurnover)
                html.Div(
                    children=[
                        html.Div(
                            children=[
                                html.H3('Organizations to Include'),
                                dcc.Dropdown(id='ratios2_tickers', options=tickers.ticker.unique(),
                                             value=['JCI', 'SANM'], multi=True)],
                            style={'width': '300px', 'height': '450px', 'display': 'inline-block',
                                   'vertical-align': 'top', 'border': '1px solid black', 'padding': '20px',
                                   'background-image': FactoringCard, 'background-repeat': 'no-repeat',
                                   'background-position': 'center', 'background-size': '290px 230px'}),
                        html.Div(
                            children=[dcc.Graph(id='ratios2')],
                            style={'width': '800px', 'display': 'inline-block'})],
                    style={'width': '1400px', 'display': 'inline-block',
                           'border': '1px solid black'}),
                # Bar plot for comparison different companies's ratios (ROCE, ROIC)
                html.Div(
                    children=[
                        html.Div(
                            children=[dcc.Graph(id='ratios3')],
                            style={'width': '800px', 'display': 'inline-block'}),
                        html.Div(
                            children=[
                                html.H3('Organizations to Include'),
                                dcc.Dropdown(id='ratios3_tickers', options=tickers.ticker.unique(),
                                             value=['JCI', 'AAL'], multi=True)],
                            style={'width': '300px', 'height': '450px', 'display': 'inline-block',
                                   'vertical-align': 'top', 'border': '1px solid black', 'padding': '20px',
                                   'background-image': SupplierCard, 'background-repeat': 'no-repeat',
                                   'background-position': 'center', 'background-size': '290px 230px'})],
                    style={'width': '1400px', 'display': 'inline-block',
                           'border': '1px solid black'}), ])


# Individual summary tabs

@app.callback(
    Output('tabs_individual_summary_content', 'children'),
    Input('tabs_individual_summary', 'value')
)
def render_individual_content(tab):
    if tab == 'tab_scatter_bars':
        return html.Div(
            children=[
                # Control Scatter and Bar plots
                html.Div(
                    children=[
                        html.Div(
                            children=[
                                html.Br(),
                                html.Br(),
                                html.H3('Organization'),
                                dcc.Dropdown(id='scatter_bar_ticker',
                                             options=options_ticker, value='JCI',
                                             style={'width': '350px', 'margin': '0 auto', 'color': 'blue',
                                                    'verticalAlign': 'top'}),
                                html.Br(),
                                html.Br(),
                                html.H3('Period'),
                                dcc.Dropdown(id='scatter_bar_period',
                                             options=options_period, value='annual',
                                             style={'width': '300px', 'margin': '0 auto',
                                                    'color': 'blue', 'verticalAlign': 'top'}),
                                html.Br(),
                                html.H3('y-axis'),
                                dcc.Dropdown(id='column_y', options=options_columns, value='totalAssets',
                                             style={'width': '300px', 'margin': '0 auto',
                                                    'color': 'blue', 'verticalAlign': 'top'}),
                                html.Br(),
                                html.H3('ColorMap'),
                                dcc.Dropdown(id='column_c', options=options_columns, value='totalLiab',
                                             style={'width': '300px', 'margin': '0 auto',
                                                    'color': 'blue', 'verticalAlign': 'top'}),
                                html.Br(),
                                html.H3('Radius'),
                                dcc.Dropdown(id='column_r', options=options_columns_pos,
                                             value='cash',
                                             style={'width': '300px', 'margin': '0 auto',
                                                    'color': 'blue', 'verticalAlign': 'top'})],
                            style={'width': '500px', 'height': '700px', 'color': 'rgb(205, 102, 0)',
                                   'display': 'inline-block', 'verticalAlign': 'top',
                                   'background-image': CaaSWalletIPhone_bg, 'background-repeat': 'no-repeat',
                                   'background-position': 'center', 'background-size': '500px 700px'}),
                        # Scatter and Bar plots
                        html.Div(
                            children=[
                                dcc.Graph(id='scatter_fig', style={'width': '700px'}),
                                dcc.Graph(id='bar_fig1', style={'width': '700px'})],
                            style={'width': '850px', 'height': '700px', 'display': 'inline-block'})],
                    style={'display': 'inline-block', 'vertical-align': 'center'}),
                dcc.Graph(id='bar_fig2'), ])
    elif tab == 'tab_scatter_figs':
        # Scatter plots
        return html.Div(children=[
            # Scatter plots with additional data
            html.Div(
                children=[
                    html.Div(
                        children=[
                            html.H3('Organization'),
                            dcc.Dropdown(id='scatters_ticker1', options=options_ticker, value='JCI',
                                         style={'width': '550px', 'margin': '0 auto', 'color': 'blue'})],
                        style={'display': 'inline-block', 'margin': '0px 10px 0px 10px'})],
                style={'width': '1400px', 'height': '120px',
                       'display': 'inline-block', 'border': '1px solid black'}),
            # Scatter figures 1
            html.Div(
                children=[
                    dcc.Graph(id='debt_rev_fig',
                              style={'width': '600px', 'height': '400px', 'display': 'inline-block'}),
                    dcc.Graph(id='debt_ebitda_fig',
                              style={'width': '600px', 'height': '400px', 'display': 'inline-block'})],
                style={'width': '1200px', 'height': '400px', 'display': 'inline-block'}),
            html.Div(
                children=[
                    dcc.Graph(id='wc_rev_fig',
                              style={'width': '600px', 'height': '400px', 'display': 'inline-block'}),
                    dcc.Graph(id='wc_inv_fig',
                              style={'width': '600px', 'height': '400px', 'display': 'inline-block'})],
                style={'width': '1200px', 'height': '400px', 'display': 'inline-block'}),
            # Scatter plots without additional data
            html.Div(
                children=[
                    html.Div(
                        children=[
                            html.H3('Organization'),
                            dcc.Dropdown(id='scatters_ticker2', options=options_ticker, value='JCI',
                                         style={'width': '550px', 'margin': '0 auto', 'color': 'blue'})],
                        style={'display': 'inline-block', 'margin': '0px 10px 0px 10px'}),
                    html.Div(
                        children=[
                            html.H3('Period'),
                            dcc.Dropdown(id='scatters_period', options=options_period, value='annual',
                                         style={'width': '250px', 'margin': '0 auto', 'color': 'blue',
                                                'verticalAlign': 'top'})],
                        style={'display': 'inline-block', 'margin': '0px 10px 0px 10px'})],
                style={'width': '1400px', 'height': '120px',
                       'display': 'inline-block', 'border': '1px solid black'}),
            # Scatter figures 2
            html.Div(
                children=[
                    dcc.Graph(id='inv_rev_fig',
                              style={'width': '600px', 'height': '400px', 'display': 'inline-block'}),
                    dcc.Graph(id='inv_cash_fig',
                              style={'width': '600px', 'height': '400px', 'display': 'inline-block'})],
                style={'width': '1200px', 'height': '400px', 'display': 'inline-block'}),
            html.Div(
                children=[
                    dcc.Graph(id='gross_pr_inv_fig',
                              style={'width': '600px', 'height': '400px', 'display': 'inline-block'}),
                    dcc.Graph(id='gross_pr_rev_fig',
                              style={'width': '600px', 'height': '400px', 'display': 'inline-block'})],
                style={'width': '1200px', 'height': '400px', 'display': 'inline-block'}), ])
    elif tab == 'tab_tcc':
        # Scatter plot for all Data with additional data
        return html.Div(children=[
            # TCC 1 ()
            html.Div(
                children=[
                    html.H3('Organization'),
                    dcc.Dropdown(id='tcc1_ticker', options=options_ticker, value='JCI',
                                 style={'width': '550px', 'margin': '0 auto', 'color': 'blue'})],
                style={'display': 'inline-block', 'margin': '0px 10px 0px 10px'}),
            html.Div(
                children=[
                    html.Center(
                        children=[
                            html.Br(),
                            html.Br(),
                            html.H3('Degree of Involvement'),
                            dcc.Slider(id='tcc1_slider', min=0, max=1,
                                       marks=None, value=1 / 2, step=1 / 100, vertical=True,
                                       tooltip={"placement": "right", "always_visible": True})],
                        style={'width': '200px', 'height': '600px', 'vertical-align': 'top',
                               'display': 'inline-block'}),
                    html.Div(
                        children=[
                            dcc.Graph(id='tcc1_scatter',
                                      style={'width': '900px', 'height': '300px', 'display': 'inline-block'}),
                            dcc.Graph(id='tcc2_scatter',
                                      style={'width': '900px', 'height': '250px', 'display': 'inline-block'})],
                        style={'width': '900px', 'height': '600px', 'display': 'inline-block'})],
                style={'display': 'inline-block', 'vertical-align': 'center'}),
            # TCC 2 ()
            html.Div(
                children=[
                    html.H3('Organizations to Consider'),
                    dcc.Dropdown(id='tcc3_ticker', options=options_tickers_exclude,
                                 value=['JCI', 'SANM'], multi=True)],
                style={'width': '550px', 'display': 'inline-block', 'margin': '0px 10px 0px 10px'}),
            html.Div(
                children=[
                    html.Center(
                        children=[
                            html.Br(),
                            html.H3('Degree of Involvement'),
                            dcc.Slider(id='tcc3_slider', min=0, max=99 / 100, value=1 / 2,
                                       marks=None, step=1 / 100, vertical=True,
                                       tooltip={"placement": "right", "always_visible": True})],
                        style={'width': '200px', 'height': '600px', 'vertical-align': 'top',
                               'display': 'inline-block', 'horizontal-align': 'right'}),
                    html.Div(
                        children=[
                            dcc.Graph(id='tcc3_bar',
                                      style={'width': '900px', 'display': 'inline-block'})],
                        style={'width': '900px', 'display': 'inline-block'})],
                style={'display': 'inline-block', 'vertical-align': 'center'}),
            # TCC 3 ()
            html.Div(
                children=[
                    html.H3('Organizations to Consider'),
                    dcc.Dropdown(id='tcc4_ticker', options=options_tickers_exclude,
                                 value=['JCI', 'SANM'], multi=True)],
                style={'width': '550px', 'display': 'inline-block', 'margin': '0px 10px 0px 10px'}),
            html.Div(
                children=[
                    html.Center(
                        children=[
                            html.Br(),
                            html.H3('Degree of Involvement'),
                            dcc.Slider(id='tcc4_slider', min=0, max=99 / 100, value=1 / 2, marks=None,
                                       step=1 / 100, vertical=True,
                                       tooltip={"placement": "right", "always_visible": True})],
                        style={'width': '200px', 'height': '600px',
                               'vertical-align': 'top', 'display': 'inline-block',
                               'horizontal-align': 'right'}),
                    html.Div(
                        children=[
                            dcc.Graph(id='tcc4_bar',
                                      style={'width': '900px', 'display': 'inline-block'})],
                        style={'width': '900px', 'display': 'inline-block'})],
                style={'display': 'inline-block', 'vertical-align': 'center'}),
            # TCC 4 ()
            html.Div(
                children=[
                    html.H3('Organizations to Consider'),
                    dcc.Dropdown(id='tcc5_ticker', options=options_tickers_exclude,
                                 value=['JCI', 'SANM'], multi=True)],
                style={'width': '550px', 'display': 'inline-block', 'margin': '0px 10px 0px 10px'}),
            html.Div(
                children=[
                    html.Center(
                        children=[
                            html.Br(),
                            html.H3('Degree of Involvement'),
                            dcc.Slider(id='tcc5_slider', min=0, max=99 / 100, value=1 / 2,
                                       marks=None, step=1 / 100, vertical=True,
                                       tooltip={"placement": "right", "always_visible": True})],
                        style={'width': '200px', 'height': '600px',
                               'vertical-align': 'top', 'display': 'inline-block',
                               'horizontal-align': 'right'}),
                    html.Div(
                        children=[
                            dcc.Graph(id='tcc5_bar',
                                      style={'width': '900px', 'display': 'inline-block'})],
                        style={'width': '900px', 'display': 'inline-block'})],
                style={'display': 'inline-block', 'vertical-align': 'center'}), ])


# Geo plot

@app.callback(
    Output(component_id='geo', component_property='figure'),
    Input(component_id='geo_column_v', component_property='value'),
    Input(component_id='geo_column_c', component_property='value'),
    Input(component_id='geo_tickers_focus', component_property='selected_rows'),
    Input(component_id='geo_tickers_exclude', component_property='selected_rows'),
    Input(component_id='geo_countries_focus', component_property='value')
)
def update_geo(column_v, column_c, tick, ticks, country):
    df = df_annual_usd

    if ticks:
        tickers_list = list(tickers_geo.loc[ticks, 'ticker'])
    else:
        tickers_list = []

    if (country == 'All'):

        df = df[['name', 'ticker', 'longitude', 'latitude', column_v, column_c, 'date2']].dropna()

    else:
        df = df[['name', 'ticker', 'longitude', 'latitude', column_v, column_c, 'date2']].dropna()
        tickers_list0 = list(tickers_geo[tickers_geo['country'] == country]['ticker'])

        df = df[df.ticker.isin(tickers_list0)]

    df.sort_values(by=['date2'], inplace=True)

    ddf = df[~df.ticker.isin(tickers_list)]

    geo_fig = px.scatter_geo(ddf,
                             lat="latitude", lon="longitude", color=column_c,
                             color_continuous_scale='RdYlGn_r',
                             animation_frame="date2",
                             hover_name="name",
                             hover_data=['ticker', 'name'],
                             size=np.array(ddf[column_v]),
                             size_max=35,
                             projection="orthographic")
    geo_fig.update_layout(geo=dict(
        resolution=50,
        showland=True,
        showcountries=True,
        showocean=True,
        showrivers=True,
        showsubunits=True,
        countrywidth=0.5,
        landcolor='rgb(105, 139, 105)',
        lakecolor='rgb(151, 255, 255)',
        oceancolor='rgb(151, 255, 255)', subunitcolor='rgb(254, 163, 27)', subunitwidth=1))
    geo_fig.update_geos(bgcolor='black', rivercolor='rgb(151, 255, 255)', riverwidth=1)

    if tick:
        #        geo_fig.update_geos(center=dict(lon=float(tickers_geo.loc[tick, 'longitude']),
        #                                        lat=float(tickers_geo.loc[tick, 'latitude'])))
        geo_fig.add_trace(go.Scattergeo(lat=tickers_geo.loc[tick, 'latitude'],
                                        lon=tickers_geo.loc[tick, 'longitude'],
                                        mode="markers",
                                        hoverinfo="text",
                                        showlegend=False,
                                        marker=dict(
                                            color="rgb(191, 62, 255)",
                                            size=16,
                                            opacity=0.5,
                                            symbol='star')))

    geo_fig.update_layout(plot_style())

    return geo_fig


# Scatter Figures 1

@app.callback(
    Output(component_id='Debt_Rev_fig', component_property='figure'),
    Input(component_id='Debt_Rev_tickers', component_property='value'),
    Input(component_id='debt_rev_sectors_focus', component_property='value'),
    Input(component_id='debt_rev_subsectors_focus', component_property='value')
)
def update_Debt_Rev(ticks, sector, subsector):
    tickers_list = ticks

    df = df_annual_new_usd[['ticker', 'date', 'TotalDebt', 'totalRevenue',
                            'ebitda', 'inventory', 'WorkingCapital', 'name', 'sector', 'subsector']].dropna()

    if (subsector == 'All'):
        if (sector == 'All'):
            ddf = df
        else:
            ddf = df[df['sector'] == sector]

    else:
        ddf = df[df['subsector'] == subsector]

    Debt_Rev = px.scatter(ddf[~ddf.ticker.isin(tickers_list)],
                          color='ebitda', size='inventory', size_max=50,
                          y='TotalDebt', x='totalRevenue', hover_name='name',
                          color_continuous_scale='RdYlGn_r', hover_data=['date', 'ticker'])

    Debt_Rev.update_layout(plot_style())

    return Debt_Rev


@app.callback(
    Output(component_id='Debt_EBITDA_fig', component_property='figure'),
    Input(component_id='Debt_EBITDA_tickers', component_property='value'),
    Input(component_id='debt_ebitda_sectors_focus', component_property='value'),
    Input(component_id='debt_ebitda_subsectors_focus', component_property='value')
)
def update_Debt_EBITDA(ticks, sector, subsector):
    tickers_list = ticks

    df = df_annual_new_usd[['ticker', 'date', 'TotalDebt', 'totalRevenue',
                            'ebitda', 'inventory', 'WorkingCapital', 'name', 'sector', 'subsector']].dropna()

    if (subsector == 'All'):
        if (sector == 'All'):
            ddf = df
        else:
            ddf = df[df['sector'] == sector]

    else:
        ddf = df[df['subsector'] == subsector]

    Debt_EBITDA = px.scatter(ddf[~ddf.ticker.isin(tickers_list)],
                             color='WorkingCapital', size='totalRevenue', size_max=50,
                             y='TotalDebt', x='ebitda', color_continuous_scale='RdYlGn_r',
                             hover_name='name', hover_data=['date', 'ticker'])
    Debt_EBITDA.update_layout(plot_style())

    return Debt_EBITDA


@app.callback(
    Output(component_id='WC_Rev_fig', component_property='figure'),
    Input(component_id='WC_Rev_tickers', component_property='value'),
    Input(component_id='wc_rev_sectors_focus', component_property='value'),
    Input(component_id='wc_rev_subsectors_focus', component_property='value')
)
def update_WC_Rev(ticks, sector, subsector):
    tickers_list = ticks

    df = df_annual_new_usd[['ticker', 'date', 'TotalDebt', 'totalRevenue',
                            'ebitda', 'inventory', 'WorkingCapital', 'name', 'sector', 'subsector']].dropna()

    if (subsector == 'All'):
        if (sector == 'All'):
            ddf = df
        else:
            ddf = df[df['sector'] == sector]

    else:
        ddf = df[df['subsector'] == subsector]

    WC_Rev = px.scatter(ddf[~ddf.ticker.isin(tickers_list)],
                        color='inventory', size='TotalDebt', size_max=50,
                        y='WorkingCapital', x='totalRevenue', color_continuous_scale='RdYlGn_r',
                        hover_name='name', hover_data=['date', 'ticker'])
    WC_Rev.update_layout(plot_style())

    return WC_Rev


@app.callback(
    Output(component_id='WC_Inv_fig', component_property='figure'),
    Input(component_id='WC_Inv_tickers', component_property='value'),
    Input(component_id='wc_inv_sectors_focus', component_property='value'),
    Input(component_id='wc_inv_subsectors_focus', component_property='value')
)
def update_WC_Inv(ticks, sector, subsector):
    tickers_list = ticks

    df = df_annual_new_usd[['ticker', 'date', 'TotalDebt', 'totalRevenue',
                            'ebitda', 'inventory', 'WorkingCapital', 'name', 'sector', 'subsector']].dropna()

    if (subsector == 'All'):
        if (sector == 'All'):
            ddf = df
        else:
            ddf = df[df['sector'] == sector]

    else:
        ddf = df[df['subsector'] == subsector]

    WC_Inv = px.scatter(ddf[~ddf.ticker.isin(tickers_list)],
                        color='TotalDebt', size='totalRevenue', size_max=50,
                        y='WorkingCapital', x='inventory', color_continuous_scale='RdYlGn_r',
                        hover_name='name', hover_data=['date', 'ticker'])
    WC_Inv.update_layout(plot_style())

    return WC_Inv


# Scatter Figures 2

@app.callback(
    Output(component_id='Inv_Rev_fig', component_property='figure'),
    Input(component_id='Inv_Rev_period', component_property='value'),
    Input(component_id='Inv_Rev_tickers', component_property='value'),
    Input(component_id='inv_rev_sectors_focus', component_property='value'),
    Input(component_id='inv_rev_subsectors_focus', component_property='value')
)
def update_Inv_Rev(per, ticks, sector, subsector):
    if per == 'annual': df = df_annual_usd
    if per == 'quarterly': df = df_quartal_usd

    tickers_list = ticks

    df = df[
        ['ticker', 'date', 'cash', 'totalRevenue', 'grossProfit', 'inventory', 'name', 'sector', 'subsector']].dropna()

    if (subsector == 'All'):
        if (sector == 'All'):
            ddf = df
        else:
            ddf = df[df['sector'] == sector]

    else:
        ddf = df[df['subsector'] == subsector]

    Inv_Rev = px.scatter(ddf[~ddf.ticker.isin(tickers_list)],
                         color='grossProfit', size='cash', size_max=50,
                         y='inventory', x='totalRevenue', color_continuous_scale='RdYlGn_r',
                         hover_name='name', hover_data=['date', 'ticker'])
    Inv_Rev.update_layout(plot_style())

    return Inv_Rev


@app.callback(
    Output(component_id='Inv_Cash_fig', component_property='figure'),
    Input(component_id='Inv_Cash_period', component_property='value'),
    Input(component_id='Inv_Cash_tickers', component_property='value'),
    Input(component_id='inv_cash_sectors_focus', component_property='value'),
    Input(component_id='inv_cash_subsectors_focus', component_property='value')
)
def update_Inv_Cash(per, ticks, sector, subsector):
    if per == 'annual': df = df_annual_usd
    if per == 'quarterly': df = df_quartal_usd

    tickers_list = ticks

    df = df[['ticker', 'date', 'cash', 'totalRevenue', 'grossProfit', 'inventory', 'name',
             'sector', 'subsector']].dropna()

    if (subsector == 'All'):
        if (sector == 'All'):
            ddf = df
        else:
            ddf = df[df['sector'] == sector]

    else:
        ddf = df[df['subsector'] == subsector]

    Inv_Cash = px.scatter(ddf[~ddf.ticker.isin(tickers_list)],
                          color='grossProfit', size='totalRevenue', size_max=50,
                          y='inventory', x='cash', color_continuous_scale='RdYlGn_r',
                          hover_name='name', hover_data=['date', 'ticker'])

    Inv_Cash.update_layout(plot_style())

    return Inv_Cash


@app.callback(
    Output(component_id='Gross_pr_Inv_fig', component_property='figure'),
    Input(component_id='Gross_pr_Inv_period', component_property='value'),
    Input(component_id='Gross_pr_Inv_tickers', component_property='value'),
    Input(component_id='gross_pr_inv_sectors_focus', component_property='value'),
    Input(component_id='gross_pr_inv_subsectors_focus', component_property='value')
)
def update_Gross_pr_Inv(per, ticks, sector, subsector):
    if per == 'annual': df = df_annual_usd
    if per == 'quarterly': df = df_quartal_usd

    tickers_list = ticks

    df = df[['ticker', 'date', 'cash', 'totalRevenue', 'grossProfit', 'inventory', 'name',
             'sector', 'subsector']].dropna()

    if (subsector == 'All'):
        if (sector == 'All'):
            ddf = df
        else:
            ddf = df[df['sector'] == sector]

    else:
        ddf = df[df['subsector'] == subsector]

    Gross_pr_Inv = px.scatter(ddf[~ddf.ticker.isin(tickers_list)],
                              color='cash', size='totalRevenue', size_max=50,
                              y='grossProfit', x='inventory', color_continuous_scale='RdYlGn_r',
                              hover_name='name', hover_data=['date', 'ticker'])
    Gross_pr_Inv.update_layout(plot_style())

    return Gross_pr_Inv


@app.callback(
    Output(component_id='Gross_pr_Rev_fig', component_property='figure'),
    Input(component_id='Gross_pr_Rev_period', component_property='value'),
    Input(component_id='Gross_pr_Rev_tickers', component_property='value'),
    Input(component_id='gross_pr_rev_sectors_focus', component_property='value'),
    Input(component_id='gross_pr_rev_subsectors_focus', component_property='value')
)
def update_Gross_pr_Rev(per, ticks, sector, subsector):
    if per == 'annual': df = df_annual_usd
    if per == 'quarterly': df = df_quartal_usd

    tickers_list = ticks

    df = df[['ticker', 'date', 'cash', 'totalRevenue', 'grossProfit', 'inventory', 'name',
             'sector', 'subsector']].dropna()

    if (subsector == 'All'):
        if (sector == 'All'):
            ddf = df
        else:
            ddf = df[df['sector'] == sector]

    else:
        ddf = df[df['subsector'] == subsector]

    Gross_pr_Rev = px.scatter(ddf[~ddf.ticker.isin(tickers_list)],
                              color='inventory', size='cash', size_max=50,
                              y='grossProfit', x='totalRevenue', color_continuous_scale='RdYlGn_r',
                              hover_name='name', hover_data=['date', 'ticker'])
    Gross_pr_Rev.update_layout(plot_style())

    return Gross_pr_Rev


# Treemap

@app.callback(
    Output(component_id='treemap1', component_property='figure'),
    Output(component_id='treemap2', component_property='figure'),
    Input(component_id='treemap_period', component_property='value'),
    Input(component_id='treemap_column_v', component_property='value'),
    Input(component_id='treemap_column_c', component_property='value'),
    Input(component_id='treemap_sectors_focus', component_property='value'),
    Input(component_id='treemap_subsectors_focus', component_property='value'),
    Input(component_id='treemap_tickers_exclude', component_property='selected_rows'),
    Input(component_id='treemap_countries_focus', component_property='value')
)
def update_treemap(per, vol_column, col_column, sector, subsector, ticks, country):
    if per == 'annual': df = df_annual_usd
    if per == 'quarterly': df = df_quartal_usd

    if ticks:
        tickers_list = list(tickers.loc[ticks, 'ticker'])
    else:
        tickers_list = []

    if (vol_column == 'inventory_to_assets'):
        if (col_column == 'inventory'):
            ddf = df[['ticker', 'totalAssets', 'inventory',
                      'sector', 'subsector', 'name', 'date']].dropna()
            ddf['inventory_to_assets'] = ddf['inventory'].div(ddf['totalAssets'])
        else:
            ddf = df[['ticker', 'totalAssets', 'inventory', col_column,
                      'sector', 'subsector', 'name', 'date']].dropna()
            ddf['inventory_to_assets'] = ddf['inventory'].div(ddf['totalAssets'])
    else:
        ddf = df[['ticker', 'totalAssets', vol_column,
                  col_column, 'sector', 'subsector', 'name', 'date']].dropna()

    if (country == 'All'):
        dddf = ddf.copy()
    else:
        tickers_country = tickers[tickers['country'] == country]
        tickers_in_country = list(tickers_country['ticker'].dropna().unique())

        dddf = ddf[ddf.ticker.isin(tickers_in_country)]

    if (subsector == 'All'):
        if (sector == 'All'):
            ddddf = dddf  # [~ddf.sector.isin(sectors_list)]
        else:
            ddddf = dddf[dddf['sector'] == sector]
    else:
        ddddf = dddf[dddf['subsector'] == subsector]

    treemap1 = px.treemap(ddddf[~ddddf.ticker.isin(tickers_list)],
                          path=[px.Constant('all sectors'), 'sector', 'subsector', 'ticker', 'date'],
                          values=vol_column,
                          color=col_column, hover_name='name', color_continuous_scale='RdYlGn_r')
    treemap2 = px.treemap(ddddf[~ddddf.ticker.isin(tickers_list)],
                          path=[px.Constant('all sectors'), 'sector', 'subsector', 'ticker', 'date'],
                          values='totalAssets',
                          color=col_column, hover_name='name', color_continuous_scale='RdYlGn_r')

    treemap1.update_layout(plot_style())
    treemap2.update_layout(plot_style())

    return treemap1, treemap2


# Bar figures for Comparison

@app.callback(
    Output(component_id='bar_columns', component_property='figure'),
    Input(component_id='bar_columns_period', component_property='value'),
    Input(component_id='bar_columns_tickers', component_property='value'),
    Input(component_id='bar_columns_columns', component_property='value'),
)
def update_bar_columns(per, ticks, cols):
    tickers_list = ticks

    if per == 'annual': df = df_annual_usd
    if per == 'quarterly': df = df_quartal_usd

    columns_list = cols

    df = df[df_annual_usd.columns.difference(['currency', 'sector', 'subsector', 'date2',
                                              'Unnamed: 0', 'latitude', 'longitude'])]

    df_melt = pd.melt(df, id_vars=['date', 'ticker', 'name'])

    df_melt['date'] = pd.to_datetime(df_melt['date'])

    df_melt_cols = df_melt[df_melt.variable.isin(columns_list)]

    df_melt_cols_ticks = df_melt_cols[df_melt_cols.ticker.isin(tickers_list)]

    bar_columns = px.bar(df_melt_cols_ticks, y='value', color='variable',
                         height=250 * len(tickers_list),
                         color_discrete_sequence=px.colors.sequential.Plasma_r,
                         x='date', barmode="group", facet_row="ticker", custom_data=['date'],
                         hover_name='name')

    bar_columns.update_layout({"bargap": 0.3, 'bargroupgap': 0.12})

    bar_columns.update_layout(plot_style())

    return bar_columns


@app.callback(
    Output(component_id='ratios1', component_property='figure'),
    Input(component_id='ratios1_tickers', component_property='value')
)
def update_ratios1(ticks):
    tickers_list = ticks

    ratios1 = ratios.drop(['date2'], axis=1)

    ratios_melt = pd.melt(ratios1, id_vars=['ticker', 'date'])

    ratios_melt['date'] = pd.to_datetime(ratios_melt['date'])

    ratios_melt_cols = ratios_melt[ratios_melt.variable.isin(['DIO', 'DPO', 'DSO'])]

    ratios_melt_cols_ticks = ratios_melt_cols[ratios_melt_cols.ticker.isin(tickers_list)].dropna()

    for tick in tickers_list:
        ratios_melt_cols_ticks.loc[ratios_melt_cols_ticks['ticker'] == tick, 'name'] = get_title(tick)

    ratios1_fig = px.bar(ratios_melt_cols_ticks, x="date", y="value",
                         height=250 * len(tickers_list), width=750,
                         color="variable", color_discrete_sequence=px.colors.sequential.Plasma_r,
                         barmode="group", facet_row="ticker", hover_name='name')

    ratios1_fig.update_layout({"bargap": 0.3, 'bargroupgap': 0.12})
    ratios1_fig.update_layout(plot_style())

    return ratios1_fig


@app.callback(
    Output(component_id='ratios2', component_property='figure'),
    Input(component_id='ratios2_tickers', component_property='value')
)
def update_ratios2(ticks):
    tickers_list = ticks

    ratios2 = ratios.drop(['date2'], axis=1)

    ratios_melt = pd.melt(ratios2, id_vars=['ticker', 'date'])

    ratios_melt['date'] = pd.to_datetime(ratios_melt['date'])

    ratios_melt_cols = ratios_melt[ratios_melt.variable.isin(['InventoryTurnover', 'CCC'])]

    ratios_melt_cols_ticks = ratios_melt_cols[ratios_melt_cols.ticker.isin(tickers_list)].dropna()

    for tick in tickers_list:
        ratios_melt_cols_ticks.loc[ratios_melt_cols_ticks['ticker'] == tick, 'name'] = get_title(tick)

    ratios2_fig = px.bar(ratios_melt_cols_ticks, x="date", y="value", height=250 * len(tickers_list),
                         width=700,
                         color="variable", color_discrete_sequence=px.colors.sequential.Plasma_r,
                         barmode="group", facet_row="ticker", hover_name='name')

    ratios2_fig.update_layout({"bargap": 0.4, 'bargroupgap': 0.12})

    ratios2_fig.update_layout(plot_style())

    return ratios2_fig


@app.callback(
    Output(component_id='ratios3', component_property='figure'),
    Input(component_id='ratios3_tickers', component_property='value')
)
def update_ratios3(ticks):
    tickers_list = ticks

    ratios3 = ratios.drop(['date2'], axis=1)

    ratios_melt = pd.melt(ratios3, id_vars=['ticker', 'date'])

    ratios_melt['date'] = pd.to_datetime(ratios_melt['date'])

    ratios_melt_cols = ratios_melt[ratios_melt.variable.isin(['ROCE', 'ROIC'])]

    ratios_melt_cols_ticks = ratios_melt_cols[ratios_melt_cols.ticker.isin(tickers_list)].dropna()

    for tick in tickers_list:
        ratios_melt_cols_ticks.loc[ratios_melt_cols_ticks['ticker'] == tick, 'name'] = get_title(tick)

    ratios3_fig = px.bar(ratios_melt_cols_ticks, x="date", y="value", height=250 * len(tickers_list),
                         width=700,
                         color="variable", color_discrete_sequence=px.colors.sequential.Plasma_r,
                         barmode="group", facet_row="ticker", hover_name='name')

    ratios3_fig.update_layout({"bargap": 0.4, 'bargroupgap': 0.12})

    ratios3_fig.update_layout(plot_style())

    return ratios3_fig


# Scatter and bar figures combined

# @app.callback(
# Output(component_id='column_y', component_property='options'),
# Output(component_id='column_c', component_property='options'),
# Output(component_id='column_r', component_property='options'),
# Input(component_id='scatter_bar_ticker', component_property='value'),
# Input(component_id='scatter_bar_period', component_property='value')
# )

# def update_columns(tick, per):
#    ticker=tick
#
#    if per=='annual': df = df_annual[df_annual['ticker']==ticker]
#    if per=='quarterly': df = df_quartal[df_quartal['ticker']==ticker]

#    df = df[df.columns.difference(['name', 'currency', 'sector', 'subsector', 'date2',
#                                              'Unnamed: 0', 'latitude', 'longitude'])]

#    columns0 = list(df.columns)

#    del columns0[columns0.index('date')]
#    del columns0[columns0.index('ticker')]

#    df_melt = pd.melt(df, id_vars=['date', 'ticker'])
#    df_melt = df_melt.dropna()

#    columns1 = []

#    for col in columns0:
#        if (col in list(df_melt['variable'])): columns1.append(col)

#    column_options = [{'label':x, 'value':x} for x in columns1]

#    positive_columns = []

#    for col in columns0:
#        if (df[col] > 0.1).all(): positive_columns.append(col)

#    column_r_options = [{'label':x, 'value':x} for x in positive_columns]

#    return column_options, column_options, column_r_options

@app.callback(
    Output(component_id='scatter_fig', component_property='figure'),
    Output(component_id='bar_fig1', component_property='figure'),
    Input(component_id='scatter_bar_ticker', component_property='value'),
    Input(component_id='scatter_bar_period', component_property='value'),
    Input(component_id='column_y', component_property='value'),
    Input(component_id='column_c', component_property='value'),
    Input(component_id='column_r', component_property='value')
)
def update_scatter(tick, per, column_name_y, column_name_c, column_name_r):
    ticker = tick

    col_name_y = column_name_y

    col_name_c = column_name_c

    col_name_r = column_name_r

    if per == 'annual': df = df_annual[df_annual['ticker'] == ticker]
    if per == 'quarterly': df = df_quartal[df_quartal['ticker'] == ticker]

    df = df[['ticker', 'date', col_name_y, col_name_c, col_name_r]].dropna()

    df['date'] = pd.to_datetime(df['date'])

    scatter_fig = px.scatter(df, x='date', y=col_name_y, size=col_name_r, color=col_name_c,
                             custom_data=['date'], size_max=50, height=360,
                             title=get_title(ticker), color_continuous_scale='RdYlGn_r')
    scatter_fig.update_layout(plot_style())

    df_melt = pd.melt(df, id_vars=['ticker', 'date'])

    df_melt['value'] = df_melt['value'].astype('float')
    bar_fig1 = px.bar(df_melt[df_melt.variable.isin([col_name_y, col_name_c, col_name_r])],
                      height=330, y='value', color='variable',
                      color_discrete_sequence=px.colors.sequential.Plasma_r,
                      x='date', barmode="group", custom_data=['date'])

    bar_fig1.update_layout({"bargap": 0.3, 'bargroupgap': 0.12})

    bar_fig1.update_layout(plot_style())

    return scatter_fig, bar_fig1


@app.callback(
    Output(component_id='bar_fig2', component_property='figure'),
    Input(component_id='scatter_bar_ticker', component_property='value'),
    Input(component_id='scatter_bar_period', component_property='value'),
    Input(component_id='bar_fig1', component_property='clickData')
)
def update_bar2(tick, per, clickData):
    ticker = tick

    if per == 'annual': df = df_annual[df_annual['ticker'] == ticker]
    if per == 'quarterly': df = df_quartal[df_quartal['ticker'] == ticker]

    df = df[df.columns.difference(['ticker', 'name', 'currency', 'sector', 'subsector', 'date2',
                                   'Unnamed: 0', 'latitude', 'longitude'])]

    df['date'] = pd.to_datetime(df['date'])

    df.set_index('date', inplace=True)

    cdate = df.index[0]
    if clickData: cdate = pd.to_datetime(clickData['points'][0]['customdata'][0])

    ser = df.loc[cdate, :].astype('float')

    bar_fig2 = px.bar(ser, height=600, title=get_title(ticker))
    bar_fig2.update_layout(plot_style())
    bar_fig2.update_traces(marker_color='rgb(254, 163, 27)')

    return bar_fig2


@app.callback(
    Output(component_id='debt_rev_fig', component_property='figure'),
    Output(component_id='debt_ebitda_fig', component_property='figure'),
    Output(component_id='wc_rev_fig', component_property='figure'),
    Output(component_id='wc_inv_fig', component_property='figure'),
    Input(component_id='scatters_ticker1', component_property='value')
)
def update_scatter_figures1(tick):
    ticker = tick

    df = df_annual_new[df_annual_new['ticker'] == ticker]

    df['date'] = pd.to_datetime(df['date'])

    df_dropna = df[['ebitda', 'inventory', 'totalRevenue', 'ticker',
                    'WorkingCapital', 'TotalDebt', 'date']].dropna()

    debt_rev_fig = px.scatter(df_dropna,
                              color='ebitda', size='inventory', size_max=50,
                              y='TotalDebt', x='totalRevenue',
                              color_continuous_scale='RdYlGn_r', hover_data=['date', 'ticker'],
                              title=get_title(ticker))
    debt_rev_fig.update_layout(plot_style())

    debt_ebitda_fig = px.scatter(df_dropna,
                                 color='WorkingCapital', size='totalRevenue', size_max=50,
                                 y='TotalDebt', x='ebitda', color_continuous_scale='RdYlGn_r',
                                 hover_data=['date', 'ticker'], title=get_title(ticker))
    debt_ebitda_fig.update_layout(plot_style())

    wc_rev_fig = px.scatter(df_dropna,
                            color='inventory', size='TotalDebt', size_max=50,
                            y='WorkingCapital', x='totalRevenue', color_continuous_scale='RdYlGn_r',
                            hover_data=['date', 'ticker'], title=get_title(ticker))
    wc_rev_fig.update_layout(plot_style())

    wc_inv_fig = px.scatter(df_dropna,
                            color='TotalDebt', size='totalRevenue', size_max=50,
                            y='WorkingCapital', x='inventory', color_continuous_scale='RdYlGn_r',
                            hover_data=['date', 'ticker'], title=get_title(ticker))
    wc_inv_fig.update_layout(plot_style())

    return debt_rev_fig, debt_ebitda_fig, wc_rev_fig, wc_inv_fig


@app.callback(
    Output(component_id='inv_rev_fig', component_property='figure'),
    Output(component_id='inv_cash_fig', component_property='figure'),
    Output(component_id='gross_pr_inv_fig', component_property='figure'),
    Output(component_id='gross_pr_rev_fig', component_property='figure'),
    Input(component_id='scatters_ticker2', component_property='value'),
    Input(component_id='scatters_period', component_property='value')
)
def update_scatter_figures2(tick, per):
    ticker = tick

    if per == 'annual': df = df_annual[df_annual['ticker'] == ticker]
    if per == 'quarterly': df = df_quartal[df_quartal['ticker'] == ticker]

    df['date'] = pd.to_datetime(df['date'])

    df_dropna = df[['cash', 'inventory', 'totalRevenue', 'grossProfit', 'date']].dropna()

    inv_rev_fig = px.scatter(df_dropna, color='cash',
                             size='grossProfit', size_max=50,
                             y='inventory', x='totalRevenue',
                             color_continuous_scale='RdYlGn_r', hover_data=['date'],
                             title=get_title(ticker))
    inv_rev_fig.update_layout(plot_style())

    inv_cash_fig = px.scatter(df_dropna, color='totalRevenue',
                              size='grossProfit', size_max=50,
                              y='inventory', x='cash',
                              color_continuous_scale='RdYlGn_r', hover_data=['date'],
                              title=get_title(ticker))
    inv_cash_fig.update_layout(plot_style())

    gross_pr_inv_fig = px.scatter(df_dropna, color='cash',
                                  size='totalRevenue', size_max=50,
                                  y='grossProfit', x='inventory',
                                  color_continuous_scale='RdYlGn_r', hover_data=['date'],
                                  title=get_title(ticker))
    gross_pr_inv_fig.update_layout(plot_style())

    gross_pr_rev_fig = px.scatter(df_dropna, color='inventory',
                                  size='cash', size_max=50,
                                  y='grossProfit', x='totalRevenue',
                                  color_continuous_scale='RdYlGn_r', hover_data=['date'],
                                  title=get_title(ticker))
    gross_pr_rev_fig.update_layout(plot_style())

    return inv_rev_fig, inv_cash_fig, gross_pr_inv_fig, gross_pr_rev_fig


@app.callback(
    Output(component_id='tcc1_scatter', component_property='figure'),
    Output(component_id='tcc2_scatter', component_property='figure'),
    Input(component_id='tcc1_ticker', component_property='value'),
    Input(component_id='tcc1_slider', component_property='value')
)
def update_tcc_scatter1(tick, Lambda):
    ticker = tick

    df0 = df_annual_new[df_annual_new['ticker'] == ticker]

    df0 = df0[['ticker', 'date', 'interestExpense', 'TotalDebt', 'ebitda', 'operatingIncome']].dropna()

    df1 = df0.copy()

    df1['ticker'] = df0['ticker'] + '_tcc'

    df1['TotalDebt'] = df0['TotalDebt'].mul(1 - Lambda)
    df1['interestExpense'] = df0['interestExpense'].mul(1 - Lambda)
    df1['operatingIncome'] = df0['operatingIncome'] - abs(df0['interestExpense']).mul(Lambda)
    df1['ebitda'] = df0['ebitda'] - abs(df0['interestExpense']).mul(Lambda)

    df = pd.concat([df0, df1], axis=0)

    tcc1_scatter = px.scatter(df, x='TotalDebt', y='interestExpense',
                              facet_col='ticker', color='operatingIncome', hover_name='date',
                              color_continuous_scale='RdYlGn_r', size='ebitda', size_max=50,
                              title=get_title(ticker))
    tcc1_scatter.update_layout(plot_style())

    tcc2_scatter = px.scatter(df, x='ebitda', y='operatingIncome',
                              facet_col='ticker', color='interestExpense', hover_name='date',
                              color_continuous_scale='RdYlGn_r', size='TotalDebt', size_max=50)
    tcc2_scatter.update_layout(plot_style())

    return tcc1_scatter, tcc2_scatter,


@app.callback(
    Output(component_id='tcc3_bar', component_property='figure'),
    Input(component_id='tcc3_ticker', component_property='value'),
    Input(component_id='tcc3_slider', component_property='value')
)
def update_tcc_bar3(ticks, Lambda):
    tickers_list = ticks

    df0 = df_annual_new[df_annual_new.ticker.isin(tickers_list)]

    df1 = df0.copy()

    df2 = df0.copy()

    df0['TCC'] = 'Without TCC'

    df1['TCC'] = 'With TCC'

    df1['TotalDebt'] = df0['TotalDebt'].mul(1 - Lambda)
    df1['interestExpense'] = df0['interestExpense'].mul(1 - Lambda)
    df1['operatingIncome'] = df0['operatingIncome'] - abs(df0['interestExpense']).mul(Lambda)
    df1['ebitda'] = df0['ebitda'] - abs(df0['interestExpense']).mul(Lambda)

    df2['TotalDebt'] = df0['TotalDebt'].mul(1 - 0.8)
    df2['interestExpense'] = df0['interestExpense'].mul(1 - 0.8)
    df2['operatingIncome'] = df0['operatingIncome'] - abs(df0['interestExpense']).mul(0.8)
    df2['ebitda'] = df0['ebitda'] - abs(df0['interestExpense']).mul(0.8)

    df = pd.concat([df0, df1], axis=0)

    df['date'] = pd.to_datetime(df['date'])

    df_ratios = df[['ticker', 'date', 'TCC', 'name']]
    df_ratios2 = df[['ticker', 'date']]

    # df = df[['ticker', 'date', 'interestExpense', 'TotalDebt', 'ebitda', 'operatingIncome']]

    df_ratios['ebit_to_interestExpense'] = df['ebit'].divide(abs(df['interestExpense']))
    df_ratios['ebitda_to_interestExpense'] = (df['operatingIncome']
                                              + df['depreciation']).divide(abs(df['interestExpense']))

    df_ratios2['ebit_to_interestExpense'] = df2['ebit'].divide(abs(df2['interestExpense']))
    df_ratios2['ebitda_to_interestExpense'] = (df2['operatingIncome']
                                               + df2['depreciation']).divide(abs(df2['interestExpense']))

    tcc3_max = max(df_ratios2['ebit_to_interestExpense'].max(),
                   df_ratios2['ebitda_to_interestExpense'].max())

    ratios_melt = pd.melt(df_ratios, id_vars=['ticker', 'date', 'TCC', 'name'])

    ratios_melt['date'] = pd.to_datetime(ratios_melt['date'])

    ratios_melt_cols3 = ratios_melt[ratios_melt.variable.isin(['ebit_to_interestExpense',
                                                               'ebitda_to_interestExpense'])]

    if (Lambda < 0.8):
        tcc3_bar = px.bar(ratios_melt_cols3, x="date", y="value", facet_row='ticker',
                          facet_col='TCC', hover_name='name', height=300 * len(tickers_list),
                          color="variable", color_discrete_sequence=px.colors.sequential.Plasma_r,
                          barmode="group", range_y=[-0.1 * tcc3_max, 1.1 * tcc3_max])
    else:
        tcc3_bar = px.bar(ratios_melt_cols3, x="date", y="value", facet_row='ticker',
                          facet_col='TCC', hover_name='name', height=300 * len(tickers_list),
                          color="variable", color_discrete_sequence=px.colors.sequential.Plasma_r,
                          barmode="group", title=get_title(ticker))

    tcc3_bar.update_layout({"bargap": 0.2, 'bargroupgap': 0.1})

    tcc3_bar.update_layout(plot_style())

    return tcc3_bar


@app.callback(
    Output(component_id='tcc4_bar', component_property='figure'),
    Input(component_id='tcc4_ticker', component_property='value'),
    Input(component_id='tcc4_slider', component_property='value')
)
def update_tcc_bar4(ticks, Lambda):
    tickers_list = ticks

    df0 = df_annual_new[df_annual_new.ticker.isin(tickers_list)]

    df1 = df0.copy()

    df2 = df0.copy()

    df0['TCC'] = 'Without TCC'

    df1['TCC'] = 'With TCC'

    df1['TotalDebt'] = df0['TotalDebt'].mul(1 - Lambda)
    df1['interestExpense'] = df0['interestExpense'].mul(1 - Lambda)
    df1['operatingIncome'] = df0['operatingIncome'] - abs(df0['interestExpense']).mul(Lambda)
    df1['ebitda'] = df0['ebitda'] - abs(df0['interestExpense']).mul(Lambda)

    df2['TotalDebt'] = df0['TotalDebt'].mul(1 - 0.8)
    df2['interestExpense'] = df0['interestExpense'].mul(1 - 0.8)
    df2['operatingIncome'] = df0['operatingIncome'] - abs(df0['interestExpense']).mul(0.8)
    df2['ebitda'] = df0['ebitda'] - abs(df0['interestExpense']).mul(0.8)

    df = pd.concat([df0, df1], axis=0)

    df['date'] = pd.to_datetime(df['date'])

    df_ratios = df[['ticker', 'date', 'TCC', 'name']]
    df_ratios2 = df[['ticker', 'date']]

    # df = df[['ticker', 'date', 'interestExpense', 'TotalDebt', 'ebitda', 'operatingIncome']]

    df_ratios['FreeOperCF_to_TotalDebt'] = (df['operatingIncome'] + df['depreciation']
                                            - df['capitalExpenditures']).divide(df['TotalDebt'])
    df_ratios['FFO_to_TotalDebt'] = (df['operatingIncome']
                                     + df['depreciation'] + df['SaleOfPPE']).divide(df['TotalDebt'])

    df_ratios2['FreeOperCF_to_TotalDebt'] = (df2['operatingIncome'] + df2['depreciation']
                                             - df2['capitalExpenditures']).divide(df2['TotalDebt'])
    df_ratios2['FFO_to_TotalDebt'] = (df2['operatingIncome']
                                      + df2['depreciation'] + df2['SaleOfPPE']).divide(df2['TotalDebt'])

    tcc4_max = max(df_ratios2['FreeOperCF_to_TotalDebt'].max(),
                   df_ratios2['FFO_to_TotalDebt'].max())

    ratios_melt = pd.melt(df_ratios, id_vars=['ticker', 'date', 'TCC', 'name'])

    ratios_melt['date'] = pd.to_datetime(ratios_melt['date'])

    ratios_melt_cols4 = ratios_melt[ratios_melt.variable.isin(['FreeOperCF_to_TotalDebt', 'FFO_to_TotalDebt'])]

    if (Lambda < 0.8):
        tcc4_bar = px.bar(ratios_melt_cols4, x="date", y="value", facet_row='ticker',
                          facet_col='TCC', hover_name='name', height=300 * len(tickers_list),
                          color="variable", range_y=[-0.1 * tcc4_max, 1.1 * tcc4_max],
                          color_discrete_sequence=px.colors.sequential.Plasma_r, barmode="group")
    else:
        tcc4_bar = px.bar(ratios_melt_cols4, x="date", y="value", facet_row='ticker',
                          facet_col='TCC', hover_name='name', height=300 * len(tickers_list),
                          color="variable", color_discrete_sequence=px.colors.sequential.Plasma_r, barmode="group")

    tcc4_bar.update_layout({"bargap": 0.2, 'bargroupgap': 0.1})

    tcc4_bar.update_layout(plot_style())

    return tcc4_bar


@app.callback(
    Output(component_id='tcc5_bar', component_property='figure'),
    Input(component_id='tcc5_ticker', component_property='value'),
    Input(component_id='tcc5_slider', component_property='value')
)
def update_tcc_bar5(ticks, Lambda):
    tickers_list = ticks

    df0 = df_annual_new[df_annual_new.ticker.isin(tickers_list)]

    df1 = df0.copy()

    df2 = df0.copy()

    df0['TCC'] = 'Without TCC'

    df1['TCC'] = 'With TCC'

    df1['TotalDebt'] = df0['TotalDebt'].mul(1 - Lambda)
    df1['interestExpense'] = df0['interestExpense'].mul(1 - Lambda)
    df1['operatingIncome'] = df0['operatingIncome'] - abs(df0['interestExpense']).mul(Lambda)
    df1['ebitda'] = df0['ebitda'] - abs(df0['interestExpense']).mul(Lambda)

    df = pd.concat([df0, df1], axis=0)

    df['date'] = pd.to_datetime(df['date'])

    df_ratios = df[['ticker', 'date', 'TCC', 'name']]

    # df = df[['ticker', 'date', 'interestExpense', 'TotalDebt', 'ebitda', 'operatingIncome']]

    df_ratios['Return_on_Capital'] = (df['operatingIncome']
                                      - df['incomeTaxExpense']).divide(df['totalStockholderEquity']
                                                                       + df['TotalDebt'] - df['cash'])
    df_ratios['ebitda_to_Revenue'] = (df['operatingIncome'] + df['depreciation']).divide(df['totalRevenue'])

    ratios_melt = pd.melt(df_ratios, id_vars=['ticker', 'date', 'TCC', 'name'])

    ratios_melt['date'] = pd.to_datetime(ratios_melt['date'])

    ratios_melt_cols5 = ratios_melt[ratios_melt.variable.isin(['Return_on_Capital', 'ebitda_to_Revenue'])]

    tcc5_bar = px.bar(ratios_melt_cols5, x="date", y="value", facet_row='ticker',
                      facet_col='TCC', hover_name='name', height=300 * len(tickers_list),
                      color="variable", color_discrete_sequence=px.colors.sequential.Plasma_r, barmode="group")

    tcc5_bar.update_layout({"bargap": 0.2, 'bargroupgap': 0.1})

    tcc5_bar.update_layout(plot_style())

    return tcc5_bar


if __name__ == '__main__':
    app.run_server(port=8050, debug=True)
