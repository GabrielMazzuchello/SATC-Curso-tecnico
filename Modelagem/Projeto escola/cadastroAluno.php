<?php
//conexao com BD
$conectar = mysql_connect("localhost", "root", "");
$banco    = mysql_select_db("escola");

//verificar a operacao usuario (botao)
if (isset($_POST['gravar'])) {
    // Capturar as variáveis HTML
    $codigo = $_POST['codigo'];
    $nome = $_POST['nome'];
    $fone = $_POST['fone'];
    $codcurso = $_POST['codcurso'];

    // Comando SQL para gravar no banco
    $sql = "INSERT INTO aluno (codigo, nome, fone, codcurso) VALUES ('$codigo', '$nome', '$fone', '$codcurso')";

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
    $fone = $_POST['fone'];
    $codcurso = $_POST['codcurso'];

    //comando SQL para gravar banco
    $sql = "update aluno set nome='$nome', codcurso='$codcurso', fone='$fone'
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
    $fone = $_POST['fone'];
    $codcurso = $_POST["codcurso"];

    // comando sql para gravar no banco
    $sql = "delete from aluno where codigo = '$codigo'";

    // comando PHP pra executar SQL no banco
    $resultado = mysql_query($sql);

    if ($resultado == True) {
        echo "dados excluidos com sucesso";
    } else {
        echo "erro ao excluir os dados";
    }
}

if (isset($_POST["pesquisar"])) {

    $sql = "SELECT * FRom aluno";
    $resultado = mysql_query($sql);

    echo "<h3>aluno cadastrados: </h3>";
    echo "<table border=1>
    <tr><td>codigo</td><td>nome</td><td>fone</td><td>codcurso</td></tr>";

    while ($dados = mysql_fetch_array($resultado)) {
        echo "
            <tr>
                <td>" . $dados['codigo'] . "</td>
                <td>" . $dados['nome'] . "</td>
                <td>" . $dados['fone'] . "</td>
                <td>" . $dados['codcurso'] . "</td>
            </tr>";
    }
    echo "</table>";
}
