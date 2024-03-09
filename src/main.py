import os
import pickle

import pandas as pd

from delphes_simulations import get_kinematics
from delphes_simulations import run_sims as run_simulations


def get_kinematics_df(output_dir: str) -> pd.DataFrame:
    print(f"Processing {output_dir}")
    parton_kinematics = get_kinematics(output_dir, kind="lhe")
    delphes_kinematics = get_kinematics(output_dir, kind="delphes")
    kinematics = parton_kinematics + delphes_kinematics
    return pd.DataFrame.from_records(kinematics)


def main():
    run_sims = False
    read_kinematics = False
    n_runs = 1
    if run_sims:
        outputs = run_simulations(n_runs)
        pickle.dump(outputs, open("outputs.pkl", "wb"))
    else:
        outputs = pickle.load(open("outputs.pkl", "rb"))
    data_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")
    os.makedirs(data_dir, exist_ok=True)
    if read_kinematics:
        for output in outputs:
            kinematics_df = get_kinematics_df(output)
            # Save the kinematics to a CSV file
            kinematics_df.to_csv(
                os.path.join(data_dir, os.path.basename(output) + ".csv"), index=False
            )
            # Save the kinematics to a excel file
            kinematics_df.to_excel(
                os.path.join(data_dir, os.path.basename(output) + ".xlsx"), index=False
            )
    else:
        # Graficar
        pass


if __name__ == "__main__":
    main()
