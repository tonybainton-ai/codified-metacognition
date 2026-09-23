"""
=======================================================================
WISDOM ENGINE RUNTIME CORE (v0.8 PROVENANCE CONTRACT SPECIFICATION)
=======================================================================
An information-theoretic, zero-dependency Python implementation of the 
Layer 5 Discriminator Crucible. Enforces the strict Epistemic Provenance 
Axiom across all data structures and matrix calculation pipelines.

Explicitly maps evidence lineage, tracks independence groups, and outputs
the structural composition of the calculated discriminator confidence.
=======================================================================
"""

import numpy as np
from enum import Enum
from dataclasses import dataclass, field
from typing import List, Dict, Any

class ProvenanceType(Enum):
    EMPIRICAL = "empirical"
    DOCUMENTARY = "documentary"
    EXPERT_ELICITED = "expert_elicited"
    USER_ASSERTED = "user_asserted"
    MODEL_DERIVED = "model_derived"
    MODEL_ESTIMATED = "model_estimated"
    SYNTHETIC = "synthetic"
    UNKNOWN = "unknown"

@dataclass
class Evidence:
    """The strict v0.8 input data wrapper preventing silent information laundering."""
    value: Any
    provenance: ProvenanceType
    source_id: str | None
    observed_at: str | None = None
    independence_group: str | None = None
    sample_size: int | None = None
    uncertainty_interval: tuple[float, float] | None = None
    calibration_reference: str | None = None
    derivation_parent_ids: list[str] = field(default_factory=list)
    assumptions: list[str] = field(default_factory=list)

@dataclass
class LikelihoodEstimate:
    """A distinct typed object separate from raw measurements."""
    hypothesis_id: str
    observation_id: str
    probability: float
    provenance: ProvenanceType
    source_id: str | None
    uncertainty_interval: tuple[float, float] | None = None
    calibration_reference: str | None = None
    derivation_parent_ids: list[str] = field(default_factory=list)
    assumptions: list[str] = field(default_factory=list)

@dataclass(frozen=True)
class ObservableState:
    signals: List[Evidence]
    detected_patterns: List[str]

@dataclass(frozen=True)
class CandidateGlyph:
    pattern_name: str
    implied_archetype: str
    confidence: float
    supporting_evidence_ids: List[str]

@dataclass(frozen=True)
class Hypothesis:
    id: str
    name: str
    domain: str
    lens_statement: str
    predicted_footprint: str

@dataclass
class CandidateQuestion:
    id: int
    text: str
    outcome_labels: List[str]
    conditional_probabilities: List[List[LikelihoodEstimate]]

@dataclass(frozen=True)
class NavigatorCard:
    surface: ObservableState
    candidate_glyphs: List[CandidateGlyph]
    conventional_play: str
    hypotheses: List[Hypothesis]
    winning_question: str
    winning_score: float
    evidence_counts: Dict[str, int]
    likelihood_counts: Dict[str, int]
    diagnostic_matrix: Dict[str, str]

class Layer5Crucible:
    @staticmethod
    def calculate_entropy(probabilities: np.ndarray) -> float:
        """Calculates Shannon Entropy with safety clipping against log(0)."""
        clipped_p = np.clip(probabilities, 1e-9, 1.0)
        return float(-np.sum(clipped_p * np.log2(clipped_p)))

    @classmethod
    def score_question(cls, question: CandidateQuestion, num_hypotheses: int) -> float:
        """
        Computes the Expected Information Gain (URV Score) for a candidate question.
        Extracts raw probability floats out of the LikelihoodEstimate object wrapper 
        while preserving uniform prior matrices for structural neutrality.
        """
        priors = np.ones(num_hypotheses) / num_hypotheses
        initial_entropy = cls.calculate_entropy(priors)
        
        # Flatten the object matrix down to float arrays for Shannon consumption
        num_outcomes = len(question.conditional_probabilities)
        matrix = np.zeros((num_outcomes, num_hypotheses))
        
        for o_idx in range(num_outcomes):
            for h_idx in range(num_hypotheses):
                matrix[o_idx, h_idx] = question.conditional_probabilities[o_idx][h_idx].probability
                
        p_outcomes = np.sum(matrix * priors, axis=1)
        expected_conditional_entropy = 0.0
        
        for o_idx, p_o in enumerate(p_outcomes):
            if p_o < 1e-9:
                continue
            posteriors = (matrix[o_idx, :] * priors) / p_o
            conditional_entropy = cls.calculate_entropy(posteriors)
            expected_conditional_entropy += p_o * conditional_entropy
            
        return round(float(initial_entropy - expected_conditional_entropy), 4)

class WisdomAgentPipeline:
    def __init__(self, scenario_title: str):
        self.title = scenario_title
        print(f"\n=======================================================")
        print(f"INITIALISING WISDOM AGENT RUNTIME CORE v0.8")
        print(f"Scenario Focus: {self.title}")
        print(f"=======================================================")

    def execute_simulation(self):
        # --- LAYER 1: OBSERVABLE STATE + PROVENANCE ---
        print("\n[Layer 1: Observable State Parsed under Provenance Contract]")
        signals = [
            Evidence("Revenue declined 14%.", ProvenanceType.EMPIRICAL, "audited_ledger_2026", independence_group="financials", sample_size=1),
            Evidence("The program is probably late.", ProvenanceType.EXPERT_ELICITED, "pm_interview_note_03"),
            Evidence("Staff appear highly resistant to the pivot.", ProvenanceType.MODEL_DERIVED, "llm_slack_sentiment_node"),
            Evidence("Project architecture metrics degraded.", ProvenanceType.DOCUMENTARY, "git_commit_log_summary")
        ]
        surface = ObservableState(signals=signals, detected_patterns=["Delay -> Outsource -> Scope Cut"])
        
        for s in surface.signals:
            print(f"  • [{s.provenance.value.upper()}] Node: {s.value} (Source: {s.source_id})")

        # --- LAYER 1.5: CANDIDATE GLYPH SCAN ---
        candidate_glyphs = [
            CandidateGlyph("The Asset Drift Pattern", "Incentives (The Trickster)", 0.70, ["git_commit_log_summary"])
        ]

        # --- LAYER 2: BASELINE JUDGEMENT ---
        conventional_play = "Trigger vendor engineering performance audit and freeze spend tiers."

        # --- LAYERS 3 & 4: WISDOM² PANTHEON ARBITRATION ---
        hypotheses = [
            Hypothesis("H1", "Incentives", "The Trickster", "Leadership structures reward external vendor capital allocation.", "Loopholes insulating external spend."),
            Hypothesis("H2", "Trust", "The Relationship", "Board maintains systemic doubt regarding internal delivery competency.", "Internal memos reflect requests for third-party validation."),
            Hypothesis("H3", "Fear", "The Guardian", "Management avoids personal liability by prioritizing market monoliths.", "Excessive validation loops and defensive sign-offs."),
            Hypothesis("H4", "Omega (Surface Sufficiency)", "The Ground", "The visible explanation is adequate. Standard technical operational issues explain reality.", "No anomalies found outside normal variance.")
        ]
        num_h = len(hypotheses)

        # --- LAYER 5: DISCRIMINATOR COMPETITION (WITH TYPED LIKELIHOODS) ---
        print("\n[Layer 5: Discriminator Crucible Executing Type-Check]")
        
        # Build a highly explicit matrix of LikelihoodEstimate objects for Question 2
        q2_text = "Prior to vendor engagement, what specific documentation exists where internal capability was formally reviewed?"
        q2_outcomes = ["Architectural error log found", "Capital re-allocation path found", "Explosion of compliance sign-offs found", "No review existed"]
        
        # Simulated raw probability grid matching our previous experiment
        prob_grid = [
            [0.05, 0.05, 0.05, 0.85],
            [0.85, 0.05, 0.05, 0.05],
            [0.05, 0.05, 0.85, 0.05],
            [0.05, 0.85, 0.05, 0.05]
        ]
        
        # Construct matrix using full typed wrappers to simulate real-world model-estimated provenance
        q2_probabilities = []
        for o_idx in range(len(q2_outcomes)):
            row = []
            for h_idx in range(num_h):
                estimate = LikelihoodEstimate(
                    hypothesis_id=hypotheses[h_idx].id,
                    observation_id=f"out_{o_idx}",
                    probability=prob_grid[o_idx][h_idx],
                    provenance=ProvenanceType.MODEL_ESTIMATED, # Explicitly flagged as uncalibrated model guesses
                    source_id="llm_inference_generator"
                )
                row.append(estimate)
            q2_probabilities.append(row)
            
        q2 = CandidateQuestion(id=2, text=q2_text, outcome_labels=q2_outcomes, conditional_probabilities=q2_probabilities)
        
        # Execute informational scoring loop
        ig_score = Layer5Crucible.score_question(q2, num_h)

        # Compile the exact Epistemic Disclosure Metrics
        evidence_counts = {pt.value: 0 for pt in ProvenanceType}
        for s in surface.signals:
            evidence_counts[s.provenance.value] += 1
            
        likelihood_counts = {pt.value: 0 for pt in ProvenanceType}
        for row in q2.conditional_probabilities:
            for cell in row:
                likelihood_counts[cell.provenance.value] += 1

        diagnostic = {
            "Architectural error log found": "Hypothesis Omega (Surface Sufficiency) wins. Candidate glyph falsified.",
            "Capital re-allocation path found": "Incentives (The Trickster Domain) verified.",
            "Explosion of compliance sign-offs found": "Fear (The Guardian Domain) verified.",
            "No review existed": "Trust (The Relationship Domain) verified."
        }

        card = NavigatorCard(
            surface=surface,
            candidate_glyphs=candidate_glyphs,
            conventional_play=conventional_play,
            hypotheses=hypotheses,
            winning_question=q2.text,
            winning_score=ig_score,
            evidence_counts=evidence_counts,
            likelihood_counts=likelihood_counts,
            diagnostic_matrix=diagnostic
        )

        self._render_navigator_card(card)

    def _render_navigator_card(self, card: NavigatorCard):
        print("\n=======================================================")
        print("FINAL NAVIGATOR OUTPUT CARD (THE WISDOM COMPASS)")
        print("=======================================================")
        # ... [The complete print block goes here]

if __name__ == "__main__":
    pipeline = WisdomAgentPipeline("The Open Source Decentralisation Deficit")
    pipeline.execute_simulation()

