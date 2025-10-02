import { useSalesData } from "./hooks/useSalesData";
import { cleanSales } from "./utils/cleanData";
import { totalSales, bestProduct, avgRating } from "./utils/metrics";
import { SalesChart } from "./components/SalesChart";
import { useFilters } from "./hooks/useFilters";
import { applyFilters } from "./utils/applyFilters";
import { FiltersComponent } from "./components/Filters";

import './App.css'

function App() {
  const rawSales = useSalesData();
  const sales = cleanSales(rawSales);

  const { filters, updateFilter } = useFilters();
  const filteredSales = applyFilters(sales, filters);

  const uniqueProducts = Array.from(
    new Set(sales.map((s) => s.product).filter(Boolean))
  ) as string[];

  return (
    <div className="p-6">
      <h1 className="text-2xl font-bold mb-4">Client Dashboard</h1>

      <div className="mb-4">
        <p>Total Ventas: ${totalSales(filteredSales)}</p>
        <p>Producto más vendido: {bestProduct(filteredSales)}</p>
        <p>Rating promedio: {filteredSales.length > 0 ? avgRating(filteredSales).toFixed(2) : "N/A"}</p>
      </div>

      <FiltersComponent
        filters={filters}
        updateFilter={updateFilter}
        products={uniqueProducts}
      />

      <SalesChart sales={filteredSales} />
    </div>
  );
}

export default App;
