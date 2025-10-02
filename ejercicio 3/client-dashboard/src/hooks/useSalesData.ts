import { useEffect, useState } from "react";
import type { Sale } from "../types/sales";

export const useSalesData = () => {
  const [sales, setSales] = useState<Sale[]>([]);

  useEffect(() => {
    fetch("http://localhost:4000/sales-data")
      .then((res) => res.json())
      .then((data) => setSales(data.sales))
      .catch((err) => console.error("Error cargando datos:", err));
  }, []);

  return sales;
};
