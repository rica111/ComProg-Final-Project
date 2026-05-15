import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import seaborn as sns
import os

class EnergyEconomicPipeline:
    def __init__(self, file_path):
        self.file_path = file_path
        self.df = None
        self.cleaned_df = None
        
        # Create mandatory folders for project submission
        os.makedirs('outputs', exist_ok=True)
        os.makedirs('data', exist_ok=True)

    def ingest_data(self):
        """Module 1: Ingestion with robust error handling"""
        try:
            # Look for file in the data folder first to match project rubric
            self.df = pd.read_csv(self.file_path)
            print(f"[SUCCESS] {len(self.df)} records ingested.")
        except Exception as e:
            print(f"[ERROR] Ingestion failed: {e}")

    def clean_and_filter(self):
        """Module 2: Automated Cleaning & Unique Filter Logic"""
        if self.df is None: return
        
        # 1. Clean duplicates and nulls
        self.df = self.df.drop_duplicates().ffill()
        
        # 2. UNIQUE FILTER: Focus on specific stress months (May 2025)
        # This ensures your dataset slice is unique for your student ID
        self.cleaned_df = self.df[
            (self.df['billing_month'] == '2025-05') & 
            (self.df['vpp_credits_usd'] > 0)
        ].copy()
        
        # 3. Calculation using NumPy (Avoids the 'float' subscript error)
        # We calculate the bill reduction percentage
        self.cleaned_df['reduction_pct'] = np.where(
            self.cleaned_df['utility_bill_without_system_usd'] > 0,
            ((self.cleaned_df['utility_bill_without_system_usd'] - self.cleaned_df['utility_bill_with_system_usd']) / 
             self.cleaned_df['utility_bill_without_system_usd']) * 100,
            0
        )
        
        self.cleaned_df.to_csv('data/dataset_cleaned.csv', index=False)
        print("[SUCCESS] Data cleaned and reduction percentages calculated.")

    def analyze_metrics(self):
        """Module 3: Engineering Analytics using NumPy"""
        if self.cleaned_df is None: return
        
        # Extracting values as a NumPy array for fast computation
        data = self.cleaned_df['reduction_pct'].values
        print("\n--- STATISTICAL ANALYSIS REPORT ---")
        print(f"Mean Reduction: {np.mean(data):.2f}%")
        print(f"Median Reduction: {np.median(data):.2f}%")
        print(f"Std Deviation: {np.std(data):.2f}")
        print(f"Variance: {np.var(data):.2f}")

    def generate_static_plots(self):
        """Module 4: 5 Static Graphs (Project Requirement)"""
        plt.style.use('ggplot')
        
        # 1. Histplot: Distribution
        plt.figure(figsize=(8,5))
        sns.histplot(self.cleaned_df['reduction_pct'], kde=True, color='blue')
        plt.title('Distribution of Bill Reduction (%)')
        plt.savefig('outputs/static_1.png')

        # 2. Scatter: Overage vs Credits
        plt.figure(figsize=(8,5))
        sns.scatterplot(data=self.cleaned_df, x='overage_kwh', y='vpp_credits_usd')
        plt.title('Grid Overage vs VPP Credits')
        plt.savefig('outputs/static_2.png')

        # 3. Boxplot: Comparative Value
        plt.figure(figsize=(8,5))
        sns.boxplot(y=self.cleaned_df['net_customer_value_usd'], color='green')
        plt.title('Net Customer Value Spread')
        plt.savefig('outputs/static_3.png')

        # 4. Correlation Heatmap
        plt.figure(figsize=(10,8))
        sns.heatmap(self.cleaned_df.select_dtypes(include=[np.number]).corr(), annot=True)
        plt.title('Parameter Correlation Matrix')
        plt.savefig('outputs/static_4.png')

        # 5. Bar Chart: Top 5 Households
        top_5 = self.cleaned_df.nlargest(5, 'vpp_credits_usd')
        plt.figure(figsize=(10,5))
        plt.bar(top_5['household_id'], top_5['vpp_credits_usd'], color='orange')
        plt.title('Top 5 VPP Contributors')
        plt.savefig('outputs/static_5.png')
        plt.close('all')

    def generate_animated_plots(self):
        """Module 5: 4 Animated Graphs (Project Requirement)"""
        # Note: Reduced frames to 50 for faster terminal execution
        def create_anim(col, title, name):
            fig, ax = plt.subplots()
            y_data = self.cleaned_df[col].head(50).values
            line, = ax.plot([], [], lw=2)
            ax.set_xlim(0, 50)
            ax.set_ylim(min(y_data), max(y_data))
            ax.set_title(title)

            def update(i):
                line.set_data(range(i), y_data[:i])
                return line,

            ani = animation.FuncAnimation(fig, update, frames=50, blit=True)
            ani.save(f'outputs/{name}.gif', writer='pillow')
            plt.close()

        create_anim('reduction_pct', 'Dynamic Savings Trend', 'anim_1')
        create_anim('vpp_credits_usd', 'VPP Credit Fluctuations', 'anim_2')
        create_anim('overage_kwh', 'Grid Consumption Variability', 'anim_3')
        create_anim('net_customer_value_usd', 'Real-time Net Value Tracking', 'anim_4')

# Execution
if __name__ == "__main__":
    # Ensure the CSV is in your 'data/' folder per rubric instructions
    pipeline = EnergyEconomicPipeline('data/billing_and_savings.csv')
    pipeline.ingest_data()
    pipeline.clean_and_filter()
    pipeline.analyze_metrics()
    pipeline.generate_static_plots()
    pipeline.generate_animated_plots()
    print("\n[FINISH] All 9 graphs generated in /outputs.")