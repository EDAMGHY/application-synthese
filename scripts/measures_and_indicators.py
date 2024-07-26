import pandas as pd
import numpy as np

def calculate_measures(sales_data):
    measures = {}
    
    # Ventes totales
    sales_data['Sales'] = sales_data['Order Quantity'] * sales_data['Unit Selling Price']
    sales_data['Profit'] = sales_data['Sales'] - (sales_data['Order Quantity'] * sales_data['Unit Cost'])
    measures['Total Sales'] = sales_data['Sales'].sum()
    
    # Profit total
    measures['Total Profit'] = sales_data['Profit'].sum()
    
    # Commandes totales
    measures['Total Orders'] = sales_data['Order Quantity'].sum()
    
    # Marge bénéficiaire
    measures['Profit Margin'] = (measures['Total Profit'] / measures['Total Sales']) * 100
    
    # Ventes totales par produit pour l'année en cours
    sales_data['Year'] = sales_data['OrderDate'].dt.year
    current_year = sales_data['Year'].max()
    previous_year = current_year - 1
    
    measures['Sales by Product Current Year'] = sales_data[sales_data['Year'] == current_year].groupby('Product Description Index')['Sales'].sum()
    measures['Sales by Product Previous Year'] = sales_data[sales_data['Year'] == previous_year].groupby('Product Description Index')['Sales'].sum()
    
    # Ventes totales par mois pour l'année en cours
    measures['Sales by Month Current Year'] = sales_data[sales_data['Year'] == current_year].groupby(sales_data['OrderDate'].dt.month)['Sales'].sum()
    measures['Sales by Month Previous Year'] = sales_data[sales_data['Year'] == previous_year].groupby(sales_data['OrderDate'].dt.month)['Sales'].sum()
    
    # Top 5 des villes par ventes
    measures['Top 5 Cities'] = sales_data.groupby('Delivery Region Index')['Sales'].sum().nlargest(5)
    
    # Profit par canal pour l'année en cours
    measures['Profit by Channel Current Year'] = sales_data[sales_data['Year'] == current_year].groupby('Channel')['Profit'].sum()
    measures['Profit by Channel Previous Year'] = sales_data[sales_data['Year'] == previous_year].groupby('Channel')['Profit'].sum()
    
    # Top 5 des clients par ventes
    measures['Top 5 Customers'] = sales_data.groupby('Customer Name Index')['Sales'].sum().nlargest(5)
    
    # 5 derniers clients par ventes
    measures['Last 5 Customers'] = sales_data.groupby('Customer Name Index')['Sales'].sum().nsmallest(5)
    
    return measures
