import { View } from "react-native";
import Gallery, { Profile, Favorites } from "./src/components/Profile";
import { StyleSheet } from "react-native";
import { Teste } from "./src/components/teste";

export default function App() {
  return (
    <View style={styles.container}>
      <Profile />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
  },
});
