def simulate(state, action):
    pollution = state["pollution"]
    economy = state["economy"]
    satisfaction = state["satisfaction"]

    tax = action["tax"]
    subsidy = action["subsidy"]
    regulation = action["regulation"]

    pollution -= (tax * 4 + regulation * 6)
    economy -= (tax * 3 + regulation * 2)
    economy += subsidy * 5

    satisfaction += subsidy * 4
    satisfaction -= tax * 2

    # Side effects
    if tax > 0.7:
        economy -= 4

    if subsidy > 0.8:
        satisfaction -= 3

    if regulation > 0.7:
        economy -= 3

    # Clamp values
    pollution = max(0, min(100, pollution))
    economy = max(0, min(100, economy))
    satisfaction = max(0, min(100, satisfaction))

    return {
        "pollution": round(pollution, 2),
        "economy": round(economy, 2),
        "satisfaction": round(satisfaction, 2)
    }