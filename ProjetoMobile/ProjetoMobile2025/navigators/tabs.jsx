import "react-native-gesture-handler";
import { NavigationContainer } from "@react-navigation/native";
import { View } from "react-native";
import { createBottomTabNavigator } from "@react-navigation/bottom-tabs";
import { Home } from "./src/screens/home";
import { Login } from "./src/screens/login";

export default function App() {
  const Tabs = createBottomTabNavigator();

  return (
    <NavigationContainer>
      <Tabs.Navigator>
        <Tabs.Screen name="Login" component={Login} />
        <Tabs.Screen name="Home" component={Home} />
      </Tabs.Navigator>
    </NavigationContainer>
  );
}
