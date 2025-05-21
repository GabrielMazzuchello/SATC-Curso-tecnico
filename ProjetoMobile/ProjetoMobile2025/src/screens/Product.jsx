import React, { useEffect, useState } from "react";
import { View, Text, StyleSheet, FlatList } from "react-native";
import Cards from "../components/Cards";
import { db } from "../services/firebase";
import { collection, getDocs } from "firebase/firestore";
import { useCart } from "../components/ProviderCart";

export default function Product({ navigation }) {
  const [produtos, setProdutos] = useState([]);
  const { addProducts } = useCart();

  useEffect(() => {
    async function carregarProdutos() {
      try {
        const querySnapshot = await getDocs(collection(db, "produtos"));
        const lista = [];
        querySnapshot.forEach((doc) => {
          lista.push({ id: doc.id, ...doc.data() });
        });
        setProdutos(lista);
      } catch (error) {
        console.log("Erro ao carregar produtos:", error);
      }
    }

    carregarProdutos();
  }, []);

  // função que será passada para cada Card
  const comprar = (produto) => {
    addProducts(produto);
  };

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Lista de Produtos</Text>
      <FlatList
        data={produtos}
        renderItem={({ item }) => (
          <Cards
            nome={item.nome}
            valor={item.valor}
            imagem={item.imagem}
            comprar={() => comprar(item)}
          />
        )}
        keyExtractor={(item) => item.id}
      />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: "center",
    alignItems: "center",
  },
  title: {
    fontSize: 40,
  },
});
