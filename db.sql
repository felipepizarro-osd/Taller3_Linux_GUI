CREATE TABLE monstruos(id serial primary key not null , name varchar(50) , velocity int, health int );

INSERT INTO monstruos (name , velocity , health) values ('spiderman',20,100);
INSERT INTO monstruos (name , velocity , health) values ('ironman',30,70);
INSERT INTO monstruos (name , velocity , health) values ('locochoro',50,30);

CREATE TABLE entrenador (
    id serial primary key not null,
    nombre varchar(50) ,
    password varchar(50) , 
    nombre_usuario varchar(50),
    fecha_nac date,
    edad int

);
INSERT INTO entrenador (nombre,password,nombre_usuario,fecha_nac,edad) VALUES ('felipe','root','el destroza imbeciles',
'12-02-1998',23);

INSERT INTO entrenador (nombre,password,nombre_usuario,fecha_nac,edad) VALUES ('Mario','root1','emilio el cara de uva',
'12-03-1998',23);

INSERT INTO entrenador (nombre,password,nombre_usuario,fecha_nac,edad) VALUES ('martin','root2','imbeciles venid a por mi',
'12-04-1998',23);
CREATE TABLE estadisticas (
    id int primary key not null,
    nombre_combate varchar(50),
    ganado boolean,
    perdido boolean
);
