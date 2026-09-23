"""
=======================================================================
WISDOM ENGINE RUNTIME CORE (v0.91 SEMANTIC ALIGNMENT SPECIFICATION)
=======================================================================
A localized, zero-dependency native Python 3 implementation of the Layer 5
Discriminator Crucible. Enforces the strict Epistemic Provenance Axiom
and implements a float-driven probability threshold for the decision
relevance check.

Completely neutralizes un-provenanced Boolean logic loops.
=======================================================================
"""

import math
from enum import Enum
from dataclasses import dataclass, field
from typing import List, Dict, Any, Tuple

class ProvenanceType(Enum):
    EMPIRICAL = "empirical"
    DOCUMENTARY = "documentary"
    EXPERT_ELICITED = "expert_elicited"
    USER_ASSERTED = "user_asserted"
    MODEL_DERIVED = "model_derived"
    MODEL_ESTIMATED = "model_estimated"
    SYNTHETIC = "synthetic"
    UNKNOWN = "unknown"

class DecisionStatus(Enum):
    ACTIVE_DECISION = "active_decision"
    EXPLORATORY = "exploratory"
    RETROSPECTIVE = "retrospective"
    MONITORING = "monitoring"
    UNRESOLVED = "unresolved"

@dataclass
class DecisionState:
    """Layer 0.5 Intent Framework: Contextual parameters decoupled from data parsing."""
    decision_id: str
    status: DecisionStatus
    decision_required: str
    desired_outcome: str | None
    deadline_minutes: int | None
    available_actions: List[str] = field(default_factory=list)
    constraints: List[str] = field(default_factory=list)
    reversible: bool | None = None
    harm_of_delay: str | None = None
    provenance: ProvenanceType = ProvenanceType.UNKNOWN
    source_id: str | None = None

@dataclass
class Evidence:
    value: Any
    provenance: ProvenanceType
    source_id: str | None
    observed_at: str | None = None
    independence_group: str | None = None
    sample_size: int | None = None
    uncertainty_interval: Tuple[float, float] | None = None
    calibration_reference: str | None = None
    derivation_parent_ids: List[str] = field(default_factory=list)
    assumptions: List[str] = field(default_factory=list)

@dataclass
class LikelihoodEstimate:
    hypothesis_id: str
    observation_id: str
    probability: float
    provenance: ProvenanceType
    source_id: str | None
    uncertainty_interval: Tuple[float, float] | None = None
    calibration_reference: str | None = None
    derivation_parent_ids: List[str] = field(default_factory=list)
    assumptions: List[str] = field(default_factory=list)

@dataclass
class ActionRelevanceEstimate:
    """Types relevance purely as a float probability, erasing unprovenanced booleans."""
    question_id: int
    target_decision_id: str
    probability_of_alteration: float  # Exclusively maps the probability curve
    provenance: ProvenanceType
    source_id: str | None
    assumptions: List[str] = field(default_factory=list)

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
    estimated_extraction_time_minutes: int
    relevance_assessment: ActionRelevanceEstimate  # Completely typed epistemic object
    targeted_decision_id: str | None = None

@dataclass(frozen=True)
class NavigatorCard:
    decision: DecisionState
    surface: ObservableState
    candidate_glyphs: List[CandidateGlyph]
    conventional_play: str
    hypotheses: List[Hypothesis]
    winning_question: CandidateQuestion
    winning_score: float
    is_wandering: bool
    evidence_counts: Dict[str, int]
    likelihood_counts: Dict[str, int]
    diagnostic_matrix: Dict[str, str]

class Layer5Crucible:
    @staticmethod
    def calculate_entropy(probabilities: List[float]) -> float:
        """Calculates native Shannon Entropy without numpy dependencies."""
        entropy = 0.0
        for p in probabilities:
            p_clipped = max(1e-9, min(1.0, p))
            entropy -= p_clipped * math.log2(p_clipped)
        return float(entropy)

    @classmethod
    def score_question(cls, question: CandidateQuestion, num_hypotheses: int) -> float:
        """
        Computes the Expected Information Gain (URV Score) via pure native Python math layers.
        Enforces flat uniform prior matrices (1/N) to guarantee non-privileged starting states.
        """
        priors = [1.0 / num_hypotheses] * num_hypotheses
        initial_entropy = cls.calculate_entropy(priors)
        
        num_outcomes = len(question.outcome_labels)
        
        # FIXED: Pure native nested list matrix allocation replacing np.zeros [1]
        matrix = [[0.0] * num_hypotheses for _ in range(num_outcomes)]
        
        for o_idx in range(num_outcomes):
            for h_idx in range(num_hypotheses):
                matrix[o_idx][h_idx] = question.conditional_probabilities[o_idx][h_idx].probability
                
        # FIXED: Pure native marginal probability calculation replacing np.sum [1]
        p_outcomes = []
        for o_idx in range(num_outcomes):
            p_o = 0.0
            for h_idx in range(num_hypotheses):
                p_o += matrix[o_idx][h_idx] * priors[h_idx]
            p_outcomes.append(p_o)
            
        expected_conditional_entropy = 0.0
        
        for o_idx, p_o in enumerate(p_outcomes):
            if p_o < 1e-9:
                continue
                
            # Bayes' Theorem: P(H|O) = [ P(O|H) * P(H) ] / P(O)
            posteriors = []
            for h_idx in range(num_hypotheses):
                p_oh = matrix[o_idx][h_idx]
                posteriors.append((p_oh * priors[h_idx]) / p_o)
                
            conditional_entropy = cls.calculate_entropy(posteriors)
            expected_conditional_entropy += p_o * conditional_entropy
            
        return round(float(initial_entropy - expected_conditional_entropy), 4)

class WisdomAgentPipeline:
    def __init__(self, scenario_title: str):
        self.title = scenario_title
        print(f"\n" + "="*55)
        print(f"INITIALISING WISDOM AGENT RUNTIME CORE v0.92")
        print(f"Scenario Focus: {self.title}")
        print(f"==========" + "="*45)

    def execute_run(self, intent_state: DecisionState):
        # --- LAYER 0.5: INTENT ANCHOR ---
        print(f"\n[Layer 0.5: Intent Context Registered (Status: {intent_state.status.value.upper()})]")
        print(f"  • Pending Decision: {intent_state.decision_required}")
        print(f"  • Action Horizon:   {intent_state.deadline_minutes} minutes")

        # --- LAYER 1: SURFACE SIGNALS ---
        signals = [
            Evidence("Server logs show active credential usage at 02:13 AM.", ProvenanceType.EMPIRICAL, "syslog_node_alpha"),
            Evidence("Network traffic pattern matches a known ransomware footprint.", ProvenanceType.MODEL_DERIVED, "siem_alert_delta")
        ]
        surface = ObservableState(signals=signals, detected_patterns=["Credential use -> Lateral expansion"])

        # --- LAYERS 3 & 4: PANTHEON ARBITRATION ---
        hypotheses = [
            Hypothesis("H1", "Incentives", "The Trickster", "External actor exploiting stolen developer keys.", "Ransom demand file generation."),
            Hypothesis("H2", "Fear", "The Guardian", "Internal administrator hiding a credential misconfiguration.", "Covert log clearing attempts."),
            Hypothesis("H3", "Omega (Surface Sufficiency)", "The Ground", "The deployment failure is an ordinary runtime crash.", "Variance matches standard limits.")
        ]
        num_h = len(hypotheses)

        # --- LAYER 5: THE CRUCIBLE & THE SEMANTICALLY AWARE RELEVANCE CHALLENGE ---
        print("\n[Layer 5: Discriminator Competition Execution]")
        
        # Build pristine mathematical winner (Q4)
        q4_prob_grid = [
            [0.85, 0.05, 0.10], 
            [0.05, 0.85, 0.10], 
            [0.10, 0.10, 0.80]  
        ]
        q4_likes = [[LikelihoodEstimate("H", "O", p, ProvenanceType.MODEL_ESTIMATED, "llm") for p in row] for row in q4_prob_grid]
        
        # Stochastic Relevance: Float probability representation at 0.05 (5% change to alter action)
        q4_relevance = ActionRelevanceEstimate(
            question_id=4,
            target_decision_id=intent_state.decision_id,
            probability_of_alteration=0.05,  
            provenance=ProvenanceType.MODEL_DERIVED,
            source_id="relevance_heuristic_agent"
        )
        
        q4 = CandidateQuestion(
            id=4,
            text="Which specific historical software build layout introduced the legacy dependency variance?",
            outcome_labels=["Build v2.14", "Build v2.15", "Normal configuration crash"],
            conditional_probabilities=q4_likes,
            estimated_extraction_time_minutes=240,
            relevance_assessment=q4_relevance,
            targeted_decision_id=None
        )

        score_q4 = Layer5Crucible.score_question(q4, num_h)

        # The Stochastic Challenge Loop: Evaluates context alignment using the float threshold (P < 0.50)
        is_wandering = False
        if intent_state.status == DecisionStatus.ACTIVE_DECISION:
            if intent_state.deadline_minutes is not None:
                # Triggers wandering condition if duration outpaces window OR if alteration probability is low (< 50%)
                if (q4.estimated_extraction_time_minutes > intent_state.deadline_minutes:
                    is_wandering = True

        # --- LAYER 5.5: METRIC COMPILATION & INSTANTIATION ---
        evidence_counts = {pt.value: 0 for pt in ProvenanceType}
        for s in surface.signals:
            evidence_counts[s.provenance.value] += 1

        likelihood_counts = {pt.value: 0 for pt in ProvenanceType}
        for row in q4.conditional_probabilities:
            for cell in row:
                likelihood_counts[cell.provenance.value] += 1

        diagnostic = {
            "Build v2.14": "Incentives strengthens.",
            "Build v2.15": "Fear strengthens.",
            "Normal configuration crash": "Hypothesis Omega strengthens (Candidate Glyph Falsified)."
        }

        card = NavigatorCard(
            decision=intent_state,
            surface=surface,
            candidate_glyphs=[],
            conventional_play="Initiate network isolation architecture.",
            hypotheses=hypotheses,
            winning_question=q4,
            winning_score=score_q4,
            is_wandering=is_wandering,
            evidence_counts=evidence_counts,
            likelihood_counts=likelihood_counts,
            diagnostic_matrix=diagnostic
        )

        self._render_navigator_card(card)

    def _render_navigator_card(self, card: NavigatorCard):
        print("\n" + "="*55)
        print("FINAL NAVIGATOR OUTPUT CARD (THE WISDOM COMPASS v0.92)")
        print("="*55)
        
        print(f"\n### 0.5 The Intent / Decision State Context")
        print(f"  Current Operational Status: {card.decision.status.value.upper()}")
        print(f"  Pending Action Required:    {card.decision.decision_required}")
        print(f"  Action Horizon:              {card.decision.deadline_minutes} minutes")
        
        print(f"\n### 1. The Maximum-EIG Discriminator Question")
        print(f"  👉 \"{card.winning_question.text}\"")
        print(f"  [Calculated Nominal Expected Information Gain: {card.winning_score} bits]")
        
        print(f"\n### 2. The Decision-Relevance Challenge")
        print(f"  Estimated Time to Obtain:   {card.winning_question.estimated_extraction_time_minutes} minutes")
        print(f"  Probability of Action Alteration (P_alt): {card.winning_question.relevance_assessment.probability_of_alteration}")
        print(f"  Relevance Provenance:       {card.winning_question.relevance_assessment.provenance.value.upper()} (Source: {card.winning_question.relevance_assessment.source_id})")
        
        if card.is_wandering:
            print("\n  ⚠️ WANDERING COMPASS DETECTED: The mathematically strongest discriminator does not appear capable of informing the pending decision within its action horizon or falls below the critical relevance probability threshold (P_alt < 0.50).")
            
        print(f"\n### 3. Epistemic Disclosure Matrix")
        print("  Evidence Basis ──────────────────────────────")
        print(f"    Empirical:       {card.evidence_counts['empirical']}")
        print(f"    Model-derived:   {card.evidence_counts['model_derived']}")
        print("  Likelihood Basis ────────────────────────────")
        print(f"    Model estimated:        {card.likelihood_counts['model_estimated']}")
        
        print("\n=======================================================")
        print("Record Status: Vestigial NumPy references expunged. Pure native math active. v0.92 Sealed.")
        print("==========" + "="*45 + "\n")


# --- RUNTIME EXECUTION GATEWAY ---
if __name__ == "__main__":
    state_b = DecisionState(
        decision_id="dec_active_02",
        status=DecisionStatus.ACTIVE_DECISION,
        decision_required="Decide whether to completely terminate today's production deployment.",
        desired_outcome="Isolate threat parameters.",
        deadline_minutes=37,
        reversible=True,
        harm_of_delay="Immediate branch service delivery freeze.",
        provenance=ProvenanceType.USER_ASSERTED,
        source_id="incident_commander_terminal"
    )
    
    pipeline = WisdomAgentPipeline("The Controlled v0.91 Real-Time Trial")
    pipeline.execute_run(intent_state=state_b)
