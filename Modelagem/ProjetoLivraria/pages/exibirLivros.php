<?php
require_once 'includes/config.php';

function limpar($valor)
{
    return htmlspecialchars(strip_tags(trim($valor)));
}

$autor = isset($_GET['autor']) ? limpar($_GET['autor']) : '';
$categoria = isset($_GET['categoria']) ? limpar($_GET['categoria']) : '';
$editora = isset($_GET['editora']) ? limpar($_GET['editora']) : '';

$sql = "
    SELECT 
        livro.*, 
        autor.nome AS autor_nome, 
        categoria.nome AS categoria_nome, 
        editora.nome AS editora_nome
    FROM livro
    JOIN autor ON autor.codigo = livro.codautor
    JOIN categoria ON categoria.codigo = livro.codcategoria
    JOIN editora ON editora.codigo = livro.codeditora
    WHERE 1
";

$params = array();
$bindValues = array();

if ($autor) {
    $sql .= " AND livro.codautor = ?";
    $params[] = 'i';
    $bindValues[] = $autor;
}
if ($categoria) {
    $sql .= " AND livro.codcategoria = ?";
    $params[] = 'i';
    $bindValues[] = $categoria;
}
if ($editora) {
    $sql .= " AND livro.codeditora = ?";
    $params[] = 'i';
    $bindValues[] = $editora;
}

$sql .= " LIMIT 10";

$stmt = mysqli_prepare($conectar, $sql);

if (count($params) > 0) {
    // bind_param precisa de argumentos por referência em PHP 5.3
    $refs = array();
    foreach ($bindValues as $key => $value) {
        $refs[$key] = &$bindValues[$key];
    }

    array_unshift($refs, implode('', $params)); // tipos no início

    call_user_func_array(array($stmt, 'bind_param'), $refs);
}

mysqli_stmt_execute($stmt);
$resultado = mysqli_stmt_get_result($stmt);

if (!$resultado || mysqli_num_rows($resultado) === 0) {
    echo "<p style='text-align:center;'>Nenhum livro encontrado.</p>";
} else {
    echo "<div class='livroGrid'>";
    while ($livro = mysqli_fetch_assoc($resultado)) {
        echo "<div class='livroCard'>";
        echo "<img src='{$livro['fotocapa1']}' alt='{$livro['titulo']}'>";
        echo "<h4>{$livro['titulo']}</h4>";
        echo "<p><strong>Autor:</strong> {$livro['autor_nome']}</p>";
        echo "<p><strong>Categoria:</strong> {$livro['categoria_nome']}</p>";
        echo "<p><strong>Editora:</strong> {$livro['editora_nome']}</p>";
        echo "<p><strong>Preço:</strong> R$ " . number_format($livro['preco'], 2, ',', '.') . "</p>";
        echo "<button class='btn-carrinho' disabled>AddCarrinho</button>";
        echo "</div>";
    }
    echo "</div>";
}
