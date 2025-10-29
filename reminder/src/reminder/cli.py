
from typing import Optional
import typer

app = typer.Typer(
    help="reminder: agende tarefas em linguagem natural (estrutura de comandos)."
)

@app.command("add")
def add(
    texto: str = typer.Argument(
        ...,
        help='Frase em linguagem natural. Ex.: "todo dia às 7h", "seg a sex às 8:30".',
        metavar="TEXTO",
    ),
    command: Optional[str] = typer.Option(
        None, "--command", "-c",
        help="Comando a executar. Dica: use após `--` para evitar conflito de flags."
    ),
    tz: Optional[str] = typer.Option(
        None, "--tz",
        help="Timezone IANA (ex.: America/Fortaleza). Padrão: timezone do sistema."
    ),
    dry_run: bool = typer.Option(
        False, "--dry-run",
        help="Só mostra a interpretação/preview (não instala)."
    ),
    yes: bool = typer.Option(
        False, "--yes", "-y",
        help="Confirma instalação sem perguntar."
    ),
):
    """
    Cria uma tarefa a partir de linguagem natural (sem instalar quando --dry-run).
    """

@app.command("ls")
def ls(
    show_all: bool = typer.Option(
        False, "--all",
        help="Inclui tarefas pausadas também."
    ),
    next_n: int = typer.Option(
        0, "--next",
        help="Mostra as próximas N execuções (0 = não calcular)."
    ),
):
    """
    Lista tarefas instaladas (visão resumida).
    """

@app.command("show")
def show(
    id: str = typer.Argument(..., help="ID da tarefa.", metavar="ID"),
    next_n: int = typer.Option(
        5, "--next",
        help="Mostra as próximas N execuções estimadas."
    ),
):
    """
    Mostra detalhes completos de uma tarefa.
    """

@app.command("explain")
def explain(
    id: str = typer.Argument(..., help="ID da tarefa.", metavar="ID"),
    next_n: int = typer.Option(
        5, "--next",
        help="Explica recorrência e próximas N datas elegíveis."
    ),
):
    """
    Explica em linguagem natural quando a tarefa roda.
    """

@app.command("run")
def run(
    id: str = typer.Argument(..., help="ID da tarefa para executar agora.", metavar="ID"),
):
    """
    Executa a tarefa imediatamente (para teste).
    """

@app.command("pause")
def pause(
    id: str = typer.Argument(..., help="ID da tarefa a pausar.", metavar="ID"),
):
    """
    Pausa (desabilita) a tarefa no scheduler.
    """

@app.command("resume")
def resume(
    id: str = typer.Argument(..., help="ID da tarefa a retomar.", metavar="ID"),
):
    """
    Retoma (habilita) a tarefa pausada.
    """

@app.command("rm")
def rm(
    id: str = typer.Argument(..., help="ID da tarefa a remover.", metavar="ID"),
    yes: bool = typer.Option(
        False, "--yes", "-y",
        help="Confirma remoção sem perguntar."
    ),
):
    """
    Remove a tarefa do scheduler e do registro local.
    """

@app.command("doctor")
def doctor():
    """
    Roda checagens básicas do ambiente (cron, PATH, TZ).
    """

if __name__ == "__main__":
    app()
