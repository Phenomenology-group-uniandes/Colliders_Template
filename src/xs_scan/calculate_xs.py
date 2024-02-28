import os
import shutil
from io import StringIO
from subprocess import Popen

import pandas as pd

from hep_pheno_tools.madgraph_tools import get_new_seed


def calculate_xs(
    mass: float,
    params_dict: dict,
    ufo_path: str,
    mg5_bin_path: str,
    outputs_dir: str,
    seeds: list,
    n_events: int = 1000,
    n_workers: int = 2,
) -> float:
    """Get the cross section for a given mass and parameters.

    This function uses MG5 to calculate the cross section for a given mass and parameters.

    Parameters:

        mass: float
            The mass of the leptoquark in TeV
        params_dict: dict
            The dictionary containing the parameters to be used in the scan
        ufo_path: str
            The path to the UFO model
        mg5_bin_path: str
            The path to the MG5 binary
        outputs_dir: str
            The path to the directory where the outputs will be saved
        seeds: list
            The list of used seeds

    returns:
        float
            The cross section in pb
    """
    # Set the mass
    params_dict["mvlq"] = mass * 1e3  # TeV to GeV
    params_dict["wvlq"] = "auto"
    seed = get_new_seed(seeds)
    output = os.path.join(outputs_dir, f"xs_vlQ_{mass:.2f}TeV")
    try:
        os.makedirs(output, exist_ok=False)
    except FileExistsError:
        shutil.rmtree(output)
        os.makedirs(output, exist_ok=True)
    with open("process.mg5", "w") as f:
        # Create the process
        f.write(f"import model {ufo_path}\n")
        f.write("define p = p b b~\n")
        f.write("generate p p > ta+ ta- QED=0 QCD=0\n")
        f.write(f"output {output} -nojpeg\n")
        # Launch the process
        f.write(f"launch {output} -m\n")
        f.write(f"{n_workers}\n")
        # Set the param_card
        [f.write(f"set {key.upper()} {value}\n") for key, value in params_dict.items()]
        # Set the run_card
        f.write(f"set iseed {seed}\n")  # 0: let MG5 choose the seed
        f.write(f"set nevents {n_events}\n")
        f.write(f"set sde_strategy {1}\n")  # 1: use the exact matrix element (slow)
        f.write("done\n")
    # Run MG5
    Popen([mg5_bin_path, "process.mg5"]).wait()
    # copy the mg5 file to the output directory
    shutil.copy("process.mg5", output)

    # Get the cross section from the html file
    with open(os.path.join(output, "crossx.html")) as f:
        html_string = f.read()
    t = pd.read_html(StringIO(html_string))[0]
    try:
        xs = float(t["Cross section (pb)"][0].split(" ")[0])
    except ValueError:
        xs = 0.0
    return xs
