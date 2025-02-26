--1--

SELECT cd.cdtitle, cdPrice  FROM cd  WHERE cd.cdtitle NOT LIKE '% %';

--2--

SELECT cd.cdtitle, cd.artID FROM cd WHERE cd.cdtitle LIKE '%ro%';

--3--

SELECT * FROM cd WHERE cd.cdtitle LIKE '_%he%';
--4--

SELECT cd.cdtitle FROM cd WHERE cd.cdgenre = (SELECT cd.cdgenre FROM cd WHERE cd.cdtitle='Version');

--5--

SELECT cdTitle FROM CD WHERE cdPrice IN (SELECT cdPrice FROM CD WHERE cdGenre = 'Electronica');

--6--

SELECT cdTitle FROM CD WHERE cdPrice < ANY (SELECT cdPrice FROM CD);

--7--

SELECT cdTitle FROM CD WHERE cdPrice <= ALL (SELECT cdPrice FROM CD);

--8--

SELECT artName FROM Artist A WHERE EXISTS (SELECT 1 FROM CD C WHERE C.artID = A.artID AND C.cdGenre = 'Pop');

--9--

SELECT DISTINCT A.artName FROM Artist A JOIN CD C ON A.artID = C.artID WHERE C.cdGenre = 'Rock';

--10--

SELECT cdTitle FROM CD WHERE artID IN (SELECT artID FROM Artist WHERE artName LIKE '% %');

--11--

SELECT * FROM CD WHERE cdGenre IN ('Rock', 'Pop') AND cdPrice < ALL (SELECT cdPrice FROM CD WHERE cdGenre IN ('Rock', 'Pop'));

--12--

SELECT Artist.artName, Artist.artID FROM Artist JOIN CD ON Artist.artID = CD.artID WHERE CD.cdPrice = 12.99;

SELECT artName, artID FROM Artist WHERE artID IN (SELECT artID FROM CD WHERE cdPrice = 12.99);

--13--

SELECT cdTitle FROM CD ORDER BY cdTitle DESC;

--14--

SELECT cdTitle, cdGenre, cdPrice FROM CD ORDER BY cdPrice ASC;

--15--

SELECT cdTitle, cdGenre, cdPrice FROM CD ORDER BY cdPrice DESC;

--16--

SELECT cdTitle, cdGenre, cdPrice FROM CD ORDER BY cdGenre ASC, cdPrice DESC;

--17--

SELECT Artist.artName, COUNT(CD.cdID) AS num_CDs, AVG(CD.cdPrice) AS avg_price FROM Artist JOIN CD ON Artist.artID = CD.artID GROUP BY Artist.artName HAVING COUNT(CD.cdID) > 1;

--18--

SELECT Artist.artName, COUNT(CD.cdID) AS num_CDs, AVG(CD.cdPrice) AS avg_price
FROM Artist
JOIN CD ON Artist.artID = CD.artID
WHERE CD.cdGenre <> 'Electronica'
GROUP BY Artist.artName
HAVING COUNT(CD.cdID) > 1;

--19--

SELECT ABS(
    (SELECT AVG(cdPrice) FROM CD WHERE cdGenre = 'Rock') - 
    (SELECT AVG(cdPrice) FROM CD WHERE artID NOT IN (SELECT artID FROM Artist WHERE artName = 'Muse'))
) AS price_difference;

--20--

SELECT Artist.artName
FROM Artist
JOIN CD ON Artist.artID = CD.artID
GROUP BY Artist.artName
ORDER BY AVG(CD.cdPrice) DESC
LIMIT 1;

--21--

SELECT cdGenre
FROM CD
GROUP BY cdGenre
ORDER BY MIN(cdPrice) DESC
LIMIT 1;

--22--

SELECT Artist.artName, COUNT(CD.cdID) AS num_CDs, AVG(CD.cdPrice) AS avg_price
FROM Artist
JOIN CD ON Artist.artID = CD.artID
WHERE CD.cdGenre <> 'Pop'
GROUP BY Artist.artName
HAVING COUNT(CD.cdID) > 1;