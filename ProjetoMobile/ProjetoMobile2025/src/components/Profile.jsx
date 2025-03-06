import { registerWebModule } from "expo";
import { StyleSheet, Text, View, Image } from "react-native";

export function Profile() {
  return (
    <View style={styles.profile}>
      <Text>Este é o perfil!</Text>
      <View style={styles.imgs}>
        <Image style={styles.img} source={require("../../assets/elite.jpg")} />
        <Image style={styles.img} source={require("../../assets/elite.jpg")} />
      </View>

      <View></View>

      <View style={styles.imgs}>
        <Image style={styles.img} source={require("../../assets/elite.jpg")} />
        <Image style={styles.img} source={require("../../assets/elite.jpg")} />
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
  },

  imgs: {
    flexDirection: "row",
    justifyContent: "space-between",
  },

  img: {
    height: 175,
    width: 175,
  },
});
