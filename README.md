# Debt Dynamics in India

This repository consists of the code and data for the paper [Fiscal rules and debt dynamics in India](https://www.tandfonline.com/doi/abs/10.1080/17520843.2020.1796733), published in [Macroeconomics and Finance in Emerging Market Economies](https://www.tandfonline.com/journals/reme20).

## Repo Structure

The repository consists of the following folders:

- `1_data`: Clean csvs, named by figure number
- `2_code`: Code required to output tables
- `3_figures`: Final figures used in paper

## Code

The folder `2_code` consists of the following scripts

- `01_figs_trends.py`: Python file producing Figures 1-7, 9 and C1 (a)-C1(j).
- `02_figs_simulations.R`" R file producing Figures 10-11 and A1-A10.

Figures 8 and 12 were produced by uploading the respective csvs on Google Sheets/

## Replication 

In order to replicate the above figures, ensure you have the following packages installed in Python: `pandas`, `plotly`, `kaleido`, `pyprojroot`. In R, ensure you have the `plotly` package installed.

**Note**: In order for the figures to be saved, please ensure that you only install the following version of Kaleido, by running

`pip install --upgrade "kaleido==0.1.0post1"`

Once these are installed, execute the following steps

1. From `2_code`, open and run `01_figs_trends.py`. Ensure that you open the folder that the project is saved in using a text editor like VS code so that the root directory is correctly set.

2. Open `02_figs_simulations.R`. Depending on the state/scenario, choose the initial and target debt levels, as well as the time to hit target. Specify the range for interest and growth rates, whose lower and upper limits is one percent below/above the 10 year average. The average can be computed from the individual csvs for each state. Once, parameters are set, run the file, and save plot generated in the window. 











## Data

The data required to produce all the figures is stored as seperate `csv` files, named after each Figure in the folder `Data`. All the csv files can be accessed in the excel sheet `Replication.xlsx`.

## Code


