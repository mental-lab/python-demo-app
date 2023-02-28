import os
from notes import note

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    note.run(host='0.0.0.0', port=port, debug=True)
