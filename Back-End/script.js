document.getElementById("search-form").addEventListener("submit", function(event) {
    event.preventDefault(); 

    const form = event.target;
    const pokemonName = form.elements["pokemon_name"].value;
    console.log("Procurando por:", pokemonName);

    const pokemonImage = document.getElementById("pokemon-image");
    const pokemonNameElement = document.getElementById("pokemon-name");
    const pokemonIdElement = document.getElementById("pokemon-id");
    const pokemonTypeElement = document.getElementById("pokemon-type");
    const pokemonDescriptionElement = document.getElementById("pokemon-description");

    pokemonImage.src = "https://images.lifestyleasia.com/wp-content/uploads/sites/2/2021/11/08151501/musa_acuminata_balbisiana25204635515wikimedia_creativecommons.jpeg?tr=w-1200,h-900";
    pokemonNameElement.textContent = "Bananiusn";
    pokemonIdElement.textContent = "1249";
    pokemonTypeElement.textContent = "Planta e Gelo";
    pokemonDescriptionElement.textContent = "Um pokemón caicho de banana ciano, que nasce em regiões frias e está disposto a ajudar treinadores que se perdem na neve a evitar morrer de fome.";

    fetch(`buscar.php?pokemon_name=${pokemonName}`)
                            .then(response=> response.json())
                            .then (data => {
                                //vai entrar aqui se der certo a comunicação
                                console.log(data)
                            })
                            .catch(error => {
                                console.error("Erro ao buscar Pokémon:", error);
                                //e aqui se der errado
                            });

});