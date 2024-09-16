import sqlite3
from models.band import Band
from models.venue import Venue
from models.concert import Concert

# Example of creating instances and calling methods
band = Band(1, 'Odeon', 'Nairobi')
venue = Venue(1, 'Wembley Stadium', 'London')

# Fetch band's concerts
connection = sqlite3.connect('database/concert.db')
cursor = connection.cursor()

concerts = band.concerts()
print(f"{band.name} has played the following concerts: {concerts}")

# Example of introduction
concert = Concert(1, '2024-09-01', 1, 1)
print(concert.introduction())

# Closing the database connection
connection.close()
