<?php
require_once 'config.php';
require_once 'alerta.php';

if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $nome = isset($_POST['nome']) ? $_POST['nome'] : '';
    $pais = isset($_POST['pais']) ? $_POST['pais'] : '';

    if ($nome && $pais) {
        $stmt = mysqli_prepare($conectar, 'INSERT INTO autor (nome, pais) VALUES (?, ?)');
        mysqli_stmt_bind_param($stmt, 'ss', $nome, $pais);

        mysqli_stmt_execute($stmt);
        mysqli_stmt_close($stmt);

        alerta("Autor cadastrado com sucesso!", "/pages/homeCadastros.php");

        exit;
    } else {
        alerta("Por favor, preencha o nome.");
    }
} else {
    alerta("Acesso inválido.");
}
