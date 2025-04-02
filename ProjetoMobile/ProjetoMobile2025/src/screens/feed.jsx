import React from "react";
import {
  View,
  Text,
  Image,
  Button,
  StyleSheet,
  TouchableOpacity,
} from "react-native";

export default function Feed({ navigation }) {
  return (
    <View style={styles.container}>
      <Text style={styles.titles}>Feed do gabriel</Text>
      <Text style={styles.titles2}>Reflexões do Dia</Text>
      <Text style={styles.texts}>
        ​Em Elite Dangerous, a vastidão da galáxia é meticulosamente recriada em
        escala 1:1, abrangendo cerca de 400 bilhões de sistemas estelares. Essa
        imersão profunda transporta os jogadores para um universo onde a solidão
        e a vastidão do espaço são palpáveis, especialmente ao explorar regiões
        distantes do "Bubble" — a área centralmente povoada da galáxia.
      </Text>
      <Image source={{uri:"https://i.ytimg.com/vi/FDnjwfpM_Ac/maxresdefault.jpg"}} />
      <View style={styles.buttons}>
        <TouchableOpacity style={styles.button}>
          <Text style={styles.buttonText}>Saiba mais</Text>
        </TouchableOpacity>
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    display: "flex",
    padding: 20,
  },
  titles: {
    display: "flex",
    justifyContent: "center",
    fontSize: 40,
    alignItems: "center",
    fontWeight: "bold",
    color: "#000",
    marginBottom: 10,
  },
  titles2: {
    display: "flex",
    justifyContent: "center",
    fontSize: 20,
    alignItems: "center",
    fontWeight: "bold",
    color: "#000",
    marginBottom: 10,
  },
  texts: {
    display: "flex",
    justifyContent: "center",
    fontSize: 20,
    alignItems: "center",
    fontWeight: "bold",
    color: "#000",
    marginBottom: 10,
  },
  buttons: {
    display: "flex",
    flexDirection: "column",
    justifyContent: "center",
    alignItems: "center",
    marginBottom: 10,
    maxHeight: 1050,
    maxWidth: 1050,
  },
  button: {
    height: 40,
    margin: 12,
    justifyContent: "center",
    alignItems: "center",
    backgroundColor: "#ff0000", // Cor de fundo do botão
    borderRadius: 5,
  },
});
