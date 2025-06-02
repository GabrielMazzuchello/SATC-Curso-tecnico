<!DOCTYPE html>
<html lang="pt-BR">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Home - Livraria</title>
    <link rel="stylesheet" href="/assets/css/style.css">
</head>

<body>
    <div class="home__pesquisas">
        <form class="home__pesquisas-form" action="" method="GET">
            <h1>Filtros</h1>

            <div>
                <label for="autor">Autor</label>
                <select name="autor" id="autor">
                    <option value="">Selecione...</option>
                    <?php $tipo = 'autor';
                    include 'includes/listaOpcoes.php'; ?>
                </select>

            </div>

            <div>
                <label for="categoria">Categoria</label>
                <select name="categoria" id="categoria">
                    <option value="">Selecione...</option>
                    <?php $tipo = 'categoria';
                    include 'includes/listaOpcoes.php'; ?>
                </select>
            </div>

            <div>
                <label for="editora">Editora</label>
                <select name="editora" id="editora">
                    <option value="">Selecione...</option>
                    <?php $tipo = 'editora';
                    include 'includes/listaOpcoes.php'; ?>
                </select>
            </div>

            <button type="submit">Buscar</button>
        </form>
    </div>
</body>

</html>