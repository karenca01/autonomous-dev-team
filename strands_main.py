from dotenv import load_dotenv
from strands_orchestrator.strands_dev_team import StrandsDevTeam


load_dotenv()

print("Describe your software idea.")
print("Write END on a new line when you finish.\n")

lines = []

while True:
    line = input()

    if line.strip().upper() == "END":
        break

    lines.append(line)

idea = "\n".join(lines)

team = StrandsDevTeam()
results = team.run(idea)

for agent_name, response in results.items():
    print(f"\n\n=== {agent_name.upper()} ===")
    print(response)