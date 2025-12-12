<?php

  $titulo = $_POST['titulo'];
  $contenido = $_POST['contenido'];
  $fecha_publicacion = $_POST['fecha_publicacion'];
  $autor_id = $_POST['autor_id'];

  $host = "localhost";
  $user = "periodico";
  $pass = "Periodico123$";
  $db   = "periodico";

  $conexion = new mysqli($host, $user, $pass, $db);

  $sql = "
  	INSERT INTO noticias VALUES(
    	NULL,
      '".$titulo."',
      '".$contenido."',
      '".$fecha_publicacion."',
     	".$autor_id."
    );
  ";
  $conexion->query($sql);
	
  $conexion->close();
  header("Location: ")
  
?>