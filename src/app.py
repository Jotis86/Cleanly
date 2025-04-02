import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from io import BytesIO
from limpiar import clean_data, remove_outliers, remove_outliers_iqr
import os

# Configuración de estilo para gráficos
sns.set_theme(style="whitegrid")

# Obtener la ruta absoluta del directorio actual
current_dir = os.path.dirname(os.path.abspath(__file__))

principal_image_path = os.path.join("images", 'portada.png')
menu_image_path = os.path.join("images", 'funko.png')


# Configuración de la barra lateral
try:
    st.sidebar.image(menu_image_path, use_container_width=True)
except Exception as e:
    st.sidebar.error(f"Error loading image: {e}")
    st.sidebar.info(f"Looking for image at: {menu_image_path}")


# Sidebar mejorado y personalizado
st.sidebar.title("✨ Cleanly")
st.sidebar.markdown("<p style='font-size: 18px; font-style: italic; color: #4d8b90;'>Your Data Cleaning Companion</p>", unsafe_allow_html=True)


# Botón de GitHub estilizado en verde
st.sidebar.markdown("""
<a href='https://github.com/Jotis86/Cleanly' target='_blank'>
    <button style='background-color: #2ea44f; border: none; color: white; padding: 10px 24px; 
    text-align: center; text-decoration: none; display: inline-block; font-size: 16px; 
    margin: 4px 2px; cursor: pointer; border-radius: 8px; width: 100%;'>
        <svg style="vertical-align: middle; margin-right: 10px;" height="20" width="20" viewBox="0 0 16 16" fill="white">
            <path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z"></path>
        </svg>
        GitHub Repository
    </button>
</a>
""", unsafe_allow_html=True)


# Sección personalizada de información del creador
st.sidebar.markdown("""
<div style='background-color: #f5f7f9; padding: 10px; border-radius: 8px; margin-top: 10px;'>
    <h4 style='color: #333; margin-bottom: 5px;'>Created with 💙</h4>
    <p style='color: #666; margin-bottom: 5px; font-size: 14px;'>by <span style='font-weight: bold; color: #2c3e50;'>Jotis</span></p>
    <p style='color: #888; font-size: 12px; margin-top: 5px;'>© 2025 Cleanly - All rights reserved</p>
</div>
""", unsafe_allow_html=True)

# Mostrar imagen principal
try:
    st.image(principal_image_path, use_container_width=True)
except Exception as e:
    st.error(f"Error loading image: {e}")
    st.info(f"Looking for image at: {principal_image_path}")

# Texto explicativo de la aplicación
st.markdown("""
## Welcome to Cleanly!

Cleanly is an interactive tool designed to simplify the data cleaning and exploratory data analysis (EDA) process. 
Whether you're a data scientist, analyst, or student, this application helps you:

- **Clean and preprocess** your CSV data with a few clicks
- **Identify and handle** missing values and duplicates
- **Remove outliers** using statistical methods
- **Visualize your data** through various chart types
- **Transform your data** through normalization and encoding
- **Export your cleaned data** for further analysis

Simply upload your CSV file to get started, and use the options below to clean and analyze your data!
""")


# File uploader
uploaded_file = st.file_uploader("Upload a CSV file", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("### Original Data")
    st.write(df)

    # Mostrar información inicial
    st.write("### Data Overview")
    st.write(f"Number of rows: {df.shape[0]}")
    st.write(f"Number of columns: {df.shape[1]}")

    # Mostrar duplicados
    st.write("### Duplicates")
    duplicates = df[df.duplicated()]
    st.write(f"Number of duplicate rows: {len(duplicates)}")
    if not duplicates.empty:
        st.write(duplicates)

    # Mostrar valores nulos
    st.write("### Missing Values")
    missing_values = df.isnull().sum()
    st.write(missing_values[missing_values > 0])

    # Visualización de valores nulos
    st.write("### Missing Values Heatmap")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.heatmap(df.isnull(), cbar=False, cmap="viridis", ax=ax)
    ax.set_title("Heatmap of Missing Values")
    st.pyplot(fig)

    # Menú para acciones
    st.write("### What would you like to do next?")
    options = [
        "Show Descriptive Statistics",
        "Clean Data",
        "Remove Duplicates",
        "Handle Missing Values",
        "Remove Outliers (Z-Score)",
        "Remove Outliers (IQR)",
        "Normalize Data",
        "Encode Categorical Columns",
        "Delete Specific Columns",
        "Rename Columns",
        "Filter Rows",
        "Sort Data",
        "Visualize Histograms",
        "Visualize Bar Charts",
        "Scatter Plot",
        "Group Data",
        "Correlation Matrix",  # Nueva opción para la matriz de correlación
        "Download Cleaned Data"
    ]
    selected_actions = st.multiselect("Choose one or more actions:", options)

    for action in selected_actions:
        if action == "Show Descriptive Statistics":
            st.write("### Descriptive Statistics")
            st.write(df.describe())
        elif action == "Clean Data":
            df = clean_data(df)
            st.write("Data after cleaning:")
            st.write(df)
        elif action == "Remove Duplicates":
            df = df.drop_duplicates()
            st.write("Data after removing duplicates:")
            st.write(df)
        elif action == "Handle Missing Values":
            df = clean_data(df)
            st.write("Data after handling missing values:")
            st.write(df)
        elif action == "Remove Outliers (Z-Score)":
            df = remove_outliers(df)
            st.write("Data after removing outliers (Z-Score):")
            st.write(df)
        elif action == "Remove Outliers (IQR)":
            df = remove_outliers_iqr(df)
            st.write("Data after removing outliers (IQR):")
            st.write(df)
        elif action == "Normalize Data":
            numeric_cols = df.select_dtypes(include=np.number).columns
            for col in numeric_cols:
                df[col] = (df[col] - df[col].min()) / (df[col].max() - df[col].min())
            st.write("Data after normalization:")
            st.write(df)
        elif action == "Encode Categorical Columns":
            categorical_cols = df.select_dtypes(include='object').columns
            for col in categorical_cols:
                df[col] = pd.factorize(df[col])[0]
            st.write("Data after encoding categorical columns:")
            st.write(df)
        elif action == "Delete Specific Columns":
            columns_to_delete = st.multiselect("Select columns to delete:", df.columns)
            df = df.drop(columns=columns_to_delete)
            st.write("Data after deleting columns:")
            st.write(df)
        elif action == "Rename Columns":
            selected_col = st.selectbox("Select a column to rename:", df.columns)
            new_name = st.text_input("Enter the new name for the column:")
            if new_name:
                df.rename(columns={selected_col: new_name}, inplace=True)
                st.write(f"Column '{selected_col}' renamed to '{new_name}'")
                st.write(df)
        elif action == "Filter Rows":
            try:
                filter_column = st.selectbox("Select column to filter by:", df.columns)
                
                # Determinar el tipo de columna
                is_numeric = pd.api.types.is_numeric_dtype(df[filter_column])
                
                # Opciones de filtrado basadas en el tipo de columna
                if is_numeric:
                    filter_type = st.radio("Filter type:", ["Equal to", "Greater than", "Less than"], horizontal=True)
                else:
                    filter_type = st.radio("Filter type:", ["Equal to", "Contains"], horizontal=True)
                
                # Entrada del valor de filtro
                filter_value = st.text_input("Enter value to filter by:")
                
                if filter_value:
                    # Crear una copia temporal para filtrar (no modificar el df original)
                    filtered_df = df.copy()
                    
                    # Aplicar el filtro según el tipo seleccionado
                    if is_numeric:
                        try:
                            # Convertir a número
                            num_value = float(filter_value)
                            if filter_type == "Equal to":
                                filtered_df = filtered_df[filtered_df[filter_column] == num_value]
                            elif filter_type == "Greater than":
                                filtered_df = filtered_df[filtered_df[filter_column] > num_value]
                            else:  # Less than
                                filtered_df = filtered_df[filtered_df[filter_column] < num_value]
                        except ValueError:
                            st.error(f"Please enter a valid number for column '{filter_column}'")
                            filtered_df = df.copy()
                    else:
                        # Para texto
                        if filter_type == "Equal to":
                            filtered_df = filtered_df[filtered_df[filter_column].astype(str) == filter_value]
                        else:  # Contains
                            filtered_df = filtered_df[filtered_df[filter_column].astype(str).str.contains(filter_value, case=False, na=False)]
                    
                    # Mostrar resultados
                    st.write(f"Data after filtering rows ({len(filtered_df)} rows found):")
                    st.write(filtered_df)
                    
                    # Opción para actualizar el DataFrame principal
                    if st.button("Use filtered data for next operations"):
                        df = filtered_df
                        st.success("Main dataset updated with filtered data!")
                        
            except Exception as e:
                st.error(f"Error during filtering: {str(e)}")
        elif action == "Sort Data":
            sort_column = st.selectbox("Select column to sort by:", df.columns)
            sort_order = st.radio("Sort order:", ["Ascending", "Descending"])
            df = df.sort_values(by=sort_column, ascending=(sort_order == "Ascending"))
            st.write("Data after sorting:")
            st.write(df)
        elif action == "Visualize Histograms":
            selected_cols = st.multiselect("Select numeric columns for histograms:", df.select_dtypes(include=np.number).columns)
            for col in selected_cols:
                fig, ax = plt.subplots()
                sns.histplot(df[col], bins=20, kde=True, color="blue", ax=ax)
                ax.set_title(f"Histogram of {col}")
                st.pyplot(fig)
        elif action == "Visualize Bar Charts":
            selected_col = st.selectbox("Select a categorical column for bar chart:", df.select_dtypes(include='object').columns)
            fig, ax = plt.subplots()
            sns.countplot(x=df[selected_col], palette="Set2", ax=ax)
            ax.set_title(f"Bar Chart of {selected_col}")
            st.pyplot(fig)
        elif action == "Scatter Plot":
            st.write("### Scatter Plot")
            numeric_cols = df.select_dtypes(include=np.number).columns
            if len(numeric_cols) >= 2:
                x_col = st.selectbox("Select X-axis column:", numeric_cols, key="scatter_x")
                y_col = st.selectbox("Select Y-axis column:", numeric_cols, key="scatter_y")
                fig, ax = plt.subplots()
                sns.scatterplot(data=df, x=x_col, y=y_col, ax=ax, color="blue", alpha=0.7)
                ax.set_title(f"Scatter Plot: {x_col} vs {y_col}")
                st.pyplot(fig)
            else:
                st.write("Not enough numeric columns to create a scatter plot.")
        elif action == "Group Data":
            try:
                # Seleccionar columna para agrupar
                group_column = st.selectbox("Select column to group by:", df.columns)
                
                # Filtrar columnas numéricas excluyendo la columna de agrupación
                numeric_cols = df.select_dtypes(include=np.number).columns
                available_agg_cols = [col for col in numeric_cols if col != group_column]
                
                if len(available_agg_cols) == 0:
                    # Si no hay columnas numéricas disponibles después de excluir la columna de agrupación
                    st.warning("No numeric columns available for aggregation. Please select a different column for grouping or add more numeric columns to your dataset.")
                else:
                    # Seleccionar columna para agregar y función de agregación
                    agg_column = st.selectbox("Select column to aggregate:", available_agg_cols)
                    agg_func = st.selectbox("Select aggregation function:", ["mean", "sum", "count", "max", "min"])
                    
                    # Realizar el agrupamiento
                    grouped_df = df.groupby(group_column)[agg_column].agg(agg_func).reset_index()
                    
                    # Mostrar resultados
                    st.write(f"Data after grouping by '{group_column}' and aggregating '{agg_column}' with '{agg_func}':")
                    st.write(grouped_df)
                    
                    # Visualizar los resultados en un gráfico de barras si no hay demasiados grupos
                    if len(grouped_df) <= 20:  # Limitar para legibilidad
                        st.write("### Visualization of Grouped Data")
                        fig, ax = plt.subplots(figsize=(10, 5))
                        sns.barplot(x=group_column, y=agg_column, data=grouped_df, ax=ax)
                        ax.set_title(f"{agg_func.capitalize()} of {agg_column} by {group_column}")
                        if len(grouped_df) > 5:  # Rotar etiquetas si hay muchos grupos
                            ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')
                        plt.tight_layout()
                        st.pyplot(fig)
            
            except Exception as e:
                st.error(f"An error occurred during data grouping: {str(e)}")
                st.info("Try selecting different columns or handling missing values first.")
        elif action == "Correlation Matrix":
            st.write("### Correlation Matrix")
            numeric_cols = df.select_dtypes(include=np.number).columns
            if len(numeric_cols) > 1:
                fig, ax = plt.subplots(figsize=(10, 6))
                corr = df[numeric_cols].corr()
                sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax)
                ax.set_title("Correlation Matrix")
                st.pyplot(fig)
            else:
                st.write("Not enough numeric columns for a correlation matrix.")
        elif action == "Download Cleaned Data":
            buffer = BytesIO()
            df.to_csv(buffer, index=False)
            buffer.seek(0)
            st.download_button(
                label="Download Cleaned CSV",
                data=buffer,
                file_name="cleaned_data.csv",
                mime="text/csv"
            )