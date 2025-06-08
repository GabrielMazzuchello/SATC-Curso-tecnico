<!DOCTYPE html>
<html lang="pt-br">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login</title>
    <link rel="stylesheet" href="/assets/css/style.css">
</head>

<body>
    <form class="form-padrao" action="/includes/processaLogin.php" method="post">
        <h2>Login</h2>
        <input type="text" name="username" placeholder="Usuário" required><br><br>
        <input type="text" name="password" placeholder="Senha" required><br><br>
        <button type="submit">Entrar</button>
    </form>
</body>

</html>