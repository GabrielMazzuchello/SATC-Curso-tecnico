<?php
require_once 'config.php';

if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $nome = isset($_POST['nome']) ? $_POST['nome'] : '';

    if ($nome) {
        $stmt = mysqli_prepare($conectar, "INSERT INTO categoria (nome) VALUES (?)");
        mysqli_stmt_bind_param($stmt, "s", $nome);
        mysqli_stmt_execute($stmt);
        mysqli_stmt_close($stmt);

        echo "Categoria cadastrada.";

        exit;
    } else {
        echo "Por favor, preencha o nome.";
    }
} else {
    echo "Acesso inválido.";
}
