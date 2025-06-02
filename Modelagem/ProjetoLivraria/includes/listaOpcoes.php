<?php
require_once dirname(__FILE__) . '/config.php';

$tipo = isset($tipo) ? $tipo : null;

$tabelasPermitidas = array(
    'autor' => 'autor',
    'categoria' => 'categoria',
    'editora' => 'editora',
);

if (!isset($tabelasPermitidas[$tipo])) {
    die("Tipo inválido.");
}

$tabela = $tabelasPermitidas[$tipo];

$sql = "SELECT codigo, nome FROM $tabela";
$resultado = mysqli_query($conectar, $sql);

if (!$resultado) {
    die("Erro na consulta da tabela '$tabela': " . mysqli_error($conectar));
}

while ($linha = mysqli_fetch_assoc($resultado)) {
    echo "<option value='" . $linha['codigo'] . "'>" . htmlspecialchars($linha['nome']) . "</option>";
}
