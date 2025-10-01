import os
import json
import csv
import logging
import numpy as np



class ReportGenerator:
    def __init__(self, prefs=None):
        self.prefs = prefs or {
            'currency': 'USD',
            'date_format': '%Y-%m-%d',
            'output_type': 'json'
        }

    def export(self, report, output_dir):
        if not all(k in report for k in ['monthly', 'yearly', 'user_id']):
            logging.error(f"Incomplete report structure: {report}")
            return

        user_id = report['user_id']
        filename = f"sales_report_{user_id}.{self.prefs['output_type']}"
        filepath = os.path.join(output_dir, filename)

        os.makedirs(output_dir, exist_ok=True)

        try:
            if self.prefs['output_type'] == 'json':
                with open(filepath, 'w', encoding='utf-8') as f:
                    json.dump(report, f, indent=2)
            elif self.prefs['output_type'] == 'csv':
                self._export_csv(report, filepath)
            else:
                logging.warning(f"Unsupported format: {self.prefs['output_type']}")
                return
            logging.info(f"Report saved: {filepath}")
        except IOError as e:
            logging.error(f"Failed to write report: {e}")

    def _export_csv(self, report, filepath):
        with open(filepath, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['Period', 'Total', 'Average', 'Count'])
            for period in ['monthly', 'yearly']:
                for name, data in report[period].items():
                    writer.writerow([
                        name,
                        np.round(data['total'], 2),
                        np.round(data['average'], 2),
                        data['count']
                    ])
