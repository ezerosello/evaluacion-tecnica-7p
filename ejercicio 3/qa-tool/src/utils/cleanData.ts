import type { Sale } from "../types/sales";

export const wrongRegisters = (sales: Sale[]) =>
  sales.filter((s) => s.quantity <= 0 || s.product == null || s.price <=0);

export const fixWrongRegisters = (sales: Sale[]): Sale[] => {
  return sales.map((s) => ({
    ...s,
    
    quantity: s.quantity <= 0 ? Math.abs(s.quantity) || 1 : s.quantity,
    
    product: s.product === null || s.product === "" ? "Producto desconocido" : s.product,
    
    price: s.price <= 0 ? 1 : s.price,
  }));
};