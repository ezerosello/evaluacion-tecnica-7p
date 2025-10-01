import logging
from datetime import datetime
import pandas as pd

class SalesAnalyzer:
    def __init__(self, data):
        self.data = data
        self.reports = {}

    @staticmethod
    def format(period_dict):
        return {
            str(k): {
                'total': float(v['sum']),
                'count': int(v['count']),
                'average': float(v['mean'])
            } for k, v in period_dict.items()
        }

    def analyze_user(self, user_id):
        user_sales_raw = [s for s in self.data if str(s.get('user_id')) == str(user_id)]
        if not user_sales_raw:
            logging.info(f"No sales for user {user_id}")
            return False

        # Validación de campos obligatorios
        user_sales = []
        for sale in user_sales_raw:
            if not all(k in sale for k in ['date', 'price', 'quantity']):
                logging.warning(f"Missing fields in record: {sale}")
                continue
            user_sales.append(sale)

        if not user_sales:
            logging.info(f"All records for user {user_id} were invalid or incomplete")
            return False

        try:
            df = pd.DataFrame(user_sales)
            df['date'] = pd.to_datetime(df['date'], errors='coerce')
            df['price'] = pd.to_numeric(df['price'], errors='coerce')
            df['quantity'] = pd.to_numeric(df['quantity'], errors='coerce')

            invalid_rows = df[df[['date', 'price', 'quantity']].isnull().any(axis=1)]
            for _, row in invalid_rows.iterrows():
                logging.warning(f"Invalid record after coercion: {row.to_dict()}")
            df.dropna(subset=['date', 'price', 'quantity'], inplace=True)
            if df.empty:
                logging.info(f"All records for user {user_id} were invalid after coercion")
                return False


            df['total'] = df['price'] * df['quantity']

            monthly = df.groupby(df['date'].dt.to_period('M'))['total'].agg(['sum', 'count', 'mean']).to_dict('index')
            yearly = df.groupby(df['date'].dt.to_period('Y'))['total'].agg(['sum', 'count', 'mean']).to_dict('index')

            self.reports[user_id] = {
                'monthly': self.format(monthly),
                'yearly': self.format(yearly),
                'user_id': user_id,
                'generated_at': datetime.now().isoformat()
            }
            return True

        except Exception as e:
            logging.error(f"Pandas analysis failed for user {user_id}: {e}")
            return False

    def get_report(self, user_id):
        return self.reports.get(user_id)
