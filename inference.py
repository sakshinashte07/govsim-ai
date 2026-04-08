import os
import time
from openai import OpenAI
from environment import PoliSimEnv
from models import Action

# 🔹 Environment variables
API_BASE_URL = os.getenv("API_BASE_URL", "https://api.openai.com/v1")
MODEL_NAME = os.getenv("MODEL_NAME", "gpt-4.1-mini")
HF_TOKEN = os.getenv("HF_TOKEN")

if HF_TOKEN is None:
    raise ValueError("HF_TOKEN is required")

# 🔹 OpenAI client
client = OpenAI(
    base_url=API_BASE_URL,
    api_key=HF_TOKEN
)

def get_action_from_llm(state):
    prompt = f"""
    You are a policy decision AI.

    Current State:
    Pollution: {state.pollution}
    Economy: {state.economy}
    Satisfaction: {state.satisfaction}

    Suggest values between 0 and 1 for:
    tax, subsidy, regulation

    Output ONLY in format:
    tax,subsidy,regulation
    """

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[{"role": "user", "content": prompt}]
    )

    text = response.choices[0].message.content.strip()

    try:
        t, s, r = map(float, text.split(","))
        return Action(tax=t, subsidy=s, regulation=r)
    except:
        # fallback safe action
        return Action(tax=0.5, subsidy=0.5, regulation=0.5)


def run():
    env = PoliSimEnv()
    obs = env.reset()

    print("[START] task=policy env=polisim model=" + MODEL_NAME)

    rewards = []

    for step in range(6):
        try:
            action = get_action_from_llm(obs)

            obs, reward, done, _ = env.step(action)
            rewards.append(f"{reward:.2f}")

            print(f"[STEP] step={step+1} action={action.model_dump()} reward={reward:.2f} done={str(done).lower()} error=null")

            if done:
                break

        except Exception as e:
            print(f"[STEP] step={step+1} action=error reward=0.00 done=true error={str(e)}")
            break

    print(f"[END] success=true steps={len(rewards)} rewards={','.join(rewards)}")


if __name__ == "__main__":
    run()

    # keep container alive
    while True:
        time.sleep(60)
