<?php
require_once 'config.php';

mysqli_set_charset($conectar, 'utf8'); // Suporte a acentos

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $username = trim($_POST['username']);
    $password = trim($_POST['password']);

    if ($username && $password) {
        // Escapa os valores manualmente
        $username = mysqli_real_escape_string($conectar, $username);
        $password = mysqli_real_escape_string($conectar, $password);

        // Monta a query diretamente
        $query = "SELECT * FROM usuarios WHERE login = '$username' AND senha = '$password'";
        $result = mysqli_query($conectar, $query);

        if ($result && mysqli_num_rows($result) > 0) {
            session_start();
            $_SESSION['loggedin'] = true;
            $_SESSION['username'] = $username;

            header('Location: /pages/homeCadastros.php');
            exit;
        } else {
            echo "Usuário ou senha inválidos.";
        }
    } else {
        echo "Preencha todos os campos.";
    }
} else {
    echo "Requisição inválida.";
}
