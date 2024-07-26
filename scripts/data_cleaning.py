def clean_sales_data(sales_data):
    # Gérez les valeurs manquantes
    sales_data = sales_data.dropna()
    
    # Supprimez les doublons
    sales_data = sales_data.drop_duplicates()
    
    return sales_data