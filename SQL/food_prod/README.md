# Food_Prod Folder

This folder contains SQL scripts related to food production data analysis. The primary file in this directory is `food_prod.sql`, which includes several queries designed to analyze and extract insights from a table named `food_prod`.

## File: `food_prod.sql`

This SQL script provides a set of queries for working with the `food_prod` table. The table is assumed to store information about various food crops, their production details, and export data. Below is a breakdown of each query and its purpose:

### 1. Count Total Records

```sql
select
    COUNT(*) AS total_records
from food_prod;
```

- **Purpose:** Calculates and displays the total number of records currently stored in the `food_prod` table.
- **Note:** The expected count is 1003 after adding three new records.

### 2. Average Market Price by Export Destination

```sql
select
    fp.export_destination,
    avg(market_price_per_kg) as avg_mp
from
    food_prod fp
group by
    fp.export_destination
order by
    avg_mp desc;
```

- **Purpose:** Calculates the average market price per kilogram for crops, grouped by their export destination (e.g., continent or region).
- **Use Case:** Useful for comparing market prices across different export destinations.

### 3. Records with Low Soil pH and Not Organically Certified

```sql
select
    *
from food_prod fp
where
    fp.soil_ph_level < 5.5 and
    fp.organic_certified = 'false';
```

- **Purpose:** Retrieves all records where the soil pH level is below 5.5 and the crop is not organically certified.
- **Use Case:** Identifies crops grown in acidic soils without organic certification, which may require attention for soil management or certification improvement.

### 4. High Quantity Harvested & Exported to 'G' Destinations

```sql
select
    *
from
    food_prod fp
where
    fp.quantity_harvested > 1000 and
    upper(left(fp.export_destination, 1)) = 'G';
```

- **Purpose:** Identifies crops with a harvested quantity greater than 1000 kg that are exported to destinations starting with the letter 'G'.
- **Note:** The export destination field contains continents, so this query may not return any records if no continent starts with 'G'.

## Usage

- Use these queries to analyze food production data, monitor market trends, and identify records of interest for further investigation or reporting.
- Modify the queries as needed to fit your specific schema or analysis requirements.
