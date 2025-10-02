import { useState } from "react";

export interface Filters {
  startDate: string;
  endDate: string;
  product: string;
}

export const useFilters = () => {
  const [filters, setFilters] = useState<Filters>({
    startDate: "",
    endDate: "",
    product: "",
  });

  const updateFilter = (field: keyof Filters, value: string) => {
    setFilters((prev) => ({ ...prev, [field]: value }));
  };

  return { filters, updateFilter };
};
