<!DOCTYPE html>
<html lang="pt-br">

<head>
    <meta charset="UTF-8">
    <link rel="stylesheet" href="/assets/css/style.css">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cadastro de Autores</title>
</head>

<body>
    <form class="form-padrao" action="/includes/processaAutor.php" method="post">
        <h1>Cadastro de Autores</h1>
        <a href="homeCadastros.php" class="btn-voltar">Voltar</a>
        <input type="text" name="nome" placeholder="Nome do autor" required>
        <input type="text" name="pais" placeholder="Pais do autor" required>
        <button type="submit">Cadastrar</button>
    </form>

</body>

</html>