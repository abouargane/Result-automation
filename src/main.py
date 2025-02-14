import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Authentification et autorisation via Google API
def authenticate_google_sheets():
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
    client = gspread.authorize(creds)
    return client

# Fonction pour ajouter un résultat dans Google Sheets
def add_result_to_sheet(participant_id, team_name, time):
    client = authenticate_google_sheets()
    sheet = client.open("Résultats Course").sheet1  # Utilise le nom de ton fichier Sheet
    row = [participant_id, team_name, time]
    sheet.append_row(row)
    print(f"Résultat ajouté pour {participant_id} à {time}")

import cv2
from pyzbar.pyzbar import decode

def read_qr_code(image_path):
    # Lire l'image contenant le QR code
    img = cv2.imread(image_path)
    
    # Décoder le QR code
    qr_codes = decode(img)
    
    for qr_code in qr_codes:
        data = qr_code.data.decode('utf-8')  # Contenu du QR code
        print(f"QR Code trouvé: {data}")
        return data
from flask import Flask, request, jsonify
import time

app = Flask(__name__)

@app.route('/scanner', methods=['POST'])
def scanner():
    image_file = request.files['file']
    # Sauvegarder l'image temporairement
    image_path = 'temp_image.png'
    image_file.save(image_path)
    
    # Lire les informations du QR code
    qr_data = read_qr_code(image_path)
    
    # Ajouter les résultats à Google Sheets
    participant_id, team_name = qr_data.split(",")  # Adapte en fonction de la structure de ton QR code
    current_time = time.time()  # Utilise l'heure actuelle
    add_result_to_sheet(participant_id, team_name, current_time)
    
    return jsonify({"message": "QR code scanné et résultat enregistré"}), 200

if __name__ == '__main__':
    app.run(debug=True)

