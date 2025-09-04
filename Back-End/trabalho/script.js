document.getElementById("buscar").addEventListener("click", () => {
  fetch("get_cat.php")
    .then(response => response.json())
    .then(data => {
      const resultado = document.getElementById("resultado");
      resultado.innerHTML = ""; 
      const img = document.createElement("img");
      img.src = data[0].url; 
      resultado.appendChild(img);
    })
    .catch(err => console.error("Erro:", err));
});
