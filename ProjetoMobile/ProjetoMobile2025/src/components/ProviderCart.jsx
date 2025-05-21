import React, { createContext, useContext, useState } from "react";

// Criando o contexto
const CartContext = createContext();

// Criando o componente provedor
export function ProviderCart({ children }) {
  const [cart, setCart] = useState([]);

  function addProducts(product) {
    setCart((prevCart) => [...prevCart, product]);
  }

  return (
    <CartContext.Provider value={{ cart, addProducts }}>
      {children}
    </CartContext.Provider>
  );
}

// Hook para acessar o contexto
export function useCart() {
  return useContext(CartContext);
}
