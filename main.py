from scripts.data_collection import load_sales_data
from scripts.data_cleaning import clean_sales_data
from scripts.date_dataframe import create_date_dataframe
from scripts.measures_and_indicators import calculate_measures
from scripts.visualizations import plot_sales_by_product, plot_sales_by_month, plot_top_5_cities, plot_profit_by_channel, plot_top_5_customers, plot_last_5_customers

# Charger les données de vente
sales_data = load_sales_data('assets/sales.xlsx')

# Nettoyer les données de vente
sales_data = clean_sales_data(sales_data)

# Créer le DataFrame de dates
date_df = create_date_dataframe(sales_data)

# Calculer les mesures et indicateurs
measures = calculate_measures(sales_data)

# Générer les visualisations
plot_sales_by_product(measures)
plot_sales_by_month(measures)
plot_top_5_cities(measures)
plot_profit_by_channel(measures)
plot_top_5_customers(measures)
plot_last_5_customers(measures)
