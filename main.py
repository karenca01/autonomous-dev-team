from orchestrator.dev_team import DevTeam


idea = """
I want an application to track personal habits.
"""


team = DevTeam()
results = team.run(idea)


for agent_name, response in results.items():
    print(f"\n\n=== {agent_name.upper()} ===")
    print(response)