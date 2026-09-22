"""
=======================================================================
WISDOM ENGINE RUNTIME CORE (v0.7 POPPERIAN FALSIFICATION ARCHITECTURE)
=======================================================================
An information-theoretic, zero-dependency Python implementation of the 
Layer 5 Discriminator Crucible. Evaluates candidate questions by measuring 
their expected Shannon Entropy reduction across competing models.

Enforces strict compliance with the Surface Sufficiency Preservation rule,
subjecting candidate glyphs to rigorous adversarial falsification.
=======================================================================
"""

import numpy as np
from dataclasses import dataclass
from typing import List, Dict

@dataclass(frozen=True)
class ObservableState:
    raw_signals: List[str]
    detected_patterns: List[str]

@dataclass(frozen=True)
class CandidateGlyph:
    """
    A structural pattern detected in the surface signals.
    Crucially: Candidate Glyph != Proven Glyph. It must earn its
    validity by demonstrating explanatory power beyond coincidence.
    """
    pattern_name: str
    implied_archetype: str
    confidence: float
    supporting_evidence: List[str]

@dataclass(frozen=True)
class Hypothesis:
    name: str
    domain: str
    lens_statement: str
    predicted_footprint: str

@dataclass(frozen=True)
class CandidateQuestion:
    id: int
    text: str
    outcome_labels: List[str]
    conditional_probabilities: np.ndarray  # Shape: (num_outcomes, num_hypotheses)

@dataclass(frozen=True)
class NavigatorCard:
    surface: ObservableState
    candidate_glyphs: List[CandidateGlyph]
    conventional_play: str
    hypotheses: List[Hypothesis]
    winning_question: str
    winning_score: float
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
        Enforces uniform prior probabilities to maintain absolute structural neutrality,
        ensuring Hypothesis Omega sits on equal footing with archetypal models.
        """
        priors = np.ones(num_hypotheses) / num_hypotheses
        initial_entropy = cls.calculate_entropy(priors)
        
        matrix = question.conditional_probabilities
        
        # Calculate marginal probability of each outcome: P(O) = Sum_h [ P(O|H) * P(H) ]
        p_outcomes = np.sum(matrix * priors, axis=1)
        
        expected_conditional_entropy = 0.0
        
        for o_idx, p_o in enumerate(p_outcomes):
            if p_o < 1e-9:
                continue
            # Bayes' Theorem: P(H|O) = [ P(O|H) * P(H) ] / P(O)
            posteriors = (matrix[o_idx, :] * priors) / p_o
            conditional_entropy = cls.calculate_entropy(posteriors)
            expected_conditional_entropy += p_o * conditional_entropy
            
        information_gain = initial_entropy - expected_conditional_entropy
        return round(float(information_gain), 4)

class WisdomAgentPipeline:
    def __init__(self, scenario_title: str):
        self.title = scenario_title
        print(f"\n" + "="*55)
        print(f"INITIALISING WISDOM AGENT RUNTIME CORE v0.7")
        print(f"Scenario Focus: {self.title}")
        print(f"==========" + "="*45)

    def execute_simulation(self):
        # --- LAYER 1: SURFACE INTELLIGENCE ---
        print("\n[Layer 1: Observable State Parsed]")
        surface = ObservableState(
            raw_signals=[
                "Internal engineering framework reported delayed.",
                "External legacy vendor engaged with double baseline budget.",
                "System architecture features systematically reduced.",
                "Total program expenditure increased by 100%."
            ],
            detected_patterns=[
                "Delay -> Outsource -> Scope Cut -> Cost Spike"
            ]
        )
        for sig in surface.raw_signals:
            print(f"  • Signal Node: {sig}")

        # --- NEW v0.7 GLYPH SCANNING ENGINE ---
        print("\n[Layer 1.5: Candidate Glyph Detection Engine]")
        # Patterns are detected but intentionally denied status as objective truth
        candidate_glyphs = [
            CandidateGlyph(
                pattern_name="The Institutional Escape Route",
                implied_archetype="Incentives (The Trickster)",
                confidence=0.75,
                supporting_evidence=["Concurrently reduced scope alongside skyrocketing vendor costs."]
            )
        ]
        for cg in candidate_glyphs:
            print(f"  • Scan Result: Found Candidate Glyph '{cg.pattern_name}' (Implied: {cg.implied_archetype})")
            print(f"    *Epistemological Warning:* Candidate Glyph != Proven Glyph. Submitting to falsification testing.")

        # --- LAYER 2: BASELINE JUDGEMENT ---
        print("\n[Layer 2: Baseline Judgement Mapped]")
        conventional_play = (
            "Trigger a standard vendor performance audit. Re-verify internal milestones. "
            "Invoke contract liability clauses to freeze further scope degradation costs."
        )
        print(f"  • Standard Enterprise Action: {conventional_play}")

        # --- LAYERS 3 & 4: WISDOM² PANTHEON ARBITRATION ---
        print("\n[Layers 3 & 4: Wisdom² Competitor Matrix Initialised]")
        # Enforcing uniform 25% priors across all four models to anchor neutrality
        hypotheses = [
            Hypothesis("Incentives", "The Trickster", "Leadership structures reward external vendor capital allocation before year-end expiry.", "Audit trails reveal specific policy loopholes insulating external spend lines."),
            Hypothesis("Trust", "The Relationship", "Board maintains systemic doubt regarding internal delivery competency due to legacy failures.", "Internal memos reflect repeated requests for third-party institutional validation."),
            Hypothesis("Fear", "The Guardian", "Middle management avoids personal liability by prioritizing established, vetted market monoliths.", "Decision-making trail demonstrates excessive validation loops and defensive sign-offs."),
            Hypothesis("Omega (Surface Sufficiency)", "The Ground", "The visible explanation is adequate. Standard technical difficulties and scope adjustments explain the reality.", "Further empirical investigation fails to reveal hidden structural footprints or anomalies outside standard parameters.")
        ]
        
        for idx, h in enumerate(hypotheses, 1):
            print(f"  Model H{idx} [{h.domain}]: {h.name} Prior -> 25.0% (Equilibrium Matrix Locked)")

        # --- LAYER 5: DISCRIMINATOR COMPETITION (THE CRUCIBLE) ---
        print("\n[Layer 5: Discriminator Competition Initialised]")
        num_h = len(hypotheses)
        
        # Question 1: Poor entropy separation
        q1 = CandidateQuestion(
            id=1,
            text="What specific internal milestones did the engineering team fail to reach before the vendor pivot?",
            outcome_labels=["Clear technical bottleneck", "Ambiguous data trail"],
            conditional_probabilities=np.array([
                [0.25, 0.25, 0.25, 0.25],  
                [0.25, 0.25, 0.25, 0.25]
            ])
        )
        
        # Question 2: The Multi-Vector Prism (Forces sharp outcome branching)
        q2 = CandidateQuestion(
            id=2,
            text="Prior to vendor engagement, what specific documentation exists where internal capability was formally reviewed, and did that result in increased sign-offs, a shift in capital funding channels, or a verified log of structural errors?",
            outcome_labels=[
                "Forced review resulting in standard architectural error log", 
                "Forced review with rapid capital re-allocation", 
                "Forced review with sudden explosion of compliance sign-offs", 
                "No formal review or data trail existed"
            ],
            conditional_probabilities=np.array([
                [0.05, 0.05, 0.05, 0.85],  # Outcome A: Separates strongly for Omega (Falsifies archetypes)
                [0.85, 0.05, 0.05, 0.05],  # Outcome B: Confirms Incentives Glyph
                [0.05, 0.05, 0.85, 0.05],  # Outcome C: Confirms Fear Glyph
                [0.05, 0.85, 0.05, 0.05]   # Outcome D: Confirms Trust Glyph
            ])
        )

        candidates = [q1, q2]
        winning_q = None
        highest_ig = -1.0
        
        print("  Scoring questions based on Expected Information Gain (Entropy Reduction Variance)...")
        for q in candidates:
            ig_score = Layer5Crucible.score_question(q, num_h)
            print(f"    -> Candidate Question {q.id} URV Capacity: {ig_score} bits")
            if ig_score > highest_ig:
                highest_ig = ig_score
                winning_q = q

        # Map diagnostic pathways for the winner card
        diagnostic = {
            winning_q.outcome_labels: "Hypothesis Omega (Surface Sufficiency) wins. The candidate glyph is falsified.",
            winning_q.outcome_labels: "Incentives (The Trickster Domain) verified. The candidate glyph transitions to a proven structural element.",
            winning_q.outcome_labels: "Fear (The Guardian Domain) verified. The candidate glyph transitions to a proven structural element.",
            winning_q.outcome_labels: "Trust (The Relationship Domain) verified. The candidate glyph transitions to a proven structural element."
        }

        # --- LAYER 6: NAVIGATOR CARD GENERATION ---
        card = NavigatorCard(
            surface=surface,
