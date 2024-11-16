# Client Project Requirements

<aside>
⚙

### Technical Requirements

- **Platform**: A public web application accessible without authentication.
- **Real-Time Data**: The dashboard should display the latest data, pulling directly from the API.
- **User Interactivity**: Users should be able to filter, compare, and rank countries based on EV sales data.
- **Design**: The dashboard should be intuitive and visually appealing, with clearly labeled sections and informative charts.
</aside>

<aside>
📊

### Key Analytical Requirements

The client’s requirements are divided into two main sections: *EV Sales and Sales Share* and *Charging Points*. Each section will help the Head of Expansion answer specific strategic questions.

- **EV Sales and Sales Share**
    - **Country-Level EV Sales**:
        - Total EV sales by country, broken down historically.
        - Breakdown by powertrain type (Battery Electric Vehicles, Fuel Cell Electric Vehicles, Plug-in Hybrid Electric Vehicles).
    - **EV Adoption Ranking**:
        - A ranked list of the top 10 countries leading in EV adoption based on sales share. The top 10 countries should be prominently highlighted.
    - **Country Comparison**:
        - Ability to select and compare EV adoption trends for specific countries (e.g., compare X, Y, and Z) over time with a filter for different powertrains.
- **Charging Points**
    - **Total Charging Points by Country**:
        - Display the total number of EV charging points available per country. Rank the top 10 countries by charging points.
    - **Charging Infrastructure Growth**:
        - Historical view of charging infrastructure expansion across different countries.
    - **Types of Charging Points**:
        - Breakdown by type (e.g., publicly available fast or slow charging points).
    - **Regional Insights**:
        - Regional breakdown of charging point density to support strategic deployment of new infrastructure.
</aside>

<aside>
💽

### Data Source

The [Global EV Data Explorer API](https://www.iea.org/data-and-statistics/data-tools/global-ev-data-explorer) from the International Energy Agency (IEA) will serve as our primary data source. Here’s a summary of the dataset’s key fields and terms:

- **Fields**: The dataset includes columns for region, category, parameter, mode, powertrain, year, unit, and value, enabling a multifaceted analysis of EV adoption.
- **Important Terms**:
    - **BEV**: Battery Electric Vehicles
    - **FCEV**: Fuel Cell Electric Vehicles
    - **PHEV**: Plug-in Hybrid Electric Vehicles
    - **Charging Points**: Publicly available fast or slow charging points
    - **Mode**: Types of vehicles, including Cars, Buses, Vans, and Trucks

This data, segmented by country and powertrain type, will allow us to deliver a comprehensive, insightful, and interactive EV adoption dashboard tailored to our client's needs.

</aside>