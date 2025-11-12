import os
import tempfile
from app.utils import format_result, save_to_json, load_from_json

def test_format_result():
    result = format_result('addition', 5)
    assert result == {'operation': 'addition', 'result': 5}

def test_save_and_load_json():
    # Créer un fichier temporaire
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.json') as f:
        temp_file = f.name
    
    try:
        # Données à sauvegarder
        data = {'test': 'data', 'number': 42}
        
        # Sauvegarder
        save_to_json(data, temp_file)
        
        # Vérifier que le fichier existe
        assert os.path.exists(temp_file)
        
        # Charger
        loaded_data = load_from_json(temp_file)
        
        # Vérifier les données
        assert loaded_data == data
    finally:
        # Nettoyer
        if os.path.exists(temp_file):
            os.unlink(temp_file)
