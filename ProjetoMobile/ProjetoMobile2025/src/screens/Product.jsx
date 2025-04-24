import React, { useState } from "react";
import { View, Text, StyleSheet, FlatList } from "react-native";
import Cards from "../components/Cards";

export default function Product() {
  const [Produtos, setProdutos] = useState([
    {
      id: 1,
      nome: "Camiseta",
      valor: 59.99,
      imagem:
        "https://loja.comerciomix.com.br/media/catalog/product/cache/fb4f878514d02efd710032ded901d118/c/a/camiseta-azul-royal-para-sublima_o-tradicional_1.jpg",
    },
    {
      id: 2,
      nome: "Moletom",
      valor: 119.99,
      imagem:
        "https://cdn.shoppub.io/cdn-cgi/image/w=1000,h=1000,q=80,f=auto/rockfit/media/uploads/produtos/foto/rtcdsjwr/moletom-unissex-cinza.jpg",
    },
    {
      id: 3,
      nome: "Calça",
      valor: 199.99,
      imagem:
        "https://images.tcdn.com.br/img/img_prod/769687/calca_jeans_masculina_mais_comprida_longa_premium_jamer_2649_1_d32393952c59a63e5a115ae22d492fd0.jpg",
    },
    {
      id: 4,
      nome: "Tenis",
      valor: 250.99,
      imagem:
        "https://imgcentauro-a.akamaihd.net/800x800/98840051A9.jpg",
    },
  ]);
  
  return (
    <View style={styles.container}>
      <Text style={styles.title}>Lista de Produtos</Text>
      <FlatList
        data={Produtos}
        renderItem={({ item }) => (
          <Cards
            nome={item.nome}
            valor={item.valor}
            imagem={item.imagem}
          />
        )}
        keyExtractor={(item) => item.id.toString()}
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
