This tutorial presents wall thickness sizing for pipeline and riser using Python for subsea applications. Wall thickness calculations are normally conducted in Excel and validated in Mathcad. Mathcad is a good engineering calculation software because of it's superb symbolic notations, however it is not free, hence the need to consider Python symbolic and numerical libraries which is free and open sourced. 

Pipeline wall thickness sizing is an important and fundamental step in subsea pipeline design. Pipeline and riser Wall thickness is usually determined to minimize the cost of the pipes.The primary design loads relevant to the containment of the wall thickness are:
- Internal pressure loads
- External hydrostatic pressure load
- Longitudinal functional loads.

The following failure criteria must be satisfied:
- Pressure containment (Burst)
- External pressure (Collapse)
- Propagating Buckling.

Propagating buckling is not considered in the final selection of wall thickness as the cost becomes higher if propagating buckling gives the governing thickness,thus it is only used to determine if buckle arrestor will be required or not. Buckle arrestor is required if propagating buckling is the governing criteria, that is if the thickness obtained from propagating buckling is greater than the thickness obtained from burst and collapse.

Codes & Standards used:
- ASME B31.4/31.8
- APIRP1111

Python libraries used:
- Sympy
- Numpy
- Pandas
- Matplotlib

Note: for the sake of privacy, input data used here were assumed and does not apply to any subsea project.
