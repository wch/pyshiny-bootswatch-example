from pathlib import Path

import matplotlib.pyplot as plt

# Import modules for plot rendering
import numpy as np
from htmltools import HTMLDependency

from shiny import App, Inputs, Outputs, Session, render, ui

www_dir = Path(__file__).parent / "www"

app_ui = ui.page_fluid(
    HTMLDependency(
        "bootstrap",
        version="9.99",
        source={"subdir": str(www_dir)},
        script={"src": "bootstrap.bundle.min.js"},
        stylesheet={"href": "bootstrap.min.css"},
    ),
    ui.layout_sidebar(
        ui.panel_sidebar(
            ui.input_text("txt", "Input some text"),
            ui.input_action_button("btn", "Click me", class_="btn-warning"),
            ui.input_slider("n", "N", 0, 100, 20),
            ui.markdown(
                "This example uses the Bootswatch [Litera](https://bootswatch.com/litera/) theme."
            ),
        ),
        ui.panel_main(
            ui.output_plot("histogram"),
        ),
    ),
)


def server(input: Inputs, output: Outputs, session: Session):
    @output
    @render.plot(alt="A histogram")
    def histogram():
        np.random.seed(19680801)
        x = 100 + 15 * np.random.randn(437)
        plt.hist(x, input.n(), density=True)


app = App(app_ui, server, static_assets=www_dir)
