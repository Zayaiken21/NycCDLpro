"""
quiz_bank.py — Practice test question bank.
Organized into per-topic quizzes (matching curriculum sections/modules)
plus a master test pulling from all topics.
"""

TOPIC_QUIZZES = {
    "Getting Licensed": [
        {"q": "What license must you already hold before applying for a NY CDL permit?",
         "choices": ["A motorcycle license", "A NY Class D, E, or Non-CDL C license", "No license is needed", "Only a passport"], "a": 1,
         "explain": "NY requires an existing valid Class D, E, or Non-CDL Class C license in good standing before you can apply for a CLP."},
        {"q": "Which CDL class is required for most tractor-trailer combinations?",
         "choices": ["Class A", "Class B", "Class C", "Class M"], "a": 0,
         "explain": "Class A covers combination vehicles over 26,001 lbs GVWR with a towed unit over 10,000 lbs — the standard tractor-trailer configuration."},
        {"q": "How long must you hold a Commercial Learner Permit before taking the road test?",
         "choices": ["No minimum", "7 days", "14 days (federal minimum)", "90 days"], "a": 2,
         "explain": "Federal rule requires at least 14 days holding the CLP before the road skills test."},
        {"q": "What does GVWR stand for?",
         "choices": ["General Vehicle Weight Rule", "Gross Vehicle Weight Rating", "Government Vehicle Weight Requirement", "Gross Vehicle Width Rating"], "a": 1,
         "explain": "GVWR is the manufacturer's maximum safe loaded weight rating for the vehicle."},
    ],
    "ELDT": [
        {"q": "Who sets the federal baseline ELDT training requirements?",
         "choices": ["NYC DOT", "FMCSA", "IRS", "USPS"], "a": 1,
         "explain": "FMCSA (Federal Motor Carrier Safety Administration) sets ELDT requirements under 49 CFR Part 380."},
        {"q": "ELDT is required when:",
         "choices": ["Adding a Tanker endorsement to an existing Class A", "Getting a Class A or B CDL for the first time", "Renewing an unchanged CDL", "Never required"], "a": 1,
         "explain": "ELDT applies to first-time Class A/B applicants, B-to-A upgrades, and first-time School Bus/Passenger/Hazmat endorsements."},
        {"q": "What must you verify about your ELDT training provider before paying them?",
         "choices": ["Nothing, all schools are approved", "They are listed on the FMCSA Training Provider Registry (TPR)", "They have a nice website", "They offer the lowest price"], "a": 1,
         "explain": "Only providers listed on the FMCSA TPR can submit valid completion certificates."},
        {"q": "What happens if your ELDT completion isn't posted before your scheduled road test?",
         "choices": ["Nothing, you can still test", "You'll be turned away even if otherwise prepared", "You get a warning only", "ELDT doesn't affect testing"], "a": 1,
         "explain": "The testing system checks for posted ELDT completion; missing records block the test regardless of your actual readiness."},
    ],
    "NYC Truck Routes": [
        {"q": "When should a truck leave a designated NYC truck route?",
         "choices": ["Whenever a GPS app suggests it", "Only at the point closest to pickup/delivery/loading/service", "To avoid traffic", "Never, under any condition"], "a": 1,
         "explain": "Local routing rules require leaving the network only at the closest practical point to your actual stop."},
        {"q": "What vehicle configuration counts as a 'truck' under NYC routing rules?",
         "choices": ["Only vehicles over 26,000 lbs", "Two axles and six tires, or three or more axles", "Only tractor-trailers", "Only vehicles with hazmat placards"], "a": 1,
         "explain": "NYC's definition is based on axle/tire configuration, not weight — catching many box trucks drivers assume are exempt."},
        {"q": "What should override a truck-navigation app's suggested route?",
         "choices": ["The fastest car route", "Posted signs and official restrictions", "A random shortcut", "A passenger's opinion"], "a": 1,
         "explain": "Posted signage and official restrictions are the legal authority — apps can be outdated or wrong."},
        {"q": "NYC parkways generally:",
         "choices": ["Allow all commercial trucks", "Ban commercial trucks outright regardless of size", "Only restrict trucks over 40 feet", "Have no restrictions at night"], "a": 1,
         "explain": "Most NYC parkways are passenger-vehicle only and ban commercial trucks as a vehicle-class restriction, not just a size/weight one."},
    ],
    "Bridges & Clearance": [
        {"q": "When a clearance sign and your truck GPS disagree, you should:",
         "choices": ["Trust the GPS, it's more current", "Trust the posted sign", "Average the two numbers", "Proceed slowly either way"], "a": 1,
         "explain": "Posted signs are the current, legal source — GPS data can lag behind real-world changes."},
        {"q": "What should you do if you cannot confirm clearance and have any doubt?",
         "choices": ["Proceed slowly", "Stop and find another route", "Honk and proceed", "Follow another truck through"], "a": 1,
         "explain": "Stopping and rerouting is always safer than risking a bridge strike — reversing out of a too-low approach is far more dangerous than the delay."},
        {"q": "A road being a legal truck route means:",
         "choices": ["Every bridge on it is automatically truck-legal", "Specific bridges on it may still carry separate weight/height limits", "No further checks are needed", "Trucks of any size are guaranteed clearance"], "a": 1,
         "explain": "Route designation and bridge-specific restrictions are separate layers — both must be checked independently."},
    ],
    "Pre-Trip Inspection": [
        {"q": "What is the main thing examiners are evaluating during the vehicle inspection test?",
         "choices": ["Memorized vocabulary", "A repeatable, complete sequence used daily", "Speed of completion", "Use of technical jargon"], "a": 1,
         "explain": "The test checks for a real, usable daily habit, not just the ability to name parts."},
        {"q": "Where does the standard pre-trip sequence typically begin?",
         "choices": ["Air brake test", "Vehicle overview walk-around", "Coupling system", "In-cab final check"], "a": 1,
         "explain": "A general walk-around for obvious issues (leaning, leaks, damage) typically comes before detailed component checks."},
        {"q": "On test day, how should you describe each inspection point?",
         "choices": ["Just name the part", "Explain what you're checking and what you're looking/listening for", "Skip explanations to save time", "Only mention parts that look unusual"], "a": 1,
         "explain": "Examiners listen for understanding, not vocabulary — explain the purpose of each check."},
    ],
    "Air Brakes": [
        {"q": "On an air-brake vehicle, what happens to spring brakes during a total air loss?",
         "choices": ["They release completely", "They automatically apply (held released by air, applied by spring force)", "They have no function", "They explode"], "a": 1,
         "explain": "Spring brakes are held released by air pressure; losing air pressure applies them as a built-in safety feature."},
        {"q": "What does the 'governor cut-out' refer to?",
         "choices": ["The pressure where the compressor stops loading", "The pressure where brakes fail", "The minimum tire pressure", "The engine shutoff point"], "a": 0,
         "explain": "Governor cut-out is the pressure point (commonly ~120-135 psi depending on vehicle) where the air compressor stops loading air into the system."},
        {"q": "During the static leak test, the vehicle is checked with:",
         "choices": ["Engine running, brakes applied", "Engine off, brakes released", "Engine off, parking brake released, moving", "Engine running, parking brake set"], "a": 1,
         "explain": "The static leak test is performed with the engine off and brakes released, checking pressure drop over one minute."},
        {"q": "What should you do if the low air warning doesn't activate at the proper threshold?",
         "choices": ["Ignore it and proceed", "The vehicle should be considered out of service until repaired", "Tap the gauge and continue", "Only a problem on long trips"], "a": 1,
         "explain": "A malfunctioning low air warning is a critical safety system failure — the vehicle should not be operated until repaired."},
    ],
    "Backing & Road Skills": [
        {"q": "What does GOAL stand for?",
         "choices": ["Go Over And Look", "Get Out And Look", "Guide Over A Lane", "Go On A Lane"], "a": 1,
         "explain": "GOAL — Get Out And Look — is the core habit for confirming clearance before and during backing."},
        {"q": "What is generally the best response to a developing bad backing angle?",
         "choices": ["Force the wheel hard to correct", "Pull forward and reset", "Speed up to compensate", "Continue and hope it improves"], "a": 1,
         "explain": "Pulling forward and resetting is almost always acceptable and safer than fighting a bad angle."},
        {"q": "When should you force a turn despite a partially blocked sightline?",
         "choices": ["Whenever you're in a hurry", "Never — stop and wait instead", "Only at low speed", "Only during daylight"], "a": 1,
         "explain": "Never force a turn with an unclear sightline — stop and wait for the hazard to clear."},
    ],
    "Hours of Service": [
        {"q": "What is the standard maximum driving limit after 10 consecutive hours off duty?",
         "choices": ["8 hours", "10 hours", "11 hours", "14 hours"], "a": 2,
         "explain": "The 11-hour driving limit applies after 10 consecutive hours off duty for property-carrying drivers."},
        {"q": "After how many cumulative hours of driving is a 30-minute break required?",
         "choices": ["4 hours", "6 hours", "8 hours", "10 hours"], "a": 2,
         "explain": "The 30-minute break requirement triggers after 8 cumulative hours of driving."},
        {"q": "What is the 14-hour rule?",
         "choices": ["Maximum 14 hours of driving", "Cannot drive beyond the 14th hour after coming on duty, following 10 hours off", "Must rest every 14 hours", "Maximum weekly hours"], "a": 1,
         "explain": "The 14-hour window starts when you come on duty and keeps running regardless of breaks taken within it."},
        {"q": "Falsifying ELD records is best described as:",
         "choices": ["A minor paperwork issue", "A serious federal violation", "Acceptable if corrected later", "Only a problem if caught twice"], "a": 1,
         "explain": "Falsifying logs is a serious federal compliance violation, not a technicality."},
    ],
    "Cargo & Securement": [
        {"q": "GCWR refers to:", "choices": ["Gross Vehicle Weight Rating for a single truck", "Gross Combination Weight Rating for tractor + trailer", "Ground Clearance Weight Ratio", "General Cargo Weight Requirement"], "a": 1,
         "explain": "GCWR is the maximum rated weight for the full tractor-trailer combination."},
        {"q": "When should cargo securement be re-checked on a trip?",
         "choices": ["Never, once loaded it's set", "After the first 50 miles, then periodically", "Only at the final destination", "Only if it looks loose"], "a": 1,
         "explain": "Cargo settles during initial movement — a 50-mile re-check, then periodic checks, is standard practice."},
        {"q": "Who is responsible for verifying cargo is legally loaded, even if a warehouse loaded it?",
         "choices": ["The warehouse only", "The driver", "The shipper only", "No one, it's assumed correct"], "a": 1,
         "explain": "The driver bears responsibility for verifying legal, secure loading regardless of who physically loaded the cargo."},
    ],
    "Combination Vehicles": [
        {"q": "What must always be done after coupling a trailer, before driving away?",
         "choices": ["Nothing extra", "A pull test to confirm the locking jaws engaged", "Only a visual check", "Wait 10 minutes"], "a": 1,
         "explain": "The pull test (gently pulling forward against the trailer brakes) confirms the fifth wheel locking jaws actually engaged."},
        {"q": "What is 'off-tracking'?",
         "choices": ["A trailer's rear wheels tracking inside the tractor's path on turns", "A brake malfunction", "A type of coupling failure", "GPS signal loss"], "a": 0,
         "explain": "Off-tracking describes how a trailer's wheels follow a tighter path than the tractor's on turns, more pronounced with longer trailers."},
    ],
    "Tanker": [
        {"q": "What is 'surge' in tanker operation?",
         "choices": ["Engine power increase", "Liquid movement inside a partially full tank during accel/braking/turns", "A type of brake failure", "Fuel consumption rate"], "a": 1,
         "explain": "Surge is the single most important tanker concept — liquid shifting can violently affect the vehicle's effective center of gravity."},
        {"q": "Smooth-bore (unbaffled) tankers require:",
         "choices": ["No special handling", "Even more conservative driving than baffled tanks", "Faster turning to reduce surge", "No different technique"], "a": 1,
         "explain": "Smooth-bore tanks have no baffles to reduce surge at all, requiring extra-conservative driving technique."},
    ],
    "Doubles/Triples": [
        {"q": "What is 'crack-the-whip' (rearward amplification)?",
         "choices": ["A coupling technique", "Steering corrections magnified at each successive trailer", "A braking system", "A loading procedure"], "a": 1,
         "explain": "Rearward amplification means the last trailer in a multi-trailer combination can swing dramatically more than the lead trailer from the same steering input."},
        {"q": "What connects multiple trailers in a doubles/triples combination?",
         "choices": ["A second fifth wheel only", "A converter dolly", "Extra glad hands alone", "A tow bar"], "a": 1,
         "explain": "The converter dolly is the connecting unit between trailers, with its own coupling and inspection points."},
    ],
    "Passenger & School Bus": [
        {"q": "What additional federal step does a Hazmat endorsement require that Passenger does not?",
         "choices": ["A driving test", "A TSA background check", "A medical exam", "An age requirement"], "a": 1,
         "explain": "This question tests cross-endorsement knowledge — TSA background checks are specific to Hazmat, not Passenger/School Bus."},
        {"q": "What is the 'danger zone' on a school bus?",
         "choices": ["The engine compartment", "The area directly around the bus checked via mirrors during loading/unloading", "The rear cargo area", "A type of route restriction"], "a": 1,
         "explain": "The danger zone is the immediate area around the bus where children may be present and hard to see — checked via mirror systems during stops."},
    ],
    "Hazmat": [
        {"q": "What additional federal process is unique to the Hazmat endorsement?",
         "choices": ["A road test", "A TSA background check (Hazmat Endorsement Threat Assessment Program)", "A medical exam", "An interview"], "a": 1,
         "explain": "Hazmat is the only endorsement requiring a TSA background check, which can take weeks to complete."},
        {"q": "Where must hazmat shipping papers be kept in the cab?",
         "choices": ["In the glove box, location doesn't matter", "Within reach and clearly identified", "In the sleeper berth", "Anywhere in the vehicle"], "a": 1,
         "explain": "Shipping papers must be within reach and clearly identifiable, not just somewhere in the vehicle."},
        {"q": "What should you do regarding loading segregation of hazard classes?",
         "choices": ["Load any classes together if space allows", "Follow segregation rules — some classes cannot be loaded together", "Only the shipper's responsibility", "Segregation only applies to liquids"], "a": 1,
         "explain": "Segregation rules are a driver responsibility to verify, not solely the shipper's."},
    ],
    "Career & Compliance": [
        {"q": "What primarily keeps a CDL driver employed after being hired?",
         "choices": ["The CDL itself", "Clean driving record, compliance, and reliability", "Seniority alone", "Vehicle ownership"], "a": 1,
         "explain": "The CDL gets you considered for a job; safety habits and reliability are what keep you employed and promotable."},
        {"q": "Which endorsements commonly open higher-paying specialized freight lanes?",
         "choices": ["None, all CDL jobs pay the same", "Hazmat and Tanker", "Only Passenger", "Only School Bus"], "a": 1,
         "explain": "Hazmat and Tanker endorsements commonly access specialized, higher-paying freight lanes, with added compliance responsibility."},
    ],
}


def all_topics() -> list:
    return list(TOPIC_QUIZZES.keys())


def get_master_test(limit: int = None) -> list:
    """Combine every topic's questions into one master test, in stable order."""
    combined = []
    for topic, questions in TOPIC_QUIZZES.items():
        for q in questions:
            combined.append({**q, "topic": topic})
    return combined[:limit] if limit else combined


def get_topic_quiz(topic: str) -> list:
    return [{**q, "topic": topic} for q in TOPIC_QUIZZES.get(topic, [])]


def total_question_count() -> int:
    return sum(len(qs) for qs in TOPIC_QUIZZES.values())
