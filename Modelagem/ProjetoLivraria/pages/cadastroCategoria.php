<!DOCTYPE html>
<html lang="pt-br">

<head>
    <meta charset="UTF-8">
    <link rel="stylesheet" href="/assets/css/style.css">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cadastro de Categorias</title>
</head>

<body>
    <h2>Cadastro de Categorias</h2>
    <form class="form-padrao" action="/includes/processaCategoria" method="post">
        <input type="text" name="nome" placeholder="Nome da categoria" required>
        <button type="submit">Cadastrar</button>
    </form>
</body>

</html>