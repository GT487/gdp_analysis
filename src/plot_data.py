import matplotlib.pyplot as plt

def plot_gdp(df):
    fig, ax = plt.subplots(figsize=(11,6))

    for country, data in df.groupby("Country"):
        ax.plot(
            data["Year"],
            data["GDP"]/1e12,
                   label=country      
         )

    ax.set_title("GDP Development (2000-2022)")
    ax.set_xlabel("Year")
    ax.set_ylabel("GDP(trillion constant US$)")
    ax.legend()
    ax.grid(True)

    fig.tight_layout()
    fig.savefig("figures/gdp_comparison.png")

    plt.close(fig)
    