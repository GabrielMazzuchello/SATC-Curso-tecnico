<?php
function alerta($mensagem, $redirect = null) {
    echo "<script>
        alert('$mensagem');
        " . ($redirect ? "window.location.href = '$redirect';" : "") . "
    </script>";
    exit;
}
