import sqlite3

class Band:
    def __init__(self, id, name, hometown):
        self.id = id
        self.name = name
        self.hometown = hometown

    def concerts(self):
        connection = sqlite3.connect('./database/concert.db')
        cursor = connection.cursor()

        query = """SELECT * FROM concerts WHERE band_id = ?"""
        concerts = cursor.execute(query, (self.id,)).fetchall()

        connection.close()
        return concerts

    def venues(self):
        connection = sqlite3.connect('../database/concert.db')
        cursor = connection.cursor()

        query = """SELECT DISTINCT venues.* FROM venues
                JOIN concerts ON concerts.venue_id = venues.id
                WHERE concerts.band_id = ?"""
        venues = cursor.execute(query, (self.id,)).fetchall()

        connection.close()
        return venues

    @staticmethod
    def most_performances():
        connection = sqlite3.connect('../database/concert.db')
        cursor = connection.cursor()

        query = """SELECT bands.*, COUNT(concerts.id) as performance_count
                FROM bands
                JOIN concerts ON concerts.band_id = bands.id
                GROUP BY bands.id
                ORDER BY performance_count DESC
                LIMIT 1"""
        most_performed_band = cursor.execute(query).fetchone()

        connection.close()
        return most_performed_band
