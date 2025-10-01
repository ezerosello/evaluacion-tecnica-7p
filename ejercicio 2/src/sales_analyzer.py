import logging
from datetime import datetime
import pandas as pd

class SalesAnalyzer:
    def __init__(self, data):
        self.data = data
        self.reports = {}

    def analyze_user(self, user_id):
        user_sales = [s for s in self.data if str(s.get('user_id')) == str(user_id)]
        if not user_sales:
            logging.info(f"No sales for user {user_id}")
            return False

        try:
            df = pd.DataFrame(user_sales)
            df['date'] = pd.to_datetime(df['date'], errors='coerce')
            df['price'] = pd.to_numeric(df['price'], errors='coerce')
            df['quantity'] = pd.to_numeric(df['quantity'], errors='coerce')
            df.dropna(subset=['date', 'price', 'quantity'], inplace=True)
            df['total'] = df['price'] * df['quantity']

            monthly = df.groupby(df['date'].dt.to_period('M'))['total'].agg(['sum', 'count', 'mean']).to_dict('index')
            yearly = df.groupby(df['date'].dt.to_period('Y'))['total'].agg(['sum', 'count', 'mean']).to_dict('index')

            def format(period_dict):
                return {
                    str(k): {
                        'total': float(v['sum']),
                        'count': int(v['count']),
                        'average': float(v['mean'])
                    } for k, v in period_dict.items()
                }

            self.reports[user_id] = {
                'monthly': format(monthly),
                'yearly': format(yearly),
                'user_id': user_id,
                'generated_at': datetime.now().isoformat()
            }
            return True
        except Exception as e:
            logging.error(f"Pandas analysis failed for user {user_id}: {e}")
            return False

    def get_report(self, user_id):
        return self.reports.get(user_id)
