from pathlib import Path


class MarkdownExporter:
    def export(self, results):
        output_dir = Path("outputs")
        output_dir.mkdir(exist_ok=True)

        output_file = output_dir / "dev_team_output.md"

        with open(output_file, "w", encoding="utf-8") as file:
            file.write("# Development Team Report\n\n")

            for agent_name, response in results.items():
                title = agent_name.replace("_", " ").title()

                file.write(f"## {title}\n\n")
                file.write(response)
                file.write("\n\n---\n\n")

        return output_file