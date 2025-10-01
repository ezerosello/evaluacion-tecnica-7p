from collections import defaultdict
from datetime import datetime
from statistics import mean
import logging

class SalesAnalyzer:
    def __init__(self, data):
        self.data = data
        self.reports = {}

    def analyze_user(self, user_id):
        user_sales = [s for s in self.data if str(s.get('user_id')) == str(user_id)]
        if not user_sales:
            logging.info(f"No sales for user {user_id}")
            return False

        monthly = defaultdict(list)
        yearly = defaultdict(list)

        for sale in user_sales:
            if not all(k in sale for k in ['date', 'price', 'quantity']):
                logging.warning(f"Missing fields in record: {sale}")
                continue
            try:
                date = datetime.strptime(sale['date'], '%Y-%m-%d')
                price = float(sale['price'])
                quantity = int(sale['quantity'])
                total = price * quantity
                monthly[date.strftime('%Y-%m')].append(total)
                yearly[date.strftime('%Y')].append(total)
            except Exception as e:
                logging.warning(f"Invalid record: {sale} → {e}")

        self.reports[user_id] = {
            'monthly': self._summarize(monthly),
            'yearly': self._summarize(yearly),
            'user_id': user_id,
            'generated_at': datetime.now().isoformat()
        }
        return True

    def _summarize(self, period_dict):
        return {
            k: {
                'total': sum(v),
                'count': len(v),
                'average': mean(v) if v else 0
            } for k, v in period_dict.items()
        }

    def get_report(self, user_id):
        return self.reports.get(user_id)
