import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend,
} 
from "chart.js";
import { Bar } from "react-chartjs-2";
import type { Sale } from "../types/sales";

ChartJS.register(CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend);

interface Props {
  sales: Sale[];
}

export const SalesChart = ({ sales }: Props) => {

  const salesByDate: Record<string, number> = {};
  sales.forEach((s) => {
    salesByDate[s.date] = (salesByDate[s.date] || 0) + s.price * s.quantity;
  });

  const labels = Object.keys(salesByDate);
  const values = Object.values(salesByDate);

  const data = {
    labels,
    datasets: [
      {
        label: "Ventas por día",
        data: values,
        backgroundColor: "rgba(54, 162, 235, 0.6)",
      },
    ],
  };

  const options = {
    responsive: true,
    plugins: {
      legend: {
        position: "top" as const,
      },
      title: {
        display: true,
        text: "Ventas por Fecha",
      },
    },
  };

  return <Bar data={data} options={options} />;
};
