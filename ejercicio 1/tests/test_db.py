from init_db import init_db

def test_init_db():
    try:
        init_db()
        assert True
    except Exception as e:
        assert False, f"Error al inicializar la DB: {e}"
