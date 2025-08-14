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
        $response = json_decode($apiResponse, true);
    }
}
echo json_encode($response);
