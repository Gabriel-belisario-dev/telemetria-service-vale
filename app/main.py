from fastapi import FastAPI

app = FastAPI(
    title="Vale Minitruck Telemetry API",
    description="API de missão crítica para monitoramento de frotas e predição de alarmes.",
    version="1.0.0"
)

@app.get("/health", tags=["Infrastructure"])
async def health_check():
    return {
        "status": "healthy",
        "environment": "development",
        "version": "1.0.0",
        "message": "Microsserviço de Telemetria Vale operando perfeitamente."
    }