import { View } from "react-native";
// Only import react-native-gesture-handler on native platforms
import 'react-native-gesture-handler';
import Gallery, { Profile, Favorites } from "./src/components/Profile";
import { StyleSheet } from "react-native";
import { Teste } from "./src/components/teste";
import { Login } from "./src/screens/login";
import { Home } from "./src/screens/home";

export default function App() {
  return (
    <View style={styles.container}>
      <Home />
      {/* <Login /> */}
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
  },
});
