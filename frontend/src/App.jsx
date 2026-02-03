import React, { useEffect, useState } from "react";
import ProductList from "./components/ProductList";
import ProductForm from "./components/ProductForm";

const API = import.meta.env.VITE_API_URL || "http://localhost:8000";

export default function App() {
  const [refresh, setRefresh] = useState(0);
  return (
    <div className="p-6 max-w-4xl mx-auto">
      <h1 className="text-2xl font-bold mb-4">Inventario — MVP</h1>
      <ProductForm api={API} onDone={() => setRefresh(r => r + 1)} />
      <ProductList api={API} key={refresh} />
    </div>
  );
}