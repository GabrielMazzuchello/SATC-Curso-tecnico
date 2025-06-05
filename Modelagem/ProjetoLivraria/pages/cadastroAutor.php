<!DOCTYPE html>
<html lang="pt-br">

<head>
    <meta charset="UTF-8">
    <link rel="stylesheet" href="/assets/css/style.css">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cadastro de Autores</title>
</head>

<body>
    <h2>Cadastro de Autores</h2>
    <form class="form-padrao" action="/includes/processaAutor.php" method="post">
        <input type="text" name="nome" placeholder="Nome do autor" required>
        <input type="text" name="pais" placeholder="Pais do autor" required>
        <button type="submit">Cadastrar</button>
    </form>

</body>

</html>