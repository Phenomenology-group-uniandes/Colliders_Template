import os

import numpy as np
from ROOT import TLorentzVector

from hep_pheno_tools.analysis_tools import get_kinematics_row
from hep_pheno_tools.delphes_reader.classifier import (
    get_good_jets,
    get_good_leptons,
    get_met,
)
from hep_pheno_tools.delphes_reader.loader import DelphesLoader
from hep_pheno_tools.lhe_reader.loader import LheLoader


def vis_mass_method(lead_tau: TLorentzVector, sub_tau: TLorentzVector) -> float:
    reco_tlv = lead_tau + sub_tau
    return reco_tlv.M()


def transverse_mass_method(
    lead_tau_p: TLorentzVector,
    sub_tau_p: TLorentzVector,
    met_p: TLorentzVector,
) -> float:
    reco_tlv = lead_tau_p + sub_tau_p + met_p
    return reco_tlv.Mt()


def collinear_approximation_method(
    lead_tau_p: TLorentzVector,
    sub_tau_p: TLorentzVector,
    met_p: TLorentzVector,
) -> float:
    et_x = met_p.Px()
    et_y = met_p.Py()

    s1c1 = np.sin(lead_tau_p.Theta()) * np.cos(lead_tau_p.Phi())
    s2c2 = np.sin(sub_tau_p.Theta()) * np.cos(sub_tau_p.Phi())
    s1s1 = np.sin(lead_tau_p.Theta()) * np.sin(lead_tau_p.Phi())
    s2s2 = np.sin(sub_tau_p.Theta()) * np.sin(sub_tau_p.Phi())

    # Solve et = A * p for p
    A = np.array(
        [
            [s1c1, s2c2],
            [s1s1, s2s2],
        ]
    )
    et = np.array([et_x, et_y])

    p = np.linalg.solve(A, et)
    pvis1 = lead_tau_p.P()
    pvis2 = sub_tau_p.P()
    x_1 = pvis1 / np.sqrt(pvis1 + p[0])
    x_2 = pvis2 / np.sqrt(pvis2 + p[1])
    return vis_mass_method(lead_tau_p, sub_tau_p) / np.sqrt(x_1 * x_2)


def missing_mass_method(
    lead_tau_p: TLorentzVector,
    sub_tau_p: TLorentzVector,
    met_p: TLorentzVector,
) -> float:
    # To do
    return 0.0


def get_kinematics(output_dir: str, kind: str = "delphes") -> list:
    if kind == "delphes":
        tree = DelphesLoader(os.path.basename(output_dir), path=output_dir).get_unfied_root_tree()
    elif kind == "lhe":
        tree = LheLoader(os.path.basename(output_dir), path=output_dir).get_unified_lhe_tree()
    else:
        raise ValueError("kind must be delphes or lhe")

    results = []
    for event in tree:
        if kind == "lhe":
            selection_kind = "partonic"
            met = event.getMissingET([-12, 12, -14, 14, -16, 16])
            taus = event.getParticlesByIDs([-15, 15])
            if len(taus) < 2:
                continue
            lead_tau = taus[0]
            sub_tau = taus[1]
        else:
            leptons = get_good_leptons(event)
            jets = get_good_jets(event)

            if len(leptons) == 2 and len(jets["tau_jet"]) == 0:
                selection_kind = "leptonic"
                lead_tau = leptons[0]
                sub_tau = leptons[1]
            elif len(jets["tau_jet"]) == 2 and len(leptons) == 0:
                selection_kind = "hadronic"
                lead_tau = jets["tau_jet"][0]
                sub_tau = jets["tau_jet"][1]
            elif len(leptons) == 1 and len(jets["tau_jet"]) == 1:
                selection_kind = "semileptonic"
                lead_tau = max(leptons[0], jets["tau_jet"][0], key=lambda x: x.pt)
                sub_tau = min(leptons[0], jets["tau_jet"][0], key=lambda x: x.pt)
            else:
                continue
            met = get_met(event)

        lead_tau.name = "tau_1"
        sub_tau.name = "tau_2"
        met.name = "met"

        row = get_kinematics_row([lead_tau, sub_tau, met])

        row["light-jet_multiplicity"] = len(jets["l_jet"]) if kind == "delphes" else 0

        row["b-jet_multiplicity"] = len(jets["b_jet"]) if kind == "delphes" else 0

        row["vis_mass"] = vis_mass_method(lead_tau.tlv, sub_tau.tlv)

        row["transverse_mass"] = transverse_mass_method(lead_tau.tlv, sub_tau.tlv, met.tlv)

        row["coll_approx"] = collinear_approximation_method(lead_tau.tlv, sub_tau.tlv, met.tlv)

        row["missing_mass"] = missing_mass_method(lead_tau.tlv, sub_tau.tlv, met.tlv)

        row["selection"] = selection_kind

        results.append(row)
    return results
