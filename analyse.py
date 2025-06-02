import pandas as pd
import numpy as np
import plotly.express as px

def load_csv_to_dataframe(file_path):
    """Load a CSV file into a Pandas DataFrame."""
    try:
        df = pd.read_csv(file_path, encoding='latin1')
        print(f"Successfully loaded data from {file_path}")
        print(df.head())
        return df
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
    except pd.errors.EmptyDataError:
        print(f"Error: The file {file_path} is empty.")
    except pd.errors.ParserError:
        print(f"Error: The file {file_path} could not be parsed.")
    except UnicodeDecodeError as e:
        print(f"Encoding error while reading the file: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    file_path = 'sales_data_sample.csv'
    df = load_csv_to_dataframe(file_path)
    
    # Quartiles 1 and 3
    if df is not None:
        # Quartiles and IQR sales
        q1 = df['SALES'].quantile(0.25)
        q3 = df['SALES'].quantile(0.75)
        print(f"Q1: {q1}, Q3: {q3}")
        # IQR
        iqr = q3 - q1
        print(f"IQR: {iqr}")
        # Outliers
        lower_bound = q1 - 1.5 * iqr
        upper_bound = q3 + 1.5 * iqr
        outliers = df[(df['SALES'] < lower_bound) | (df['SALES'] > upper_bound)]
        print(f"Outliers:\n{outliers}")
        
        # Quatiles and IQR Price
        q1_price = df['PRICEEACH'].quantile(0.25)
        q3_price = df['PRICEEACH'].quantile(0.75)
        print(f"Q1 Price: {q1_price}, Q3 Price: {q3_price}")
        # IQR Price
        iqr_price = q3_price - q1_price
        print(f"IQR Price: {iqr_price}")
        # Outliers Price
        lower_bound_price = q1_price - 1.5 * iqr_price
        upper_bound_price = q3_price + 1.5 * iqr_price
        outliers_price = df[(df['PRICEEACH'] < lower_bound_price) | (df['PRICEEACH'] > upper_bound_price)]
        print(f"Outliers Price:\n{outliers_price}")
        
        #Quantiles and IQR Quantity
        q1_quantity = df['QUANTITYORDERED'].quantile(0.25)
        q3_quantity = df['QUANTITYORDERED'].quantile(0.75)
        print(f"Q1 Quantity: {q1_quantity}, Q3 Quantity: {q3_quantity}")
        # IQR Quantity
        iqr_quantity = q3_quantity - q1_quantity
        print(f"IQR Quantity: {iqr_quantity}")
        # Outliers Quantity
        lower_bound_quantity = q1_quantity - 1.5 * iqr_quantity
        upper_bound_quantity = q3_quantity + 1.5 * iqr_quantity
        outliers_quantity = df[(df['QUANTITYORDERED'] < lower_bound_quantity) | (df['QUANTITYORDERED'] > upper_bound_quantity)]
        print(f"Outliers Quantity:\n{outliers_quantity}")
        [
        # Plotting the sales data]
        fig = px.box(df, y='SALES', title='Box Plot of Sales Data')
        fig.show()
        
        #Plotting sales data with outliers highlighted and lower and upper bounds in a line plot  
        
        fig_outliers = px.box(df, y='SALES', points='all', title='Box Plot of Sales Data with Outliers')
        fig_outliers.add_scatter(y=[lower_bound, lower_bound], mode='lines', name='Lower Bound', line=dict(color='red', dash='dash'))
        fig_outliers.add_scatter(y=[upper_bound, upper_bound], mode='lines', name='Upper Bound', line=dict(color='green', dash='dash'))
        fig_outliers.show()
        
        # Plotting the price data
        fig_price = px.box(df, y='PRICEEACH', title='Box Plot of Price Data')
        fig_price.show()
        # Plotting price data with outliers highlighted and lower and upper bounds
        fig_price_outliers = px.box(df, y='PRICEEACH', points='all', title='Box Plot of Price Data with Outliers')
        fig_price_outliers.add_scatter(y=[lower_bound_price, lower_bound_price], mode='lines', name='Lower Bound', line=dict(color='red', dash='dash'))
        fig_price_outliers.add_scatter(y=[upper_bound_price, upper_bound_price], mode='lines', name='Upper Bound', line=dict(color='green', dash='dash'))
        fig_price_outliers.show()
        
        # Plotting the quantity data
        fig_quantity = px.box(df, y='QUANTITYORDERED', title='Box Plot of Quantity Data')
        fig_quantity.show()
        # Plotting quantity data with outliers highlighted and lower and upper bounds
        fig_quantity_outliers = px.box(df, y='QUANTITYORDERED', points='all', title='Box Plot of Quantity Data with Outliers')
        fig_quantity_outliers.add_scatter(y=[lower_bound_quantity, lower_bound_quantity], mode='lines', name='Lower Bound', line=dict(color='red', dash='dash'))
        fig_quantity_outliers.add_scatter(y=[upper_bound_quantity, upper_bound_quantity], mode='lines', name='Upper Bound', line=dict(color='green', dash='dash'))
        fig_quantity_outliers.show()
        
        # Correlation matrix
        correlation_matrix = df[['SALES', 'PRICEEACH', 'QUANTITYORDERED']].corr()
        print("Correlation Matrix:")
        print(correlation_matrix)
        # Plotting the correlation matrix
        fig_corr = px.imshow(correlation_matrix, text_auto=True, title='Correlation Matrix')
        fig_corr.show()
        
        # Plotting the sales vs price
        fig_sales_price = px.scatter(df, x='PRICEEACH', y='SALES', title='Sales vs Price', trendline='ols')
        fig_sales_price.show()
        
        # Plotting the sales vs quantity
        fig_sales_quantity = px.scatter(df, x='QUANTITYORDERED', y='SALES', title='Sales vs Quantity', trendline='ols')
        fig_sales_quantity.show()
        # Plotting the price vs quantity
        fig_price_quantity = px.scatter(df, x='PRICEEACH', y='QUANTITYORDERED', title='Price vs Quantity', trendline='ols')
        fig_price_quantity.show()
        
        
    
    