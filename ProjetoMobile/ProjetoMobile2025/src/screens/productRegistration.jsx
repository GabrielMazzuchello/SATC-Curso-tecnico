import { addDoc, collection } from "firebase/firestore";
import React, { useState } from "react";
import { db } from "../services/firebase";
import {
  Alert,
  StyleSheet,
  TextInput,
  TouchableOpacity,
  View,
  Text,
} from "react-native";

const ProductRegistration = () => {
  const [imagem, setImagem] = useState("");
  const [nome, setNome] = useState("");
  const [valor, setValor] = useState("");

  const cadastraProduto = async () => {
    if (!imagem || !valor || !nome) {
      Alert.alert("Erro", "Preencha todos os campos");
      return;
    }
    
    try {
      await addDoc(collection(db, "produtos"), {
        imagem,
        nome,
        valor: parseFloat(valor),
      });

      Alert.alert("Sucesso", "Produto cadastrado com sucesso!");

      setImagem("");
      setNome("");
      setValor("");
    } catch (error) {
      console.error("Erro ao cadastrar produto:", error);
      Alert.alert("Erro", "Não foi possível cadastrar o produto.");
    }
  };

  return (
    <View style={styles.container}>
      <TextInput
        style={styles.input}
        value={imagem}
        onChangeText={setImagem}
        placeholder="Imagem link"
      />
      <TextInput
        style={styles.input}
        value={nome}
        onChangeText={setNome}
        placeholder="Nome"
      />
      <TextInput
        style={styles.input}
        value={valor}
        onChangeText={setValor}
        placeholder="Valor"
        keyboardType="numeric"
      />

      <TouchableOpacity style={styles.button} onPress={cadastraProduto}>
        <Text style={styles.buttonText}>Cadastrar Produto</Text>
      </TouchableOpacity>
    </View>
  );
};

export default ProductRegistration;

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "#fff",
    justifyContent: "center",
    paddingHorizontal: 30,
  },
  input: {
    borderWidth: 1,
    borderColor: "#ccc",
    backgroundColor: "#f9f9f9",
    borderRadius: 5,
    padding: 12,
    marginBottom: 15,
  },
  button: {
    backgroundColor: "#a11",
    paddingVertical: 12,
    borderRadius: 5,
    marginBottom: 15,
  },
  buttonText: {
    color: "#fff",
    textAlign: "center",
    fontWeight: "bold",
    fontSize: 16,
  },
});
