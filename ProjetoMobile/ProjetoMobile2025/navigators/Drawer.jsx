import "react-native-gesture-handler";
import { NavigationContainer } from "@react-navigation/native";
import { View } from "react-native";
import { createDrawerNavigator } from "@react-navigation/drawer";
import { Home } from "./src/screens/home";
import { Login } from "./src/screens/login";

export default function App() {
  const drawer = createDrawerNavigator();

  return (
    <NavigationContainer>
      <drawer.Navigator>
        <drawer.Screen name="Login" component={Login} />
        <drawer.Screen name="Home" component={Home} />
      </drawer.Navigator>
    </NavigationContainer>
  );
}
