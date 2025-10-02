import { useEffect, useState } from "react";
import type { Sale } from "../types/sales";

export const useSalesData = () => {
  const [sales, setSales] = useState<Sale[]>([]);

  useEffect(() => {
    fetch("/sales_data.json")
      .then((res) => res.json())
      .then((data) => setSales(data.sales))
      .catch((err) => console.error("Error cargando datos:", err));
  }, []);

  return sales;
};
