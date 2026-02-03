import React, { useState } from "react";
import { fetchJSON } from "../api";

export default function ProductForm({ api, onDone }) {
  const [form, setForm] = useState({ name: "", sku: "", description: "", price: 0, stock: 0, category: "" });

  async function submit(e) {
    e.preventDefault();
    await fetchJSON(api + "/products", { method: "POST", body: JSON.stringify(form) });
    setForm({ name: "", sku: "", description: "", price: 0, stock: 0, category: "" });
    onDone();
  }

  return (
    <form onSubmit={submit} className="bg-white p-4 rounded shadow">
      <div className="grid grid-cols-2 gap-3">
        <input required placeholder="Nombre" value={form.name} onChange={e=>setForm({...form, name:e.target.value})} className="border p-2"/>
        <input placeholder="SKU" value={form.sku} onChange={e=>setForm({...form, sku:e.target.value})} className="border p-2"/>
        <input type="number" placeholder="Precio" value={form.price} onChange={e=>setForm({...form, price: parseFloat(e.target.value)})} className="border p-2"/>
        <input type="number" placeholder="Stock" value={form.stock} onChange={e=>setForm({...form, stock: parseInt(e.target.value)})} className="border p-2"/>
        <input placeholder="Categoría" value={form.category} onChange={e=>setForm({...form, category:e.target.value})} className="border p-2 col-span-2"/>
        <textarea placeholder="Descripción" value={form.description} onChange={e=>setForm({...form, description:e.target.value})} className="border p-2 col-span-2"/>
      </div>
      <div className="mt-3">
        <button className="bg-green-600 text-white px-4 py-2 rounded">Agregar</button>
      </div>
    </form>
  );
}