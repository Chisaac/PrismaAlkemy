SELECT 
    MAX(buyprice) AS Precio_maximo, productLine
FROM
    products
GROUP BY productLine

#3.De la tabla EMPLOYEES mostrar cuanta cantidad de representantes de ventas hay en cada oficina que no sea la 4

SELECT 
    officecode, 
    COUNT(employeeNumber)
FROM
    employees
    where UPPER(jobTitle) = 'SALES REP'
	and officecode != 4
GROUP BY officecode 
    

#5.Mostrar en una tabla el número de cada orden, la cantidad y la fecha de envío (shippedDate)

SELECT 
    od.orderNumber, od.quantityOrdered, o.shippedDate
FROM
    orderdetails AS od
        LEFT JOIN
    orders AS o ON od.orderNumber = o.orderNumber

#7.Obtener la cantidad de clientes por país, ordenado de mayor a menor. Solo mostrar aquellos países con mas de 5 clientes.

SELECT 
    c.country, COUNT(customerNumber) AS cn
FROM
    customers AS c
GROUP BY country
HAVING COUNT(customerNumber) > 5
ORDER BY COUNT(customerNumber) DESC

#9. Obtener una lista con los nombres de clientes y la cantidad de ordenes que se emitieron para ellos.

SELECT 
    o.customerNumber, COUNT(orderNumber) AS cant
FROM
    orders AS o
GROUP BY o.customerNumber

#11.Aplicar un descuento del 10% (buyPrice) a los productos cuya cantidad en stock sea mayor a 8000 (quantityInStock)

SELECT 
    p.productCode AS codigo,
    productName AS Nombre_producto,
    buyPrice * 0.9 AS precio_descontado
FROM
    products p
WHERE
    quantityInStock > 8000

/*13.Obtenga los codigos de producto, nombre, linea a la que pertenecen y descripción de aquellos en los cuales
 la descripción del producto contenga la palabra "features"*/
 
SELECT 
    p.productCode AS codigo,
    productName AS Nombre_producto,
    productLine AS Linea,
    productDescription AS descripcion
FROM
    products AS p
WHERE
    p.productDescription LIKE '%features%'
    
#15.Obtener los nombres de las líneas de producto que tengan más de una palabra

SELECT DISTINCT
    p.productLine
FROM
    products p
WHERE
    p.productLine LIKE '% %'
        AND p.productLine NOT LIKE '% '
        AND p.productLine NOT LIKE ' %'

#17. Obtener un listado de ordenes emitidas a clientes de USA mostrando el valor total de cada orden si se le aplicará un aumento del 10%

SELECT o.orderNumber 
     , ((od.priceEach * od.quantityOrdered)*1.1) AS Total_Orden
  FROM orders o
 INNER JOIN orderdetails od ON o.orderNumber = od.orderNumber 
 INNER JOIN customers c ON o.customerNumber = c.customerNumber 
 WHERE c.country = 'USA'
GROUP BY o.orderNumber 