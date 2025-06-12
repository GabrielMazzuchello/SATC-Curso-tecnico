<?php
session_start();

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $id = intval($_POST['id_livro']);
    $qtd = intval($_POST['quantidade']);

    if (!isset($_SESSION['carrinho'])) {
        $_SESSION['carrinho'] = array();
    }

    if (isset($_SESSION['carrinho'][$id])) {
        $_SESSION['carrinho'][$id] += $qtd;
    } else {
        $_SESSION['carrinho'][$id] = $qtd;
    }

    header("Location: ../index.php");
    exit;
}
