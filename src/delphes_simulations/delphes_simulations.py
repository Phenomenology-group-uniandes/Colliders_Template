import os
import shutil
from subprocess import Popen

import numpy as np

from hep_pheno_tools.madgraph_tools import get_new_seed

# Set coupling parameters for the scan
params_dict = {
    # mg5_name: value
    "gu": 1.0,
    "betal33": 1.0,
    "betard33": -1.0,
    "betal23": 0.2,
    "betal32": 0.0,
    "kappau": 0.0,
    "kappautilde": 0.0,
}

# Set the mass range for the scan
m_min = 0.5
m_max = 3.5
step = 0.5
masses = np.arange(m_min, m_max + step, step)
n_workers = 4
seeds = []


# Set the paths
ufo_path = os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "model", "vLQ_UFO"
)
mg5_bin_path = os.path.join(os.sep, "Collider", "MG5_aMC_v3_1_0", "bin", "mg5_aMC")
pythia_card = os.path.join(os.path.dirname(os.path.dirname(__file__)), "pythia8_card.dat")
outputs_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "outputs")
os.makedirs(outputs_dir, exist_ok=True)


def create_output(title: str, ufo_path: str, mg5_bin_path: str, outputs_dir: str) -> float:
    output = os.path.join(outputs_dir, f"{title}")
    file_name = "proc_comand.mg5"
    try:
        os.makedirs(output, exist_ok=False)
    except FileExistsError:
        shutil.rmtree(output)
        os.makedirs(output, exist_ok=True)
    with open(file_name, "w") as f:
        # Create the process
        f.write(f"import model {ufo_path}\n")
        f.write("define p = p b b~\n")
        f.write("generate p p > ta+ ta- QED=0 QCD=0\n")
        f.write(f"output {output} -nojpeg\n")
    Popen([mg5_bin_path, file_name]).wait()
    shutil.copy("proc_comand.mg5", os.path.join(output, "proc_comand.mg5"))
    return output


def launch_process(
    mass: float,
    params_dict: dict,
    mg5_bin_path: str,
    output_dir: str,
    seeds: list,
    pythia8_card_path: str = None,
    delphes_card_path: str = None,
    n_events: int = 50000,
    n_workers: int = 4,
) -> float:
    params_dict["mvlq"] = mass * 1e3  # TeV to GeV
    params_dict["wvlq"] = "auto"
    seed = get_new_seed(seeds)
    file_name = "settings.mg5"
    with open(file_name, "w") as f:
        f.write(f"launch {output_dir} -m\n")
        f.write(f"{n_workers}\n")
        f.write("SHOWER=Pythia8\n")
        f.write("DETECTOR=Delphes\n")
        f.write("done\n")
        f.write(f"set seed {seed}\n")
        f.write(f"set nevents {n_events}\n")
        f.write(f"set sde_strategy {1}\n")
        [f.write(f"set {key.upper()} {value}\n") for key, value in params_dict.items()]
        if pythia8_card_path:
            f.write(f"{pythia8_card_path}\n")
            if delphes_card_path:
                f.write(f"{delphes_card_path}\n")
        f.write("done\n")
    Popen([mg5_bin_path, file_name]).wait()
    shutil.copy(file_name, os.path.join(output_dir, "settings.mg5"))
    return seed


def full_sim(n_runs: int):

    def run_mass(mass: float):
        output = create_output(f"delphes_vlQ_{mass:.2f}TeV", ufo_path, mg5_bin_path, outputs_dir)
        for _ in range(n_runs):
            launch_process(
                mass,
                params_dict,
                mg5_bin_path,
                output,
                seeds,
                pythia8_card_path=pythia_card,
                n_workers=n_workers,
            )

        return output

    return list(map(run_mass, masses))
