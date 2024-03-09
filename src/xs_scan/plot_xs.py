import multiprocessing as mp
import os

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import ROOT

from . import calculate_cross_section

ufo_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "model", "vLQ_UFO")
# # You also can use path like this
# ufo_path = "/home/pheno/github/Colliders_Template/model/vLQ_UFO"

mg5_bin_path = os.path.join(os.sep, "Collider", "MG5_aMC_v3_1_0", "bin", "mg5_aMC")

outputs_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "outputs")
os.makedirs(outputs_dir, exist_ok=True)
plot_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "pdfs")
n_cores = mp.cpu_count()
n_workers = n_cores - 2 if n_cores > 2 else 1

n_events = int(1e5)

print("Loading UFO model from:\n", ufo_path)
print("Using MG5 binary from:\n", mg5_bin_path)
print("Saving MG5 outputs in directory:\n", outputs_dir)
print("Using", n_workers, "workers")
print("Using", n_events, "events per run")

# Set coupling parameters for the scan
params_dict = {
    # mg5_name: value
    "gu": 1.000000e-00,
    "betal33": 1.000000e00,
    "betard33": -1.000000e00,
    "betal23": 0.200000e00,
    "betal32": 0.000000e00,
    "kappau": 0.000000e00,
    "kappautilde": 0.000000e00,
}

# Set the mass range for the scan
m_min = 0.5
m_max = 3.5
step = 0.25
masses = np.arange(m_min, m_max + step, step)

# Declare the list to store the used seeds
seeds = []


def get_xs(mass: float):
    xs = calculate_cross_section(
        mass,
        params_dict,
        ufo_path,
        mg5_bin_path,
        outputs_dir,
        seeds,
        n_events,
        n_workers,
    )
    return (mass, xs)


results = list(map(get_xs, masses))

df = pd.DataFrame(results, columns=["mass", "xs"])

# Draw the results using ROOT
canva = ROOT.TCanvas("canva", "canva", 800, 600)
x, y = zip(*results)
gr = ROOT.TGraph(len(x), np.array(x), np.array(y))
gr.SetTitle("Cross section scan;Mass [TeV];Cross section [pb]")
gr.SetMarkerStyle(20)
gr.Draw("ALP")
legend = ROOT.TLegend(0.5, 0.7, 0.88, 0.9)
legend.AddEntry(gr, "non-resonant ditau production", "lp")
legend.Draw()  # Draw the legend
canva.SetLogy(1)  # Set y-axis to logarithmic scale
canva.Draw()
canva.SaveAs(os.path.join(plot_dir, "root_xs_plot.pdf"))

# Draw the results using matplotlib
x, y = zip(*results)
plt.plot(x, y, "o-", label="non-resonant ditau production")  # Add label to the plot
plt.xlabel("Mass [TeV]")
plt.ylabel("Cross section [pb]")
plt.yscale("log")  # Set y-axis to logarithmic scale
plt.title("Cross section scan")
plt.legend()  # Draw the legend
plt.savefig(os.path.join(plot_dir, "matplotlib_xs_plot.pdf"))
plt.show()


# Write a report
with open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "xs_report.txt"), "w") as f:
    # header
    f.write("=" * 80 + "\n")
    f.write("Cross section scan report\n")
    f.write("=" * 80 + "\n")
    # Settings
    f.write(f"UFO model path: {ufo_path}\n")
    f.write(f"MG5 binary path: {mg5_bin_path}\n")
    f.write(f"Outputs directory: {outputs_dir}\n")
    f.write(f"Number of workers: {n_workers}\n")
    f.write(f"Number of events per run: {n_events}\n")
    # Parameters
    f.write("Coupling parameters:\n")
    for k, v in params_dict.items():
        f.write(f"{k} = {v}\n")
    # Results
    f.write("Results:\n")
    f.write(df.to_string(index=False))
    f.write("\n")
    # Footer
    f.write("=" * 80 + "\n")

# Print the report
list(map(print, open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "xs_report.txt"))))
