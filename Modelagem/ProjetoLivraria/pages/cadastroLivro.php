<?php
require_once '../includes/config.php';

// Função utilitária para montar selects
function gerarOpcoes($conexao, $tabela)
{
    $dados = '';
    $query = "SELECT codigo, nome FROM $tabela ORDER BY nome";
    $res = mysqli_query($conexao, $query);
    while ($row = mysqli_fetch_assoc($res)) {
        $dados .= "<option value='{$row['codigo']}'>" . htmlspecialchars($row['nome']) . "</option>\n";
    }
    return $dados;
}
?>


<!DOCTYPE html>
<html lang="pt-br">

<head>
    <meta charset="UTF-8">
    <link rel="stylesheet" href="/assets/css/style.css">
    <title>Cadastro de Livro</title>
</head>

<body>
    <form class="form-padrao" action="/includes/processaLivro.php" method="post" enctype="multipart/form-data">
        <h1>Cadastro de Livro</h1>
        <a href="homeCadastros.php" class="btn-voltar">Voltar</a>

        <input type="text" name="titulo" placeholder="Título" required><br><br>
        <input type="number" name="nrpaginas" placeholder="Número de páginas" required><br><br>
        <input type="number" name="ano" placeholder="Ano" required><br><br>

        <!-- Autor -->
        <label class="visually-hidden" for="codautor">Autor:</label><br>
        <select name="codautor" required>
            <option value="">Selecione o autor</option>
            <?php echo gerarOpcoes($conectar, 'autor'); ?>
        </select><br><br>

        <!-- Categoria -->
        <label class="visually-hidden" for="codcategoria">Categoria:</label><br>
        <select name="codcategoria" required>
            <option value="">Selecione a categoria</option>
            <?php echo gerarOpcoes($conectar, 'categoria'); ?>
        </select><br><br>

        <!-- Editora -->
        <label class="visually-hidden" for="codeditora">Editora:</label><br>
        <select name="codeditora" required>
            <option value="">Selecione a editora</option>
            <?php echo gerarOpcoes($conectar, 'editora'); ?>
        </select><br><br>

        <textarea name="resenha" placeholder="Resenha" rows="4" required></textarea><br><br>
        <input type="number" step="0.01" name="preco" placeholder="Preço" required><br><br>

        <label>Foto Capa 1:</label><br>
        <input type="file" name="fotocapa1" required><br><br>

        <label>Foto Capa 2:</label><br>
        <input type="file" name="fotocapa2"><br><br>

        <button type="submit">Cadastrar Livro</button>
    </form>

</body>

</html>