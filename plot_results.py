import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load CSV
df = pd.read_csv("algorithm_comparison_results.csv")

# Metrics to plot
metrics = ["Fault Ratio", "Hit Ratio", "Execution Time", "Memory Usage"]

# Plotting
for metric in metrics:
    plt.figure(figsize=(10, 6))
    sns.lineplot(
        data=df,
        x="Frame Size",
        y=metric,
        hue="Algorithm",
        style="Reference Length",
        markers=True,
        dashes=False
    )
    plt.title(f"{metric} vs Frame Size")
    plt.xlabel("Frame Size")
    plt.ylabel(metric)
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(f"{metric.replace(' ', '_').lower()}_vs_frame_size.png")
    plt.show()

for metric in metrics:
    plt.figure(figsize=(10, 6))
    sns.lineplot(
        data=df,
        x="Reference Length",
        y=metric,
        hue="Algorithm",
        style="Frame Size",
        markers=True,
        dashes=False
    )
    plt.title(f"{metric} vs Reference String Length")
    plt.xlabel("Reference String Length")
    plt.ylabel(metric)
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(f"{metric.replace(' ', '_').lower()}_vs_reference_length.png")
    plt.show()
    
# === Comparison Plots: Enhanced vs Original Versions ===

# Pairs to compare
comparison_pairs = [
    ("Aging (NFU)", "Aging Optimized"),
    ("Enhanced Second Chance", "Enhanced Second Chance Optimized"),
    ("Page Buffering", "Page Buffering Optimized")
]

# Metrics to plot
metrics = ["Fault Ratio", "Hit Ratio", "Execution Time", "Memory Usage"]

for original, optimized in comparison_pairs:
    for metric in metrics:
        plt.figure(figsize=(10, 6))
        subset = df[df["Algorithm"].isin([original, optimized])]
        sns.lineplot(
            data=subset,
            x="Frame Size",
            y=metric,
            hue="Algorithm",
            style="Reference Length",
            markers=True,
            dashes=False
        )
        plt.title(f"{metric} Comparison: {original} vs Optimized")
        plt.xlabel("Frame Size")
        plt.ylabel(metric)
        plt.grid(True)
        plt.tight_layout()

        # Safe filename
        file_name = f"compare_{original.replace(' ', '_').replace('(', '').replace(')', '').lower()}_{metric.replace(' ', '_').lower()}.png"
        plt.savefig(file_name)
        plt.show()

    