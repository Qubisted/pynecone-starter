import pynecone as pc


config = pc.Config(
    app_name="pynecone_starter",
    port=3945,
    db_url="sqlite:///pynecone.db",
    env=pc.Env.DEV,
)
