# run_project.ps1
$workingDir = "d:\Project Aurelius"

# Start the Backend Server
Start-Process powershell -ArgumentList "-NoExit","-Command","cd `"$workingDir`"; Write-Host 'Starting Backend API on port 8000...'; python -m uvicorn src.api.main:app --host 0.0.0.0 --port 8000 2> backend_err.log; if (`$LASTEXITCODE -ne 0) { Read-Host 'Backend failed. Press Enter to close' }"

# Start the Streamlit Dashboard 
Start-Process powershell -ArgumentList "-NoExit","-Command","cd `"$workingDir`"; Write-Host 'Starting Streamlit Dashboard on port 8501...'; python -m streamlit run dashboard/app.py --server.port 8501 --server.headless true; if (`$LASTEXITCODE -ne 0) { Read-Host 'Dashboard failed. Press Enter to close' }"

# Start the Vite React Frontend
Start-Process powershell -ArgumentList "-NoExit","-Command","cd `"$workingDir\frontend`"; Write-Host 'Starting Frontend on port 5173...'; npm run dev; if (`$LASTEXITCODE -ne 0) { Read-Host 'Frontend failed. Press Enter to close' }"

Write-Host "All components have been launched in separate windows."
