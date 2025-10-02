import type { Filters } from "../hooks/useFilters";


interface Props {
  filters: Filters;
  updateFilter: (field: keyof Filters, value: string) => void;
  products: string[];
}

export const FiltersComponent = ({ filters, updateFilter, products }: Props) => {
  return (
    <div className="flex gap-4 mb-6">
      <div>
        <label className="block text-sm">Desde:</label>
        <input
          type="date"
          value={filters.startDate}
          onChange={(e) => updateFilter("startDate", e.target.value)}
          className="border px-2 py-1 rounded"
        />
      </div>

      <div>
        <label className="block text-sm">Hasta:</label>
        <input
          type="date"
          value={filters.endDate}
          onChange={(e) => updateFilter("endDate", e.target.value)}
          className="border px-2 py-1 rounded"
        />
      </div>

      <div>
        <label className="block text-sm">Producto:</label>
        <select
          value={filters.product}
          onChange={(e) => updateFilter("product", e.target.value)}
          className="border px-2 py-1 rounded"
        >
          <option value="">Todos</option>
          {products.map((p) => (
            <option key={p} value={p}>
              {p}
            </option>
          ))}
        </select>
      </div>
    </div>
  );
};
