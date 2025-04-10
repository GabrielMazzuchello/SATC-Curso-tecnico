<?php
$connect = mysql_connect('localhost', 'root', ''); // Conectar ao banco de dados
$db      = mysql_select_db('loja'); // Selecionar o banco de dados
?>

<HTML>

<HEAD>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <TITLE>Pagina Principal</TITLE>
    <link rel="stylesheet" type="text/css" href="../styles/estilos.css">
</HEAD>

<body>
    <div class="home_header">
        <div>
            <img src="../imgs/logo.png" class="home_logo">
        </div>
        <div>
            <h1 class="title">Arena Esportiva</h1><br>
        </div>
        <div>
            <a href="../BackEnd/loginUsuario.php"><img src="../imgs/enter.png" class="home_login-img"></a>
        </div>
    </div>
    <div class="home_container">
        <form name="formulario" method="post" action="home.php">
            <h1>Pesquisas</h1>

            <!------ pesquisar Categorias -------------->
            <label for="">Categorias: </label>
            <select name="categoria">
                <option value="" selected="selected">Selecione...</option>
                <?php
                $query = mysql_query("SELECT codigo, nome FROM categoria");
                while ($categorias = mysql_fetch_array($query)) { ?>
                    <option value="<?php echo $categorias['codigo']; ?>">
                        <?php echo $categorias['nome']; ?>
                    </option>
                <?php }
                ?>
            </select>

            <!------ pesquisar tipo -------------->
            <label for="">Tipo: </label>
            <select name="classificacao">
                <option value="" selected="selected">Selecione...</option>
                <?php
                $query = mysql_query("SELECT codigo, nome FROM tipo");
                while ($classificacao = mysql_fetch_array($query)) { ?>
                    <option value="<?php echo $classificacao['codigo']; ?>">
                        <?php echo $classificacao['nome']; ?>
                    </option>
                <?php }
                ?>
            </select>

            <!------ pesquisar marcas -------------->
            <label for="">Marcas: </label>
            <select name="marca">
                <option value="" selected="selected">Selecione...</option>
                <?php
                $query = mysql_query("SELECT codigo, nome FROM marca");
                while ($marcas = mysql_fetch_array($query)) { ?>
                    <option value="<?php echo $marcas['codigo']; ?>">
                        <?php echo $marcas['nome']; ?>
                    </option>
                <?php }
                ?>
            </select>

            <input type="submit" name="pesquisar" value="Pesquisar">
        </form>
        <br><br>
    </div>

    <?php
    if (!isset($_POST['pesquisar'])) {
        $sql_produtos = "SELECT descricao, cor, tamanho, preco, foto1 FROM produto ORDER BY codigo DESC LIMIT 8";
        $resultado = mysql_query($sql_produtos);

        if (mysql_num_rows($resultado) > 0) {
            echo "<div class='produtos-container'>";
            while ($dados = mysql_fetch_array($resultado)) {
                echo "<div class='produto-item'>";
                echo "<div>";
                echo "<img src='../imgs/imagensProdutos/" . htmlspecialchars($dados['foto1']) . "' alt='Imagem 1' class='imagem-produto' />";
                echo "</div>";
                echo "<div class='produto-info'>";
                echo "<p>Descrição: " . htmlspecialchars($dados['descricao']) . "</p>";
                echo "<p>Cor: " . htmlspecialchars($dados['cor']) . "</p>";
                echo "<p>Tamanho: " . htmlspecialchars($dados['tamanho']) . "</p>";
                echo "<p>Preço R$: " . number_format($dados['preco'], 2, ',', '.') . "</p>";
                echo "</div>";
                echo "</div>";
            }
            echo "</div>";
        } else {
            echo "<h1>Nenhum produto disponível.</h1>";
        }
    }
    ?>


    <?php
    if (isset($_POST['pesquisar'])) {
        // Pegando os filtros
        $marca         = (empty($_POST['marca'])) ? 'null' : $_POST['marca'];
        $categoria     = (empty($_POST['categoria'])) ? 'null' : $_POST['categoria'];
        $classificacao = (empty($_POST['tipo'])) ? 'null' : $_POST['tipo'];

        // Construindo a consulta de produtos com base nos filtros
        $sql_produtos = "SELECT produto.descricao, produto.cor, produto.tamanho, produto.preco, produto.foto1, produto.foto2
                         FROM produto, marca, categoria, tipo
                         WHERE produto.codmarca = marca.codigo
                         AND produto.codcategoria = categoria.codigo
                         AND produto.codtipo = tipo.codigo";

        // Adicionando filtros à consulta
        if ($marca != 'null') {
            $sql_produtos .= " AND marca.codigo = $marca";
        }

        if ($categoria != 'null') {
            $sql_produtos .= " AND categoria.codigo = $categoria";
        }

        if ($classificacao != 'null') {
            $sql_produtos .= " AND tipo.codigo = $classificacao";
        }

        // Executando a consulta
        $seleciona_produtos = mysql_query($sql_produtos);

        // Verificando se a consulta retornou resultados
        if (mysql_num_rows($seleciona_produtos) == 0) {
            echo '<h1>Desculpe, mas sua busca não retornou resultados.</h1>';
        } else {
            echo "<div class='produtos-container'>";
            while ($dados = mysql_fetch_object($seleciona_produtos)) {
                echo "<div class='produto-item'>";
                echo "<div>";
                echo "<img src='../imgs/imagensProdutos/" . htmlspecialchars($dados->foto1) . "' alt='Imagem 1' class='imagem-produto' />";
                echo "</div>"; // .imagens
                echo "<div class='produto-info'>";
                echo "<p>Descrição: " . htmlspecialchars($dados->descricao) . "</p>";
                echo "<p>Cor: " . htmlspecialchars($dados->cor) . "</p>";
                echo "<p>Tamanho: " . htmlspecialchars($dados->tamanho) . "</p>";
                echo "<p> Preço R$: " . number_format($dados->preco, 2, ',', '.') . "</p>";
                echo "</div>"; // .produto-info
                echo "</div>"; // .produto-item
            }
            echo "</div>"; // .produtos-container
        }
    }
    ?>
</body>

</HTML>