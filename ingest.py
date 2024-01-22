import os
import json
from neo4j import GraphDatabase

class GeoJSONImporter:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def import_geojson(self, file_path):
        with open(file_path) as file:
            data = json.load(file)
            for feature in data['features']:
                self.create_node(feature)

    def create_node(self, feature):
        with self.driver.session() as session:
            session.write_transaction(self._create_node_tx, feature)

    @staticmethod
    def _create_node_tx(tx, feature):
        query = (
            "CREATE (a:Address {id: $id, unit: $unit, number: $number, "
            "street: $street, city: $city, district: $district, region: $region, "
            "postcode: $postcode, latitude: $latitude, longitude: $longitude})"
        )
        properties = feature['properties']
        coordinates = feature['geometry']['coordinates']
        tx.run(query, id=properties['id'], unit=properties['unit'],
               number=properties['number'], street=properties['street'],
               city=properties['city'], district=properties['district'],
               region=properties['region'], postcode=properties['postcode'],
               latitude=coordinates[1], longitude=coordinates[0])

def main():
    importer = GeoJSONImporter("neo4j://localhost:7687", "username", "password")

    # Replace with your directories and files structure
    for state_folder in ['path_to_state_folders']:
        for file_name in os.listdir(state_folder):
            if file_name.endswith('.geojson'):
                importer.import_geojson(os.path.join(state_folder, file_name))

    importer.close()

if __name__ == "__main__":
    main()
