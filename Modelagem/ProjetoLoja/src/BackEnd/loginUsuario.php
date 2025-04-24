<?php
$acessar  = mysql_connect('localhost', 'root', '');
$banco    = mysql_select_db('loja');

if (isset($_POST['conectar'])) {
    $login = $_POST['login'];
    $senha = $_POST['senha'];

    $sql = "SELECT login, senha FROM usuario
        WHERE login = '$login' and senha = '$senha'";

    $resultado = mysql_query($sql);

    if (mysql_num_rows($resultado) == 0) {
        echo "<script language='javascript' type='text/javascript'>
        alert('Login e/ou senha incorretos');
        window.location.href='loginusuario.php';
        </script>";
    } else {
        setcookie('login', $login);
        header('Location:../pages/registrationPage.html');
    }
}
?>

<!DOCTYPE html>
<html lang="pt-br">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="../styles/estilos.css"> <!-- Link para o arquivo CSS -->
    <title>Login - Usuário</title>
</head>

<body>

    <div class="container">
        <form class="form_Login" name="formulario" method="post" action="loginusuario.php">
            <h2>Login de Usuário</h2>

            <!-- Campo para login -->
            <label for="login">Login:</label>
            <input type="text" name="login" id="login" size="10" required>

            <!-- Campo para senha -->
            <label for="senha">Senha:</label>
            <input type="password" name="senha" id="senha" size="10" required>

            <!-- Botão de envio -->
            <input type="submit" name="conectar" value="Conectar">

            <!-- Caso queira adicionar um link para recuperação de senha -->
            <!-- <a href="recuperar-senha.php">Esqueci minha senha</a> -->
        </form>
    </div>

</body>

</html>