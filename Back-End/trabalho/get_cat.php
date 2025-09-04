<?php
$url = "https://api.thecatapi.com/v1/images/search";

$response = file_get_contents($url);

header('Content-Type: application/json');
echo $response;
