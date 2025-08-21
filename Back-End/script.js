document
  .getElementById("search-form")
  .addEventListener("submit", function (event) {
    event.preventDefault();

    const form = event.target;
    const pokemonName = form.elements["pokemon_name"].value;
    console.log("Procurando por:", pokemonName);

    const pokemonImage = document.getElementById("pokemon-image");
    const pokemonNameElement = document.getElementById("pokemon-name");
    const pokemonIdElement = document.getElementById("pokemon-id");
    const pokemonTypeElement = document.getElementById("pokemon-type");
    const pokemonDescriptionElement = document.getElementById(
      "pokemon-description"
    );

    fetch(`buscar.php?pokemon_name=${pokemonName}`)
      .then((response) => response.json())
      .then((data) => {
        //vai entrar aqui se der certo a comunicação
        console.log(data);

        pokemonImage.src = data.image;
        pokemonNameElement.textContent = data.name;
        pokemonIdElement.textContent = data.id;
        pokemonTypeElement.textContent = data.type;
        pokemonDescriptionElement.textContent = data.description;
      })
      .catch((error) => {
        console.error("Erro ao buscar Pokémon:", error);
        //e aqui se der errado
      });
  });
