--Calculate and display the total number of records currently stored in the food_prod table.
-- expected to be 1003 after adding three records.
select  
	COUNT(*) AS total_records
from food_prod;


-- Calculate the average market price for crops grouped by their export destination.
select
	fp.export_destination,
	avg(market_price_per_kg) as avg_mp
from
	food_prod fp 
group by 
	fp.export_destination
order by
	avg_mp desc;


-- Retrieve all records where the soil pH level is below 5.5 and the crop is not organically certified.
select 
	*
from food_prod fp 
where
	fp.soil_ph_level < 5.5 and
	fp.organic_certified = 'false';


-- Identify crops with quantity harvested greater than 1000 kg that are exported to countries whose names start with the letter 'G'.
-- !!! export destination has continents, won't have any records for countries
select 
	*
from
	food_prod fp
where
	fp.quantity_harvested > 1000 and
	upper(left(fp.export_destination, 1)) = 'G'; 











