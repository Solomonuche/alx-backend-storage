-- a SQL script that lists all bands with Glam rock as their main style, ranked by their longevity

SELECT band_name, IFNULL(split, '2022') - formed AS life_span 
FROM metal_bands 
WHERE FIND_IN_SET('Glam rock', IFNULL(style, "")) > 0
ORDER BY life_span DESC;
