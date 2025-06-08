<!DOCTYPE html>
<html lang="pt-br">

<head>
    <meta charset="UTF-8">
    <link rel="stylesheet" href="/assets/css/style.css">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cadastro de Categorias</title>
</head>

<body>
    <form class="form-padrao" action="/includes/processaCategoria" method="post">
        <h1>Cadastro de Categorias</h1>
        <input type="text" name="nome" placeholder="Nome da categoria" required>
        <button type="submit">Cadastrar</button>
    </form>
</body>

</html>