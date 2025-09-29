import sys
import subprocess

print("🔍 Ejecutando todos los tests en /tests...")
result = subprocess.run([sys.executable, "-m", "pytest", "tests/", "--maxfail=3", "--tb=short"])

if result.returncode == 0:
    print("✅ Todos los tests pasaron correctamente.")
else:
    print("❌ Algunos tests fallaron.")

sys.exit(result.returncode)
