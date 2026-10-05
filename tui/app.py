"""Terminal front end. Display only; all math lives in core/."""
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from core.membership import membership_birth_year
from core.rank import load_data, rank_birth_year

console = Console()


def show(year):
    _, pop = load_data()
    membership = membership_birth_year(year)
    ranks = rank_birth_year(year)

    headline = "  +  ".join(f"[bold]{m.pct}% {m.label}[/bold]" for m in membership)
    console.print(Panel(headline, title=f"Born {year}", style="bold cyan", padding=(1, 4)))

    table = Table(title="How you compare with each generation")
    table.add_column("Generation")
    table.add_column("Birth years")
    table.add_column("% older than you", justify="right")
    table.add_column("% younger than you", justify="right")
    for r in ranks:
        mark = "*" if r.approximate else ""
        table.add_row(r.name, f"{r.start_year}-{r.end_year}",
                      f"{r.older_pct:.1f}%{mark}", f"{r.younger_pct:.1f}%{mark}")
    console.print(table)
    if any(r.approximate for r in ranks):
        console.print("[dim]* approximate (people aged 100+ spread evenly over birth years)[/dim]")
    console.print(f"[dim]Source: US Census Bureau {pop['dataset']}, "
                  f"Vintage {pop['vintage']}. Generations: Pew Research Center.[/dim]")


def main():
    console.print("[bold]Find my generation[/bold]")
    while True:
        text = console.input("\nBirth year (or q to quit): ").strip()
        if text.lower() in ("q", "quit", "exit"):
            break
        try:
            year = int(text)
        except ValueError:
            console.print("[yellow]Please enter a whole number, e.g. 1985.[/yellow]")
            continue
        try:
            show(year)
        except ValueError as err:
            console.print(f"[yellow]{err}[/yellow]")


if __name__ == "__main__":
    main()
