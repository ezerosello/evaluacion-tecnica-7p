import os
import logging
from src import DataLoader, SalesAnalyzer, ReportGenerator

logging.basicConfig(level=logging.INFO)

def main():
    logging.info("Starting report generation...")

    loader = DataLoader()
    # loader.load_files('data/sales1.json', 'data/sales2.csv')

    data_folder = 'data'
    file_paths = [os.path.join(data_folder, f) for f in os.listdir(data_folder) if f.endswith(('.json', '.csv'))]
    loader.load_files(*file_paths)


    analyzer = SalesAnalyzer(loader.get_data())
    generator = ReportGenerator({'output_type': 'json'})

    user_ids = loader.get_user_ids("data/")

    for user_id in user_ids:
        if analyzer.analyze_user(user_id):
            report = analyzer.get_report(user_id)
            generator.export(report, 'reports')

    logging.info("All reports generated.")

if __name__ == '__main__':
    main()
