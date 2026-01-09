<?php
$archivo_reservas = 'reservas.json';
if (!file_exists($archivo_reservas)) file_put_contents($archivo_reservas, json_encode([]));
$reservas_actuales = json_decode(file_get_contents($archivo_reservas), true);

if (isset($_POST['confirmar'])) {
    $nueva_reserva = [
        'nombre' => htmlspecialchars($_POST['nombre']),
        'email' => htmlspecialchars($_POST['email']),
        'telefono' => htmlspecialchars($_POST['telefono']),
        'campo' => $_POST['campo'],
        'fecha' => $_POST['fecha'],
        'hora' => $_POST['hora'],
        'duracion' => $_POST['duracion'],
        'fin' => date("H:i", strtotime($_POST['hora'] . " + " . $_POST['duracion'] . " hours"))
    ];
    $reservas_actuales[] = $nueva_reserva;
    file_put_contents($archivo_reservas, json_encode($reservas_actuales));
    $mensaje_exito = "RESERVA CONFIRMADA PARA " . strtoupper($nueva_reserva['nombre']);
}

function obtener_estado($num_campo, $reservas) {
    $hoy = date('Y-m-d');
    $ahora = date('H:i');
    foreach ($reservas as $r) {
        if ($r['campo'] == $num_campo && $r['fecha'] == $hoy) {
            if ($ahora >= $r['hora'] && $ahora < $r['fin']) {
                $restante = round((strtotime($r['fin']) - strtotime($ahora)) / 60);
                return ['ocupado' => true, 'libre_en' => $restante];
            }
        }
    }
    return ['ocupado' => false];
}
?>

<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>SOFIVE MANISES | RESERVAS</title>
    <style>
        :root {
            --neon-green: #00ff00;
            --dark-bg: #0b0c24;
            --card-bg: #161b33;
            --text-gray: #a0a0a0;
        }

        body {
            background-color: var(--dark-bg);
            color: white;
            font-family: 'Segoe UI', sans-serif;
            margin: 0;
            padding: 20px;
        }

        .container { max-width: 1000px; margin: auto; }

        h1 { color: var(--neon-green); font-size: 2.5rem; text-transform: uppercase; margin-bottom: 0; }
        
        .location-header {
            color: var(--text-gray);
            margin-bottom: 20px;
            border-bottom: 1px solid #333;
            padding-bottom: 10px;
            text-transform: uppercase;
            letter-spacing: 1px;
        }

        .pago-aviso {
            background: rgba(0, 255, 0, 0.1);
            border: 1px dashed var(--neon-green);
            color: var(--neon-green);
            padding: 15px;
            text-align: center;
            font-weight: bold;
            margin-bottom: 30px;
            text-transform: uppercase;
        }

        .grid-campos {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 15px;
            margin-bottom: 30px;
        }

        .campo-card {
            background: var(--card-bg);
            border: 1px solid #333;
            padding: 20px;
            border-radius: 4px;
            transition: 0.3s;
            cursor: pointer;
        }

        .campo-card:hover:not(.ocupado) { border-color: var(--neon-green); }
        .campo-card.selected { border-color: var(--neon-green); background: #1a2a24; }

        .campo-nombre { display: block; font-size: 1.1rem; font-weight: bold; margin-top: 5px; }
        
        .status-pill {
            display: inline-block;
            margin-top: 10px;
            font-size: 0.7rem;
            padding: 4px 8px;
            text-transform: uppercase;
        }
        .status-available { color: var(--neon-green); }
        .status-busy { color: #ff4444; }

        .form-section { background: var(--card-bg); padding: 30px; border-radius: 8px; }

        input, select {
            background: #050614;
            border: 1px solid #333;
            color: white;
            padding: 12px;
            margin-bottom: 15px;
            width: 100%;
            box-sizing: border-box;
        }

        input:focus { border-color: var(--neon-green); outline: none; }

        .btn-reserve {
            background: var(--neon-green);
            color: black;
            border: none;
            padding: 20px;
            width: 100%;
            font-weight: bold;
            text-transform: uppercase;
            cursor: pointer;
            font-size: 1rem;
        }

        .contact-info {
            margin-top: 50px;
            padding: 20px;
            border-top: 1px solid #333;
            display: flex;
            justify-content: space-around;
            color: var(--text-gray);
            font-size: 0.9rem;
        }

        .contact-item strong { color: var(--neon-green); display: block; margin-bottom: 5px; }

        .ocupado { opacity: 0.4; cursor: not-allowed; border-color: #ff4444; }
        input[type="radio"] { display: none; }
        
        .success-msg {
            background: var(--neon-green); color: black;
            padding: 15px; margin-bottom: 20px; text-align: center; font-weight: bold;
        }
    </style>
</head>
<body>

<div class="container">
    <h1>SOFIVE MANISES</h1>
    <div class="location-header"> NAVE AEROPUERTO MANISES, VALENCIA</div>

    <div class="pago-aviso">
         EL PAGO SE REALIZA AL LLEGAR AL ESTABLECIMIENTO
    </div>

    <?php if(isset($mensaje_exito)) echo "<div class='success-msg'>$mensaje_exito</div>"; ?>

    <form method="POST">
        <div class="grid-campos">
            <?php for($i = 1; $i <= 8; $i++): 
                $estado = obtener_estado($i, $reservas_actuales);
            ?>
                <label class="campo-card <?php echo $estado['ocupado'] ? 'ocupado' : ''; ?>">
                    <?php if(!$estado['ocupado']): ?>
                        <input type="radio" name="campo" value="<?php echo $i; ?>" required>
                    <?php endif; ?>
                    <span style="font-size: 0.65rem; color: var(--text-gray)">MANISES </span>
                    <span class="campo-nombre">CAMPO 0<?php echo $i; ?></span>
                    <?php if($estado['ocupado']): ?>
                        <span class="status-pill status-busy">● OCUPADO (Libre en <?php echo $estado['libre_en']; ?>m)</span>
                    <?php else: ?>
                        <span class="status-pill status-available">● DISPONIBLE</span>
                    <?php endif; ?>
                </label>
            <?php endfor; ?>
        </div>

        <div class="form-section">
            <h3 style="color:var(--neon-green); margin-top:0">INFORMACIÓN DEL CLIENTE</h3>
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px;">
                <input type="text" name="nombre" placeholder="NOMBRE COMPLETO" required>
                <input type="email" name="email" placeholder="CORREO ELECTRÓNICO" required>
                <input type="tel" name="telefono" placeholder="NÚMERO DE TELÉFONO" required>
                <input type="date" name="fecha" value="<?php echo date('Y-m-d'); ?>" required>
                <input type="time" name="hora" required>
                <select name="duracion">
                    <option value="1">1 HORA DE JUEGO</option>
                    <option value="2">2 HORAS DE JUEGO</option>
                </select>
            </div>
            <button type="submit" name="confirmar" class="btn-reserve">Confirmar Reserva Online</button>
        </div>
    </form>

    <div class="contact-info">
        <div class="contact-item">
            <strong>EMAIL</strong>
            sofivemanisesvalencia@gmail.es
        </div>
        <div class="contact-item">
            <strong>TELÉFONO</strong>
            690 900 200
        </div>
        <div class="contact-item">
            <strong>UBICACIÓN</strong>
            Nave aeropuerto Manises, Valencia
        </div>
    </div>
</div>

<script>
    document.querySelectorAll('.campo-card').forEach(card => {
        card.addEventListener('click', function() {
            if(!this.classList.contains('ocupado')) {
                document.querySelectorAll('.campo-card').forEach(c => c.classList.remove('selected'));
                this.classList.add('selected');
            }
        });
    });
</script>

</body>
</html>