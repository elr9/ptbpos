from supabase import create_client, Client

# Replace these with your Supabase URL and API key
SUPABASE_URL = "https://zpvevwaqrqeqhjwumyqf.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InpwdmV2d2FxcnFlcWhqd3VteXFmIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MTcxODk5MDMsImV4cCI6MjAzMjc2NTkwM30.vfcXuIgIR5J4hZAxI7DpKxztwzPAyIz9LSmW4h5uyVQ"

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
