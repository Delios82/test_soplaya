from django.core.management.base import BaseCommand, CommandError
import os
import mimetypes
from restaurant.excetions import NotCSVFileException
import numpy as np
from restaurant.models import Restaurant
from tqdm import tqdm


class Command(BaseCommand):
    help = "Importa il file csv con i dati dei restaurant"

    def add_arguments(self, parser):
        parser.add_argument('path_file')

    def handle(self, *args, **options):
        if not os.path.exists(options['path_file']):
            raise FileNotFoundError(f"Il file {options['path_file']} non esiste!")

        mime_type, _ = mimetypes.guess_type(options['path_file'])
        if mime_type != 'text/csv':
            raise NotCSVFileException(f"Il file {options['path_file']} non è un file CSV")

        data = np.genfromtxt(options['path_file'], delimiter=',', dtype=None, encoding='utf-8', skip_header=1)

        progress = tqdm(range(len(data)), position=0)
        progress.set_description('import restaurant')

        for row in data:
            hours_variance = int(row[2]) - int(row[3])
            budget_variance = round(float(row[4]) - float(row[5]), 2)
            restaurant = Restaurant.objects.create(
                date=row[0],
                restaurant=row[1],
                planned_hours=row[2],
                actual_hours=row[3],
                budget=row[4],
                sells=row[5],
                hours_variance=hours_variance,
                budget_variance=budget_variance,
            )
            progress.update(1)
