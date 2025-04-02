import { StyleSheet, Text, View, Image, ImageBackground } from "react-native";
import imagemFundo from "../../assets/elite-wallpaper.jpg";

export default function Home() {
  return (
    <ImageBackground style={styles.backgroundImage} source={imagemFundo}>
      <View style={styles.home}>
        <View style={styles.title}>
          <Text style={styles.texts}>Elite Dangerous</Text>
        </View>
        <View style={styles.imgs}>
          <Image
            style={styles.img}
            source={require("../../assets/elite.jpg")}
          />
          <Image
            style={styles.img}
            source={require("../../assets/elite2.jpg")}
          />
        </View>

        <View style={styles.textRight}>
          <Text style={styles.texts}>Baixar jogo</Text>
        </View>

        <View style={styles.imgs}>
          <Image
            style={styles.img}
            source={require("../../assets/elite3.png")}
          />
          <Image
            style={styles.img}
            source={require("../../assets/elite4.jpg")}
          />
        </View>
      </View>
    </ImageBackground>
  );
}

const styles = StyleSheet.create({
  backgroundImage: {
    flex: 1,
    width: "100%",
    height: "100%",
    justifyContent: "center",
    padding: 20,
  },

  home: {
    gap: 10,
    padding: 10,
    flexDirection: "column",
    alignItems: "stretch",
    justifyContent: "space-evenly",
    flex: 1,
    padding: 10,
    opacity: 1,
  },

  title: {
    display: "flex",
    alignItems: "center",
  },

  texts: { color: "#fff" },

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
});
