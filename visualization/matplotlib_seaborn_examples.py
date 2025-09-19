"""
Essential data visualization examples using matplotlib and seaborn.
"""

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
from datetime import datetime, timedelta
import warnings
warnings.filterwarnings('ignore')

# Set style for better-looking plots
plt.style.use('default')
sns.set_palette("husl")

def create_sample_datasets():
    """Create sample datasets for visualization examples."""
    np.random.seed(42)
    
    # Dataset 1: Sales data
    dates = pd.date_range('2020-01-01', periods=365, freq='D')
    sales_data = {
        'date': dates,
        'sales': np.random.normal(1000, 200, 365) + np.sin(np.arange(365) * 2 * np.pi / 365) * 100,
        'region': np.random.choice(['North', 'South', 'East', 'West'], 365),
        'product': np.random.choice(['A', 'B', 'C', 'D'], 365),
        'marketing_spend': np.random.normal(500, 100, 365)
    }
    sales_df = pd.DataFrame(sales_data)
    
    # Dataset 2: Customer data
    n_customers = 1000
    customer_data = {
        'customer_id': range(1, n_customers + 1),
        'age': np.random.normal(35, 12, n_customers),
        'income': np.random.lognormal(10, 0.5, n_customers),
        'satisfaction': np.random.randint(1, 6, n_customers),
        'segment': np.random.choice(['Premium', 'Standard', 'Basic'], n_customers)
    }
    customer_df = pd.DataFrame(customer_data)
    
    # Dataset 3: Multivariate data for correlation analysis
    correlation_matrix = np.array([
        [1.0, 0.8, -0.6, 0.3],
        [0.8, 1.0, -0.4, 0.5],
        [-0.6, -0.4, 1.0, -0.2],
        [0.3, 0.5, -0.2, 1.0]
    ])
    
    multivar_data = np.random.multivariate_normal([0, 0, 0, 0], correlation_matrix, 500)
    multivar_df = pd.DataFrame(multivar_data, columns=['Var1', 'Var2', 'Var3', 'Var4'])
    
    return sales_df, customer_df, multivar_df

def basic_plots_demo(sales_df):
    """Demonstrate basic plot types."""
    print("=== BASIC PLOTS DEMONSTRATION ===")
    
    fig, axes = plt.subplots(2, 2, figsize=(15, 12))
    fig.suptitle('Basic Plot Types', fontsize=16, fontweight='bold')
    
    # Line plot - Time series
    monthly_sales = sales_df.groupby(sales_df['date'].dt.to_period('M'))['sales'].mean()
    axes[0, 0].plot(monthly_sales.index.astype(str), monthly_sales.values, marker='o')
    axes[0, 0].set_title('Monthly Average Sales (Line Plot)')
    axes[0, 0].set_xlabel('Month')
    axes[0, 0].set_ylabel('Average Sales')
    axes[0, 0].tick_params(axis='x', rotation=45)
    
    # Bar plot - Sales by region
    region_sales = sales_df.groupby('region')['sales'].mean()
    axes[0, 1].bar(region_sales.index, region_sales.values, color=['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4'])
    axes[0, 1].set_title('Average Sales by Region (Bar Plot)')
    axes[0, 1].set_xlabel('Region')
    axes[0, 1].set_ylabel('Average Sales')
    
    # Histogram - Sales distribution
    axes[1, 0].hist(sales_df['sales'], bins=30, alpha=0.7, color='skyblue', edgecolor='black')
    axes[1, 0].set_title('Sales Distribution (Histogram)')
    axes[1, 0].set_xlabel('Sales')
    axes[1, 0].set_ylabel('Frequency')
    
    # Scatter plot - Sales vs Marketing Spend
    axes[1, 1].scatter(sales_df['marketing_spend'], sales_df['sales'], alpha=0.6, color='coral')
    axes[1, 1].set_title('Sales vs Marketing Spend (Scatter Plot)')
    axes[1, 1].set_xlabel('Marketing Spend')
    axes[1, 1].set_ylabel('Sales')
    
    plt.tight_layout()
    plt.show()
    
    print("Basic plots completed!")

def statistical_plots_demo(customer_df):
    """Demonstrate statistical plots using seaborn."""
    print("\n=== STATISTICAL PLOTS DEMONSTRATION ===")
    
    fig, axes = plt.subplots(2, 2, figsize=(15, 12))
    fig.suptitle('Statistical Plots with Seaborn', fontsize=16, fontweight='bold')
    
    # Box plot - Income by segment
    sns.boxplot(data=customer_df, x='segment', y='income', ax=axes[0, 0])
    axes[0, 0].set_title('Income Distribution by Customer Segment')
    axes[0, 0].set_ylabel('Income')
    
    # Violin plot - Age by segment
    sns.violinplot(data=customer_df, x='segment', y='age', ax=axes[0, 1])
    axes[0, 1].set_title('Age Distribution by Customer Segment')
    axes[0, 1].set_ylabel('Age')
    
    # Count plot - Satisfaction ratings
    sns.countplot(data=customer_df, x='satisfaction', ax=axes[1, 0])
    axes[1, 0].set_title('Customer Satisfaction Ratings')
    axes[1, 0].set_xlabel('Satisfaction Score')
    axes[1, 0].set_ylabel('Count')
    
    # Joint plot in the last subplot area (we'll use the space differently)
    axes[1, 1].scatter(customer_df['age'], customer_df['income'], alpha=0.6, c=customer_df['satisfaction'], cmap='viridis')
    axes[1, 1].set_title('Age vs Income (colored by Satisfaction)')
    axes[1, 1].set_xlabel('Age')
    axes[1, 1].set_ylabel('Income')
    cbar = plt.colorbar(axes[1, 1].collections[0], ax=axes[1, 1])
    cbar.set_label('Satisfaction Score')
    
    plt.tight_layout()
    plt.show()
    
    print("Statistical plots completed!")

def correlation_and_heatmap_demo(multivar_df):
    """Demonstrate correlation analysis and heatmaps."""
    print("\n=== CORRELATION ANALYSIS DEMONSTRATION ===")
    
    fig, axes = plt.subplots(1, 2, figsize=(15, 6))
    fig.suptitle('Correlation Analysis', fontsize=16, fontweight='bold')
    
    # Correlation heatmap
    correlation = multivar_df.corr()
    sns.heatmap(correlation, annot=True, cmap='coolwarm', center=0, 
                square=True, ax=axes[0], cbar_kws={'shrink': 0.8})
    axes[0].set_title('Correlation Matrix Heatmap')
    
    # Pair plot (using scatter plots in a grid)
    # Since we can't easily use sns.pairplot in subplots, we'll create a custom grid
    vars_to_plot = ['Var1', 'Var2']
    axes[1].scatter(multivar_df['Var1'], multivar_df['Var2'], alpha=0.6)
    axes[1].set_title('Scatter Plot: Var1 vs Var2')
    axes[1].set_xlabel('Var1')
    axes[1].set_ylabel('Var2')
    
    # Add regression line
    z = np.polyfit(multivar_df['Var1'], multivar_df['Var2'], 1)
    p = np.poly1d(z)
    axes[1].plot(multivar_df['Var1'], p(multivar_df['Var1']), "r--", alpha=0.8)
    
    plt.tight_layout()
    plt.show()
    
    print("Correlation analysis completed!")

def advanced_visualizations_demo(sales_df):
    """Demonstrate advanced visualization techniques."""
    print("\n=== ADVANCED VISUALIZATIONS DEMONSTRATION ===")
    
    fig, axes = plt.subplots(2, 2, figsize=(16, 12))
    fig.suptitle('Advanced Visualization Techniques', fontsize=16, fontweight='bold')
    
    # Subplot 1: Multiple time series
    for region in sales_df['region'].unique():
        region_data = sales_df[sales_df['region'] == region]
        monthly_data = region_data.groupby(region_data['date'].dt.to_period('M'))['sales'].mean()
        axes[0, 0].plot(monthly_data.index.astype(str), monthly_data.values, marker='o', label=region)
    
    axes[0, 0].set_title('Monthly Sales by Region')
    axes[0, 0].set_xlabel('Month')
    axes[0, 0].set_ylabel('Average Sales')
    axes[0, 0].legend()
    axes[0, 0].tick_params(axis='x', rotation=45)
    
    # Subplot 2: Stacked bar chart
    product_region = sales_df.groupby(['region', 'product'])['sales'].mean().unstack()
    product_region.plot(kind='bar', stacked=True, ax=axes[0, 1], colormap='Set3')
    axes[0, 1].set_title('Average Sales by Region and Product (Stacked)')
    axes[0, 1].set_xlabel('Region')
    axes[0, 1].set_ylabel('Average Sales')
    axes[0, 1].tick_params(axis='x', rotation=45)
    axes[0, 1].legend(title='Product', bbox_to_anchor=(1.05, 1), loc='upper left')
    
    # Subplot 3: Distribution comparison
    for i, product in enumerate(sales_df['product'].unique()[:3]):  # Show only 3 products
        product_data = sales_df[sales_df['product'] == product]['sales']
        axes[1, 0].hist(product_data, bins=20, alpha=0.6, label=f'Product {product}')
    
    axes[1, 0].set_title('Sales Distribution by Product')
    axes[1, 0].set_xlabel('Sales')
    axes[1, 0].set_ylabel('Frequency')
    axes[1, 0].legend()
    
    # Subplot 4: Bubble chart (size represents marketing spend)
    # Group by region and product for clarity
    bubble_data = sales_df.groupby(['region', 'product']).agg({
        'sales': 'mean',
        'marketing_spend': 'mean'
    }).reset_index()
    
    colors = {'North': 'red', 'South': 'blue', 'East': 'green', 'West': 'orange'}
    for region in bubble_data['region'].unique():
        region_data = bubble_data[bubble_data['region'] == region]
        axes[1, 1].scatter(
            region_data['marketing_spend'], 
            region_data['sales'],
            s=region_data['marketing_spend']/5,  # Size based on marketing spend
            c=colors[region],
            alpha=0.6,
            label=region
        )
    
    axes[1, 1].set_title('Sales vs Marketing Spend by Region (Bubble Chart)')
    axes[1, 1].set_xlabel('Average Marketing Spend')
    axes[1, 1].set_ylabel('Average Sales')
    axes[1, 1].legend()
    
    plt.tight_layout()
    plt.show()
    
    print("Advanced visualizations completed!")

def customization_demo():
    """Demonstrate plot customization techniques."""
    print("\n=== PLOT CUSTOMIZATION DEMONSTRATION ===")
    
    # Create sample data
    x = np.linspace(0, 10, 100)
    y1 = np.sin(x)
    y2 = np.cos(x)
    y3 = np.sin(x) * np.cos(x)
    
    # Create figure with custom styling
    fig, ax = plt.subplots(figsize=(12, 8))
    
    # Plot multiple lines with different styles
    ax.plot(x, y1, linestyle='-', linewidth=2, color='#FF6B6B', label='sin(x)', marker='o', markersize=4, markevery=10)
    ax.plot(x, y2, linestyle='--', linewidth=2, color='#4ECDC4', label='cos(x)', marker='s', markersize=4, markevery=10)
    ax.plot(x, y3, linestyle='-.', linewidth=2, color='#45B7D1', label='sin(x)cos(x)', marker='^', markersize=4, markevery=10)
    
    # Customize the plot
    ax.set_title('Trigonometric Functions', fontsize=18, fontweight='bold', pad=20)
    ax.set_xlabel('X values', fontsize=14, fontweight='bold')
    ax.set_ylabel('Y values', fontsize=14, fontweight='bold')
    
    # Customize grid
    ax.grid(True, linestyle=':', alpha=0.7)
    ax.set_facecolor('#F8F9FA')
    
    # Customize legend
    legend = ax.legend(loc='upper right', frameon=True, fancybox=True, shadow=True)
    legend.get_frame().set_facecolor('#FFFFFF')
    legend.get_frame().set_alpha(0.9)
    
    # Customize tick marks
    ax.tick_params(axis='both', which='major', labelsize=12, direction='inout', length=6)
    ax.tick_params(axis='both', which='minor', length=3)
    
    # Add annotations
    ax.annotate('Maximum', xy=(np.pi/2, 1), xytext=(np.pi/2 + 1, 1.2),
                arrowprops=dict(arrowstyle='->', color='red', lw=1.5),
                fontsize=12, color='red', fontweight='bold')
    
    # Set axis limits
    ax.set_xlim(0, 10)
    ax.set_ylim(-1.5, 1.5)
    
    plt.tight_layout()
    plt.show()
    
    print("Plot customization completed!")

def main_visualization_demo():
    """Run all visualization demonstrations."""
    print("=== COMPREHENSIVE VISUALIZATION DEMONSTRATION ===")
    
    # Create sample data
    sales_df, customer_df, multivar_df = create_sample_datasets()
    
    # Run demonstrations
    basic_plots_demo(sales_df)
    statistical_plots_demo(customer_df)
    correlation_and_heatmap_demo(multivar_df)
    advanced_visualizations_demo(sales_df)
    customization_demo()
    
    # Display summary
    print("\n=== VISUALIZATION BEST PRACTICES ===")
    print("1. Always include clear titles and axis labels")
    print("2. Choose appropriate colors and avoid too many colors")
    print("3. Use legends when plotting multiple series")
    print("4. Consider your audience and the story you want to tell")
    print("5. Ensure text is readable (font size, contrast)")
    print("6. Use appropriate chart types for your data")
    print("7. Remove chart junk and focus on the data")
    print("8. Test your visualizations with others")
    
    print("\n=== DEMONSTRATION COMPLETED ===")

if __name__ == "__main__":
    main_visualization_demo()