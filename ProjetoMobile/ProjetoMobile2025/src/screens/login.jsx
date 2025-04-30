import {
  StyleSheet,
  Text,
  View,
  TextInput,
  ImageBackground,
  TouchableOpacity,
} from "react-native";
import imagemFundo from "../../assets/elite-wallpaper.jpg";
import { signInWithEmailAndPassword } from "firebase/auth";
import { auth } from "../services/firebase";
import React, { useState } from "react";

export default function Login({ navigation }) {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const handleLogin = async () => {
    if (!email || !password) {
      window.alert("Erro: Preencha todos os campos!"); // Usando window.alert() para exibir alerta no navegador
      return;
    }

    try {
      await signInWithEmailAndPassword(auth, email, password);
      window.alert("Login feito com sucesso!"); // Usando window.alert() no sucesso
      navigation.navigate("HomeTabs");
    } catch (error) {
      window.alert("Erro no login: " + error.message); // Exibe o erro no alert
    }
  };

  return (
    <View style={styles.login}>
      <ImageBackground style={styles.backgroundImage} source={imagemFundo}>
        <View style={styles.container}>
          <View style={styles.formContainer}>
            <TextInput
              style={styles.input}
              placeholder="Digite seu e-mail aqui: "
              value={email}
              onChangeText={setEmail}
            />
            <TextInput
              style={styles.input}
              placeholder="Digite sua senha aqui: "
              secureTextEntry
              value={password}
              onChangeText={setPassword}
            />

            {/* Botão de Login */}
            <TouchableOpacity style={styles.button} onPress={handleLogin}>
              <Text style={styles.buttonText}>Login</Text>
            </TouchableOpacity>

            {/* Botão de Criar Conta */}
            <TouchableOpacity
              style={styles.button}
              onPress={() => navigation.navigate("Cadastro")}
            >
              <Text style={styles.buttonText}>Criar uma conta</Text>
            </TouchableOpacity>
          </View>
        </View>
      </ImageBackground>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    display: "flex",
    alignItems: "center",
    Height: 550,
    Width: 550,
  },

  login: {
    flex: 1,
    display: "flex",
    flexDirection: "column",
    justifyContent: "center",
    alignItems: "center",
  },
  backgroundImage: {
    flex: 1,
    width: "100%",
    height: "100%",
    justifyContent: "center",
    padding: 20,
  },
  formContainer: {
    backgroundColor: "rgba(0, 0, 0, 0.6)",
    padding: 20,
    borderRadius: 10,
    maxHeight: 550,
    maxWidth: 550,
  },
  input: {
    height: 40,
    margin: 12,
    borderWidth: 1,
    borderColor: "#fff", // Para que os inputs se destaquem na tela
    padding: 10,
    color: "#fff", // Cor do texto dentro dos inputs
    borderRadius: 5,
  },
  button: {
    height: 40,
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