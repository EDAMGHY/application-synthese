import pandas as pd

def create_date_dataframe(sales_data):
    # Assurez-vous que la colonne 'OrderDate' est au format datetime
    sales_data['OrderDate'] = pd.to_datetime(sales_data['OrderDate'])
    
    # Créez une plage de dates couvrant toute la période des données de vente
    date_range = pd.date_range(start=sales_data['OrderDate'].min(), end=sales_data['OrderDate'].max())
    
    # Créez un DataFrame de dates
    date_df = pd.DataFrame(date_range, columns=['Date'])
    
    # Ajoutez des colonnes supplémentaires pour l'année, le trimestre, le mois et le jour de la semaine
    date_df['Year'] = date_df['Date'].dt.year
    date_df['Quarter'] = date_df['Date'].dt.quarter
    date_df['Month'] = date_df['Date'].dt.month
    date_df['DayOfWeek'] = date_df['Date'].dt.dayofweek
    
    return date_df


