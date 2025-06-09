<!DOCTYPE html>
<html lang="pt-BR">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Home - Livraria</title>
    <link rel="stylesheet" href="/assets/css/style.css">
</head>

<body>
    <div class="home__nav">
        <div>
            <a href="/pages/login.php"><img class="home__nav-img btn-brilho" src="/assets/img/versoEprosa.png" alt="Imagem do login"></a>
        </div>
        <div>
            <h1>Verso & Prosa</h1>
        </div>
        <div class="home__login-container">
            <a href="../index.php" class="btn btn-white btn-animate btn-brilho">Carrinho</a>
        </div>
    </div>
    <div class="home__pesquisas">
        <form class="home__pesquisas-form custom-select" action="" method="GET">

            <?php include 'includes/listaOpcoes.php'; ?>

            <!-- Autor -->

            <label for="autor">Autor:</label>
            <select name="autor" id="autor">
                <option value="">Selecione...</option>
                <?php listarOpcoes('autor'); ?>
            </select>


            <!-- Categoria -->

            <label for="categoria">Categoria:</label>
            <select name="categoria" id="categoria">
                <option value="">Selecione...</option>
                <?php listarOpcoes('categoria'); ?>
            </select>


            <!-- Editora -->

            <label for="editora">Editora:</label>
            <select name="editora" id="editora">
                <option value="">Selecione...</option>
                <?php listarOpcoes('editora'); ?>
            </select>

            <button class="btn" type="submit">Buscar</button>
        </form>
    </div>
    <div class="home__banners btn-brilho">
        <img src="/assets/img/banner2.jpg" id="banner-image" alt="Banner 1">
    </div>
    <div class="home__products btn-brilho">
        <?php include 'exibirLivros.php'; ?>
    </div>
</body>
<script>
    const banners = [
        "/assets/img/banner1.png",
        "/assets/img/banner2.jpg"
    ];
    let current = 0;
    const bannerImg = document.getElementById("banner-image");

    setInterval(() => {
        current = (current + 1) % banners.length;
        bannerImg.src = banners[current];
    }, 5000); // Troca a cada 5 segundos
</script>

</html>