import React from "react";
import { View, Text, StyleSheet, FlatList, Image } from "react-native";
import { useCart } from "../components/ProviderCart";

export default function Cart() {
  const { cart } = useCart();

  const total = cart.reduce((sum, item) => sum + Number(item.valor), 0);

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Carrinho de Compras</Text>

      {cart.length === 0 ? (
        <Text style={styles.empty}>Seu carrinho está vazio</Text>
      ) : (
        <>
          <FlatList
            data={cart}
            keyExtractor={(item, index) => index.toString()}
            renderItem={({ item }) => (
              <View style={styles.item}>
                <Image source={{ uri: item.imagem }} style={styles.imagem} />
                <View style={styles.info}>
                  <Text style={styles.nome}>{item.nome}</Text>
                  <Text style={styles.valor}>R$ {item.valor}</Text>
                </View>
              </View>
            )}
          />
          <Text style={styles.total}>Total: R$ {total.toFixed(2)}</Text>
        </>
      )}
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    padding: 20,
    backgroundColor: "#dddd",
  },
  title: {
    fontSize: 28,
    fontWeight: "bold",
    marginBottom: 20,
    textAlign: "center",
  },
  empty: {
    fontSize: 18,
    textAlign: "center",
    marginTop: 50,
  },
  item: {
    flexDirection: "row",
    justifyContent: "space-between",
    paddingVertical: 10,
    borderBottomWidth: 1,
    borderBottomColor: "#ccc",
  },
  nome: {
    fontSize: 18,
  },
  valor: {
    fontSize: 18,
    fontWeight: "bold",
  },
  total: {
    marginTop: 20,
    fontSize: 22,
    fontWeight: "bold",
    textAlign: "center",
  },
  imagem: {
    width: 60,
    height: 60,
    borderRadius: 10,
    marginRight: 10,
  },
  info: {
    flex: 1,
    justifyContent: "center",
  },
});
