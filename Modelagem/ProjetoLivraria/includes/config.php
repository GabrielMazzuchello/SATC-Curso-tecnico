<?php
$conectar = mysqli_connect("localhost", "root", "", "livraria");

if (!$conectar) {
    die("Erro na conexão: " . mysqli_connect_error());
}
?>