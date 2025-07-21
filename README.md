# SARS-CoV-2 Genomic Surveillance Dashboard

## Overview
This project presents a Streamlit dashboard for visualizing SARS-CoV-2 genomic data. It supports real-time surveillance by showing variant distributions, mutation loads, and temporal trends across geographic regions and viral lineages.

## Objective
To provide a user-friendly dashboard for exploring SARS-CoV-2 genomic data, enabling researchers and public health stakeholders to monitor evolving variants.

## Data Source
Mocked GISAID-like data (`data/sars_cov2_mock_data.csv`) is used to simulate variant distribution and mutation trends.

## Features
- Visualize variant distribution by lineage
- Display mutation load by region
- Explore temporal trends by month and region
- Supports interactive data filtering

## Methods
- **Streamlit** for dashboard development
- **Pandas** for data wrangling
- **Matplotlib/Seaborn** for plotting

## Limitations
- This version uses simulated data for demonstration purposes.
- Does not integrate live GISAID API or updates.

## Future Work
- Connect to real-time GISAID API (if available)
- Enable deeper mutation tracking and filtering
- Add advanced analytics (e.g., phylogenetic clustering)

## Folder Structure
```
sars-cov2-dashboard/
├── app.py
├── README.md
├── data/
│   └── sars_cov2_mock_data.csv
└── output/
    ├── mutation_load_by_region.png
    ├── variant_distribution_by_lineage.png
    └── temporal_trend_lineage.png
```
