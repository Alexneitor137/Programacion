<?php include "inc/cabecera.php"; ?>

<section id="paginaproducto">

    <?php
      $host = "localhost";
      $user = "tiendaonlinedamdaw";
      $pass = "Tiendaonlinedamdaw123$";
      $db   = "tiendaonlinedamdaw";

      $conexion = new mysqli($host, $user, $pass, $db);

      $sql = "SELECT * FROM producto WHERE id = ".$_GET['id'].";"; // NUEVO ///////////

      $resultado = $conexion->query($sql);
      while ($fila = $resultado->fetch_assoc()) {
    ?>
      <article>
        <div class="imagen"></div>
        <p><?= $fila['precio'] ?></p>
        <a href="producto.php?id=<?= $fila['id'] ?>">Comprar</a> <!-- NUEVO -->
      </article>
      <article>
      	<h3><?= $fila['nombre_producto'] ?></h3>
        <p><?= $fila['descripcion'] ?></p>
      </article
    <?php
        }

        $conexion->close();
    ?>

</section>

<style>
	#paginaproducto{
  	display:flex;
    gap:20px;
  }
  #paginaproducto article{
  	text-align:center;
    flex:1;
  }
  #paginaproducto article .imagen{
  	background:darkorchid;
    height:100px;
    border-radius:5px 5px 0px 0px;
  }
  #paginaproducto article a{
  	background:darkorchid;
    padding:10px;
    border-radius:5px;
    color:white;
    text-decoration:none;
  }
</style>

<?php include "inc/piedepagina.php"; ?>