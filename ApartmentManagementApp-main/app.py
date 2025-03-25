from flask import Flask, jsonify, request
from flask_cors import CORS
from Classes.config import configure_app, db
from Classes.Apartment import Apartment  

app = Flask(__name__)
configure_app(app)
CORS(app)  # ✅ Enable CORS to prevent API request errors

# ✅ Correct way to initialize DB tables
with app.app_context():
    db.create_all()

# ✅ Route to Get All Apartments
@app.route('/apartments', methods=['GET'])
def get_apartments():
    apartments = Apartment.query.all()
    return jsonify([
        {
            'id': apt.id,
            'location': apt.location,
            'price': apt.price,
            'number_of_rooms': apt.number_of_rooms,
            'type': apt.type
        }
        for apt in apartments
    ])

# ✅ Route to Get a Single Apartment by ID
@app.route('/apartments/<int:id>', methods=['GET'])
def get_apartment(id):
    print(f"Fetching apartment with ID: {id}")  # ✅ Debugging log

    apartment = Apartment.query.get(id)

    if not apartment:
        print(f"❌ Apartment ID {id} not found in database")  # ✅ Debug log
        return jsonify({'error': 'Apartment not found'}), 404  

    print(f"✅ Apartment found: {apartment.location}")  # ✅ Debugging log

    return jsonify({
        'id': apartment.id,
        'owner_id': apartment.owner_id,
        'location': apartment.location or "Unknown Location",
        'price': apartment.price or "Price Not Available",
        'unit_number': apartment.unit_number or "N/A",
        'area': apartment.area or "N/A",
        'number_of_rooms': apartment.number_of_rooms or "N/A",
        'type': apartment.type or "N/A",
        'description': apartment.description or "No description available",
        'photos': apartment.photos if apartment.photos else ["assets/default-image.jpg"],  # ✅ Default Image
        'parking_availability': getattr(apartment, 'parking_availability', None),
        'video': getattr(apartment, 'video', None),
        'map_location': getattr(apartment, 'map_location', None),
        'status': apartment.status or "N/A",
        'created_at': apartment.created_at
    })

if __name__ == '__main__':
    app.run(debug=True)
