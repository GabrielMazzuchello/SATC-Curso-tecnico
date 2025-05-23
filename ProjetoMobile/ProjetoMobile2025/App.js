import "react-native-gesture-handler";
import { NavigationContainer } from "@react-navigation/native";
import { createBottomTabNavigator } from "@react-navigation/bottom-tabs";
import { createStackNavigator } from "@react-navigation/stack";
import Home from "./src/screens/home";
import Login from "./src/screens/login";
import Feed from "./src/screens/feed";
import Counter from "./src/screens/counter";
import Product from "./src/screens/Product";
import register from "./src/screens/register";
import productRegistration from "./src/screens/productRegistration";
import MaterialCommunityIcons from "@expo/vector-icons/MaterialCommunityIcons";
import FontAwesome from "@expo/vector-icons/FontAwesome";
import { ProviderCart } from "./src/components/ProviderCart";
import cart from "./src/screens/cart";

function HomeTabs() {
  const Tabs = createBottomTabNavigator();
  return (
    <Tabs.Navigator
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
          borderTopWidth: 0, // Remove a borda superior
          borderBottomWidth: 0, // Remove a borda inferior
          elevation: 0, // Remove qualquer sombra (Android)
          shadowOpacity: 0, // Remove sombra (iOS)
        },
      }}
    >
      <Tabs.Screen
        name="Home"
        component={Home}
        options={{
          tabBarIcon: () => (
            <MaterialCommunityIcons name="home" size={24} color="white" />
          ),
        }}
      />
      <Tabs.Screen
        name="Feed"
        component={Feed}
        options={{
          tabBarIcon: () => <FontAwesome name="feed" size={24} color="white" />,
        }}
      />

      <Tabs.Screen
        name="Counter"
        component={Counter}
        options={{
          tabBarIcon: () => (
            <MaterialCommunityIcons name="counter" size={24} color="white" />
          ),
        }}
      />

      <Tabs.Screen
        name="Cadastro Produtos"
        component={productRegistration}
        options={{
          tabBarIcon: () => (
            <MaterialCommunityIcons name="counter" size={24} color="white" />
          ),
        }}
      />

      <Tabs.Screen
        name="Products"
        component={Product}
        options={{
          tabBarIcon: () => (
            <MaterialCommunityIcons
              name="shopping-search"
              size={24}
              color="white"
            />
          ),
        }}
      />

      <Tabs.Screen
        name="Carrinho"
        component={cart}
        options={{
          tabBarIcon: () => (
            <MaterialCommunityIcons name="counter" size={24} color="white" />
          ),
        }}
      />
    </Tabs.Navigator>
  );
}

export default function App() {
  const Stack = createStackNavigator();

  return (
    <ProviderCart>
      <NavigationContainer>
        <Stack.Navigator>
          <Stack.Screen name="Login" component={Login} />
          <Stack.Screen
            options={{ headerShown: false }}
            name="HomeTabs"
            component={HomeTabs}
          />
          <Stack.Screen name="Cadastro" component={register} />
        </Stack.Navigator>
      </NavigationContainer>
    </ProviderCart>
  );
}
