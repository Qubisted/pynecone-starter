import pynecone as pc


config = pc.Config(
    app_name="pynecone_starter",
    api_url="pynecone-starter-production.up.railway.app",
    bun_path="$HOME/.bun/bin/bun",
    db_url="sqlite:///pynecone.db",
    env=pc.Env.DEV,
)
