
# GDP Analysis (2000–2022)

## Project Overview

This project analyses GDP development in seven countries from 2000 to 2022:

- United Kingdom
- United States
- Brazil
- Japan
- China
- Germany
- Switzerland

The project demonstrates modular Python programming, data cleaning, visualisation, and version control using Git and GitHub.

## Data Source

The data comes from the World Bank's World Development Indicators database.

Indicator: GDP (constant 2015 US$)

Indicator Code: NY.GDP.MKTP.KD

Period: 2000–2022

## Project Structure

- `data/`: Raw GDP data
- `src/load_data.py`: Functions for loading data
- `src/clean_data.py`: Functions for cleaning data
- `src/plot_data.py`: Functions for visualising GDP
- `notebooks/analysis.ipynb`: Analysis notebook
- `figures/`: Generated GDP charts
- `requirements.txt`: Python dependencies

## Installation

Install the required Python packages:

```bash
python -m pip install -r requirements.txt
```

## Usage

Open `notebooks/analysis.ipynb` in Jupyter Notebook or VS Code.

Run the cells in order to:

1. Import the Python modules.
2. Load and clean the GDP data.
3. Generate GDP visualisations.
4. Examine the economic analysis.

## Main Findings

The United States remained the largest economy in the sample.

China experienced rapid GDP growth, substantially narrowing the gap with the United States.

Japan and several European economies experienced more moderate growth.

The global financial crisis and COVID-19 pandemic affected economic output across multiple countries.

## Modularity

The project separates data loading, cleaning, and plotting into independent Python modules.

The analysis notebook imports these functions rather than repeating their implementations, improving code organisation and maintainability.