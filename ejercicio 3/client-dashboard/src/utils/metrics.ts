import type { Sale } from "../types/sales";

export const totalSales = (sales: Sale[]) =>
  sales.reduce((sum, s) => sum + s.price * s.quantity, 0);

export const bestProduct = (sales: Sale[]) => {
  const counts: Record<string, number> = {};
  sales.forEach((s) => {
    if (!s.product) return;
    counts[s.product] = (counts[s.product] || 0) + s.quantity;
  });
  return Object.entries(counts).sort((a, b) => b[1] - a[1])[0]?.[0] || "N/A";
};

export const avgRating = (sales: Sale[]) =>
  sales.reduce((sum, s) => sum + s.rating, 0) / sales.length;
