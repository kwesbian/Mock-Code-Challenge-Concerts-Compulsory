import sqlite3

class Concert:
    def __init__(self, id, date, band_id, venue_id):
        self.id = id
        self.date = date
        self.band_id = band_id
        self.venue_id = venue_id

    def band(self):
        connection = sqlite3.connect('../database/concert.db')
        cursor = connection.cursor()

        query = """SELECT bands.* FROM bands
                JOIN concerts ON concerts.band_id = bands.id
                WHERE concerts.id = ?"""
        band = cursor.execute(query, (self.id,)).fetchone()

        connection.close()
        return band

    def venue(self):
        connection = sqlite3.connect('../database/concert.db')
        cursor = connection.cursor()

        query = """SELECT venues.* FROM venues
                JOIN concerts ON concerts.venue_id = venues.id
                WHERE concerts.id = ?"""
        venue = cursor.execute(query, (self.id,)).fetchone()

        connection.close()
        return venue

    def introduction(self):
        connection = sqlite3.connect('../database/concert.db')
        cursor = connection.cursor()

        query = """SELECT bands.name, bands.hometown, venues.city FROM concerts
                JOIN bands ON concerts.band_id = bands.id
                JOIN venues ON concerts.venue_id = venues.id
                WHERE concerts.id = ?"""
        result = cursor.execute(query, (self.id,)).fetchone()

        connection.close()
        return f"Hello {result['city']}!!!!! We are {result['name']} and we're from {result['hometown']}"
