<?php
//conexao com BD
$conectar = mysql_connect("localhost","root","");
$banco    = mysql_select_db("escola");

//verificar a operacao usuario (botao)
if (isset($_POST['gravar'])) {
    // Capturar as variáveis HTML
    $codigo = $_POST['codigo'];
    $nome = $_POST['nome'];
    $coordenador = $_POST['coordenador'];

    // Comando SQL para gravar no banco
    $sql = "INSERT INTO curso (codigo, nome, coordenador) VALUES ('$codigo', '$nome', '$coordenador')";

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
  $coordenador = $_POST['coordenador'];

  //comando SQL para gravar banco
  $sql = "update curso set nome='$nome',coordenador='$coordenador'
          where codigo = '$codigo'";

  //comando PHP pra executar SQl no banco (boolean)
  $resultado = mysql_query($sql);

  if ($resultado == TRUE)
  {
     echo "Dados alterados com sucesso!!!";
  }
  else
  {
     echo "Erro ao alterar os dados no banco!!!";
  }
}

if (isset($_POST["excluir"])) {
    // capturar variaveis do HTML
    $codigo = $_POST["codigo"];
    $nome = $_POST["nome"];
    $coordenador = $_POST["coordenador"];

    // comando sql para gravar no banco
    $sql = "delete from curso where codigo = '$codigo'";

    // comando PHP pra executar SQL no banco
    $resultado = mysql_query($sql);

    if ($resultado == True) {
        echo "dados excluidos com sucesso";
    } else {
        echo "erro ao excluir os dados";
    }
}

if (isset($_POST["pesquisar"])) {

    $sql = "SELECT * FRom curso";
    $resultado = mysql_query($sql);

    echo "<h3>curso cadastrados: </h3>";
    echo "<table border=1>
    <tr><td>codigo</td><td>curso</td><td>coordenador</td></tr>";

    while ($dados = mysql_fetch_array($resultado)) {
        echo"
            <tr>
                <td>".$dados['codigo']."</td>
                <td>".$dados['nome']."</td>
                <td>".$dados['coordenador']."</td>
            </tr>";
    }
    echo "</table>";
}
?>