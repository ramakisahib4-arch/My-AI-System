from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent

MODEL_PATH = ROOT / "model"
ENGINE_PATH = ROOT / "engine"
AGENT_PATH = ROOT / "agent"
TOOLS_PATH = ROOT / "tools"
API_PATH = ROOT / "api"

print("Project paths loaded")
