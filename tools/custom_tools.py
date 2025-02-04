from crewai.tools import BaseTool
from pydantic import BaseModel, Field
from typing import Type

class LatexEditorInput(BaseModel):
    """Schema di input per il LatexEditorTool."""
    new_content: str = Field(..., description="Il nuovo contenuto da scrivere nel file LaTeX.")

class LatexEditorTool(BaseTool):
    """Tool per modificare file LaTeX."""
    name: str = "latex_editor_tool"
    description: str = "Modifica il contenuto di un file LaTeX specifico."
    args_schema: Type[BaseModel] = LatexEditorInput  # Validazione input con Pydantic

    def _run(self, new_content: str) -> str:
        """Scrive il nuovo contenuto in un file .tex."""
        file_path = "cv_dynamic.tex"  # Nome del file LaTeX

        try:
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(new_content)
            return f"✅ Il file {file_path} è stato aggiornato con successo."
        except Exception as e:
            return f"❌ Errore durante la modifica del file: {str(e)}"

class LaTeXCompilerTool(BaseTool):
    name:str = "LaTeX Compiler"
    description:str = "Compila il file LaTeX e genera un PDF."

    def _run(self):
        import os
        file_path = "cv_dynamic.tex"  # Nome del file LaTeX
        try:
            os.system(f"pdflatex {file_path} > /dev/null 2>&1")
            return f"Compilazione completata. File PDF generato."
        except Exception as e:
            return f"Errore durante la compilazione LaTeX: {str(e)}"