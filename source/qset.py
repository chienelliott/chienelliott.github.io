# Tutoring question set: Intro to Anatomy (Nausheen) + Epithelial Tissues (Ettarh).
# Authoring convention: the correct answer is written FIRST in opts; build.py
# shuffles with a per-id seed. origin "prof" keeps the lecturer's order and key.
#   origin: "gen" = written from the slides; "prof" = lecturer's MCQ as written;
#           "repaired" = lecturer's MCQ with the option set fixed (see flag)

LECTURES = {
    "ANAT": "Introduction to Anatomy – Dr. Nausheen",
    "EPI": "Epithelial Tissues – Dr. Ettarh",
}


def Q(id, lec, ref, stem, opts, why, img=None, beyond=False, flag=None,
      origin="gen", ans=0):
    return dict(id=id, lec=lec, ref=ref, stem=stem, opts=opts, why=why,
                img=img, beyond=beyond, flag=flag, origin=origin, ans=ans)


QS = [
# ============================== ANATOMY ==============================
# --- ways to study anatomy (p. 3–7)
Q("A-01", "ANAT", "p. 3",
  "Which approach to anatomy follows the body from a two-cell embryo to a "
  "fully developed baby?",
  ["Developmental anatomy", "Surgical anatomy", "Systemic anatomy",
   "Radiological anatomy"],
  "<b>Developmental anatomy</b> traces structure through embryonic and fetal "
  "life. Surgical anatomy is anatomy organized around operative procedures; "
  "systemic anatomy studies one organ system across the whole body; "
  "radiological anatomy studies structures as they appear on imaging."),
Q("A-02", "ANAT", "p. 3",
  "A resident reviews the layers that must be divided to reach the appendix "
  "during an appendectomy. Which approach to anatomy is this?",
  ["Surgical anatomy", "Surface anatomy", "Developmental anatomy",
   "Systemic anatomy"],
  "Studying structure for its relevance to an operation is <b>surgical "
  "anatomy</b>. Surface anatomy concerns external features; developmental "
  "anatomy concerns the embryo; systemic anatomy follows one system through "
  "the body."),
Q("A-03", "ANAT", "p. 4",
  "A student traces the outline of the clavicle and the tip of the shoulder "
  "on a classmate's skin. Which approach to anatomy is this?",
  ["Surface anatomy", "Radiological anatomy", "Regional anatomy",
   "Surgical anatomy"],
  "<b>Surface anatomy</b> studies external features – what can be seen and "
  "palpated. Regional anatomy studies all the structures of one body region "
  "together; radiological anatomy uses imaging."),
Q("A-04", "ANAT", "p. 4–6",
  "The circulatory system is spread through every region of the body. "
  "Studying it as one continuous whole is an example of which approach?",
  ["Systemic anatomy", "Regional anatomy", "Surface anatomy",
   "Developmental anatomy"],
  "<b>Systemic anatomy</b> studies a whole system made of different organs, "
  "such as the nervous or circulatory system, even though that system is "
  "located in many regions. Regional anatomy would instead study the thorax "
  "or the axilla with all its systems together."),
Q("A-05", "ANAT", "p. 5",
  "In a lab session, students study the thorax – its bones, muscles, vessels, "
  "nerves and organs – before moving on to the abdomen. Which approach is "
  "this?",
  ["Regional anatomy", "Systemic anatomy", "Surface anatomy",
   "Radiological anatomy"],
  "Studying everything within one body region together is <b>regional "
  "anatomy</b> – the \"Regions\" views on p. 5 (head and neck, thorax, "
  "abdomen, pelvis). Systemic anatomy would follow one system, such as the "
  "circulatory system, across all regions."),
Q("A-06", "ANAT", "p. 7",
  "Which approach studies organs, systems and regions using CT, MRI and "
  "ultrasound?",
  ["Radiological anatomy", "Surgical anatomy", "Surface anatomy",
   "Developmental anatomy"],
  "<b>Radiological anatomy</b> studies structure through imaging. It is the "
  "approach that connects this lecture's terminology to the imaging modalities "
  "on p. 29–35."),

# --- anatomical position, planes, terms (p. 8–12)
Q("A-07", "ANAT", "p. 8",
  "Why are anatomical descriptions always made relative to the anatomical "
  "position?",
  ["It gives one standard reference, so terms mean the same in any posture",
   "It is the posture in which cadavers are dissected and then preserved",
   "It is the position that minimizes organ overlap on plain radiographs",
   "It is the resting posture a patient adopts when lying on the table"],
  "The anatomical position is the <b>standard reference position</b>; "
  "structures are described relative to it, so \"the hand is distal to the "
  "elbow\" stays true whether the patient is standing, lying or has the arm "
  "raised. It is not defined by dissection, radiography or a resting "
  "posture."),
Q("A-08", "ANAT", "p. 8",
  "In the anatomical position, which way do the palms face?",
  ["Anteriorly", "Posteriorly", "Medially, toward the thighs", "Laterally"],
  "The figure on p. 8 shows the body upright, facing forward, with the upper "
  "limbs at the sides and the <b>palms facing anteriorly</b>. Palms facing the "
  "thighs is the relaxed standing posture, not the anatomical position – and "
  "that difference changes which forearm bone counts as lateral."),
Q("A-09", "ANAT", "p. 10",
  "The coronal (frontal) plane divides the body into which portions?",
  ["Anterior and posterior", "Right and left", "Superior and inferior",
   "Equal right and left halves"],
  "The <b>coronal</b> plane is vertical and separates front from back. A "
  "sagittal plane gives right and left portions, the median plane gives equal "
  "right and left halves, and the transverse plane gives superior and "
  "inferior portions."),
Q("A-10", "ANAT", "p. 10",
  "Which plane divides the body into superior and inferior portions?",
  ["Transverse", "Coronal", "Sagittal", "Median"],
  "The <b>transverse</b> plane – also called the horizontal plane – is the only "
  "one of the four that is horizontal. Coronal, sagittal and median planes are "
  "all vertical."),
Q("A-11", "ANAT", "p. 10",
  "How does the median plane differ from every other sagittal plane?",
  ["It passes through the exact midline, giving equal halves",
   "It is horizontal, whereas other sagittal planes are vertical",
   "It divides the body into front and back portions instead",
   "It is angled obliquely across the long axis of the body"],
  "All sagittal planes are vertical and divide right from left; the "
  "<b>median</b> (midsagittal) plane is the one that does so <b>at the precise "
  "midline</b>, giving equal halves. Front and back portions come from the "
  "coronal plane; a horizontal plane is transverse."),
Q("A-59", "ANAT", "p. 10",
  "Which vertical plane divides the body into right and left portions that "
  "need not be equal?",
  ["Sagittal", "Median", "Coronal", "Transverse"],
  "Any <b>sagittal</b> plane divides right from left. Only the median "
  "(midsagittal) plane does so at the exact midline, giving equal halves. "
  "The coronal plane divides front from back, and the transverse plane top "
  "from bottom."),
Q("A-12", "ANAT", "p. 44",
  "Which plane of section is shown in the image?",
  ["Coronal", "Sagittal", "Transverse", "Oblique"],
  "This is a <b>coronal</b> MRI of the head: both cerebral hemispheres and "
  "both lateral ventricles are seen side by side, as if looking at the face. "
  "A sagittal section would show one side in profile; a transverse section "
  "would be seen from below, like the abdominal CT on p. 43.",
  img="a44_coronal_mri.jpg", origin="repaired",
  flag="The slide lists both \"Transverse\" and \"Horizontal\", which p. 10 "
       "defines as the same plane. One of the pair was removed so each option "
       "is a different plane; the key is unchanged."),
Q("A-13", "ANAT", "p. 43",
  "Which plane of section is shown in the image?",
  ["Transverse (horizontal)", "Coronal", "Sagittal", "Oblique"],
  "An abdominal CT slice through the kidneys, aorta and a vertebral body is a "
  "<b>transverse</b> section, viewed by convention from the patient's feet. "
  "Coronal and sagittal sections are vertical and would show the organs "
  "stacked from top to bottom.",
  img="a43_axial_ct.jpg", origin="repaired",
  flag="As written, the slide offers \"Transverse\" and \"Horizontal\" as "
       "separate options, and both are correct – p. 10 gives them as synonyms. "
       "They are merged into one option here."),
Q("A-14", "ANAT", "p. 12",
  "Medial and lateral are defined relative to which reference?",
  ["The median sagittal plane", "The surface of the body",
   "The starting point of a structure", "The vertical axis of the body"],
  "Medial means closer to the <b>median sagittal plane</b>; lateral means "
  "farther from it. The surface of the body is the reference for superficial "
  "and deep, the starting point of a structure for proximal and distal, and "
  "the vertical axis for superior and inferior."),
Q("A-15", "ANAT", "p. 12",
  "Which statement uses a directional term correctly?",
  ["The hand is distal to the elbow joint",
   "The nose is distal to the ears",
   "The sternum is proximal to the heart",
   "The head is proximal to the shoulders"],
  "Proximal and distal compare positions along a structure from its starting "
  "point, so they suit the limbs: the <b>hand is distal to the elbow</b>. The "
  "nose is anterior and medial to the ears; the sternum is superficial to the "
  "heart; the head is superior to the shoulders."),
Q("A-60", "ANAT", "p. 12",
  "Compared with the wrist, the elbow is:",
  ["Proximal", "Distal", "Superficial", "Medial"],
  "Along the upper limb, measured from its starting point at the shoulder, "
  "the elbow is closer – <b>proximal</b> – and the wrist is distal. Superficial "
  "refers to depth from the body surface, and medial to the median plane."),
Q("A-16", "ANAT", "p. 12",
  "Which pair of terms is defined relative to the surface of the body?",
  ["Superficial and deep", "Anterior and posterior", "Medial and lateral",
   "Proximal and distal"],
  "<b>Superficial and deep</b> describe closeness to the body surface – the "
  "sternum is superficial to the heart. Anterior and posterior refer to front "
  "and back, medial and lateral to the median plane, and proximal and distal to "
  "a structure's starting point."),
Q("A-17", "ANAT", "p. 12",
  "The nose lies closer to the midline of the body than the ears do. Which "
  "term expresses this relationship?",
  ["Medial", "Anterior", "Proximal", "Superior"],
  "Closer to the median plane is <b>medial</b>. The nose is also anterior to "
  "the ears, which is why p. 12 uses it for both examples, but anterior "
  "describes its relation to the front of the body, not to the midline."),
Q("A-18", "ANAT", "p. 13",
  "Bending the elbow so the forearm moves toward the arm is which movement?",
  ["Flexion", "Extension", "Adduction", "Medial rotation"],
  "<b>Flexion</b> bends a joint, decreasing the angle between the bones; "
  "extension straightens it. Adduction moves a part toward the midline, and "
  "medial rotation turns it around its long axis."),
Q("A-19", "ANAT", "p. 13",
  "Raising the upper limb out to the side, away from the trunk, is which "
  "movement?",
  ["Abduction", "Adduction", "Flexion", "Elevation"],
  "Moving a limb <b>away from the median plane</b> is <b>abduction</b>; "
  "bringing it back is adduction. Raising the arm forward would be flexion, "
  "and elevation describes raising the shoulder girdle, as in a shrug."),
Q("A-20", "ANAT", "p. 13",
  "Tilting the head back to look at the ceiling, beyond the anatomical "
  "position, is which movement?",
  ["Hyperextension", "Flexion", "Elevation", "Retraction"],
  "Extension past the anatomical position is <b>hyperextension</b>. Flexion "
  "would bring the chin to the chest; elevation and retraction describe "
  "movements of the shoulder girdle and jaw, not bending at a joint."),
Q("A-21", "ANAT", "p. 13",
  "With the elbow flexed, the forearm is swung outward so the hand moves away "
  "from the abdomen. Which movement occurs at the shoulder?",
  ["Lateral (external) rotation", "Medial (internal) rotation", "Abduction",
   "Eversion"],
  "Turning the arm around its long axis so the front faces away from the "
  "midline is <b>lateral (external) rotation</b> – panel d on p. 13. Medial "
  "rotation brings the hand across the abdomen. Abduction lifts the arm away "
  "from the trunk rather than rotating it; eversion is a movement of the foot."),
Q("A-22", "ANAT", "p. 14",
  "Shrugging the shoulders toward the ears is which movement?",
  ["Elevation", "Protraction", "Abduction", "Hyperextension"],
  "Raising a part superiorly is <b>elevation</b>; lowering it is depression. "
  "Protraction moves the shoulder girdle forward, and abduction moves a limb "
  "away from the midline."),
Q("A-23", "ANAT", "p. 14",
  "Reaching forward with the shoulder girdle, as in a punch, is which "
  "movement?",
  ["Protraction", "Retraction", "Elevation", "Lateral rotation"],
  "Moving a part <b>anteriorly</b> is <b>protraction</b>; pulling it "
  "posteriorly, as in bracing the shoulders back, is retraction. Elevation "
  "raises the girdle; lateral rotation turns the arm."),
Q("A-24", "ANAT", "p. 14",
  "Turning the sole of the foot so it faces medially is which movement?",
  ["Inversion", "Eversion", "Medial rotation", "Adduction"],
  "Sole facing <b>medially</b> is <b>inversion</b>; sole facing laterally is "
  "eversion. These terms are specific to the foot. Medial rotation and "
  "adduction describe movements of a whole limb."),

# --- systems and specialties (p. 16–28)
Q("A-25", "ANAT", "p. 16",
  "A patient with a disorder of the renal system would most likely be seen by "
  "which specialty?",
  ["Nephrology", "Gastroenterology", "Endocrinology", "Hematology"],
  "The lecture pairs the renal system with <b>urology and nephrology</b>. "
  "Gastroenterology covers the digestive system, endocrinology the endocrine "
  "system, and hematology the cardiovascular and lymphatic systems."),
Q("A-26", "ANAT", "p. 16",
  "Orthopedics is the clinical specialty for which body system?",
  ["Musculoskeletal", "Integumentary", "Nervous", "Lymphatic"],
  "<b>Musculoskeletal → orthopedics.</b> Integumentary is dermatology, "
  "nervous is neurology (and psychiatry, ophthalmology, otolaryngology), and "
  "lymphatic is listed with hematology."),
Q("A-27", "ANAT", "p. 16",
  "In the lecture's table, ophthalmology and otolaryngology are listed under "
  "which body system?",
  ["Nervous", "Integumentary", "Immune", "Respiratory"],
  "The <b>nervous</b> system row lists neurology, psychiatry, ophthalmology "
  "and otolaryngology – the eye and ear are sensory organs. Integumentary is "
  "dermatology, immune is immunology and oncology, and respiratory is "
  "pulmonology."),
Q("A-28", "ANAT", "p. 17",
  "Which of the following is one of the three types of cartilage?",
  ["Elastic", "Spongy", "Compact", "Synovial"],
  "The three cartilages are <b>hyaline, elastic and fibrocartilage</b>. "
  "Spongy and compact are the two types of bone, and synovial is a type of "
  "joint."),
Q("A-29", "ANAT", "p. 17",
  "What are the two types of bone?",
  ["Spongy and compact", "Hyaline and elastic", "Solid and synovial",
   "Axial and appendicular"],
  "Bone is <b>spongy</b> (trabecular) or <b>compact</b> (cortical). Hyaline "
  "and elastic are cartilages, solid and synovial are joint types, and axial "
  "and appendicular are the two divisions of the skeleton rather than kinds "
  "of bone tissue."),
Q("A-30", "ANAT", "p. 18",
  "A joint that has a joint cavity is classified as:",
  ["Synovial", "Solid", "Fibrous", "Cartilaginous"],
  "The lecture divides joints into <b>solid</b> (no joint cavity) and "
  "<b>synovial</b> (a joint cavity). Fibrous and cartilaginous joints are the "
  "two kinds of solid joint, so neither has a cavity."),
Q("A-31", "ANAT", "p. 19",
  "The wall of the heart is made of which type of muscle?",
  ["Cardiac", "Skeletal", "Smooth"],
  "<b>Cardiac</b> muscle forms the heart wall. Skeletal muscle moves the "
  "skeleton under voluntary control, and smooth muscle lines hollow organs "
  "such as the gut and blood vessels.",
  beyond=True),
Q("A-32", "ANAT", "p. 20",
  "A broad, flat sheet of dense connective tissue that attaches a muscle is "
  "called:",
  ["An aponeurosis", "A tendon", "Deep fascia", "A ligament"],
  "Muscles attach through <b>tendons and aponeuroses</b>. A tendon is a cord; "
  "an <b>aponeurosis</b> is the flat, sheet-like form. Deep fascia wraps "
  "muscles rather than attaching them, and a ligament joins bone to bone.",
  beyond=True),
Q("A-33", "ANAT", "p. 21",
  "Which layer of the skin is the outermost?",
  ["Epidermis", "Dermis", "Superficial fascia", "Deep fascia"],
  "The <b>epidermis</b> lies on top of the dermis. Beneath the skin are the "
  "superficial fascia and then the deep fascia, which the lecture groups "
  "with the integumentary system.",
  beyond=True),
Q("A-34", "ANAT", "p. 21",
  "In this lecture, the superficial and deep fascia are grouped with which "
  "system?",
  ["Integumentary", "Musculoskeletal", "Lymphatic", "Nervous"],
  "The integumentary slide lists <b>skin</b> (epidermis, dermis) and "
  "<b>fascia</b> (superficial, deep). Tendons and aponeuroses, which the "
  "fascia is easily confused with, are under the musculoskeletal system."),
Q("A-35", "ANAT", "p. 22",
  "The central nervous system consists of:",
  ["The brain and spinal cord", "The brain and cranial nerves",
   "The spinal cord and spinal nerves", "The brain, spinal cord and ganglia"],
  "<b>CNS = brain and spinal cord.</b> Cranial nerves, spinal nerves and "
  "ganglia all belong to the peripheral nervous system."),
Q("A-36", "ANAT", "p. 22",
  "Nerve fibers that carry sensation from the stomach wall to the CNS are "
  "classified as:",
  ["Visceral afferent", "Somatic afferent", "Visceral efferent",
   "Somatic efferent"],
  "The stomach is an organ, so the fibers are <b>visceral</b>; carrying "
  "sensation toward the CNS makes them <b>afferent</b>. Somatic fibers serve "
  "the body wall and limbs, and efferent fibers carry motor commands away "
  "from the CNS.",
  flag="Slide p. 22 labels the visceral branch \"somatic sensory "
       "(afferents)\" and \"somatic motor (efferent)\" – a copy-over from the "
       "somatic branch above it. It should read visceral afferent and "
       "visceral efferent."),
Q("A-61", "ANAT", "p. 22",
  "Nerve fibers that carry motor commands from the CNS to the muscle of the "
  "gut wall are classified as:",
  ["Visceral efferent", "Visceral afferent", "Somatic efferent",
   "Somatic afferent"],
  "The gut wall is an organ, so the fibers are <b>visceral</b>; carrying "
  "commands away from the CNS makes them <b>efferent</b> (motor). Somatic "
  "efferent fibers supply skeletal muscle of the body wall and limbs.",
  flag="Slide p. 22 mislabels this branch \"somatic motor (efferent)\" under "
       "the visceral heading; see the note on the visceral afferent "
       "question."),
Q("A-37", "ANAT", "p. 40",
  "Which of the following organs/structures belongs to the system that "
  "circulates oxygen in the body?",
  ["Lymphatics", "Aorta", "Spleen", "Uterus", "Ureters"], ans=1,
  why="The <b>aorta</b> belongs to the cardiovascular system – the heart and "
  "its arteries, veins and capillaries. Lymphatics and the spleen are "
  "lymphatic, the uterus is reproductive, and the ureters are urinary.",
  origin="prof"),
Q("A-38", "ANAT", "p. 41",
  "Which of the following organs/structures belongs to the system that "
  "removes CO<sub>2</sub> from the body?",
  ["Lymphatics", "Lungs", "Spleen", "Uterus", "Ureters"], ans=1,
  why="The respiratory system – nose and <b>lungs</b> – brings in oxygen and "
  "sends out carbon dioxide. The ureters remove waste in urine, not "
  "CO<sub>2</sub>.",
  origin="prof"),
Q("A-39", "ANAT", "p. 42",
  "Which of the following is an accessory gland of the gastrointestinal "
  "system?",
  ["Lymphatics", "Pancreas", "Spleen", "Kidneys", "Urinary bladder"], ans=1,
  why="The digestive system includes the mouth, stomach, intestines and "
  "<b>the glands that help break down food</b> – the salivary glands, liver "
  "and <b>pancreas</b>. The spleen sits beside the stomach but is a lymphatic "
  "organ; the kidneys and bladder are urinary.",
  origin="repaired", beyond=True,
  flag="As written (lymphatics, heart, spleen, kidneys, urinary bladder), "
       "none of the options is a GI accessory gland. \"Heart\" was replaced "
       "with \"Pancreas\". The slides never name the glands, so the key is "
       "beyond the slides."),
Q("A-40", "ANAT", "p. 26",
  "Removing waste and water from the body through the kidneys is the main "
  "role of which system?",
  ["Urinary", "Digestive", "Lymphatic", "Integumentary"],
  "The <b>urinary</b> system removes waste and water through the kidneys and "
  "urinary bladder. The digestive system breaks down food; the lymphatic "
  "system returns tissue fluid and serves immunity; the integumentary system "
  "is skin and fascia."),
Q("A-41", "ANAT", "p. 27–28",
  "Which structures are the female gonads?",
  ["Ovaries", "Uterus", "Uterine tubes", "Mammary glands"],
  "The gonads produce gametes: the <b>ovaries</b> (eggs) in the female and the "
  "testes (sperm) in the male. The uterus provides the environment for the "
  "developing fetus; the uterine tubes carry the ovum toward it."),

# --- imaging modalities (p. 29–35, plus LO 4)
Q("A-42", "ANAT", "p. 29",
  "Which imaging modality produced this image?",
  ["Ultrasound", "Computed tomography", "MRI", "Plain radiograph"],
  "The fan-shaped, grainy grey image with a depth scale along its edge is an "
  "<b>ultrasound</b> (sonogram). On p. 29 it shows hydronephrosis – dilated "
  "renal collecting spaces. Ultrasound is the natural first test for the "
  "kidney because it is real-time and uses no ionizing radiation.",
  img="a29_us.jpg"),
Q("A-43", "ANAT", "p. 29",
  "Which imaging modality produced this image of the head?",
  ["Computed tomography", "MRI", "Plain radiograph", "Ultrasound"],
  "This is <b>CT</b>: a transverse slice in which the skull is bright white, as "
  "bone is on a plain radiograph (p. 33). On p. 29 it shows subarachnoid "
  "hemorrhage. On MRI, cortical bone would be dark and the brain far more "
  "detailed.",
  img="a29_ct.jpg"),
Q("A-44", "ANAT", "p. 29",
  "Which imaging modality produced this sagittal image of the lumbar spine?",
  ["MRI", "Computed tomography", "Plain radiograph", "Ultrasound"],
  "This is <b>MRI</b>: a sagittal section with detailed soft tissue, including "
  "the discs and marrow, where CT would show bright bone. On p. 29 it "
  "shows osteomyelitis of a vertebral body. MRI signal comes from hydrogen "
  "protons in tissue water, which is why marrow and discs are so well shown.",
  img="a29_mri.jpg"),
Q("A-45", "ANAT", "p. 29",
  "Which imaging modality produced this image?",
  ["Plain radiograph", "Computed tomography", "MRI", "PET"],
  "A single projection of the whole chest with white ribs and dark air-filled "
  "lungs is a <b>plain radiograph</b>. On p. 29 the circle marks a round "
  "pneumonia. CT would show a cross-sectional slice rather than a "
  "superimposed projection.",
  img="a29_xray.jpg"),
Q("A-46", "ANAT", "p. 37",
  "Which of the following radiological modality is shown in the image?",
  ["X-rays", "fMRI", "CT scan", "MRI", "Ultrasound"], ans=0,
  why="This is a contrast <b>x-ray</b>: barium sulfate fills and outlines the "
  "colon (a barium enema). Contrast agents increase attenuation, so the "
  "barium-filled bowel appears white on a single projection image (p. 31).",
  img="a37_barium.jpg", origin="prof"),
Q("A-47", "ANAT", "p. 38",
  "Which radiological modality is shown in the image?",
  ["X-rays", "PET-CT", "CT scan", "MRI", "Ultrasound"], ans=1,
  why="Three panels of the same patient – a PET image, the matching CT, and "
  "the two fused in color – make this <b>PET-CT</b>. The color map shows where "
  "the positron-emitting tracer collected, laid over CT anatomy.",
  img="a38_petct.jpg", origin="repaired",
  flag="As written, the options are X-rays, fMRI, CT scan, MRI and Ultrasound "
       "– there is no PET option, so the image has no correct answer. \"fMRI\" "
       "was replaced with \"PET-CT\". \"CT scan\" is the closest original "
       "option, but it describes only one of the three panels."),
Q("A-48", "ANAT", "p. 34, 39",
  "Which radiological modality uses radio waves to create its image?",
  ["MRI", "X-rays", "CT scan", "Ultrasound", "Nuclear medicine"],
  "<b>MRI</b> uses radio waves to deflect aligned hydrogen protons, and builds "
  "the image from their return. X-rays and CT use ionizing x-rays, ultrasound "
  "uses sound, and nuclear medicine detects gamma rays.",
  origin="repaired",
  flag="The slide asks which modality \"does not use radio waves\", with "
       "options X-rays, fMRI, CT, MRI and Ultrasound. Three of those – x-ray, "
       "CT and ultrasound – are correct. The polarity was reversed and fMRI "
       "dropped (it also uses radio waves), leaving one correct answer."),
Q("A-49", "ANAT", "p. 30–31",
  "On a plain radiograph, why does bone appear white?",
  ["Bone attenuates more of the x-ray beam than the soft tissues do",
   "Bone emits more gamma radiation than the surrounding soft tissues",
   "Bone holds more free hydrogen protons than the soft tissues do",
   "Bone reflects more sound waves back than the soft tissues do"],
  "Dense bone <b>attenuates</b> (absorbs) more of the beam, so less reaches the "
  "detector and the area stays white. The distractors each describe a "
  "different modality: gamma emission is nuclear medicine, hydrogen protons "
  "are MRI, and reflected sound is ultrasound."),
Q("A-50", "ANAT", "p. 31",
  "Which contrast agent is used to increase the visibility of the bowel on "
  "x-ray imaging?",
  ["Barium sulfate", "Gadolinium", "Fluorodeoxyglucose (FDG)",
   "Technetium-99m"],
  "<b>Barium sulfate</b> and iodine increase x-ray attenuation, which is how "
  "the colon on p. 37 is outlined. Gadolinium is an MRI contrast agent; FDG "
  "is the PET tracer; technetium-99m is a gamma-emitting nuclear medicine "
  "tracer. (The distractors themselves are beyond the slides.)"),
Q("A-51", "ANAT", "p. 32",
  "Ultrasound waves are generated by:",
  ["Piezoelectric materials", "A cathode ray tube",
   "Radio waves deflecting protons", "Radionuclides decaying in the body"],
  "<b>Piezoelectric materials</b> in the transducer convert electrical energy "
  "into high-frequency sound. A cathode ray tube generates x-rays; radio "
  "waves deflecting protons is MRI; radionuclides are nuclear medicine and "
  "PET."),
Q("A-52", "ANAT", "p. 32",
  "Which modality is commonly used to assess a fetus, displaying a real-time "
  "image?",
  ["Ultrasound", "Computed tomography", "Plain radiograph",
   "Nuclear medicine"],
  "<b>Ultrasound</b> produces a real-time sonogram and is commonly used for "
  "the abdomen, the fetus and the musculoskeletal system. CT, plain film and "
  "nuclear medicine all expose the fetus to ionizing radiation."),
Q("A-53", "ANAT", "p. 33",
  "Which modality produces serial images by passing an x-ray tube around the "
  "body?",
  ["Computed tomography", "Fluoroscopy", "MRI", "PET"],
  "<b>CT</b> takes serial radiographs as the tube circles the patient and "
  "reconstructs them as slices; bone is bright, as on a plain film. "
  "Fluoroscopy is continuous x-ray imaging from a fixed tube; MRI and PET use "
  "no x-ray tube at all."),
Q("A-54", "ANAT", "p. 34",
  "What is the source of the signal in MRI?",
  ["Hydrogen protons in tissue water returning to alignment after deflection",
   "Gamma rays emitted from the nuclei of radionuclides injected into tissue",
   "Echoes of sound waves reflected at interfaces between different tissues",
   "X-rays attenuated to different degrees by tissues of differing density"],
  "Free protons in the <b>hydrogen atoms of tissue water</b> act like mini "
  "magnets. Radio waves deflect them, and the image is built from their "
  "<b>return to the pre-deflected state</b>. The other options describe "
  "nuclear medicine, ultrasound and x-ray/CT respectively."),
Q("A-55", "ANAT", "p. 35",
  "Nuclear medicine imaging detects:",
  ["Gamma rays produced from the nucleus of the atom",
   "X-rays generated by a cathode ray tube",
   "Radio waves released by realigning protons",
   "Sound waves reflected back from organ surfaces"],
  "Nuclear medicine images <b>gamma rays from atomic nuclei</b> of a tracer "
  "given to the patient. Cathode-tube x-rays are radiography and CT, "
  "realigning protons are MRI, and reflected sound is ultrasound."),
Q("A-56", "ANAT", "p. 35",
  "Positron emission tomography (PET) records the position of:",
  ["Positron-emitting radionuclides introduced into the body",
   "Hydrogen protons realigning after a radiofrequency pulse",
   "Barium sulfate outlining the lumen of the bowel wall",
   "Sound echoes reflected back from organ boundaries"],
  "<b>PET</b> localizes <b>positron-emitting radionuclides</b> given to the "
  "patient, which is why it is so often fused with CT for anatomy (p. 38). "
  "Realigning protons is MRI, barium is x-ray contrast, and echoes are "
  "ultrasound."),
Q("A-57", "ANAT", "LO 4 – not on the slides",
  "Which modality provides continuous, real-time x-ray imaging – for example, "
  "watching barium pass down the esophagus as the patient swallows?",
  ["Fluoroscopy", "Computed tomography", "Plain radiograph", "Ultrasound"],
  "<b>Fluoroscopy</b> is moving, real-time x-ray imaging, often with contrast. "
  "A plain radiograph is a single still exposure, CT reconstructs slices, "
  "and ultrasound is real-time but uses sound rather than x-rays.",
  beyond=True,
  flag="Learning objective 4 lists fluoroscopy, but no slide covers it."),
Q("A-58", "ANAT", "LO 4 – not on the slides",
  "Placing a stent through a catheter under image guidance, without open "
  "surgery, belongs to which field?",
  ["Interventional radiology", "Nuclear medicine imaging",
   "Positron emission tomography", "Diagnostic ultrasound"],
  "<b>Interventional radiology</b> uses imaging to guide minimally invasive "
  "procedures – catheters, stents, drains, biopsies. The other three are "
  "diagnostic modalities that create images rather than treat.",
  beyond=True,
  flag="Learning objective 4 lists interventional radiology, but no slide "
       "covers it."),

# ============================== EPITHELIUM ==============================
# --- basic tissues and definition (p. 4–5)
Q("E-01", "EPI", "p. 4",
  "Which basic tissue is specialized for communication?",
  ["Nerve", "Epithelium", "Connective tissue", "Muscle"],
  "The lecture pairs each basic tissue with its role: <b>nerve – "
  "communication</b>, epithelium – covering and lining, connective tissue – "
  "support, muscle – movement."),
Q("E-02", "EPI", "p. 4",
  "Which basic tissue is specialized for support?",
  ["Connective tissue", "Epithelium", "Nerve", "Muscle"],
  "<b>Connective tissue</b> supports. Epithelium covers and lines, nerve "
  "communicates, and muscle moves. The basement membrane (p. 25) is where "
  "epithelium meets that supporting connective tissue."),
Q("E-03", "EPI", "p. 5",
  "Which description best defines epithelium?",
  ["Sheets of continuous cells that cover or line surfaces, tubes and cavities",
   "Scattered cells in an abundant extracellular matrix that support organs",
   "Elongated contractile cells that shorten to move body parts and organs",
   "Excitable cells that carry electrical signals between distant regions"],
  "Epithelium is <b>sheets of continuous cells</b> covering or lining surfaces "
  "– tubes, cavities, organs, glands – built from cells and a basement "
  "membrane. Scattered cells in abundant matrix describe connective tissue; "
  "contractile cells are muscle; excitable cells are nerve."),
Q("E-04", "EPI", "p. 5",
  "Epithelium is constructed from cells and:",
  ["A basement membrane", "Abundant ground substance",
   "A surrounding myelin sheath", "Interwoven collagen bundles"],
  "The lecture states epithelium is <b>cells plus a basement membrane</b>. "
  "Epithelial cells are tightly packed with little intercellular material – "
  "abundant ground substance and collagen bundles are features of connective "
  "tissue, and myelin belongs to nerve."),
Q("E-05", "EPI", "p. 5",
  "Which of the following is NOT one of the functions of epithelium listed in "
  "the lecture?",
  ["Contraction", "Absorption", "Secretion", "Permeability"],
  "The listed functions are <b>protection, absorption, secretion, excretion "
  "and permeability</b>. Contraction is the function of muscle tissue."),

# --- classification (p. 8–16)
Q("E-06", "EPI", "p. 8",
  "Covering epithelia are classified by:",
  ["The number of cell layers and the shape of the surface cells",
   "The number of cell layers and the shape of the basal cells",
   "The presence of cilia and the type of cell junction present",
   "The thickness of the basement membrane and the gland type"],
  "Classification uses the <b>number of layers</b> (simple vs stratified) and "
  "the <b>shape of the surface cells</b>. The basal-cell trap matters most in "
  "stratified squamous epithelium, where the basal cells are cuboidal or "
  "columnar but the tissue is named for its flattened surface."),
Q("E-07", "EPI", "p. 8, 18",
  "A multilayered epithelium has cuboidal cells at its base and flattened "
  "cells at its surface. How is it classified?",
  ["Stratified squamous", "Stratified cuboidal", "Transitional",
   "Pseudostratified columnar"],
  "It is named by the <b>surface</b> cells: flattened means <b>squamous</b>, "
  "and multiple layers means stratified. Stratified cuboidal would have "
  "cuboidal surface cells; transitional has dome-shaped surface cells; "
  "pseudostratified is really a single layer."),
Q("E-08", "EPI", "p. 11, 13",
  "Which statement about pseudostratified epithelium is correct?",
  ["It is one cell layer, although its nuclei sit at different heights",
   "It has several layers, and only the top layer reaches the surface",
   "Its cells lack nuclei, so the layer appears pale on routine stains",
   "Its surface cells are dome-shaped and flatten when the organ fills"],
  "Pseudostratified epithelium <b>appears stratified but is one cell "
  "layer</b>: every cell rests on the basement membrane, but the nuclei sit at "
  "different levels. The cross-check on p. 11 is explicit that its cells "
  "<b>do</b> contain nuclei, and dome-shaped surface cells are "
  "transitional."),
Q("E-09", "EPI", "p. 13",
  "The simple squamous epithelium lining the body cavities is called:",
  ["Mesothelium", "Endothelium", "Transitional epithelium",
   "Keratinized epithelium"],
  "Simple epithelium in <b>body cavities</b> is <b>mesothelium</b> (pleura, "
  "peritoneum, pericardium). In <b>blood vessels</b> it is endothelium. "
  "Transitional epithelium lines the urinary bladder; keratinized epithelium "
  "is the epidermis."),
Q("E-10", "EPI", "p. 13, 18",
  "The arrows mark flattened nuclei in the single cell layer lining this "
  "vessel, which contains red blood cells. What is this lining called?",
  ["Endothelium", "Mesothelium", "Stratified squamous epithelium",
   "Simple cuboidal epithelium"],
  "A single layer of flat cells lining a blood vessel is <b>endothelium</b>. "
  "In section, simple squamous nuclei look spindle-like, as here. Mesothelium "
  "is the same kind of epithelium lining body cavities rather than vessels.",
  img="e18_endothelium.jpg"),
Q("E-11", "EPI", "p. 13",
  "In a single-layered epithelium, the nuclei lie near the base of each cell. "
  "What shape are the cells most likely to be?",
  ["Columnar", "Squamous", "Cuboidal", "Umbrella-shaped"],
  "The lecture's visualization rule: nuclei in the <b>lower part</b> of the "
  "cell suggest the cells are <b>columnar</b> – tall enough to leave cytoplasm "
  "above the nucleus. Cuboidal cells have central round nuclei; squamous "
  "nuclei are flat; umbrella cells sit on the surface of transitional "
  "epithelium."),
Q("E-12", "EPI", "p. 16",
  "Dome-shaped (umbrella) cells at the surface of an epithelium indicate "
  "which type?",
  ["Transitional", "Non-keratinized stratified squamous",
   "Pseudostratified columnar", "Stratified cuboidal"],
  "<b>Umbrella or dome cells</b> on the surface are the signature of "
  "<b>transitional</b> epithelium. Non-keratinized stratified squamous "
  "epithelium flattens toward its surface; pseudostratified and stratified "
  "cuboidal epithelia have no dome cells."),
Q("E-13", "EPI", "p. 13, 16",
  "What allows the lining of the urinary bladder to accommodate filling?",
  ["Its cells can change shape as the organ is stretched",
   "Its surface cells are keratinized and resist the urine",
   "Its single cell layer is folded into pleats that unfold",
   "Its cells are held by gap junctions that slide apart"],
  "In transitional epithelium, <b>all the cells can change shape when the "
  "organ is stretched</b> – the dome cells flatten as the bladder fills. It is "
  "multilayered, not a folded single layer, and it is not keratinized. Gap "
  "junctions communicate; they do not let cells slide apart."),
Q("E-14", "EPI", "p. 8, 17",
  "Which epithelium lines the trachea?",
  ["Pseudostratified columnar", "Simple columnar", "Stratified squamous",
   "Transitional"],
  "The trachea is the lecture's example of <b>pseudostratified</b> columnar "
  "epithelium, and it is ciliated – which is why primary ciliary dyskinesia "
  "affects the airway (p. 27). Simple columnar lines the stomach; stratified "
  "squamous lines the esophagus; transitional lines the bladder."),
Q("E-15", "EPI", "p. 17",
  "Which epithelium lines the lung alveoli?",
  ["Simple squamous", "Simple cuboidal", "Pseudostratified columnar",
   "Stratified squamous"],
  "Alveoli are lined by <b>simple squamous</b> epithelium – a single layer of "
  "flat cells, the thinnest possible barrier for gas diffusion. "
  "Pseudostratified epithelium lines the larger airways, not the alveoli."),
Q("E-16", "EPI", "p. 17–18",
  "Which epithelium lines the kidney tubules?",
  ["Simple cuboidal", "Simple squamous", "Transitional",
   "Stratified cuboidal"],
  "Kidney tubules are the lecture's example of <b>simple cuboidal</b> "
  "epithelium – one layer of cube-shaped cells with central, spherical nuclei. "
  "Transitional epithelium begins downstream, in the urinary tract."),
Q("E-17", "EPI", "p. 17",
  "Which epithelium lines the stomach?",
  ["Simple columnar", "Stratified squamous", "Pseudostratified columnar",
   "Simple cuboidal"],
  "The stomach is lined by <b>simple columnar</b> epithelium, suited to "
  "secretion and absorption. The esophagus just above it is stratified "
  "squamous, so the lining changes abruptly at the junction."),
Q("E-18", "EPI", "p. 17–18",
  "Which epithelium lines the esophagus?",
  ["Non-keratinized stratified squamous", "Keratinized stratified squamous",
   "Simple columnar", "Transitional"],
  "The esophagus, mouth and vagina are wet surfaces lined by "
  "<b>non-keratinized</b> stratified squamous epithelium. The keratinized form "
  "is the epidermis of the skin."),
Q("E-19", "EPI", "p. 18",
  "Where is keratinized stratified squamous epithelium found?",
  ["Epidermis of the skin", "Lining of the esophagus", "Lining of the vagina",
   "Lining of the mouth"],
  "<b>Keratinized</b> stratified squamous epithelium forms the <b>epidermis</b>. "
  "The mouth, esophagus and vagina are the lecture's examples of wet surfaces "
  "lined by the non-keratinized form."),
Q("E-20", "EPI", "p. 17–18",
  "Stratified cuboidal epithelium, usually two cell layers thick, is found "
  "in:",
  ["Ducts of sweat glands", "Kidney tubules", "Lung alveoli",
   "Urinary bladder"],
  "<b>Sweat gland ducts</b> are the lecture's example of stratified cuboidal "
  "epithelium. Kidney tubules are simple cuboidal, alveoli are simple "
  "squamous, and the bladder is transitional."),
Q("E-21", "EPI", "p. 19",
  "Stratified columnar epithelium is found in a few places, including:",
  ["Parts of the male urethra", "Kidney tubules", "Lung alveoli",
   "Lining of the stomach"],
  "Stratified columnar epithelium is rare – the lecture names the "
  "<b>epiglottis, urethra and some gland ducts</b>. Kidney tubules are simple "
  "cuboidal, alveoli simple squamous, and the stomach simple columnar.",
  flag="The decks disagree on salivary ducts: p. 17 labels stratified "
       "columnar \"salivary duct\", while the p. 18 caption lists salivary "
       "ducts under stratified cuboidal. Both occur along the larger ducts, "
       "so neither is used as a key here."),
Q("E-22", "EPI", "p. 17",
  "Which function best fits simple squamous epithelium?",
  ["Diffusion and filtration", "Protection from abrasion",
   "Expansion and stretching", "Secretion of mucus"],
  "A single layer of flat cells is the thinnest barrier, which suits "
  "<b>diffusion and filtration</b> – alveoli, capillaries, the glomerular "
  "capsule. Protection needs many layers; stretching is transitional "
  "epithelium; mucus secretion is typical of columnar epithelium."),
Q("E-23", "EPI", "p. 17–18",
  "Which function best fits stratified squamous epithelium?",
  ["Protection of underlying tissue from abrasion",
   "Diffusion and filtration across a thin barrier",
   "Expansion and stretching as the organ fills",
   "Absorption and secretion at a free surface"],
  "Many layers of cells that are shed and replaced from below make stratified "
  "squamous epithelium <b>protective</b> – the skin, mouth and esophagus. "
  "Expansion and stretching is transitional epithelium.",
  beyond=True,
  flag="The summary table on p. 17 gives stratified squamous the function "
       "\"allows expansion and stretching\" – the transitional row's "
       "function, repeated. It is protection. The same table describes "
       "ciliated columnar as \"many layers of flat cells\", which is also "
       "wrong."),

# --- histology recognition (image stems, p. 17–19)
Q("E-24", "EPI", "p. 17",
  "Identify the epithelium lining these air spaces.",
  ["Simple squamous", "Simple cuboidal", "Stratified squamous",
   "Transitional"],
  "Very thin walls with flattened nuclei around large air spaces: <b>simple "
  "squamous</b> epithelium of the lung alveoli. Cuboidal cells would give a "
  "row of round central nuclei; stratified squamous would be many layers "
  "thick.",
  img="e17_simple_squamous.jpg"),
Q("E-25", "EPI", "p. 17",
  "Identify the epithelium lining these tubules.",
  ["Simple cuboidal", "Simple squamous", "Stratified cuboidal",
   "Simple columnar"],
  "One row of cells about as tall as they are wide, each with a round central "
  "nucleus, around a lumen: <b>simple cuboidal</b> (kidney tubule). "
  "Stratified cuboidal would show two layers of nuclei; columnar cells are "
  "taller, with basal nuclei.",
  img="e17_simple_cuboidal.jpg"),
Q("E-26", "EPI", "p. 17",
  "Identify the epithelium covering these projections.",
  ["Simple columnar", "Pseudostratified columnar", "Simple cuboidal",
   "Stratified columnar"],
  "A single row of tall cells with nuclei lined up near the base: <b>simple "
  "columnar</b> (stomach). Pseudostratified epithelium would show nuclei at "
  "several different heights; stratified columnar would show more than one "
  "layer.",
  img="e17_simple_columnar.jpg"),
Q("E-27", "EPI", "p. 17",
  "Identify this epithelium.",
  ["Transitional", "Non-keratinized stratified squamous",
   "Stratified cuboidal", "Pseudostratified columnar"],
  "Several layers with large, rounded, dome-shaped cells bulging at the "
  "surface: <b>transitional</b> epithelium (urinary bladder). Stratified "
  "squamous epithelium flattens toward its surface instead.",
  img="e17_transitional.jpg"),
Q("E-28", "EPI", "p. 17",
  "Identify this epithelium.",
  ["Non-keratinized stratified squamous", "Keratinized stratified squamous",
   "Transitional", "Stratified columnar"],
  "Many layers, with round nuclei at the base becoming flat toward the "
  "surface, and <b>nuclei still present in the surface cells</b>: "
  "non-keratinized stratified squamous (esophagus). A keratinized epithelium "
  "would be topped by an anucleate, pink keratin layer.",
  img="e17_strat_squamous.jpg"),
Q("E-29", "EPI", "p. 18",
  "Identify this epithelium.",
  ["Keratinized stratified squamous", "Non-keratinized stratified squamous",
   "Transitional", "Stratified cuboidal"],
  "Stratified squamous cells topped by thick, pink, flaky layers <b>without "
  "nuclei</b>: that surface is keratin, making this <b>keratinized</b> "
  "stratified squamous epithelium (skin). Compare the esophagus, where the "
  "surface cells keep their nuclei.",
  img="e18_keratinized.jpg"),
Q("E-30", "EPI", "p. 17",
  "Identify the epithelium lining these ducts.",
  ["Stratified cuboidal", "Simple cuboidal", "Simple squamous",
   "Transitional"],
  "Two layers of cube-shaped cells around a small lumen: <b>stratified "
  "cuboidal</b> epithelium (sweat gland duct). Simple cuboidal would be a "
  "single ring of nuclei.",
  img="e17_strat_cuboidal.jpg"),
Q("E-31", "EPI", "p. 17",
  "Identify this epithelium.",
  ["Stratified columnar", "Pseudostratified columnar", "Simple columnar",
   "Transitional"],
  "Tall surface cells sitting on a separate basal layer of smaller cells: "
  "<b>stratified columnar</b> (salivary duct in the p. 17 panel). "
  "Pseudostratified epithelium also shows nuclei at several levels, but it has "
  "no discrete second layer, and it is usually ciliated with goblet cells.",
  img="e17_strat_columnar.jpg"),
Q("E-32", "EPI", "p. 17, 19",
  "Identify this epithelium.",
  ["Pseudostratified columnar", "Stratified columnar", "Simple columnar",
   "Transitional"],
  "Nuclei at many different heights, but every cell reaches the basement "
  "membrane, with cilia fringing the surface: <b>pseudostratified</b> "
  "columnar (trachea). The scattered heights are what make it look – falsely "
  "– stratified.",
  img="e19_pseudostrat.jpg"),
Q("E-33", "EPI", "p. 19",
  "These follicles of cells surround a pool of stored secretion. Which "
  "gland type is shown?",
  ["Endocrine", "Exocrine", "Compound exocrine", "Holocrine"],
  "Glandular epithelium arranged around stored colloid, with no duct, is an "
  "<b>endocrine</b> gland – the thyroid in the p. 19 panel. Endocrine glands "
  "release hormones into the blood; exocrine glands release their products "
  "through ducts onto a surface.",
  img="e19_endocrine.jpg"),

# --- glands (p. 14–16, 19)
Q("E-34", "EPI", "p. 16",
  "Epithelial cells are arranged in a circle around a central lumen, and all "
  "are committed to secreting a common product. What kind of epithelium is "
  "this?",
  ["Glandular", "Transitional", "Pseudostratified", "Stratified squamous"],
  "The lecture's rule: a <b>circular arrangement with a lumen</b>, cells "
  "sharing one secretory purpose, is <b>glandular</b> epithelium (acinar or "
  "tubular). Transitional epithelium is identified by dome cells, and "
  "pseudostratified by nuclei at mixed heights.",
  img="e19_exocrine.jpg"),
Q("E-35", "EPI", "p. 15, 19",
  "A gland that releases its secretion through a duct onto a surface is:",
  ["Exocrine", "Endocrine", "Holocrine", "Apocrine"],
  "<b>Exocrine</b> glands secrete through ducts – into the gut or onto the "
  "skin. Endocrine glands have no ducts and release hormones into the blood. "
  "Holocrine and apocrine describe how the cell releases its product, not "
  "where the product goes."),
Q("E-36", "EPI", "p. 15",
  "Exocrine glands are classified as simple or compound based on:",
  ["The branching of the duct", "The shape of the secretory unit",
   "The mechanism of secretion", "Whether the product enters blood"],
  "Simple vs compound is about the <b>duct</b>: unbranched or branched. "
  "Tubular vs acinar describes the shape of the secretory unit; "
  "merocrine/apocrine/holocrine is the mechanism; exocrine vs endocrine is "
  "where the product goes."),
Q("E-37", "EPI", "p. 15",
  "Describing a gland's secretory unit as tubular or acinar classifies it by:",
  ["The shape of the secretory portion", "The branching pattern of the duct",
   "The mechanism by which it secretes", "The number of cell layers it has"],
  "Tubular (tube-shaped) and acinar (flask- or berry-shaped) describe the "
  "<b>shape of the secretory unit</b>. Duct branching gives simple vs "
  "compound; release mechanism gives merocrine, apocrine or holocrine."),
Q("E-38", "EPI", "p. 15",
  "In holocrine secretion, the product is released by:",
  ["Breakdown of the whole secretory cell",
   "Exocytosis from membrane-bound vesicles",
   "Pinching off of the apical cytoplasm",
   "Diffusion across the basal membrane"],
  "<b>Holocrine</b> means the <b>whole cell</b> disintegrates and becomes the "
  "secretion (the sebaceous gland is the classic example). Exocytosis is "
  "merocrine; pinching off the apex is apocrine."),
Q("E-39", "EPI", "p. 15",
  "Release of a secretory product by exocytosis, leaving the cell intact, is "
  "called:",
  ["Merocrine secretion", "Apocrine secretion", "Holocrine secretion",
   "Endocrine secretion"],
  "Exocytosis with the cell intact is <b>merocrine</b> secretion – the most "
  "common type (salivary glands, pancreas). Apocrine loses a portion of the "
  "apical cytoplasm; holocrine loses the whole cell. Endocrine refers to "
  "where the product goes, not how it leaves the cell.",
  beyond=True,
  flag="Slide p. 15 gives \"apocrine (exocytosis)\" and omits merocrine "
       "entirely. Exocytosis is merocrine; apocrine is secretion with loss of "
       "the apical cytoplasm. Expect \"apocrine\" to be the tempting answer "
       "here for anyone working from the slide."),
Q("E-40", "EPI", "p. 15",
  "In apocrine secretion, the product is released by:",
  ["Pinching off of the apical cytoplasm",
   "Exocytosis with the membrane left intact",
   "Breakdown of the whole secretory cell",
   "Diffusion across the basal membrane"],
  "<b>Apocrine</b> glands shed a portion of the <b>apical cytoplasm</b> along "
  "with the product – the mammary gland's lipid secretion is the usual "
  "example. Exocytosis alone is merocrine; whole-cell breakdown is "
  "holocrine.",
  beyond=True,
  flag="This corrects slide p. 15, which pairs apocrine with exocytosis."),

# --- polarity and domains (p. 20–25)
Q("E-41", "EPI", "p. 20",
  "Through which domain do absorption and secretion usually occur?",
  ["Apical", "Lateral", "Basal"],
  "The <b>apical</b> domain faces the lumen or free surface, so it handles "
  "secretion, absorption and movement. The lateral domain attaches and "
  "communicates with neighboring cells; the basal domain attaches to the "
  "connective tissue."),
Q("E-42", "EPI", "p. 20",
  "Through which domain does an epithelial cell attach to and communicate "
  "with the underlying connective tissue?",
  ["Basal", "Lateral", "Apical"],
  "The <b>basal</b> domain meets the basement membrane and the connective "
  "tissue beneath it. Cell-to-cell attachment is lateral; the apical domain "
  "faces the lumen."),
Q("E-43", "EPI", "p. 20–21",
  "The lateral domain of an epithelial cell is specialized mainly for:",
  ["Attachment and communication between adjacent cells",
   "Secretion and absorption at the free surface",
   "Anchoring the cell to the underlying basement membrane",
   "Moving mucus and fluid across the free surface"],
  "The <b>lateral</b> domain carries the junctions that join neighboring cells "
  "(tight, adherens, desmosome) and let them communicate (gap junctions). "
  "Secretion and absorption, and mucus movement by cilia, are apical; "
  "anchoring to the basement membrane is basal."),
Q("E-44", "EPI", "p. 21",
  "Which of the following is a specialization of the apical domain?",
  ["Stereocilia", "Hemidesmosomes", "Focal adhesions", "Adherens junctions"],
  "Apical specializations are <b>microvilli, cilia and stereocilia</b>. "
  "Hemidesmosomes and focal adhesions are basal; adherens junctions are "
  "lateral."),
Q("E-45", "EPI", "p. 21",
  "Which of the following is a specialization of the basal domain?",
  ["Hemidesmosomes", "Microvilli", "Tight junctions", "Gap junctions"],
  "Basal specializations are <b>infoldings, hemidesmosomes and focal "
  "adhesions</b>. Microvilli are apical; tight and gap junctions are "
  "lateral."),
Q("E-46", "EPI", "p. 22",
  "Which apical structure contains microtubules in a 9+2 arrangement?",
  ["Cilia", "Microvilli", "Stereocilia", "Desmosomes"],
  "<b>Cilia</b> are motile, about 10 µm long, with a <b>9+2 microtubule</b> "
  "axoneme. Microvilli and stereocilia are non-motile projections supported by "
  "actin, and desmosomes are lateral junctions, not projections."),
Q("E-47", "EPI", "p. 22",
  "Long, branching, non-motile microvilli lining the epididymis are called:",
  ["Stereocilia", "Cilia", "Flagella", "Microvilli"],
  "Elongated, branching, immobile microvilli are <b>stereocilia</b> – despite "
  "the name they are not cilia, and they have no 9+2 core. Ordinary "
  "microvilli are about 1 µm long and unbranched; cilia and flagella are "
  "motile."),
Q("E-48", "EPI", "p. 22",
  "Slender, non-motile apical projections about 1 µm long that increase the "
  "absorptive surface are:",
  ["Microvilli", "Cilia", "Stereocilia", "Flagella"],
  "<b>Microvilli</b> are about 1 µm long and immobile, and form the brush "
  "border of absorptive cells. Cilia are about ten times longer and motile; "
  "stereocilia are long and branching; flagella are the long motile tails of "
  "sperm."),
Q("E-49", "EPI", "p. 22, 26",
  "Which component of the ciliary axoneme generates the force that moves the "
  "cilium?",
  ["Dynein arms", "Nexin links", "The central microtubule pair",
   "Actin filaments"],
  "<b>Dynein arms</b> are motor proteins that walk along the neighboring "
  "doublet, bending the cilium. Without them the cilium is immotile – the "
  "defect in primary ciliary dyskinesia. Nexin links hold the doublets "
  "together; actin is the core of microvilli.",
  flag="Slide p. 22 says the 9+2 microtubules are \"held in place by dynein "
       "arms\". Dynein arms are the motors; the nexin links hold the doublets "
       "in position. The p. 26 statement – that missing dynein arms leave "
       "cilia immotile – is correct."),
Q("E-50", "EPI", "p. 24",
  "Which junction lies closest to the apical surface?",
  ["Tight junction", "Adherens junction", "Desmosome", "Gap junction"],
  "<b>Tight junctions occur at a higher level than adherens junctions</b>, "
  "sealing the apex of the lateral surface. Desmosomes and gap junctions sit "
  "further down the lateral domain."),
Q("E-63", "EPI", "p. 24",
  "Which junction forms a continuous zone around each cell just below the "
  "tight junction?",
  ["Adherens junction", "Desmosome", "Gap junction", "Hemidesmosome"],
  "The <b>adherens junction</b> (zonula adherens) is the second belt, lying "
  "beneath the tight junction. Desmosomes are localized spots rather than "
  "zones, gap junctions are communicating plaques, and hemidesmosomes are "
  "on the basal surface."),
Q("E-51", "EPI", "p. 24",
  "Which junction forms a localized spot rather than a continuous zone around "
  "the cell?",
  ["Desmosome (macula adherens)", "Tight junction (zonula occludens)",
   "Adherens junction (zonula adherens)"],
  "Tight and adherens junctions are <b>zones</b> (<i>zonula</i>) that encircle "
  "each cell; the <b>desmosome</b> is a <b>localized unit</b> – a spot, "
  "<i>macula</i>. The Latin names encode the shape."),
Q("E-52", "EPI", "p. 24",
  "Which junction is built around the intermediate filaments of adjacent "
  "cells?",
  ["Desmosome", "Tight junction", "Adherens junction", "Gap junction"],
  "<b>Intermediate filaments</b> from adjacent cells anchor into "
  "<b>desmosomes</b>, which is what makes them resist shearing. Adherens "
  "junctions link to actin instead; tight junctions seal, and gap junctions "
  "form channels."),
Q("E-53", "EPI", "p. 21, 23",
  "Which junction allows communication between adjacent cells?",
  ["Gap junction", "Tight junction", "Desmosome", "Hemidesmosome"],
  "The <b>gap junction</b> is the communicating junction; it links the "
  "cytoplasm of neighboring cells. Tight junctions occlude, desmosomes "
  "anchor, and hemidesmosomes attach the base of the cell to the basement "
  "membrane."),
Q("E-54", "EPI", "p. 21, LO 3",
  "Which junction seals adjacent cells together, blocking passage of "
  "substances between them?",
  ["Tight junction", "Adherens junction", "Desmosome", "Gap junction"],
  "The <b>tight junction</b> (zonula occludens) is the <b>occluding</b> "
  "junction of learning objective 3 – it seals the space between cells. "
  "Adherens junctions and desmosomes are anchoring junctions, and gap "
  "junctions are communicating."),
Q("E-55", "EPI", "p. 25",
  "What is the basement membrane?",
  ["A specialized extracellular matrix between epithelium and connective "
   "tissue",
   "The lipid bilayer that forms the basal plasma membrane of each "
   "epithelial cell",
   "A layer of flattened basal cells that renews the epithelium above "
   "it",
   "A continuous sheet of junctions that anchors cells to their "
   "neighbors"],
  "The basement membrane is a <b>specialized extracellular matrix</b> "
  "structure between the basal domain and the connective tissue. Despite the "
  "name, it is not a cell membrane – the basal plasma membrane of the cell sits "
  "on top of it."),
Q("E-56", "EPI", "p. 25",
  "Which structures attach the base of epithelial cells to the underlying "
  "connective tissue?",
  ["Focal adhesions and hemidesmosomes", "Tight and adherens junctions",
   "Desmosomes and gap junctions", "Microvilli and stereocilia"],
  "<b>Focal adhesions and hemidesmosomes</b> anchor the basal domain to the "
  "basement membrane. Tight, adherens and gap junctions and desmosomes all "
  "join cell to cell; microvilli and stereocilia are apical."),

# --- primary ciliary dyskinesia (p. 26–27)
Q("E-57", "EPI", "p. 26",
  "What is the structural defect in primary ciliary dyskinesia?",
  ["Absent dynein arms, leaving the cilia immotile",
   "Absent microvilli, reducing the absorptive surface",
   "Defective tight junctions, letting fluid leak through",
   "Defective hemidesmosomes, detaching the epithelium"],
  "<b>Absence of dynein arms renders cilia immotile</b> – the defect in primary "
  "ciliary dyskinesia. The other options are real epithelial structures, but "
  "none would cause the respiratory and fertility picture on p. 27."),
Q("E-58", "EPI", "p. 27",
  "What is the inheritance pattern of primary ciliary dyskinesia?",
  ["Autosomal recessive", "Autosomal dominant", "X-linked recessive",
   "Mitochondrial"],
  "The presenting profile on p. 27 gives <b>autosomal recessive</b>. Both "
  "parents are usually unaffected carriers, and males and females are "
  "affected equally – which fits the lecture's list of both male and female "
  "fertility effects."),
Q("E-59", "EPI", "p. 26–27",
  "A 24-year-old man has had recurrent sinusitis and bronchitis since "
  "childhood. Semen analysis shows a normal sperm count, but the sperm are "
  "immotile. Which defect best explains both problems?",
  ["Missing dynein arms in the axonemes",
   "Absent microvilli on airway epithelium",
   "Defective desmosomes in airway epithelium",
   "Keratinization of the tracheal epithelium"],
  "Airway cilia and the sperm flagellum share the same <b>9+2 axoneme</b>. "
  "<b>Missing dynein arms</b> make both immotile: mucus is not cleared, so "
  "infections recur, and sperm cannot swim. This is primary ciliary "
  "dyskinesia. Microvilli and desmosomes are unrelated to motility."),
Q("E-60", "EPI", "p. 27",
  "A woman with primary ciliary dyskinesia has difficulty conceiving. What is "
  "the most likely mechanism?",
  ["Cilia of the uterine tubes cannot move the ovum toward the uterus",
   "Ovarian follicles lack the gap junctions needed for them to mature",
   "Stereocilia of the endometrium fail to capture the fertilized ovum",
   "Transitional epithelium of the uterus cannot stretch to hold a fetus"],
  "The uterine tubes are lined by <b>ciliated</b> epithelium that transports "
  "the ovum from the ovary to the uterine cavity. With immotile cilia that "
  "transport is impaired, so female fertility is reduced – though not abolished, "
  "unlike the male sterility from immotile sperm. The endometrium has no "
  "stereocilia, and the uterus is not lined by transitional epithelium."),
Q("E-61", "EPI", "p. 27",
  "Why do patients with primary ciliary dyskinesia have recurrent "
  "respiratory infections?",
  ["Mucus secretions are not cleared from the airways and sinuses",
   "The airway lining lacks the goblet cells needed to make mucus",
   "The alveolar walls thicken and block gas diffusion into blood",
   "Leaky tight junctions let bacteria cross into the bloodstream"],
  "Ciliated cells of the trachea, bronchi and sinuses normally sweep mucus "
  "out. With immotile cilia, <b>mucus is not cleared</b> and trapped microbes "
  "cause recurrent bronchitis and sinusitis. Mucus is still made – the problem "
  "is moving it."),
Q("E-62", "EPI", "p. 27",
  "Primary ciliary dyskinesia accompanied by situs inversus (reversed "
  "position of the internal organs) is known as:",
  ["Kartagener syndrome", "Cystic fibrosis", "Marfan syndrome",
   "Ehlers–Danlos syndrome"],
  "<b>Kartagener syndrome</b> is PCD with situs inversus: embryonic nodal "
  "cilia normally set left–right asymmetry, and without them organ placement "
  "is random. Cystic fibrosis also causes sinusitis, lung infections and male "
  "infertility, but through thick mucus from a chloride-channel defect – the "
  "cilia themselves work.",
  beyond=True,
  flag="The slide names Kartagener's syndrome but does not say what "
       "distinguishes it; situs inversus is beyond the slides."),
]
