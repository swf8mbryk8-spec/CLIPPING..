# Installazione su Windows
1. Installa Python 3.12+ (da python.org).
2. Installa FFmpeg (da ffmpeg.org) e aggiungilo al PATH.
3. Crea un venv: `python -m venv venv`
4. Attiva il venv e installa i requisiti: `venv\Scripts\pip install -r requirements.txt -r requirements-local.txt`
5. Crea un file `.env` copiando da `.env.example` e inserisci le tue chiavi API.
6. Avvia l'app: `venv\Scripts\python main.py`

# Deployment Online (Frontend + Backend)
*   **Vercel** è purtroppo inadatta al rendering video (FFmpeg + tempi lunghi).
*   **Soluzione gratuita (Limitata):** Render (piano free) può ospitare il backend, ma il rendering video causerà timeout e esaurimento RAM.
*   **Soluzione raccomandata:** VPS economico (es. Hetzner, 5€/mese).
    *   Vantaggio: FFmpeg sempre disponibile, backend FastAPI sempre attivo.
    *   Sicurezza: Configurare Nginx con Basic Auth per proteggere l'accesso.

# Sicurezza
*   Mai caricare file `.env` o chiavi API su GitHub.
*   Usa repository privati.
