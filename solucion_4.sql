
/*CREATE TABLE evento(
	id_evento SERIAL PRIMARY KEY,
	nombre VARCHAR(50) NOT NULL
);

CREATE TABLE entradas(
	id_entradas SERIAL PRIMARY KEY,
	id_evento INTEGER,
	fecha_compra DATE,
	costo NUMERIC,
	CONSTRAINT id_evento_fk FOREIGN KEY (id_evento) REFERENCES evento(id_evento)
);

INSERT INTO evento (nombre) VALUES ('Concierto');
INSERT INTO evento (nombre) VALUES ('Campeonato de fútbol');
INSERT INTO evento (nombre) VALUES ('Ballet');
INSERT INTO evento (nombre) VALUES ('Fiesta');

INSERT INTO entradas (id_evento, fecha_compra, costo) VALUES
(1, '2019-03-21', 20000),
(1, '2019-03-22', 30000),
(4, '2019-03-22', 6000),
(4, '2019-03-23', 6000),
(4, '2019-03-24', 6000),
(1, '2019-03-25', 15000),
(3, '2019-03-25', 8000);*/


--Consulta SQL
SELECT 
	ev.nombre AS nombre_evento,
	COALESCE(SUM(en.costo), 0) AS recaudacion
FROM evento ev
LEFT JOIN entradas en ON en.id_evento = ev.id_evento
GROUP BY ev.nombre
ORDER BY recaudacion DESC;


