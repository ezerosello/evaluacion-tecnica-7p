import type { Sale } from "../types/sales";

export const cleanSales = (sales: Sale[]) =>
  sales.filter((s) => s.quantity > 0 && s.product !== null && s.price >0 );
