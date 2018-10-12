import pandas as pd

from .models import Guest


def import_csv_file(csv_path):
    data = pd.read_csv(csv_path, header=None, names=['First Name', 'Last Name', 'Badge Number', 'Department'])

    for row in data.iterrows():
        row = row[1]
        guest = Guest.create(name=str(row[0] + " " + row[1]), badge_number=row[2], department=row[3])
        guest.save()


if __name__ == "__main__":
    import_csv_file('final_badges.csv')
