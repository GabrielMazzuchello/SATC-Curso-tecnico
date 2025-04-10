import React, { useState } from "react";
import {
  View,
  Text,
  StyleSheet,
  TouchableOpacity,
  TextInput,
} from "react-native";

export default function Counter() {
  const [count, setCount] = useState(0);
  const [nome, setNome] = useState("");
  const [email, setEmail] = useState("");

  const Aumentar = () => {
    setCount(count + 1);
  };

  const Diminuir = () => {
    if (count > 0) {
      setCount(count - 1);
    }
  };

  return (
    <View style={styles.container}>
      <View>
        <Text style={styles.titles}>Contador de Passos: {count}</Text>
      </View>
      <View style={styles.buttons}>
        <TouchableOpacity onPress={Aumentar} style={styles.button}>
          <Text style={styles.buttonText}>+</Text>
        </TouchableOpacity>
        <TouchableOpacity onPress={Diminuir} style={styles.button}>
          <Text style={styles.buttonText}>-</Text>
        </TouchableOpacity>
      </View>
      <View style={styles.inputs}>
        <TextInput
          style={styles.input}
          value={nome}
          onChangeText={setNome}
          placeholder="Nome: "
        />
        <TextInput
          style={styles.input}
          value={email}
          onChangeText={setEmail}
          placeholder="Email: "
        />
      </View>
      <Text>Oi, {nome}, seu email é {email}</Text>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    display: "flex",
    alignItems: "center",
    flexDirection: "column",
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
    width: "20%",
    flexDirection: "row",
    justifyContent: "center",
  },
  button: {
    height: 40,
    width: 40,
    margin: 12,
    justifyContent: "center",
    alignItems: "center",
    backgroundColor: "#ff0000", // Cor de fundo do botão
    borderRadius: 5,
  },
  inputs: {
    height: "60%",
    justifyContent: "space-evenly",
  },
  input: {
    height: 30,
    borderWidth: 1,
    justifyContent: "space-evenly",
    borderColor: "#fff", // Para que os inputs se destaquem na tela
    color: "#000", // Cor do texto dentro dos inputs
    borderRadius: 10,
    borderColor: "#000",
  },
});
