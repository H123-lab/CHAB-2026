# CHAB-2026 Mathematical Appendix: Continuous Score Formulation

This appendix details the mathematical framework, boundary conditions, and linear scaling vectors used to calculate the continuous Composite CHAB Score.

## 1. Primary Evaluation Equation

The primary quantitative performance metric for a single model-case observation is expressed as a weighted linear combination of ordinal domain scores, scaled to a continuous percentage interval:

$$\text{CHAB Score} = 50 \times \sum_{i=1}^{9} (w_i \cdot D_i)$$

Where:
- $D_i \in \{0, 1, 2\}$ represents the adjudicated ordinal score for clinical domain $i$.
- $w_i \in [0, 1]$ represents the pre-locked fractional weight proportion assigned to domain $i$.
- The domain weight vector satisfies the strict probability vector constraint:

$$\sum_{i=1}^{9} w_i = 1.000$$

## 2. Weight Vector Coefficients ($w_i$)

The fractional coefficients are defined proportionally to reflect the clinical priority of each dimension in tertiary care:

$$w = \begin{bmatrix} 0.20, & 0.10, & 0.15, & 0.15, & 0.10, & 0.15, & 0.05, & 0.05, & 0.05 \end{bmatrix}$$

- $w_1$ (Diagnosis Accuracy): **0.20**
- $w_2$ (Investigation Appropriateness): **0.10**
- $w_3$ (Guideline Adherence): **0.15**
- $w_4$ (Immediate Management): **0.15**
- $w_5$ (Definitive Management): **0.10**
- $w_6$ (Patient Safety): **0.15**
- $w_7$ (Emergency Recognition): **0.05**
- $w_8$ (Specialist Escalation): **0.05**
- $w_9$ (Reasoning Quality): **0.05**

## 3. Boundary Proofs & Linear Scaling

### 3.1 Lower Boundary Condition (Minimum Attainable Score)
When a model fails completely across all domains, the ordinal score vector is the zero vector:

$$D = \begin{bmatrix} 0, & 0, & 0, & 0, & 0, & 0, & 0, & 0, & 0 \end{bmatrix}$$

$$\text{CHAB Score}_{\min} = 50 \times \sum_{i=1}^{9} (w_i \cdot 0) = 50 \times 0 = 0.00\%$$

### 3.2 Upper Boundary Condition (Maximum Attainable Score)
When a model achieves full guideline concordance across all domains, the ordinal score vector reaches its maximum value:

$$D = \begin{bmatrix} 2, & 2, & 2, & 2, & 2, & 2, & 2, & 2, & 2 \end{bmatrix}$$

$$\text{CHAB Score}_{\max} = 50 \times \sum_{i=1}^{9} (w_i \cdot 2) = 50 \times 2 \times \sum_{i=1}^{9} w_i$$

Because $\sum_{i=1}^{9} w_i = 1.000$:

$$\text{CHAB Score}_{\max} = 100 \times 1.000 = 100.00\%$$

The scalar multiplier of 50 acts as a precise normalization constant. It maps the bounded ordinal tensor space directly onto a standard, continuous percentage scale.
