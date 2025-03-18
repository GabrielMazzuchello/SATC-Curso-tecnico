import { StyleSheet, Text, View, Image } from "react-native";

export function Profile() {
  return (
    <View style={styles.profile}>
      <Text>Este é o perfil!</Text>
      <View style={styles.imgs}>
        <Image style={styles.img} source={require("../../assets/elite.jpg")} />
        <Image style={styles.img} source={require("../../assets/elite.jpg")} />
      </View>

      <View style={styles.textRight}>
        <Text>Texto à direita</Text>
      </View>

      <View style={styles.imgs}>
        <Image style={styles.img} source={require("../../assets/elite.jpg")} />
        <Image style={styles.img} source={require("../../assets/elite.jpg")} />
      </View>
      <View style={styles.textCenter}>
        <Text>Texto centralizado</Text>
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "#20CFFF",
  },
  profile: {
    gap: 10,
    flexDirection: "column",
    flex: 1,
    backgroundColor: "#F99",
    padding: 10,  // Adicionei padding para dar um pouco de espaço nas bordas
  },
  imgs: {
    flexDirection: "row",
    justifyContent: "space-between",
  },
  img: {
    height: 175,
    width: 175,
  },
  textRight: {
    alignItems: "flex-end", // Alinha o texto à direita
  },
  textCenter: {
    alignItems: "center", // Centraliza o texto
    justifyContent: "center", // Centraliza verticalmente
  }
});
