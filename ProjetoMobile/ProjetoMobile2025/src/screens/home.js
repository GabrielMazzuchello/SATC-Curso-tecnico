import { StyleSheet, Text, View, Image } from "react-native";

export function Home() {
  return (
    <View style={styles.profile}>
      <Text>Este é a home!</Text>
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
    padding: 10,
  },
  imgs: {
    flexDirection: "row",
    justifyContent: "space-evenly",
  },
  img: {
    height: 175,
    width: 175,
  },
  textRight: {
    alignItems: "flex-end",
  },
  textCenter: {
    alignItems: "center", // Centraliza verticalmente
  },
});
