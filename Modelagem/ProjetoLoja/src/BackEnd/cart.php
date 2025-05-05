<?php
session_start(); // Inicia a sessão para acessar os dados do carrinho

// Verifica se o carrinho está vazio
if (empty($_SESSION['carrinho'])) {
    echo "<h1>Seu carrinho está vazio.</h1>";
    exit; // Sai do script se o carrinho estiver vazio
}

?>
<html>

<head>
    <meta charset="UTF-8">
    <title>Carrinho de Compras</title>
    <link rel="stylesheet" type="text/css" href="../styles/estilos.css"> <!-- Estilo do carrinho -->
</head>

<body>
    <div class="home_header">
        <a href="home.php">Voltar para a loja</a>
    </div>

    <div class="carrinho-container">
        <h1>Seu Carrinho</h1>
        <table border="1">
            <tr>
                <th>Produto</th>
                <th>Preço</th>
                <th>Quantidade</th>
                <th>Total</th>
                <th>Remover</th>
            </tr>

            <?php
            $totalCarrinho = 0;

            // Exibe os produtos do carrinho
            foreach ($_SESSION['carrinho'] as $item) {
                $totalProduto = $item['preco'] * $item['quantidade'];
                $totalCarrinho += $totalProduto;

                echo "<tr>";
                echo "<td>" . htmlspecialchars($item['nome']) . "</td>";
                echo "<td>R$ " . number_format($item['preco'], 2, ',', '.') . "</td>";
                echo "<td>" . $item['quantidade'] . "</td>";
                echo "<td>R$ " . number_format($totalProduto, 2, ',', '.') . "</td>";
                echo "<td><a href='remover.php?codigo=" . $item['codigo'] . "'>Remover</a></td>"; // Link para remover o item
                echo "</tr>";
            }
            ?>

        </table>

        <h2>Total do Carrinho: R$ <?php echo number_format($totalCarrinho, 2, ',', '.'); ?></h2>

        <!-- Botão de Finalizar Compra (se quiser adicionar depois) -->
        <a href="finalizar.php">Finalizar Compra</a>
    </div>
</body>

</html>