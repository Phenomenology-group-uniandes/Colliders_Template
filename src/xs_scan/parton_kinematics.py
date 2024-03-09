import os

import numpy as np
import pandas as pd
import ROOT

from hep_pheno_tools.lhe_reader import get_event_by_child, readLHEF

masses = np.array([0.5, 1.5, 2.5, 3.5])
colors = {
    # mass: color
    "0.5": ROOT.kRed,
    "1.5": ROOT.kBlue,
    "2.5": ROOT.kGreen,
    "3.5": ROOT.kBlack,
}
outputs_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "outputs")
print("Loading LHE outputs from directory:\n", outputs_dir)


def get_kinematics_df(mass: float) -> pd.DataFrame:
    """Get the kinematics of the final state particles for a given mass.

    Parameters:

        mass: float
            The mass of the leptoquark in TeV

    returns:
        pd.DataFrame
            The kinematics of the final state particles
    """
    # Load the ROOT file
    file_path = os.path.join(
        outputs_dir, f"xs_vlQ_{mass:.2f}TeV", "Events", "run_01", "unweighted_events.lhe.gz"
    )

    tree = list(map(get_event_by_child, readLHEF(file_path)))
    results = []
    for event in tree:
        kin_row = {}
        taus = event.getParticlesByIDs([-15, 15])

        if len(taus) != 2:
            continue
        leading_tau = taus[0]
        subleading_tau = taus[1]
        kin_row["leading_tau_pt"] = leading_tau.tlv.Pt()
        kin_row["leading_tau_eta"] = leading_tau.tlv.Eta()
        kin_row["leading_tau_phi"] = leading_tau.tlv.Phi()
        kin_row["leading_tau_energy"] = leading_tau.tlv.E()

        kin_row["subleading_tau_pt"] = subleading_tau.tlv.Pt()
        kin_row["subleading_tau_eta"] = subleading_tau.tlv.Eta()
        kin_row["subleading_tau_phi"] = subleading_tau.tlv.Phi()
        kin_row["subleading_tau_energy"] = subleading_tau.tlv.E()

        kin_row["reco_mass"] = (leading_tau.tlv + subleading_tau.tlv).M()
        kin_row["reco_pt"] = (leading_tau.tlv + subleading_tau.tlv).Pt()

        results.append(kin_row)
    df = pd.DataFrame.from_records(results)
    return df


# draw "reco_mass" for each mass in the same plot
observable = "reco_mass"
histos = []
for mass in masses:
    df = get_kinematics_df(mass)
    histo = ROOT.TH1F(f"{observable}_{mass:.2f}TeV", "", 50, 0, 2000)
    df[observable].apply(histo.Fill)
    histo.Scale(1 / histo.Integral())  # normalize
    histo.SetLineColor(colors[str(mass)])
    histo.SetLineWidth(2)
    histo.SetStats(False)
    histo.GetXaxis().SetTitle("Reconstructed mass [GeV]")
    histo.GetYaxis().SetTitle("a.u")
    histos.append(histo)
canva = ROOT.TCanvas("canva", "canva", 800, 600)
histos[0].Draw("hist")
for h in histos[1:]:
    h.Draw("hist same")
canva.Draw()
canva.BuildLegend()
canva.SaveAs(os.path.join(os.path.dirname(outputs_dir), "pdfs", "observable.pdf"))
