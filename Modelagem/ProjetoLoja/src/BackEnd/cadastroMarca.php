<?php
//conexao com BD
$conectar = mysql_connect("localhost", "root", "");
$banco    = mysql_select_db("loja");

//verificar a operacao usuario (botao)
if (isset($_POST['gravar'])) {
    // Capturar as variáveis HTML
    $codigo = $_POST['codigo'];
    $nome = $_POST['nome'];

    // Comando SQL para gravar no banco
    $sql = "INSERT INTO marca (nome) VALUES ('$nome')";

    // Executar a consulta
    $resultado = mysql_query($sql);

    if ($resultado) {
        echo "Dados gravados com sucesso!!!";
    } else {
        echo "Erro ao gravar os dados no banco ";
    }
}


//verificar a operacao usuario (botao)
if (isset($_POST['alterar'])) {
    //capturar as variaveis HTML
    $codigo      = $_POST['codigo'];
    $nome        = $_POST['nome'];

    //comando SQL para gravar banco
    $sql = "update marca set nome='$nome''
          where codigo = '$codigo'";

    //comando PHP pra executar SQl no banco (boolean)
    $resultado = mysql_query($sql);

    if ($resultado == TRUE) {
        echo "Dados alterados com sucesso!!!";
    } else {
        echo "Erro ao alterar os dados no banco!!!";
    }
}

if (isset($_POST["excluir"])) {
    // capturar variaveis do HTML
    $codigo = $_POST["codigo"];
    $nome = $_POST["nome"];

    // comando sql para gravar no banco
    $sql = "delete from marca where codigo = '$codigo'";

    // comando PHP pra executar SQL no banco
    $resultado = mysql_query($sql);

    if ($resultado == True) {
        echo "dados excluidos com sucesso";
    } else {
        echo "erro ao excluir os dados";
    }
}

if (isset($_POST["pesquisar"])) {

    $sql = "SELECT * FRom marca";
    $resultado = mysql_query($sql);

    echo "<h3>marca cadastrados: </h3>";
    echo "<table border=1>
    <tr><td>codigo</td><td>nome</td></tr>";

    while ($dados = mysql_fetch_array($resultado)) {
        echo "
            <tr>
                <td>" . $dados['codigo'] . "</td>
                <td>" . $dados['nome'] . "</td>
            </tr>";
    }
    echo "</table>";
}
