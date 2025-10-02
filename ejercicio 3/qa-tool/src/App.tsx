import { useEffect, useState } from "react";
import type { Sale } from "./types/sales";
import { wrongRegisters, fixWrongRegisters } from "./utils/cleanData";
import './App.css'

function App() {
  const [sales, setSales] = useState<Sale[]>([]);       
  const [errors, setErrors] = useState<Sale[]>([]);     

  
  useEffect(() => {
    fetch("/sales_data.json")
      .then((res) => res.json())
      .then((data) => {
        setSales(data.sales);
        setErrors(wrongRegisters(data.sales));
      })
      .catch(console.error);
  }, []);

  // funcion para corregir los datos
  const handleFixAll = () => {
    const fixedErrors = fixWrongRegisters(errors);
    setErrors(fixedErrors);


    const updatedSales = sales.map((s) => {
      const corrected = fixedErrors.find((e) => e.id === s.id);
      return corrected ? corrected : s;
    });
    setSales(updatedSales);

    alert("Datos corregidos");
  };

  

  // funcion para enviar el json limpio al backend
  const handleSaveToDashboard = () => {
    fetch("http://localhost:4000/save-clean-to-dashboard", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ sales }), 
    })
      .then((res) => res.json())
      .then(() => {
        alert("Podés ver los datos actualizados en el Dashboard de cliente");
      })
      .catch(console.error);

  };


  return (
    <div className="p-4">
      <h1 className="text-xl font-bold mb-4">QA Tool - Registros con errores</h1>

      {errors.length > 0 ? (
        <table className="border-collapse border border-gray-400 w-full">
          <thead>
            <tr>
              <th className="border border-gray-400 p-2">ID</th>
              <th className="border border-gray-400 p-2">Fecha</th>
              <th className="border border-gray-400 p-2">Producto</th>
              <th className="border border-gray-400 p-2">Cantidad</th>
              <th className="border border-gray-400 p-2">Precio</th>
              <th className="border border-gray-400 p-2">Rating</th>
            </tr>
          </thead>
          <tbody>
            {errors.map((s) => (
              <tr key={s.id}>
                <td className="border border-gray-400 p-2">{s.id}</td>
                <td className="border border-gray-400 p-2">{s.date}</td>
                <td className="border border-gray-400 p-2">{s.product ?? "N/A"}</td>
                <td className="border border-gray-400 p-2">{s.quantity}</td>
                <td className="border border-gray-400 p-2">{s.price}</td>
                <td className="border border-gray-400 p-2">{s.rating}</td>
              </tr>
            ))}
          </tbody>
        </table>
      ) : (
        <p>No hay registros con errores 🎉</p>
      )}

      <div className="mb-4">
        <button className="button-datos mr-2" onClick={handleFixAll}>
          Corregir datos
        </button>
        <button className="button-datos mr-2" onClick={handleSaveToDashboard}>
          Exportar datos
        </button>
      </div>
    </div>
  );
}

export default App;
