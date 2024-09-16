import sqlite3

class Venue:
    def __init__(self, id, title, city):
        self.id = id
        self.title = title
        self.city = city

    def concerts(self):
        connection = sqlite3.connect('../database/concert.db')
        cursor = connection.cursor()

        query = "SELECT * FROM concerts WHERE venue_id = ?"
        concerts = cursor.execute(query, (self.id,)).fetchall()

        connection.close()
        return concerts

    def bands(self):
        connection = sqlite3.connect('../database/concert.db')
        cursor = connection.cursor()

        query = """SELECT DISTINCT bands.* FROM bands
                JOIN concerts ON concerts.band_id = bands.id
                WHERE concerts.venue_id = ?"""
        bands = cursor.execute(query, (self.id,)).fetchall()

        connection.close()
        return bands

    def most_frequent_band(self):
        connection = sqlite3.connect('../database/concert.db')
        cursor = connection.cursor()

        query = """SELECT bands.*, COUNT(concerts.id) as performance_count
                FROM bands
                JOIN concerts ON concerts.band_id = bands.id
                WHERE concerts.venue_id = ?
                GROUP BY bands.id
                ORDER BY performance_count DESC
                LIMIT 1"""
        most_frequent_band = cursor.execute(query, (self.id,)).fetchone()

        connection.close()
        return most_frequent_band
