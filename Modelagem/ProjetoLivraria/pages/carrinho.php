<?php
session_start();
require_once '../includes/config.php';

// Inicializa carrinho se não existir
if (!isset($_SESSION['carrinho'])) {
    $_SESSION['carrinho'] = array();
}

// Atualizar quantidade
if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['atualizar_id'], $_POST['quantidade'])) {
    $id = intval($_POST['atualizar_id']);
    $qtd = max(1, intval($_POST['quantidade'])); // evita valores 0 ou negativos
    $_SESSION['carrinho'][$id] = $qtd;
    header("Location: carrinho.php");
    exit;
}

// Remover item
if (isset($_GET['remover'])) {
    unset($_SESSION['carrinho'][$_GET['remover']]);
    header("Location: carrinho.php");
    exit;
}

// Obter dados
$livros = array();
$total = 0;

if (!empty($_SESSION['carrinho'])) {
    $ids = implode(',', array_map('intval', array_keys($_SESSION['carrinho'])));
    $query = "SELECT codigo, titulo, preco, fotocapa1 FROM livro WHERE codigo IN ($ids)";
    $resultado = mysqli_query($conectar, $query);

    while ($livro = mysqli_fetch_assoc($resultado)) {
        $id = $livro['codigo'];
        $qtd = $_SESSION['carrinho'][$id];
        $livro['quantidade'] = $qtd;
        $livro['subtotal'] = $livro['preco'] * $qtd;
        $total += $livro['subtotal'];
        $livros[] = $livro;
    }
}
?>

<!DOCTYPE html>
<html lang="pt-br">

<head>
    <meta charset="UTF-8">
    <title>Carrinho</title>
    <link rel="stylesheet" href="/assets/css/style.css">
</head>

<body>
    <div class="form-padrao">
        <a href="../index.php" class="btn-voltar">Voltar</a>
        <h1>Seu Carrinho</h1>

        <?php if (empty($livros)) : ?>
            <p style="text-align: center">Seu carrinho está vazio.</p>
        <?php else : ?>
            <div class="livroGrid">
                <?php foreach ($livros as $livro) : ?>
                    <div class="livroCard">
                        <img src="/<?php echo htmlspecialchars($livro['fotocapa1']); ?>" alt="<?php echo htmlspecialchars($livro['titulo']); ?>">
                        <h4><?php echo htmlspecialchars($livro['titulo']); ?></h4>
                        <p><strong>Preço:</strong> R$ <?php echo number_format($livro['preco'], 2, ',', '.'); ?></p>

                        <form action="carrinho.php" method="post" class="form-quantidade">
                            <input type="hidden" name="atualizar_id" value="<?php echo $livro['codigo']; ?>">
                            <label for="quantidade_<?php echo $livro['codigo']; ?>">Qtd:</label>
                            <input type="number"
                                min="1"
                                name="quantidade"
                                id="quantidade_<?php echo $livro['codigo']; ?>"
                                value="<?php echo $livro['quantidade']; ?>"
                                onchange="this.form.submit()" />
                        </form>

                        <p><strong>Subtotal:</strong> R$ <?php echo number_format($livro['subtotal'], 2, ',', '.'); ?></p>
                        <a class="btn-carrinho" href="?remover=<?php echo $livro['codigo']; ?>">Remover</a>
                    </div>
                <?php endforeach; ?>
            </div>
            <h3 style="text-align: center; margin-top: 20px;">Total: R$ <?php echo number_format($total, 2, ',', '.'); ?></h3>
        <?php endif; ?>
    </div>
</body>

</html>