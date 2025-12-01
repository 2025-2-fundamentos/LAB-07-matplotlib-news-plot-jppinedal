"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel

import os
import pandas as pd
import matplotlib.pyplot as plt

def pregunta_01():
    """
    Siga las instrucciones del video https://youtu.be/qVdwpxG_JpE para
    generar el archivo `files/plots/news.png`.

    Un ejemplo de la grafica final esta ubicado en la raíz de
    este repo.

    El gráfico debe salvarse al archivo `files/plots/news.png`.

    """
    input_path = "files/input/news.csv"
    output_path = "files/plots/news.png"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # --- Configuraciones por categoría ---
    colors = {
        'Television': 'blue',
        'Newspaper': 'purple',
        'Internet': 'pink',
        'Radio': 'orange',
    }

    zorder = {
        'Television': 1,
        'Newspaper': 1,
        'Internet': 2,
        'Radio': 1,
    }

    linewidths = {
        'Television': 2,
        'Newspaper': 2,
        'Internet': 4,
        'Radio': 2,
    }

    # --- Lectura del archivo ---
    df = pd.read_csv(input_path, index_col=0)

    # --- Estilo base ---
    plt.figure(figsize=(10, 6))

    # --- Líneas principales ---
    for col in df.columns:
        plt.plot(
            df.index,
            df[col],
            color=colors[col],
            label=col,
            linewidth=linewidths[col],
            zorder=zorder[col]
        )

    # --- Ajustes del gráfico ---
    plt.title("How people get their news", fontsize=16)
    ax = plt.gca()
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_visible(False)
    ax.get_yaxis().set_visible(False)

    # --- Puntos iniciales y finales + etiquetas ---
    for col in df.columns:
        first_year = df.index[0]
        last_year = df.index[-1]

        # Punto inicial
        plt.scatter(
            first_year,
            df.loc[first_year, col],
            color=colors[col],
            zorder=zorder[col]
        )
        plt.text(
            first_year - 0.2,
            df.loc[first_year, col],
            f"{col} {df.loc[first_year, col]}%",
            ha="right",
            va="center",
            color=colors[col],
        )

        # Punto final
        plt.scatter(
            last_year,
            df.loc[last_year, col],
            color=colors[col],
            zorder=zorder[col]
        )
        plt.text(
            last_year + 0.2,
            df.loc[last_year, col],
            f"{df.loc[last_year, col]}%",
            ha="left",
            va="center",
            color=colors[col],
        )

    # --- Etiquetas del eje X ---
    plt.xticks(ticks=df.index, labels=df.index)

    # --- Guardado ---
    plt.tight_layout()
    plt.savefig(output_path)
    plt.show()
