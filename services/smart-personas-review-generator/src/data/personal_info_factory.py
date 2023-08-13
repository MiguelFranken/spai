import csv


class PersonalInfoFactory:
    """
    A factory class for retrieving personal information from a CSV file.

    Attributes:
        None

    Methods:
        get_persona: Retrieves personal information for a given name from a CSV file.

    Usage:
        To use this class, simply call the get_persona method with the name of the person you want to retrieve
        information for. If the name is found in the CSV file, the method will return a dictionary containing the
        person's information. If the name is not found, a ValueError will be raised.
    """

    @staticmethod
    def get_persona(name: str) -> dict:
        """
        Retrieves personal information for a given name from a CSV file.

        Args:
            name: A string representing the name of the person to retrieve information for.

        Returns:
            A dictionary containing the person's information if the name is found in the CSV file.

        Raises:
            ValueError: If the name is not found in the CSV file.
        """
        with open('data/personas.csv', mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['name'] == name:
                    return row
        raise ValueError(f"No personal info found for name: {name}")

