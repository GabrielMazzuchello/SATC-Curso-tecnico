<!DOCTYPE html>
<html lang="pt-br">

<head>
    <meta charset="UTF-8">
    <link rel="stylesheet" href="/assets/css/style.css">
    <title>Cadastro de Livro</title>
</head>

<body>
    <h2>Cadastro de Livro</h2>
    <form class="form-padrao" action="/includes/processaLivro.php" method="post" enctype="multipart/form-data">
        <input type="text" name="titulo" placeholder="Título" required><br><br>

        <input type="number" name="nrpaginas" placeholder="Número de páginas" required><br><br>

        <input type="number" name="ano" placeholder="Ano" required><br><br>

        <input type="number" name="codautor" placeholder="Código do autor" required><br><br>

        <input type="number" name="codcategoria" placeholder="Código da categoria" required><br><br>

        <input type="number" name="codeditora" placeholder="Código da editora" required><br><br>

        <textarea name="resenha" placeholder="Resenha" rows="4" cols="50" required></textarea><br><br>

        <input type="number" step="0.01" name="preco" placeholder="Preço" required><br><br>

        <label>Foto Capa 1:</label><br>
        <input type="file" name="fotocapa1" required><br><br>

        <label>Foto Capa 2:</label><br>
        <input type="file" name="fotocapa2"><br><br>

        <button type="submit">Cadastrar Livro</button>
    </form>
</body>

</html>