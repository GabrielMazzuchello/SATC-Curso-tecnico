<?php
header("content-type: application/json;");
header("access-control-allow-Origin: *");
header("access-control-allow-Methods: *");
header("access-control-allow-Headers: *");

$response = array(
    "success" => false,
    "name" => "Pokémon não encontrado",
    "id" => "",
    "type" => "",
    "description" => "",
    "image" => "https://images.lifestyleasia.com/wp-content/uploads/sites/2/2021/11/08151501/musa_acuminata_balbisiana25204635515wikimedia_creativecommons.jpeg?tr=w-1200,h-900"
);

if (!empty($_GET["pokemon_name"])) {
    $searchName = strtolower($_GET["pokemon_name"]);

    $url = "https://pokeapi.co/api/v2/pokemon/" . $searchName;

    $ch = curl_init();
    curl_setopt($ch, CURLOPT_URL, $url);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);
    curl_setopt($ch, CURLOPT_SSL_VERIFYHOST, true);
    $apiResponse = curl_exec($ch);
    $httpcode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
    curl_close($ch);

    if ($httpcode == 200) {
        $pokemonData = json_decode($apiResponse, true);

        $pokemonName = ucfirst($pokemonData['name']);
        $pokemonId = $pokemonData['id'];
        $pokemonTypes = ucfirst($pokemonData['types'][0]['type']['name']);
        $pokemonImage = $pokemonData['sprites']["other"]['official-artwork']['front_default'];

        $descriptionUrl = $pokemonData['species']['url'];
        $ch = curl_init();
        curl_setopt($ch, CURLOPT_URL, $descriptionUrl);
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
        curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);
        curl_setopt($ch, CURLOPT_SSL_VERIFYHOST, true);
        $speciesResponse = curl_exec($ch);
        curl_close($ch);

        $descriptionData = json_decode($speciesResponse, true);
        $description = "Descrição não encontrada";

        foreach ($descriptionData['flavor_text_entries'] as $entry) {
            if ($entry['language']['name'] === 'en') {
                $description = $entry['flavor_text'];
                break;
            }
        }

        $response = array(
            "success" => true,
            "name" => $pokemonName,
            "id" => $pokemonId,
            "type" => $pokemonTypes,
            "description" => $description,
            "image" => $pokemonImage
        );
    }
}
echo json_encode($response);
