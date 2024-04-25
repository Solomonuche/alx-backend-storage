-- a SQL script that lists all bands with Glam rock as their main style, ranked by their longevity

SELECT band_name, split - formed AS life_span 
FROM metal_bands 
ORDER BY life_span DESC;
