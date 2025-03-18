import { StyleSheet, Text, View, TextInput, ImageBackground, TouchableOpacity } from "react-native";
import imagemFundo from "../../assets/elite-wallpaper.jpg";

export function Login() {
  return (
    <View style={styles.login}>
      <ImageBackground
        style={styles.backgroundImage}
        source={imagemFundo}
      >
        <View style={styles.formContainer}>
          <TextInput style={styles.input} placeholder="Digite seu e-mail aqui: " />
          <TextInput style={styles.input} placeholder="Digite sua senha aqui: " secureTextEntry />
          
          {/* Botão de Login */}
          <TouchableOpacity style={styles.button}>
            <Text style={styles.buttonText}>Login</Text>
          </TouchableOpacity>

          {/* Botão de Criar Conta */}
          <TouchableOpacity style={styles.button}>
            <Text style={styles.buttonText}>Criar uma conta</Text>
          </TouchableOpacity>
        </View>
      </ImageBackground>
    </View>
  );
}

const styles = StyleSheet.create({
  login: {
    flex: 1,
  },
  backgroundImage: {
    flex: 1,
    width: "100%",
    height: "100%",
    justifyContent: "center", // Ajuste para centralizar os elementos dentro da tela
    padding: 20, // Adicionando um pouco de espaçamento
  },
  formContainer: {
    backgroundColor: "rgba(0, 0, 0, 0.6)", // Fundo semi-transparente para os inputs
    padding: 20,
    borderRadius: 10,
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
