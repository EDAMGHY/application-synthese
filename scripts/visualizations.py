import matplotlib.pyplot as plt
import seaborn as sns

    # Crée une figure pour les ventes par produit
def plot_sales_by_product(measures):
    plt.figure(figsize=(10, 6))
    sns.barplot(x=measures['Sales by Product Current Year'].index, y=measures['Sales by Product Current Year'].values, color='blue', label='Current Year')
    sns.barplot(x=measures['Sales by Product Previous Year'].index, y=measures['Sales by Product Previous Year'].values, color='red', label='Previous Year')
    plt.title('Ventes par Produit et Comparaison avec l\'Année Dernière')
    plt.xlabel('Produit')
    plt.ylabel('Ventes')
    plt.legend()
    plt.show()

    # Crée une figure pour les ventes par mois
def plot_sales_by_month(measures):
    plt.figure(figsize=(10, 6))
    sns.lineplot(x=measures['Sales by Month Current Year'].index, y=measures['Sales by Month Current Year'].values, marker='o', label='Current Year')
    sns.lineplot(x=measures['Sales by Month Previous Year'].index, y=measures['Sales by Month Previous Year'].values, marker='o', label='Previous Year')
    plt.title('Ventes par Mois et Comparaison avec l\'Année Dernière')
    plt.xlabel('Mois')
    plt.ylabel('Ventes')
    plt.legend()
    plt.show()

    # Crée une figure pour les 5 villes principales
def plot_top_5_cities(measures):
    plt.figure(figsize=(10, 6))
    sns.barplot(x=measures['Top 5 Cities'].index, y=measures['Top 5 Cities'].values)
    plt.title('Top 5 Villes par Ventes')
    plt.xlabel('Ville')
    plt.ylabel('Ventes')
    plt.show()

    # Crée une figure pour le profit par canal
def plot_profit_by_channel(measures):
    plt.figure(figsize=(10, 6))
    sns.barplot(x=measures['Profit by Channel Current Year'].index, y=measures['Profit by Channel Current Year'].values, color='blue', label='Current Year')
    sns.barplot(x=measures['Profit by Channel Previous Year'].index, y=measures['Profit by Channel Previous Year'].values, color='red', label='Previous Year')
    plt.title('Profit par Canal et Comparaison avec l\'Année Dernière')
    plt.xlabel('Canal')
    plt.ylabel('Profit')
    plt.legend()
    plt.show()

    # Crée une figure pour les 5 meilleurs clients
def plot_top_5_customers(measures):
    plt.figure(figsize=(10, 6))
    sns.barplot(x=measures['Top 5 Customers'].index, y=measures['Top 5 Customers'].values)
    plt.title('Top 5 Clients par Ventes')
    plt.xlabel('Client')
    plt.ylabel('Ventes')
    plt.show()

    # Crée une figure pour les 5 derniers clients
def plot_last_5_customers(measures):
    plt.figure(figsize=(10, 6))
    sns.barplot(x=measures['Last 5 Customers'].index, y=measures['Last 5 Customers'].values)
    plt.title('Derniers 5 Clients par Ventes')
    plt.xlabel('Client')
    plt.ylabel('Ventes')
    plt.show()