<?php
session_start();

// Verifica se o código do produto foi passado via GET
if (isset($_GET['codigo'])) {
    $codigo = $_GET['codigo'];

    // Verifica se o produto existe no carrinho
    if (isset($_SESSION['carrinho'][$codigo])) {
        unset($_SESSION['carrinho'][$codigo]); // Remove o item do carrinho
    }
}

// Redireciona de volta para o carrinho
header('Location: cart.php');
exit();
