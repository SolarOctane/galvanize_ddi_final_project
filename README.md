# galvanize_ddi_final_project
Final Project for the Galvanize's Data and Development Immersive-Cohort 12 for Active Duty Service Members Bootcamp.

Immigration Nationwide Encounter FY25 Forecasting App.

Overview of the Project. 

This application uses a **Random Forest Regressor** model to predict **nationwide immigration encounters** for **Fiscal Year 2025** based on historical data.

The underlying dataset includes U.S. immigration encounter records from **Fiscal Years 2021 through 2024**, capturing multiple categorical and numerical variables such as:

- **Citizenship**
- **Demographic group**
- **Encounter type**
- **Area of Responsibility (AOR)**
- **Fiscal year**

The goal is to generate forward-looking insights that can help policy analysts, agencies, and stakeholders **anticipate border activity trends**.

### Key Features:
- View and explore the dataset used for modeling.
- Generate predictions for FY2025 based on selected features.
- Visualize actual vs. predicted values, residuals, and feature importance.
- Download prediction results for further analysis.

This app is built with **Streamlit** and powered by **scikit-learn's Random Forest Regressor**, offering a balance of interpretability and predictive power.

Project Proposal or Research Question.

What is the sum of the total encounter count by fiscal year?
What is the sum of the total encounters by month and fiscal year?
Sum of total encounters by fiscal year and month with statistics.
What are the max and min values of the total encounter count?
What is the sum of the total encounters count by citizenship and fiscal year?
Trend line of the sum of total encounters by citizenship and fiscal year with statistics.
Yearly trendline of demographics by fiscal year.
Trend line of total encounters by FY and month for citizens == ‘China’ with statistics.
Trend line of total encounters by FY and month for citizens == ‘Russia’ with statistics.
Trend line of total encounters by FY and month for citizens == ‘Venezuela’ with statistics.
Describe the Source of Data.

Encounters data includes U.S. Border Patrol Title 8 apprehensions, Office of Field Operations Title 8 inadmissibles, and all Tilt 42 expulsions for fiscal years 2020 to date. Data is available from the Northern Land Border and Nationwide (i.e., air, land, and sea modes of transportation) encounters.
Data is extracted from live CBP systems and data sources. Statistical information is subject to change due to corrections, system changes, changes in data definition, additional information, or encounters pending final review. Final statistics are available after each fiscal year.
(https://www.cbp.gov/newsroom/stats/cbp-public-data-portal)
(https://www.cbp.gov/document/stats/nationwide-encounters)
(https://www.cbp.gov/sites/default/files/assets/documents/2023-Sep/nationwide-encounters-data-dictionary.pdf)

