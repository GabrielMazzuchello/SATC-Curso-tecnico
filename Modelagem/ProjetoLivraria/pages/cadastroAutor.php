<!DOCTYPE html>
<html lang="pt-br">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cadastro de Autores</title>
</head>

<body>
    <h2>Cadastro de Autores</h2>
    <form action="/includes/processaAutor.php" method="post">
        <input type="text" name="nome" placeholder="Nome do autor">
        <input type="text" name="pais" placeholder="Pais do autor">
        <button type="submit">Cadastrar</button>
    </form>

</body>

</html>