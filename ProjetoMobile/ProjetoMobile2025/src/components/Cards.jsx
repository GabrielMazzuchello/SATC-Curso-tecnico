import React from "react";
import { View, Image, Text, StyleSheet, TouchableOpacity } from "react-native";

const Cards = ({ nome, valor, imagem, comprar }) => {
  return (
    <View style={styles.card}>
      <Image style={styles.imagem} source={{ uri: imagem }} />
      <View>
        <Text style={styles.texts}>{nome}</Text>
        <Text style={styles.texts}>R$: {valor.toFixed(2)}</Text>
        <TouchableOpacity style={styles.button} onPress={comprar}>
          <Text style={styles.buttonText}>Comprar</Text>
        </TouchableOpacity>
      </View>
    </View>
  );
};
export default Cards;

const styles = StyleSheet.create({
  card: {
    width: "auto", // verificar
    height: "auto",
    padding: 10,
    margin: 10,
    backgroundColor: "#808080",
    borderRadius: 8,
    alignItems: "center",
    // justifyContent: "space-around",
    display: "Flex",
    flexDirection: "row",
  },
  imagem: {
    width: 100,
    height: 100,
    resizeMode: "contain",
    borderRadius: 5,
    pedding: 5,
  },
  texts: {
    pedding: 5,
    fontSize: 20,
    color: "#000",
  },
  button: {
    height: 40,
    width: 100,
    margin: 12,
    justifyContent: "center",
    alignItems: "center",
    backgroundColor: "#ff0000", // Cor de fundo do botão
    borderRadius: 5,
  },
  buttonText: {
    color: "#fff", // Cor do texto do botão
    fontSize: 16,
    fontWeight: "bold",
  },
});
