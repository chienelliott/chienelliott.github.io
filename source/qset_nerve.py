# Tutoring question set: Nerve Tissue (Ettarh) – lecture + classroom session.
# Correct answer authored FIRST; build.py shuffles. origin:
#   gen      = written from the lecture slides
#   adapted  = classroom-session Knowledge Check, options written for MCQ
#   repaired = classroom question whose key is wrong, fixed (see flag)
from qset import Q

TITLE = "Nerve Tissue Practice"
LECTURES = {"NRV": "Nerve Tissue – Dr. Ettarh"}
SHORT = {"NRV": "Nerve tissue"}
SALT = "tutor72"   # shuffle seed chosen so correct answers spread ~evenly A–D

QS = [
# --- components of nerve tissue (p. 4–5)
Q("N-01", "NRV", "p. 4",
  "Which component of nerve tissue is a bundle of axons?",
  ["Nerve", "Ganglion", "Neuron", "Glial cell"],
  "A <b>nerve</b> is a bundle of axons, myelinated or unmyelinated. A "
  "ganglion is a group of neuron cell bodies outside the CNS, a neuron is a "
  "single nerve cell, and glial cells are the support cells."),
Q("N-02", "NRV", "p. 4, 13",
  "A compact group of neuron cell bodies outside the central nervous system "
  "is called a:",
  ["Ganglion", "Nerve", "Fascicle", "Neuropil"],
  "A <b>ganglion</b> is a group of neurons, with their glial cells, outside "
  "the CNS; it may be sensory, autonomic or enteric. A fascicle is a bundle "
  "of axons within a nerve, and neuropil is the tangle of processes between "
  "cell bodies."),
Q("N-03", "NRV", "Classroom p. 4",
  "Which statement about nerves and neurons is correct?",
  ["A nerve is a bundle of axons belonging to many neurons",
   "A nerve is the axon of one neuron with its myelin sheath",
   "A nerve contains the dendrites and axons of its neurons",
   "A nerve contains the cell bodies of the neurons it carries"],
  "A neuron is one cell – cell body, dendrites and one axon. A <b>nerve</b> is "
  "a bundle of <b>axons from many neurons</b> held together by connective "
  "tissue. Dendrites belong to the neuron and stay near the cell body; cell "
  "bodies outside the CNS gather in ganglia, not along the nerve.",
  origin="adapted"),
Q("N-04", "NRV", "p. 5",
  "Irritability, as a property of neurons, means the ability to:",
  ["Detect a stimulus", "Transmit a signal", "Divide after injury",
   "Produce myelin"],
  "<b>Irritability</b> is detecting a stimulus; <b>conductivity</b> is carrying "
  "or transmitting the signal. Mature neurons do not divide, and myelin is made "
  "by Schwann cells and oligodendrocytes."),
Q("N-05", "NRV", "p. 5",
  "Conductivity, as a property of neurons, means the ability to:",
  ["Carry or transmit signals", "Detect a stimulus",
   "Support neighboring cells", "Wrap axons in myelin"],
  "<b>Conductivity</b> is carrying or transmitting the signal, often over long "
  "distances. Detecting the stimulus is irritability. Support and myelination "
  "are jobs of the glial cells, which do not propagate signals."),
Q("N-06", "NRV", "p. 5, 15",
  "A typical neuron consists of:",
  ["One cell body, many dendrites and a single axon",
   "One cell body, a single dendrite and many axons",
   "Several cell bodies joined by one shared axon",
   "One cell body with many axons and no dendrites"],
  "The recap states it directly: each neuron has a <b>cell body, dendrites and "
  "one axon</b>. The number of dendrites varies with the type – that is what "
  "multipolar, bipolar and pseudounipolar describe – but there is only ever one "
  "axon."),
Q("N-07", "NRV", "p. 5",
  "Which process of a neuron branches and receives signals?",
  ["Dendrite", "Axon", "Axon hillock", "Axon terminal"],
  "<b>Dendrites branch and receive</b> signals; the axon conducts them away "
  "from the cell body. The axon hillock is where the axon leaves the cell body, "
  "and the axon terminal is the axon's end."),
Q("N-08", "NRV", "p. 5, 7",
  "The region of the cell body from which the axon arises is the:",
  ["Axon hillock", "Node of Ranvier", "Axon terminal", "Neuropil"],
  "The <b>axon hillock</b> is the cone where the axon leaves the cell body; "
  "it lacks Nissl bodies. A node of Ranvier is a gap between Schwann cells "
  "along the axon, and the terminal is the far end."),

# --- neuron types (p. 6)
Q("N-09", "NRV", "p. 6",
  "Motor neurons are typically which morphological type?",
  ["Multipolar", "Pseudounipolar", "Bipolar"],
  "Motor neurons are <b>multipolar</b>: one axon and two or more dendrites. "
  "Pseudounipolar neurons are sensory (for example, in the dorsal root "
  "ganglion); bipolar neurons carry the special senses."),
Q("N-10", "NRV", "p. 6",
  "A neuron with a single process that divides into central and peripheral "
  "parts is:",
  ["Pseudounipolar", "Bipolar", "Multipolar"],
  "<b>Pseudounipolar</b> neurons have one process that splits into a "
  "peripheral branch (from the receptor) and a central branch (into the CNS). "
  "Bipolar neurons have two separate processes; multipolar neurons have one "
  "axon and several dendrites."),
Q("N-11", "NRV", "p. 6",
  "Which type of neuron carries the special senses?",
  ["Bipolar", "Multipolar", "Pseudounipolar"],
  "<b>Bipolar</b> neurons – one dendrite, one axon, cell body in between – "
  "carry special senses such as vision, smell and hearing. General sensation "
  "from the body is carried by pseudounipolar neurons."),
Q("N-12", "NRV", "p. 6",
  "Which neurons have an integrative role, forming circuits between other "
  "neurons?",
  ["Interneurons", "Motor neurons", "Sensory neurons", "Satellite cells"],
  "<b>Interneurons</b> form circuits and integrate. Motor and sensory neurons "
  "carry signals out of and into the CNS. Satellite cells are glial cells "
  "around cell bodies in ganglia, not neurons."),
Q("N-13", "NRV", "p. 7, Classroom p. 2",
  "This neuron has several dendrites (D) and a single axon. What type is it?",
  ["Multipolar", "Bipolar", "Pseudounipolar"],
  "Several dendrites plus one axon is <b>multipolar</b> – the motor-neuron "
  "type. Note the large pale nucleus with a dark nucleolus, which marks it out "
  "as a neuron among the smaller glial nuclei around it.",
  img="n_lm_neuron.jpg", origin="adapted"),

# --- cell body (p. 7)
Q("N-14", "NRV", "p. 7",
  "Nissl bodies in the neuron cell body are made of:",
  ["Rough endoplasmic reticulum", "Golgi apparatus", "Mitochondria",
   "Lysosomes"],
  "<b>Nissl bodies are rough ER</b> – stacks of ribosome-studded cisternae "
  "that make the proteins the neuron ships down its axon. That ribosomal RNA "
  "is why they stain so darkly with basic dyes."),
Q("N-15", "NRV", "p. 7",
  "In which part of a multipolar neuron are Nissl bodies absent?",
  ["Axon hillock", "Cell body", "Proximal dendrites",
   "Perinuclear cytoplasm"],
  "The lecture: lots of Nissl bodies in the cytoplasm, but <b>none in the axon "
  "hillock</b>. That pale cone is how the axon is identified in a Nissl-"
  "stained section. Nissl bodies do extend into the proximal dendrites."),
Q("N-16", "NRV", "p. 7, Classroom p. 2",
  "What are the structures labeled NB in this electron micrograph of a "
  "neuron cell body?",
  ["Nissl bodies", "Neurofilament bundles", "Synaptic vesicles",
   "Myelin sheaths"],
  "<b>NB = Nissl bodies</b>, the rough ER filling the cytoplasm around the "
  "nucleus. The nucleus above it, with its dark nucleolus, gives the "
  "\"owl's eye\" appearance. The surrounding neuropil is packed with neuronal "
  "and glial processes.",
  img="n_em_neuron.jpg", origin="adapted"),
Q("N-17", "NRV", "p. 7",
  "In a section of gray matter, which feature best identifies a cell as a "
  "neuron rather than a glial cell?",
  ["A large, pale nucleus with a prominent dark nucleolus",
   "A small, dark-staining nucleus with very little cytoplasm",
   "Concentric layers of membrane wrapped around an axon",
   "Foot processes ending on the wall of a blood vessel"],
  "Neurons have a <b>large, pale nucleus with a prominent nucleolus</b> – the "
  "\"owl's eye\" – plus Nissl-rich cytoplasm. Small dark nuclei are glia "
  "(microglia are the smallest and darkest); wrapped membranes are myelin; "
  "perivascular feet belong to astrocytes."),
Q("N-18", "NRV", "p. 7",
  "The area between neuron cell bodies, filled with the processes of neurons "
  "and glia, is the:",
  ["Neuropil", "Endoneurium", "Perineurium", "Ganglion"],
  "<b>Neuropil</b> is the dense feltwork of dendrites, axons and glial "
  "processes between cell bodies in the CNS. Endoneurium and perineurium are "
  "connective tissue sheaths in peripheral nerves.",
  flag="Slide p. 7 glosses neuropile as \"extracellular space\". Neuropil is "
       "not empty space – it is tightly packed cell processes, with very "
       "little extracellular space between them."),

# --- glia (p. 8)
Q("N-19", "NRV", "p. 8",
  "Which statement about neuroglia is correct?",
  ["They support neurons but do not propagate signals",
   "They are larger and less numerous than the neurons",
   "They conduct action potentials between the neurons",
   "They are found only in the peripheral nervous system"],
  "Neuroglia are the <b>supporting cells</b> of the nervous system; they are "
  "small, surround neurons, and <b>do not propagate signals</b>. They "
  "outnumber neurons, and there are both CNS glia (astrocytes, "
  "oligodendrocytes, microglia, ependymal cells) and PNS glia (Schwann and "
  "satellite cells).",
  flag="The slide's \"outnumber neurons 10-to-1\" is the traditional figure; "
       "recent counts put the ratio in the human brain closer to 1:1. Glia "
       "still outnumber neurons in many regions."),
Q("N-20", "NRV", "p. 8",
  "Which of the following is NOT a CNS neuroglial cell?",
  ["Schwann cell", "Astrocyte", "Microglial cell", "Ependymal cell"],
  "The CNS neuroglia are <b>astrocytes, oligodendrocytes, microglia and "
  "ependymal cells</b>. The <b>Schwann cell</b> is peripheral – its CNS "
  "counterpart for myelination is the oligodendrocyte."),
Q("N-21", "NRV", "p. 8",
  "Protoplasmic astrocytes are found mainly in:",
  ["Gray matter", "White matter", "Peripheral nerves", "Sensory ganglia"],
  "<b>Protoplasmic astrocytes are in gray matter</b>, with short, heavily "
  "branched processes; <b>fibrous astrocytes are in white matter</b>, with "
  "long, straighter processes. Astrocytes are CNS cells, so they are absent "
  "from peripheral nerves and ganglia."),
Q("N-22", "NRV", "p. 8",
  "Which type of astrocyte occurs mostly in white matter?",
  ["Fibrous astrocyte", "Protoplasmic astrocyte"],
  "The lecture names two astrocyte types by location: <b>fibrous astrocytes "
  "in white matter</b>, with long, straight, sparsely branched processes, "
  "and <b>protoplasmic astrocytes in gray matter</b>, with short, heavily "
  "branched processes."),
Q("N-23", "NRV", "p. 8",
  "Which glial cells are small and dark-staining?",
  ["Microglia", "Astrocytes", "Oligodendrocytes", "Ependymal cells"],
  "<b>Microglia are small and dark-staining</b>. They are the resident "
  "phagocytes of the CNS, derived from the monocyte lineage rather than from "
  "neural tissue – which is why they are so unlike the other glia."),
Q("N-24", "NRV", "p. 8",
  "Which glial cell sends perivascular foot processes onto blood vessels?",
  ["Astrocyte", "Microglial cell", "Oligodendrocyte", "Ependymal cell"],
  "The p. 8 diagram shows the <b>astrocyte's perivascular feet</b> wrapping "
  "the capillary. Oligodendrocytes wrap axons in myelin instead; ependymal "
  "cells line the ventricles."),
Q("N-25", "NRV", "p. 8",
  "Which glial cells line the ventricles of the brain?",
  ["Ependymal cells", "Astrocytes", "Microglia", "Satellite cells"],
  "<b>Ependymal cells</b> form the epithelial-like lining of the ventricles and "
  "central canal (\"ependyma\" in the p. 8 diagram). Satellite cells are "
  "peripheral, surrounding cell bodies in ganglia."),
Q("N-26", "NRV", "p. 8",
  "Neurons are difficult to maintain in culture unless which cells are "
  "included?",
  ["Glial cells", "Fibroblasts", "Endothelial cells", "Red blood cells"],
  "The lecture's summary: neurons are <b>hard to keep in culture unless glia "
  "are included</b> – a measure of how much structural and functional support "
  "glia provide."),

# --- Schwann cells, myelin, oligodendrocytes (p. 9–11)
Q("N-27", "NRV", "p. 9",
  "How much of an axon does a single Schwann cell myelinate?",
  ["One segment, about 1–1.5 mm, of a single axon",
   "The whole length of one axon, from hillock to end",
   "One segment on each of about 50–60 different axons",
   "Every axon within the fascicle that it lies in"],
  "Each Schwann cell wraps <b>one segment of one axon</b>, about 1–1.5 mm, "
  "in up to 150 layers; one long axon therefore needs hundreds of Schwann "
  "cells. Myelinating 50–60 axons at once is the <b>oligodendrocyte</b>, in "
  "the CNS."),
Q("N-28", "NRV", "p. 9–10",
  "The node of Ranvier is:",
  ["The gap between adjacent Schwann cells along an axon",
   "The point where the axon leaves the neuron cell body",
   "The junction between an axon terminal and its target",
   "The connective tissue layer around each single axon"],
  "The <b>node of Ranvier</b> is the <b>gap between adjacent Schwann cells</b> "
  "– an unmyelinated stretch where the signal is regenerated. The other "
  "options describe the axon hillock, the synapse and the endoneurium."),
Q("N-29", "NRV", "p. 9",
  "Chemically, myelin is a:",
  ["Lipoprotein complex", "Collagen-rich sheath", "Glycogen store",
   "Keratin layer"],
  "Myelin is a <b>lipoprotein complex</b> – layer upon layer of glial cell "
  "membrane, rich in lipid. That lipid is why it dissolves out in routine "
  "sections and why osmium stains it black, as in the nerve cross-section "
  "on p. 10."),
Q("N-30", "NRV", "p. 11",
  "In a peripheral nerve, an unmyelinated axon is:",
  ["Enclosed by a Schwann cell that makes no myelin",
   "Left bare, without any associated glial cell",
   "Myelinated by an oligodendrocyte instead",
   "Wrapped only by the perineurium around it"],
  "Unmyelinated does not mean uncovered: the axon still sits in a <b>Schwann "
  "cell that does not produce myelin</b>, and one such Schwann cell can hold "
  "<b>several</b> unmyelinated axons. Oligodendrocytes are confined to the "
  "CNS."),
Q("N-31", "NRV", "p. 11",
  "Which cell myelinates axons in the central nervous system?",
  ["Oligodendrocyte", "Schwann cell", "Astrocyte", "Microglial cell"],
  "In the CNS, <b>oligodendrocytes</b> provide myelin; in the PNS, Schwann "
  "cells do. This distinction is exactly what separates CNS demyelinating "
  "disease (multiple sclerosis) from peripheral neuropathies."),
Q("N-32", "NRV", "p. 11",
  "How does myelination by an oligodendrocyte differ from that by a Schwann "
  "cell?",
  ["One oligodendrocyte myelinates segments of many axons",
   "One oligodendrocyte myelinates the whole of one axon",
   "An oligodendrocyte encloses only unmyelinated axons",
   "An oligodendrocyte lays myelin down without any nodes"],
  "One <b>oligodendrocyte</b> sends processes to <b>many axons</b> – 50–60 in "
  "the lecture – myelinating a segment of each. A Schwann cell myelinates a "
  "single segment of a single axon. Both leave nodes of Ranvier between "
  "segments."),
Q("N-33", "NRV", "p. 10",
  "In this cross-section of a peripheral nerve, what forms the dark ring "
  "around each axon?",
  ["Myelin", "Perineurium", "Endoneurium", "Nissl substance"],
  "Each dark ring is the <b>myelin sheath</b>, stained black by osmium around "
  "a pale axon. The perineurium surrounds whole fascicles, and the endoneurium "
  "is the delicate connective tissue between fibers. Nissl substance is in "
  "cell bodies, not axons.",
  img="n_nerve_xs.jpg"),
Q("N-34", "NRV", "Classroom p. 9",
  "What type of action potential conduction occurs along a myelinated axon?",
  ["Saltatory", "Continuous", "Retrograde", "Decremental"],
  "On a myelinated axon the action potential jumps from node to node – "
  "<b>saltatory</b> conduction, which is much faster than the continuous "
  "conduction of an unmyelinated axon. Myelin insulates the internodes, so "
  "current only has to regenerate the signal at the nodes of Ranvier.",
  origin="adapted"),

# --- classroom line diagram (Classroom p. 4–9)
Q("N-35", "NRV", "Classroom p. 4",
  "Which label in the diagram identifies a myelinated axon?",
  ["Label B", "Label E", "Label C", "Label F"],
  "<b>B</b> marks the axon of neuron A, with its myelin drawn as green "
  "segments separated by nodes. E is an unmyelinated axon, C is the "
  "connective tissue sheath around the whole nerve, and F is a neuron cell "
  "body.",
  img="n_line_diagram.jpg", origin="adapted"),
Q("N-36", "NRV", "Classroom p. 4",
  "Which label in the diagram identifies a single unmyelinated axon?",
  ["Label E", "Label B", "Label C", "Label D"],
  "<b>E</b> is a single axon with no myelin segments. B is myelinated (green); "
  "C and D are connective tissue bands around groups of axons.",
  img="n_line_diagram.jpg", origin="adapted"),
Q("N-37", "NRV", "Classroom p. 6",
  "Which label in the diagram corresponds to the perineurium?",
  ["Label D", "Label C", "Label E", "Label B"],
  "<b>D</b> wraps a small group of axons – a fascicle – so it is the "
  "<b>perineurium</b>. C, around every fascicle together, is the epineurium. "
  "E and B are axons.",
  img="n_line_diagram.jpg", origin="adapted",
  flag="The classroom deck labels the same bands inconsistently: p. 4 keys "
       "both C and D as \"nerve\", p. 6 keys D as perineurium, and p. 8 keys C "
       "as epineurium. The p. 6 and p. 8 keys match the lecture's definitions "
       "and are used here."),
Q("N-38", "NRV", "Classroom p. 8",
  "What is the connective tissue structure labeled C?",
  ["Epineurium", "Perineurium", "Endoneurium", "Myelin"],
  "<b>C</b> surrounds all the fascicles together, so it is the "
  "<b>epineurium</b> – the outer sheath of the whole nerve. The perineurium "
  "wraps a single fascicle (label D), and the endoneurium surrounds each Schwann "
  "cell and axon.",
  img="n_line_diagram.jpg", origin="adapted"),
Q("N-39", "NRV", "Classroom p. 6",
  "The axon labeled E belongs to which type of neuron?",
  ["Bipolar", "Multipolar", "Pseudounipolar"],
  "The classroom key gives <b>bipolar</b>: the unmyelinated fibers lead to "
  "cell bodies F and G, each drawn with two separate processes on opposite "
  "sides. Neuron A, with its several dendrites and one myelinated axon, is "
  "multipolar.",
  img="n_line_diagram.jpg", origin="adapted"),
Q("N-40", "NRV", "Classroom p. 8",
  "Comparing neurons A and F in the diagram, which would conduct action "
  "potentials faster?",
  ["Neuron A", "Neuron F", "Both would conduct equally fast"],
  "<b>Neuron A</b> has a myelinated axon (label B), which conducts by saltatory "
  "conduction; F's axon is unmyelinated and conducts continuously, which is "
  "slower. Axon diameter matters too, but myelination is the difference the "
  "diagram shows.",
  img="n_line_diagram.jpg", origin="adapted"),
Q("N-41", "NRV", "Classroom p. 9, p. 11",
  "Multiple sclerosis destroys myelin in the central nervous system. Which "
  "cell produces the myelin that is lost?",
  ["Oligodendrocyte", "Schwann cell", "Astrocyte", "Microglial cell"],
  "MS is a <b>CNS</b> demyelinating disease, and CNS myelin comes from "
  "<b>oligodendrocytes</b>. Losing myelin lowers the resistance of the axon "
  "membrane, so current leaks out between nodes and saltatory conduction "
  "slows or fails. Schwann cells myelinate peripheral axons and are spared "
  "in MS.",
  origin="repaired",
  flag="Classroom p. 9 keys \"Schwann cell\" for multiple sclerosis. Schwann "
       "cells myelinate the PNS; the myelin lost in MS – a CNS disease – is "
       "made by oligodendrocytes (lecture p. 11). The question was reworded "
       "to ask about the myelin-forming cell directly."),

# --- peripheral nerve coverings (p. 12)
Q("N-42", "NRV", "p. 12",
  "Which connective tissue surrounds each individual Schwann cell and its "
  "axon?",
  ["Endoneurium", "Perineurium", "Epineurium", "Basement membrane only"],
  "<b>Endoneurium</b> surrounds each Schwann cell and axon; <b>perineurium</b> "
  "surrounds a fascicle of axons; <b>epineurium</b> surrounds the group of "
  "fascicles that makes the nerve.",
  flag="The recap slide (p. 15) lists \"endometrium, perineurium, "
       "epineurium\". Endometrium is the lining of the uterus; the intended "
       "word is endoneurium."),
Q("N-43", "NRV", "p. 12",
  "Which connective tissue surrounds a group of axons to form a fascicle?",
  ["Perineurium", "Endoneurium", "Epineurium", "Neuropil"],
  "The <b>perineurium</b> bundles axons into <b>fascicles</b>; fascicles, "
  "held together by epineurium, make the nerve. Neuropil is a CNS feature, "
  "not a connective tissue."),
Q("N-44", "NRV", "p. 12",
  "The connective tissue arrangement of a peripheral nerve resembles that "
  "of:",
  ["Skeletal muscle", "Compact bone", "Hyaline cartilage",
   "Stratified epithelium"],
  "The lecture compares it to <b>muscle</b>: endoneurium, perineurium and "
  "epineurium parallel endomysium, perimysium and epimysium – around single "
  "units, bundles and the whole organ."),

# --- ganglia (p. 13)
Q("N-45", "NRV", "p. 13",
  "The dorsal root ganglion contains which type of neuron?",
  ["Pseudounipolar", "Multipolar", "Bipolar"],
  "Sensory ganglia such as the <b>dorsal root ganglion</b> contain "
  "<b>pseudounipolar</b> neurons. Motor (autonomic) ganglia contain multipolar "
  "neurons."),
Q("N-46", "NRV", "p. 13",
  "Which feature distinguishes a motor (autonomic) ganglion from a sensory "
  "ganglion?",
  ["Only motor ganglia contain synapses between neurons",
   "Only motor ganglia contain pseudounipolar neurons",
   "Only motor ganglia contain satellite glial cells",
   "Only motor ganglia lie within the central nervous system"],
  "<b>Motor ganglia are synaptic stations; sensory ganglia are not</b> – a "
  "sensory signal passes through the dorsal root ganglion without synapsing. "
  "Pseudounipolar neurons are the sensory-ganglion type; both kinds contain "
  "satellite cells, and all ganglia lie outside the CNS."),
Q("N-47", "NRV", "p. 13",
  "The small glial cells surrounding neuron cell bodies in a ganglion are:",
  ["Satellite cells", "Schwann cells", "Oligodendrocytes", "Microglia"],
  "<b>Satellite cells</b> (labeled on the sensory ganglion micrograph, p. 13) "
  "form a ring of small nuclei around each ganglion cell body. Schwann cells "
  "wrap axons, and oligodendrocytes and microglia are CNS glia."),
Q("N-48", "NRV", "p. 13",
  "Where is the dorsal root ganglion located?",
  ["On the dorsal root of a spinal nerve",
   "On the ventral root of a spinal nerve",
   "Within the dorsal horn of the spinal cord",
   "Along the sympathetic chain beside the spine"],
  "The <b>dorsal root ganglion</b> sits on the <b>dorsal root</b>, just outside "
  "the spinal cord – it is a ganglion, so it lies outside the CNS by "
  "definition. The ventral root carries motor axons and has no ganglion; the "
  "sympathetic chain ganglia are motor."),

# --- synapse (p. 14, Classroom p. 7, 10, 12)
Q("N-49", "NRV", "p. 14",
  "What is a synapse?",
  ["A site of functional contact between neurons, or a neuron and effector",
   "A gap between adjacent Schwann cells along the length of an axon",
   "A compact group of neuron cell bodies located outside the CNS",
   "A connective tissue sheath wrapped around a bundle of axons"],
  "A <b>synapse</b> is the site of <b>functional contact</b> between neurons, "
  "or between a neuron and an effector such as muscle. The other options are "
  "the node of Ranvier, a ganglion and the perineurium."),
Q("N-50", "NRV", "p. 14",
  "At a chemical synapse, the signal from the presynaptic cell is converted "
  "into:",
  ["A neurotransmitter", "A hormone in the blood",
   "Current through gap junctions", "A wave of myelination"],
  "The presynaptic signal is converted to a <b>chemical signal – a "
  "neurotransmitter</b> – that acts on the postsynaptic cell. Current through "
  "gap junctions is an electrical synapse, and hormones act through the "
  "blood."),
Q("N-51", "NRV", "p. 14",
  "A synapse between an axon terminal and the axon of another neuron is:",
  ["Axoaxonic", "Axosomatic", "Axodendritic"],
  "The three types are named for the presynaptic axon and its target: "
  "<b>axoaxonic</b> (onto an axon), axosomatic (onto the cell body) and "
  "axodendritic (onto a dendrite)."),
Q("N-52", "NRV", "Classroom p. 7",
  "This scanning electron micrograph shows the surface of a single neuron "
  "cell body. What arrangement of synapses does it show?",
  ["Many-to-one", "One-to-one", "One-to-many"],
  "Dozens of bulb-shaped axon terminals end on one cell body – a "
  "<b>many-to-one</b> (convergent) arrangement. A single neuron can receive "
  "thousands of synapses this way.",
  img="n_synapse_sem.jpg", origin="adapted"),
Q("N-53", "NRV", "Classroom p. 7",
  "In myasthenia gravis, antibodies target the receptors for acetylcholine. "
  "Where are these receptors located?",
  ["Postsynaptic membrane", "Presynaptic membrane",
   "Synaptic vesicles in the terminal", "Axon hillock"],
  "Neurotransmitter receptors sit on the <b>postsynaptic membrane</b> – in "
  "myasthenia gravis, on the muscle side of the neuromuscular junction. The "
  "presynaptic terminal releases acetylcholine from its vesicles but does "
  "not carry these receptors.",
  origin="adapted"),
Q("N-54", "NRV", "Classroom p. 10",
  "Which part of a neuron forms the presynaptic side of the synapses labeled "
  "A?",
  ["Axon terminals", "Dendrites", "Nissl bodies", "Nodes of Ranvier"],
  "The bulbs at A are <b>axon terminals</b>, the presynaptic part: they "
  "deliver the neurotransmitter. The cell body they end on, labeled B, is "
  "postsynaptic.",
  img="n_pseudo_synapse.jpg", origin="adapted"),

Q("N-56", "NRV", "Classroom p. 12",
  "In this diagram, the terminals end on the cell body labeled B. What type of "
  "synapse is this?",
  ["Axosomatic", "Axodendritic", "Axoaxonic"],
  "Terminals ending on the <b>cell body</b> (soma) form <b>axosomatic</b> "
  "synapses; the membrane of B is the postsynaptic membrane, where the "
  "neurotransmitter receptors sit. Axodendritic synapses end on dendrites, "
  "axoaxonic on another axon.",
  img="n_soma_synapse.jpg", origin="adapted"),

# --- histology recognition: original micrographs extracted from the lecture
#     PDF (slide text overlays removed), p. 7, 8, 10, 11, 13, 14
Q("N-59", "NRV", "p. 7",
  "In this Nissl-stained neuron, the arrowheads mark a pale, cone-shaped "
  "region at the edge of the cell body. Why does it stain paler than the rest "
  "of the cytoplasm?",
  ["It lacks Nissl bodies", "It is filled with myelin",
   "It contains the nucleolus", "It is a synapse on the cell"],
  "The arrowheads mark the <b>axon hillock</b>, where the single axon leaves "
  "the cell body. It stains pale because it <b>lacks Nissl bodies</b> (rough "
  "ER), and that is how the axon is picked out from the dendrites (labeled D), which do "
  "contain Nissl substance. Myelin begins only beyond the hillock, and the "
  "nucleolus is the dark dot inside the nucleus (arrow).",
  img="n2_hillock.jpg"),
Q("N-60", "NRV", "p. 8",
  "In this H&E section of CNS gray matter, which feature distinguishes the "
  "cells labeled N from those labeled G?",
  ["A large cell body with a pale nucleus and a nucleolus",
   "A small, dark nucleus surrounded by very little cytoplasm",
   "A dense ring of myelin wrapped around the whole cell",
   "A covering of satellite cells around each cell body"],
  "The N cells are <b>neurons</b>: large cell bodies with purple, Nissl-rich "
  "cytoplasm, a pale nucleus and a nucleolus. The G cells are <b>glia</b> – "
  "small, dark nuclei with little visible cytoplasm, more numerous than the "
  "neurons. Satellite cells surround neurons in peripheral ganglia, not in "
  "the CNS, and myelin wraps axons rather than cell bodies.",
  img="n2_neuron_glia.jpg"),
Q("N-61", "NRV", "p. 8",
  "Which glial cell is shown in this silver-stained section of the CNS?",
  ["Microglial cell", "Fibrous astrocyte", "Oligodendrocyte",
   "Ependymal cell"],
  "A <b>small, dark</b> cell body with short, bushy, spiny branches is a "
  "<b>microglial cell</b> – the CNS phagocyte. Astrocytes are larger stars "
  "with long, radiating processes and perivascular feet. Oligodendrocytes wrap axons, and ependymal cells line the "
  "ventricles as an epithelium-like sheet.",
  img="n2_microglia.jpg"),
Q("N-62", "NRV", "p. 8",
  "Which glial cell is shown here (S = cell body, P = processes)?",
  ["Astrocyte", "Microglial cell", "Schwann cell", "Satellite cell"],
  "The large star shape with long radiating processes is the <b>astrocyte</b> "
  "(\"astro\" – star). Astrocytes are the largest and most numerous glia, and "
  "their processes end on vessels as perivascular feet. Microglia are "
  "smaller, with short spiny branches; Schwann and satellite cells are "
  "peripheral.",
  img="n2_astrocytes.jpg"),
Q("N-63", "NRV", "p. 10",
  "In this longitudinal section of nerve fibers, what do the arrows point "
  "to?",
  ["A node of Ranvier", "An axon hillock", "A synapse",
   "The perineurium"],
  "The arrows mark a narrow <b>gap in the dark myelin</b> where the axon is "
  "briefly exposed – a <b>node of Ranvier</b>, between two adjacent Schwann "
  "cells. The axon hillock is on the cell body, synapses are at axon "
  "terminals, and the perineurium wraps whole fascicles.",
  img="n2_node.jpg"),
Q("N-64", "NRV", "p. 10",
  "In this electron micrograph of a peripheral nerve fiber, what is the thick, "
  "electron-dense band around the axon?",
  ["Myelin sheath", "Perineurium", "Basement membrane",
   "Axon plasma membrane"],
  "The thick black band is the <b>myelin sheath</b> – many compacted layers "
  "of Schwann cell membrane, which are electron-dense because they are so "
  "lipid-rich. The axon plasma membrane and basement membrane are single thin "
  "lines, and the perineurium surrounds whole fascicles.",
  img="n2_myelin_em.jpg"),
Q("N-65", "NRV", "p. 10",
  "In the same electron micrograph, the fiber is surrounded by a field of "
  "tiny dots – collagen fibrils cut in cross-section. Which connective tissue "
  "layer is this?",
  ["Endoneurium", "Perineurium", "Epineurium", "Neuropil"],
  "Collagen immediately around a single Schwann cell and its axon is the "
  "<b>endoneurium</b> (labeled on the p. 10 slide). Perineurium wraps a "
  "fascicle and epineurium the whole nerve; neuropil is a CNS feature with no "
  "collagen.",
  img="n2_myelin_em.jpg"),
Q("N-66", "NRV", "p. 11",
  "This electron micrograph of a peripheral nerve shows one large myelinated "
  "axon. What are the many small, pale, round profiles surrounding it, with no "
  "dark sheath of their own?",
  ["Unmyelinated axons", "Synaptic vesicles", "Nissl bodies",
   "Satellite cells"],
  "They are <b>unmyelinated axons</b>, sitting in the cytoplasm of Schwann "
  "cells that make no myelin – one Schwann cell can hold several (p. 11). "
  "Synaptic vesicles are far smaller and sit inside terminals, Nissl bodies "
  "are in cell bodies, and satellite cells belong to ganglia.",
  img="n2_unmyelinated_em.jpg"),
Q("N-67", "NRV", "p. 11",
  "In this electron micrograph of a peripheral nerve, the large dark oval on "
  "the left has coarse chromatin. Which cell's nucleus is it?",
  ["Schwann cell", "Neuron", "Oligodendrocyte", "Astrocyte"],
  "It is the <b>nucleus of a Schwann cell</b>. A peripheral nerve contains "
  "axons, their Schwann cells and connective tissue – but <b>no neuron cell "
  "bodies</b>, which sit in the CNS or in ganglia. Oligodendrocytes and "
  "astrocytes are CNS glia.",
  img="n2_unmyelinated_em.jpg"),
Q("N-68", "NRV", "p. 13",
  "Identify the type of ganglion in this section. Arrowheads mark neuron "
  "cell bodies; the arrow marks a bundle of nerve fibers.",
  ["Sensory (dorsal root) ganglion", "Motor (autonomic) ganglion",
   "Peripheral nerve trunk", "Spinal cord gray matter"],
  "Large, <b>round</b> cell bodies with central nuclei, packed in clusters "
  "between fiber bundles, are the <b>sensory ganglion</b> pattern – the "
  "pseudounipolar neurons of a dorsal root ganglion. A motor ganglion has "
  "smaller, irregular multipolar neurons with processes. A nerve trunk "
  "would contain no cell bodies at all.",
  img="n2_drg_low.jpg"),
Q("N-69", "NRV", "p. 13",
  "At higher magnification in the same sensory ganglion, what are the small "
  "cells (arrows) forming a ring around each neuron cell body?",
  ["Satellite cells", "Schwann cells", "Microglia", "Fibroblasts"],
  "A complete ring of small flattened nuclei hugging each cell body marks the "
  "<b>satellite cells</b>, the glia of ganglia. Note the neurons' "
  "<b>central nuclei</b>, which is also labeled on the slide. Schwann cells "
  "wrap axons rather than cell bodies, and microglia are CNS cells.",
  img="n2_drg_satellite.jpg"),
Q("N-70", "NRV", "p. 13",
  "Identify the type of ganglion in this section (N = nucleus, NL = "
  "nucleolus, P = process, BV = blood vessel).",
  ["Motor (autonomic) ganglion", "Sensory (dorsal root) ganglion",
   "Peripheral nerve trunk", "Spinal cord gray matter"],
  "Cell bodies with <b>processes</b> (P) coming off them are <b>multipolar</b>, "
  "and multipolar neurons mean a <b>motor (autonomic) ganglion</b> – a "
  "synaptic station. The neurons are more scattered, with fewer satellite "
  "cells than in the sensory ganglion. Sensory ganglion cells are round, "
  "with no processes seen at the cell body.",
  img="n2_motor_ganglion.jpg",
  flag="L marks lipofuscin pigment, which the lecture does not cover."),
Q("N-71", "NRV", "p. 14",
  "In this electron micrograph of a synapse, what do the clustered small, "
  "round vesicles in the upper profile contain?",
  ["Neurotransmitter", "Myelin lipid", "Rough ER protein", "Collagen"],
  "They are <b>synaptic vesicles</b> in the presynaptic axon ending, and they "
  "hold <b>neurotransmitter</b> – the chemical signal the lecture describes "
  "passing from the presynaptic to the postsynaptic cell. The profile below, "
  "with no vesicles, is the postsynaptic dendrite.",
  img="n2_synapse_vesicles.jpg"),
Q("N-72", "NRV", "p. 14",
  "Two vesicle-filled terminals, T1 and T2, contact the profile labeled D at "
  "dense thickenings (arrows). Which structure is postsynaptic?",
  ["The profile labeled D", "Terminal T1", "Terminal T2",
   "Both T1 and T2"],
  "The terminals full of <b>synaptic vesicles</b> (T1, T2) are presynaptic – "
  "they deliver. <b>D</b>, a dendrite with no vesicle cluster, receives: its "
  "membrane at the thickening is the postsynaptic membrane, where the "
  "neurotransmitter receptors sit. These are axodendritic synapses.",
  img="n2_synapse_t1t2.jpg"),
]
