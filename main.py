from orchestrator.dev_team import DevTeam

print("Describe your software idea.")
print("Write END on a new line when you finish.\n")

lines = []

while True:
    line = input()

    if line.strip().upper() == "END":
        break

    lines.append(line)

idea = "\n".join(lines)


team = DevTeam()
results = team.run(idea)


for agent_name, response in results.items():
    print(f"\n\n=== {agent_name.upper()} ===")
    print(response)