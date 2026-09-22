"""
=======================================================================
WISDOM ENGINE RUNTIME CORE (v0.6 ANTI-GLYPH SPECIFICATION)
=======================================================================
A localized, zero-dependency Python implementation of the Layer 5 
Discriminator Crucible. Programmatically scores candidate questions based 
on Bayesian probability updates and Shannon Entropy reduction.

Enforces strict compliance with the Surface Sufficiency Preservation rule.
=======================================================================
"""

import numpy as np
from dataclasses import dataclass
from typing import List, Dict

@dataclass(frozen=True)
class VisibleGlyphs:
    observations: List[str]
    surface_patterns: str

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
    glyphs: VisibleGlyphs
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
        print(f"INITIALISING WISDOM AGENT RUNTIME CORE v0.6")
        print(f"Scenario Focus: {self.title}")
        print(f"==========" + "="*45)

    def execute_simulation(self):
        # --- LAYER 1: SURFACE INTELLIGENCE ---
        print("\n[Layer 1: Surface Intelligence Active]")
        glyphs = VisibleGlyphs(
            observations=[
                "Internal engineering framework reported delayed.",
                "External legacy vendor engaged with double baseline budget.",
                "System architecture features systematically reduced.",
                "Total program expenditure increased by 100%."
            ],
            surface_patterns="Sequential failure -> Outsourcing -> Scope Reduction -> Cost Escalation."
        )
        for obs in glyphs.observations:
            print(f"  • Fact Node: {obs}")
        print(f"  • Extracted Systemic Pattern: {glyphs.surface_patterns}")

        # --- LAYER 2: BASELINE JUDGEMENT ---
        print("\n[Layer 2: Baseline Judgement Mapped]")
        conventional_play = (
            "Trigger a standard vendor performance audit. Re-verify internal milestones. "
            "Invoke contract liability clauses to freeze further scope degradation costs."
        )
        print(f"  • Standard Enterprise Action: {conventional_play}")

        # --- LAYERS 3 & 4: THE SHADOW PANTHEON CATALOGUE & SURFACE ENGAGEMENT ---
        print("\n[Layers 3 & 4: Wisdom² Archetypal Arbitration Matrix Generated]")
        # Hardcoding the strict integration of Hypothesis Omega alongside the Pantheon
        hypotheses = [
            Hypothesis("Incentives", "The Trickster", "Leadership structures reward external vendor capital allocation before year-end expiry.", "Audit trails reveal specific policy loopholes insulating external spend lines."),
            Hypothesis("Trust", "The Relationship", "Board maintains systemic doubt regarding internal delivery competency due to legacy failures.", "Internal memos reflect repeated requests for third-party institutional validation."),
            Hypothesis("Fear", "The Guardian", "Middle management avoids personal liability by prioritizing established, vetted market monoliths.", "Decision-making trail demonstrates excessive validation loops and defensive sign-offs."),
            Hypothesis("Omega (Surface Sufficiency)", "The Ground", "The visible explanation is adequate. Standard technical difficulties and scope adjustments explain the reality.", "Further empirical investigation fails to reveal hidden structural footprints or anomalies outside standard parameters.")
        ]
        
        for idx, h in enumerate(hypotheses, 1):
            print(f"  Model H{idx} [{h.domain}]: {h.name} -> *Predicts:* {h.predicted_footprint}")
        print("  *System Safeguard:* Anti-glyph clause validated. Hypothesis Omega integrated with uniform prior weight.")

        # --- LAYER 5: DISCRIMINATOR COMPETITION (THE CRUCIBLE) ---
        print("\n[Layer 5: Discriminator Competition Initialised]")
        num_h = len(hypotheses)
        
        # Question 1: Weak structural resolution
        q1 = CandidateQuestion(
            id=1,
            text="What specific internal milestones did the engineering team fail to reach before the vendor pivot?",
            outcome_labels=["Clear technical bottleneck", "Ambiguous data trail"],
            conditional_probabilities=np.array([
                [0.25, 0.25, 0.25, 0.25],  
                [0.25, 0.25, 0.25, 0.25]
            ])
        )
        
        # Question 2: High-entropy discriminator targeting the multi-vector prism split
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
                [0.05, 0.05, 0.05, 0.85],  # Outcome A: Separates strongly for Omega (Surface)
                [0.85, 0.05, 0.05, 0.05],  # Outcome B: Separates strongly for Incentives
                [0.05, 0.05, 0.85, 0.05],  # Outcome C: Separates strongly for Fear
                [0.05, 0.85, 0.05, 0.05]   # Outcome D: Separates strongly for Trust
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
            winning_q.outcome_labels[0]: "Hypothesis Omega (Surface Sufficiency) wins. No hidden dimension required.",
            winning_q.outcome_labels[1]: "Incentives (The Trickster Domain) handles the primary structural compression.",
            winning_q.outcome_labels[2]: "Fear (The Guardian Domain) handles the primary structural compression.",
            winning_q.outcome_labels[3]: "Trust (The Relationship Domain) handles the primary structural compression."
        }

        # --- LAYER 6: NAVIGATOR CARD GENERATION ---
        card = NavigatorCard(
            glyphs=glyphs,
            conventional_play=conventional_play,
            hypotheses=hypotheses,
            winning_question=winning_q.text,
            winning_score=highest_ig,
            diagnostic_matrix=diagnostic
        )

        self._render_navigator_card(card)

    def _render_navigator_card(self, card: NavigatorCard):
        print("\n" + "="*55)
        print("FINAL NAVIGATOR OUTPUT CARD (THE WISDOM COMPASS)")
        print("="*55)
        print(f"\n### 1. The Surface Stance")
        print(f"  Observations demonstrate: {card.glyphs.surface_patterns}")
        print(f"  Conventional operations would execute: {card.conventional_play}")
        
        print(f"\n### 2. Competing Architectural Explanations (The Pantheon Stance)")
        for h in card.hypotheses:
            print(f"  • Hypothesis [{h.name}]: *Predicts* -> {h.predicted_footprint}")
            
        print(f"\n### 3. The Maximum-URV Discriminator Question")
        print(f"  👉 \"{card.winning_question}\"")
        print(f"  [Calculated Information Gain Entropy Vector: {card.winning_score} bits]")
        
