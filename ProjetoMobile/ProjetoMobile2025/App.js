import "react-native-gesture-handler";
import { NavigationContainer } from "@react-navigation/native";
import { View } from "react-native";
import { createStackNavigator } from "@react-navigation/stack";
import { Home } from "./src/screens/home";
import { Login } from "./src/screens/login";



export default function App() {
  const Stack = createStackNavigator();

  return (
    <NavigationContainer>
      <Stack.Navigator>
        <Stack.Screen name="Login" component={Login} />
        <Stack.Screen name="Home" component={Home} />
      </Stack.Navigator>
    </NavigationContainer>
  );
}
