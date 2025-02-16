import gspread
from oauth2client.service_account import ServiceAccountCredentials
import cv2
from pyzbar.pyzbar import decode
from flask import Flask, request, jsonify
import time

# Authentification Google Sheets
def authenticate_google_sheets():
    scope = ["https://spreadsheets.google.com/feeds",
             "https://www.googleapis.com/auth/spreadsheets",
             "https://www.googleapis.com/auth/drive.file",
             "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
    client = gspread.authorize(creds)
    return client

# Ajouter un résultat dans Google Sheets
def add_result_to_sheet(participant_id, team_name, time):
    client = authenticate_google_sheets()
    sheet = client.open("Résultats Course").sheet1  # Assure-toi que ce fichier existe
    row = [participant_id, team_name, time]
    sheet.append_row(row)
    print(f"Résultat ajouté pour {participant_id} à {time}")

# Scanner un QR Code
def read_qr_code(image_path):
    img = cv2.imread(image_path)
    qr_codes = decode(img)
    for qr_code in qr_codes:
        data = qr_code.data.decode('utf-8')  # Contenu du QR code
        return data
    return None

# Flask API
app = Flask(__name__)

@app.route('/scanner', methods=['POST'])
def scanner():
    image_file = request.files['file']
    image_path = 'temp_image.png'
    image_file.save(image_path)

    qr_data = read_qr_code(image_path)
    if not qr_data:
        return jsonify({"error": "QR code non détecté"}), 400
    
    try:
        participant_id, team_name = qr_data.split(",")  
        current_time = time.strftime('%Y-%m-%d %H:%M:%S')
        add_result_to_sheet(participant_id, team_name, current_time)
        return jsonify({"message": "QR code scanné et résultat enregistré"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
