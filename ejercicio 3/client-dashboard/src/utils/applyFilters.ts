import type { Sale } from "../types/sales";
import type { Filters } from "../hooks/useFilters";

export const applyFilters = (sales: Sale[], filters: Filters) => {
  return sales.filter((s) => {
    const date = new Date(s.date);

    if (filters.startDate && date < new Date(filters.startDate)) {
      return false;
    }

    if (filters.endDate && date > new Date(filters.endDate)) {
      return false;
    }

    if (filters.product && s.product !== filters.product) {
      return false;
    }

    return true;
  });
};
