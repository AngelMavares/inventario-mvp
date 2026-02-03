import React, { useEffect, useState } from "react";
import { fetchJSON } from "../api";

export default function ProductList({ api }) {
  const [products, setProducts] = useState([]);
  const [q, setQ] = useState("");

  useEffect(() => {
    load();
  }, []);

  async function load() {
    const url = new URL(api + "/products");
    if (q) url.searchParams.set("q", q);
    const data = await fetchJSON(url.toString());
    setProducts(data);
  }

  return (
    <div className="mt-6">
      <div className="flex gap-2 mb-4">
        <input className="border p-2 flex-1" placeholder="Buscar..." value={q} onChange={(e)=>setQ(e.target.value)} />
        <button className="bg-sky-600 text-white px-4 rounded" onClick={load}>Buscar</button>
      </div>
      <table className="w-full border-collapse">
        <thead>
          <tr className="text-left border-b">
            <th>Nombre</th><th>SKU</th><th>Stock</th><th>Precio</th>
          </tr>
        </thead>
        <tbody>
          {products.map(p => (
            <tr key={p.id} className="border-b">
              <td className="py-2">{p.name}</td>
              <td>{p.sku}</td>
              <td>{p.stock}</td>
              <td>{p.price}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}