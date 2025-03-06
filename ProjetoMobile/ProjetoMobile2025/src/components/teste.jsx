import { registerWebModule } from "expo";
import { StyleSheet, Text, View, Image } from "react-native";

export default function Gallery() {
  return (
    <View style={styles.container}>
      <Text>Esta é a galeria!</Text>
    </View>
  );
}

export function Favorites() {
  return (
    <View style={styles.favorites}>
      <Text>Este é o favoritos!</Text>
      <Image style={styles.img} source={require("../../assets/elite.jpg")} />
    </View>
  );
}

export function Profile() {
  return (
    <View style={styles.profile}>
      <Text>Este é o perfil!</Text>
      <View></View>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    alignItems: "center",
    justifyContent: "center",
    backgroundColor: "#20CFFF",
  },
  profile: {
    flexDirection: "row",
    justifyContent: "center",
    alignItems: "center",
    flex: 3,
    backgroundColor: "#F99",
  },
  favorites: {
    justifyContent: "center",
    alignItems: "center",
    flex: 1,
    backgroundColor: "#4E4",
  },
  img: {
    height: 175,
    width: 175,
  },
});
