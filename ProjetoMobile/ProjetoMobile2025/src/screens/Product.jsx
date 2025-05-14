import React, { useEffect, useState } from "react";
import { View, Text, StyleSheet, FlatList } from "react-native";
import Cards from "../components/Cards";
import { db } from "../services/firebase";
import { collection, getDocs } from "firebase/firestore";

export default function Product() {
  const [produtos, setProdutos] = useState([]);

  useEffect(() => {
    async function carregarProdutos() {
      try {
        const querySnapshot = await getDocs(collection(db, 'produtos'));
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

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Lista de Produtos</Text>
      <FlatList
        data={produtos}
        renderItem={({ item }) => (
          <Cards nome={item.nome} valor={item.valor} imagem={item.imagem} />
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
