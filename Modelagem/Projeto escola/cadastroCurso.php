<?php 
// conexão com DB
$conectar = mysql_connect("localhost", "root", "");
$banco = mysql_select_db("escola");

// verificar a opção de usuario (botão)
if (isset($_POST['gravar'])) {
    // capturar variaveis do HTML
    $codigo = $_POST['codigo'];
    $nome = $_POST['nome'];
    $coordenador = $_POST['coordenador'];

    // comando sql para gravar no banco
    $sql = "insert into cursos (codigo,nome,coordenador) values ('$codigo', '$nome', '$coordenador')";

    // comando PHP pra executar SQL no banco

    $resultado = mysql_query($sql);

    if ($resultado == TRUE) {
        echo "dados cadastrados com sucesso";
    }
    else {
        echo "erro ao cadastrar os dados";
    }
};

if (isset($_POST['gravar'])) {
    
};

if (isset($_POST['gravar'])) {
    
};

if (isset($_POST['gravar'])) {
    
};
?>