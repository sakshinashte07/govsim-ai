from environment import PoliSimEnv
from models import Action

def run():
    env = PoliSimEnv()
    obs = env.reset()

    print("[START] task=policy env=polisim model=baseline")

    rewards = []

    for step in range(6):
        action = Action(tax=0.5, subsidy=0.6, regulation=0.5)

        obs, reward, done, _ = env.step(action)
        rewards.append(f"{reward:.2f}")

        print(f"[STEP] step={step+1} action={action.dict()} reward={reward:.2f} done={str(done).lower()} error=null")

        if done:
            break

    print(f"[END] success=true steps={len(rewards)} rewards={','.join(rewards)}")

if __name__ == "__main__":
    run()