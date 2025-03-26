import "react-native-gesture-handler";
import { NavigationContainer } from "@react-navigation/native";
import { View } from "react-native";
import { createBottomTabNavigator } from "@react-navigation/bottom-tabs";
import { Home } from "./src/screens/home";
import { Login } from "./src/screens/login";
import MaterialCommunityIcons from "@expo/vector-icons/MaterialCommunityIcons";

export default function App() {
  const Tabs = createBottomTabNavigator();

  return (
    <NavigationContainer>
      <Tabs.Navigator
        initialRouteName="Login"
        screenOptions={{
          tabBarActiveBackgroundColor: "#000",
          tabBarActiveTintColor: "#a11",
          tabBarInactiveTintColor: "#ffff",
          tabBarInactiveBackgroundColor: "#0005",
          headerShown: false,
          headerStyle: { backgroundColor: "#a11" },
          headerTitleAlign: "center",
          tabBarBadge: 6,
          tabBarStyle: {
            backgroundColor: "red", // Cor de fundo da barra de abas
            // borderTopWidth: 0, // Remove a borda superior
            // borderBottomWidth: 0, // Remove a borda inferior
            // elevation: 0, // Remove qualquer sombra (Android)
            // shadowOpacity: 0, // Remove sombra (iOS)
          },
          // tabBarLabelPosition: "below-icon", coloca o texto abaixo do icone
        }}
      >
        <Tabs.Screen
          name="Login"
          component={Login}
          options={{
            tabBarIcon: () => (
              <MaterialCommunityIcons name="login" size={24} color="white" />
            ),
          }}
        />
        <Tabs.Screen
          name="Home"
          component={Home}
          options={{
            tabBarIcon: () => (
              <MaterialCommunityIcons name="home" size={24} color="white" />
            ),
          }}
        />
      </Tabs.Navigator>
    </NavigationContainer>
  );
}
