"""
glossary_topics.py — Glossary-first CDL Pro knowledge base.
Each topic combines overlapping manual sections into one clean, readable source of truth.
"""

GLOSSARY_TOPICS = [
    {
        "id": "license_path", "title": "CDL / CLP License Path", "category": "Getting Licensed", "minutes": 12,
        "definition": "The Commercial Learner Permit (CLP) and CDL process is the official path from a regular license into commercial driving. In New York, study starts with choosing the right class, passing knowledge tests, completing required ELDT, holding the CLP, then passing inspection, basic control, and road skills tests.",
        "sources": ["NY CDL Manual Section 1", "NY DMV CDL requirements", "FMCSA ELDT"],
        "must_know": [
            "Class A covers heavy combination vehicles, usually tractor-trailers, where the towed unit is over 10,000 lbs.",
            "Class B covers heavy single vehicles over 26,001 lbs and smaller trailers under 10,000 lbs.",
            "Class C applies to smaller vehicles that carry placarded hazmat or passenger counts requiring a CDL.",
            "A CLP must be held for the required waiting period before the skills test.",
            "The skills test is not one test only; it includes vehicle inspection, basic control, and on-road driving."
        ],
        "pro_tip": "Pick the class based on the work you really want. Class A keeps the most doors open, but Class B can be faster and cheaper if your goal is local straight truck, dump truck, sanitation, or bus work.",
        "duplicate_notes": "Combined license class, permit, skills test, and licensing requirement material that repeats across the full handbooks."
    },
    {
        "id": "eldt", "title": "ELDT — Entry-Level Driver Training", "category": "Getting Licensed", "minutes": 10,
        "definition": "ELDT is federal training required before certain CDL skills tests or endorsements. It applies to first-time Class A or B applicants, Class B-to-A upgrades, and first-time Passenger, School Bus, or Hazmat endorsements.",
        "sources": ["FMCSA Training Provider Registry", "NY CDL Manual Section 1"],
        "must_know": ["Your provider must be listed on the FMCSA Training Provider Registry.", "Theory and behind-the-wheel training are separate pieces.", "There is no federal minimum BTW hour count; the provider certifies proficiency.", "If completion is not posted, the skills test can be blocked."],
        "pro_tip": "Before paying a school, verify the exact training type they are registered for, not just that the school exists.",
        "duplicate_notes": "Separated from general licensing because it is a federal gate that affects testing."
    },
    {
        "id": "vehicle_inspection", "title": "Vehicle Inspection / Pre-Trip", "category": "Vehicle Systems & Inspection", "minutes": 18,
        "definition": "A pre-trip inspection is the driver’s repeatable safety system for finding defects before they become crashes, breakdowns, or out-of-service violations.",
        "sources": ["NY CDL Manual Section 2", "NY CDL Manual Section 11"],
        "must_know": ["Inspect tires, wheels, rims, brakes, steering, suspension, lights, reflectors, coupling, cargo securement, and emergency equipment.", "Federal and state inspectors can place unsafe vehicles out of service.", "The test rewards a consistent flow, not random part naming.", "During a trip, watch gauges and use sight, sound, smell, and feel to catch trouble."],
        "pro_tip": "Use the same order every time: overview, engine, cab, steering/suspension, brakes, tires/wheels, lights, coupling/trailer, in-cab, air brakes.",
        "duplicate_notes": "Combines Section 2 inspection logic with Section 11 test-day inspection flow."
    },
    {
        "id": "air_brakes", "title": "Air Brakes", "category": "Vehicle Systems & Inspection", "minutes": 18,
        "definition": "Air brakes use compressed air to operate service brakes, parking brakes, and emergency brakes. Large vehicles rely on air systems because they are strong and safe when inspected and used correctly.",
        "sources": ["NY CDL Manual Section 5", "Combination air-brake notes"],
        "must_know": ["Service brakes apply and release with the foot pedal.", "Parking brakes on air-brake vehicles are spring-applied and air-released.", "Governor cut-out is where the compressor stops loading; cut-in is where it starts again.", "Air tanks must be drained to remove water and oil unless automatic drains are fitted.", "Low-air warning and spring brake pop-out are critical safety checks."],
        "pro_tip": "Don’t only memorize PSI numbers. Know what each check proves: warning system, air build, leak rate, compressor control, and spring brake emergency function.",
        "duplicate_notes": "Merged standalone air brake section with combination vehicle air-brake overlap."
    },
    {
        "id": "basic_control", "title": "Basic Vehicle Control", "category": "Driving Safely", "minutes": 10,
        "definition": "Basic control means steering, accelerating, braking, backing, and shifting smoothly enough to keep a large vehicle balanced, predictable, and inside its path.",
        "sources": ["NY CDL Manual Section 2", "Skills test guidance"],
        "must_know": ["Use smooth steering and gradual acceleration.", "Do not roll backward when starting on a grade.", "Back slowly and use GOAL — Get Out And Look.", "Pull-ups are better than forcing a bad backing angle.", "City driving requires protecting pedestrians, cyclists, and parked vehicles."],
        "pro_tip": "In tight NYC-style spaces, slow control beats fast confidence. A clean reset is professional, not embarrassing.",
        "duplicate_notes": "Combines manual basic control, backing, and practical road test behavior."
    },
    {
        "id": "shifting_gears", "title": "Shifting Gears", "category": "Driving Safely", "minutes": 8,
        "definition": "Shifting correctly keeps the engine in the right power range and prevents loss of control, especially on grades, curves, and slippery roads.",
        "sources": ["NY CDL Manual Section 2"],
        "must_know": ["Select the right gear before starting down a hill.", "Do not coast in neutral.", "Use progressive shifting where appropriate to save fuel and reduce wear.", "Automatic transmissions still require gear awareness on grades.", "Missed shifts can become dangerous when speed builds downhill."],
        "pro_tip": "The gear you choose before the hill matters more than the gear you wish you had halfway down.",
        "duplicate_notes": "Kept as its own glossary topic because shifting shows up in speed, grades, and emergency control."
    },
    {
        "id": "seeing", "title": "Seeing / Visual Search", "category": "Driving Safely", "minutes": 10,
        "definition": "Seeing means scanning far enough ahead, to the sides, and behind to spot hazards early and keep space around a commercial vehicle.",
        "sources": ["NY CDL Manual Section 2"],
        "must_know": ["Look far ahead, commonly 12–15 seconds in city driving and farther on highways.", "Check mirrors regularly and before lane changes, turns, merges, and stops.", "Watch for pedestrians, cyclists, work zones, brake lights, and traffic patterns.", "Use mirrors through the entire turn, not only before it.", "Blind spots are larger and more dangerous in trucks."],
        "pro_tip": "In NYC, your mirrors are active instruments. Check before, during, and after the maneuver.",
        "duplicate_notes": "Merged seeing, mirrors, lane changes, and hazard scanning overlap."
    },
    {
        "id": "communicating", "title": "Communicating", "category": "Driving Safely", "minutes": 8,
        "definition": "Commercial drivers communicate intentions with signals, brake lights, horn, headlights, lane position, and timing so others can predict what the truck will do.",
        "sources": ["NY CDL Manual Section 2"],
        "must_know": ["Signal early before turns and lane changes.", "Use four-way flashers when stopped or moving slowly as required.", "Tap brakes to warn drivers behind when slowing unexpectedly.", "Use the horn only when needed to prevent danger.", "Do not assume other road users understand your turn swing."],
        "pro_tip": "Signal early enough that people can react, but do not signal so early that your actual turn becomes unclear.",
        "duplicate_notes": "Combines signaling, horn, brake-light warnings, and visibility behavior."
    },
    {
        "id": "speed", "title": "Controlling Speed", "category": "Driving Safely", "minutes": 12,
        "definition": "Speed control is matching speed to road, traffic, weather, visibility, cargo, vehicle weight, and downgrade conditions — not just obeying the posted limit.",
        "sources": ["NY CDL Manual Section 2"],
        "must_know": ["Stopping distance includes perception, reaction, and braking distance.", "If speed doubles, stopping distance can increase about four times.", "Slow before curves, ramps, downgrades, intersections, and bad weather.", "Heavy vehicles need more room to stop, especially when loaded.", "Empty trucks can have poor traction and longer stopping in some conditions."],
        "pro_tip": "A safe truck speed is the speed that lets you stop without drama if the next hazard appears now.",
        "duplicate_notes": "Merged speed, stopping distance, curves, and braking-distance material."
    },
    {
        "id": "space", "title": "Managing Space", "category": "Driving Safely", "minutes": 12,
        "definition": "Space management means keeping enough room ahead, behind, to the sides, overhead, and below so the truck has time and room to react.",
        "sources": ["NY CDL Manual Section 2"],
        "must_know": ["Use at least one second per 10 feet of vehicle length below 40 mph, plus one second above 40 mph.", "Keep side space around cyclists, parked cars, and lane edges.", "Check overhead clearance and weight limits before committing.", "Avoid trapping yourself where you cannot clear an intersection.", "Leave extra room in bad weather or heavy traffic."],
        "pro_tip": "Space is a professional driver’s escape route. Once you give it away, you have fewer safe choices.",
        "duplicate_notes": "Combines following distance, side clearance, overhead clearance, and intersection space."
    },
    {
        "id": "hazards", "title": "Seeing Hazards", "category": "Driving Safely", "minutes": 10,
        "definition": "A hazard is any road user, road condition, vehicle condition, or traffic pattern that can develop into danger if not handled early.",
        "sources": ["NY CDL Manual Section 2"],
        "must_know": ["Scan parked cars for doors, pedestrians, and vehicles pulling out.", "Expect cyclists and pedestrians near intersections and bus stops.", "Work zones create sudden stops and narrow lanes.", "Weather, road surface, and visibility can turn normal maneuvers into hazards.", "Recognize hazards early enough to slow smoothly."],
        "pro_tip": "Treat every blocked sightline as a hidden hazard until proven otherwise.",
        "duplicate_notes": "Merged manual hazard recognition with city-operating examples."
    },
    {
        "id": "distracted_aggressive", "title": "Distracted Driving / Road Rage", "category": "Driving Safely", "minutes": 8,
        "definition": "Distracted and aggressive driving reduce the time and judgment a truck driver needs to safely control a large vehicle.",
        "sources": ["NY CDL Manual Section 2"],
        "must_know": ["Phones, food, dispatch devices, and emotional conversations can all distract.", "Avoid eye contact or confrontation with aggressive drivers.", "Create space instead of escalating.", "Do not use a hand-held mobile phone while operating a CMV.", "Professional drivers are expected to stay calm under pressure."],
        "pro_tip": "A CDL driver wins by staying calm, not by proving a point to a car driver.",
        "duplicate_notes": "Combined distracted driving and road-rage topics because the prevention is the same: control attention and emotions."
    },
    {
        "id": "night_fog_weather", "title": "Night, Fog, Winter, and Hot Weather", "category": "Weather & Conditions", "minutes": 14,
        "definition": "Adverse conditions require lower speed, more space, better visibility management, and extra vehicle checks because stopping, steering, and driver alertness all degrade.",
        "sources": ["NY CDL Manual Section 2"],
        "must_know": ["At night, reduce speed and keep lights clean and properly aimed.", "In fog, use low beams and slow enough to stop within visible distance.", "In winter, watch for black ice, frozen brakes, and reduced traction.", "In hot weather, monitor tires, coolant, belts, and brake heat.", "Do not use engine brakes/retarders on slippery roads if they can cause drive-wheel traction loss."],
        "pro_tip": "Bad weather does not make a safe driver late; it makes the unsafe driver visible.",
        "duplicate_notes": "Merged four weather chapters into one conditions topic for quicker study."
    },
    {
        "id": "railroad", "title": "Railroad-Highway Crossings", "category": "Driving Safely", "minutes": 8,
        "definition": "Railroad crossings require full attention because trains cannot stop quickly and a truck can become trapped, stalled, or struck if the driver misjudges timing or clearance.",
        "sources": ["NY CDL Manual Section 2"],
        "must_know": ["Never race a train or drive around lowered gates.", "Know if your vehicle is required to stop at crossings.", "Do not shift gears while crossing tracks if it risks stalling.", "Make sure there is enough room on the far side before entering.", "Use flashers when stopping as required."],
        "pro_tip": "Do not enter a crossing until your whole vehicle can clear it, including the trailer.",
        "duplicate_notes": "Kept separate because railroad questions are high-risk and commonly tested."
    },
    {
        "id": "mountain", "title": "Mountain Driving / Downgrades", "category": "Weather & Conditions", "minutes": 10,
        "definition": "Mountain driving requires speed and gear control before grades, especially downhill, because overheated brakes can fade or fail.",
        "sources": ["NY CDL Manual Section 2"],
        "must_know": ["Choose the proper gear before starting downhill.", "Use braking methods that prevent overheating.", "Never coast downhill in neutral.", "Use escape ramps if brakes fail; do not hesitate.", "Check brakes before long grades when signs or conditions call for it."],
        "pro_tip": "Go down the hill in a gear that lets the engine help hold speed without riding the brakes.",
        "duplicate_notes": "Merged mountain grades with speed and brake-fade logic, but kept as a quick-reference topic."
    },
    {
        "id": "emergencies", "title": "Driving Emergencies / Crash Procedures", "category": "Emergencies", "minutes": 14,
        "definition": "Emergency driving is the ability to brake, steer, recover, protect the scene, and report correctly when something goes wrong.",
        "sources": ["NY CDL Manual Section 2"],
        "must_know": ["Controlled braking keeps wheels rolling while slowing hard.", "Stab braking is used only on vehicles without ABS when appropriate.", "With ABS, brake firmly and maintain steering control.", "After a crash, protect the area, notify authorities, care for injured people if safe, and report as required.", "Use warning devices at required distances."],
        "pro_tip": "Steering may be better than braking if you can avoid a crash safely, but do not create a worse crash with sudden oversteer.",
        "duplicate_notes": "Combines emergency braking, crash procedures, warning devices, and ABS basics."
    },
    {
        "id": "skids", "title": "Skid Control and Recovery", "category": "Emergencies", "minutes": 10,
        "definition": "A skid happens when tires lose traction. Recovery requires restoring traction, steering where you want to go, and avoiding overcorrection.",
        "sources": ["NY CDL Manual Section 2"],
        "must_know": ["Drive-wheel skids can happen from too much power or engine braking on slippery surfaces.", "Rear trailer skids can lead to jackknife.", "Take your foot off the brake or accelerator as needed to restore rolling traction.", "Steer in the direction you want the vehicle to go.", "Avoid sudden steering corrections after traction returns."],
        "pro_tip": "Most skid prevention happens before the skid: slower speed, more space, and smooth inputs.",
        "duplicate_notes": "Merged skid recovery logic with slippery-road control."
    },
    {
        "id": "fires", "title": "Vehicle Fires", "category": "Emergencies", "minutes": 8,
        "definition": "Vehicle fires often start from electrical faults, fuel leaks, overheated brakes/tires, or cargo problems and must be handled quickly without risking the driver’s life.",
        "sources": ["NY CDL Manual Section 2"],
        "must_know": ["Pull off safely, shut down, and evacuate when needed.", "Know the fire extinguisher location and rating.", "Do not open a hood fully if fire is under it; oxygen can intensify fire.", "Use the correct extinguisher technique from a safe distance.", "Report and protect the scene."],
        "pro_tip": "Smell matters. Burning rubber, hot brakes, fuel, or electrical odor deserves immediate attention.",
        "duplicate_notes": "Combined fire prevention and response into one emergency reference."
    },
    {
        "id": "alcohol_drugs", "title": "Alcohol, Drugs, and Driver Fitness", "category": "Compliance & Safety", "minutes": 12,
        "definition": "Commercial drivers are held to strict alcohol, drug, and fitness standards because impairment and fatigue are major crash risks.",
        "sources": ["NY CDL Manual Section 2", "FMCSA drug/alcohol rules"],
        "must_know": ["A CMV driver has stricter alcohol limits than a regular driver.", "Using controlled substances without lawful medical direction can disqualify a driver.", "Fatigue can impair judgment like alcohol.", "Illness, medications, and sleep debt can make a driver unfit.", "Drug and alcohol violations affect CDL privileges and employment."],
        "pro_tip": "Ask about medication side effects before driving. Legal medication can still make you unsafe.",
        "duplicate_notes": "Merged alcohol, drugs, fatigue, alertness, and fitness to drive."
    },
    {
        "id": "cargo", "title": "Cargo Securement / Weight / Balance", "category": "Cargo & Compliance", "minutes": 12,
        "definition": "Cargo must be loaded, balanced, secured, inspected, and rechecked so it does not shift, fall, leak, or make the vehicle overweight or unstable.",
        "sources": ["NY CDL Manual Section 3"],
        "must_know": ["The driver is responsible even when someone else loaded the vehicle.", "Know GVWR, GCWR, axle weights, and bridge-law concerns.", "Secure cargo against forward, rearward, sideways, and vertical movement.", "Recheck securement after the first 50 miles and periodically after.", "Special cargo such as logs, machinery, vehicles, or liquids can have extra rules."],
        "pro_tip": "A load can be under gross weight and still illegal if one axle is overloaded.",
        "duplicate_notes": "Combines cargo inspection, securement, weight, and balance."
    },
    {
        "id": "passengers", "title": "Passenger Transport", "category": "Endorsements", "minutes": 10,
        "definition": "Passenger drivers carry extra responsibility for loading, safe movement, emergency exits, passenger behavior, and route stops.",
        "sources": ["NY CDL Manual Section 4"],
        "must_know": ["Inspect emergency exits, seats, aisles, handholds, and lighting.", "Do not move until passengers are safe and doors are secured.", "Manage stops so passengers board and exit safely.", "Know prohibited practices such as fueling with passengers aboard when restricted.", "Passenger endorsement may require ELDT if first-time."],
        "pro_tip": "Passenger driving is customer safety plus vehicle control — both are tested by real life every stop.",
        "duplicate_notes": "Combined passenger vehicle inspection and road behavior."
    },
    {
        "id": "combination", "title": "Combination Vehicles", "category": "Endorsements", "minutes": 14,
        "definition": "Combination vehicles include a power unit and trailer. They require knowledge of coupling, uncoupling, air/electrical connections, trailer tracking, rollover risk, and longer stopping distance.",
        "sources": ["NY CDL Manual Section 6"],
        "must_know": ["Always confirm fifth-wheel locking jaws and perform a pull test after coupling.", "Inspect kingpin, apron, fifth wheel, glad hands, air lines, electrical cord, and landing gear.", "Trailers off-track on turns, cutting inside the tractor path.", "Combination vehicles are more vulnerable to jackknife and rollover.", "Trailer air-supply and emergency lines must be connected correctly."],
        "pro_tip": "Never skip the pull test. A dropped trailer is preventable and career-damaging.",
        "duplicate_notes": "Merged coupling/uncoupling, air lines, off-tracking, and inspection."
    },
    {
        "id": "doubles_triples", "title": "Doubles and Triples", "category": "Endorsements", "minutes": 10,
        "definition": "Doubles and triples are multi-trailer combinations that are less stable and more affected by rearward amplification, also known as crack-the-whip.",
        "sources": ["NY CDL Manual Section 7"],
        "must_know": ["The last trailer is most likely to roll over.", "Steer gently and avoid sudden lane changes.", "Allow extra following distance and larger gaps.", "Inspect every coupling, converter dolly, air line, and electrical connection.", "Triple trailers are not allowed on New York highways even though endorsement knowledge covers them."],
        "pro_tip": "With multiple trailers, small steering mistakes become big trailer movements.",
        "duplicate_notes": "Combined doubles/triples manual and combination vehicle stability concepts."
    },
    {
        "id": "tanker", "title": "Tank Vehicles", "category": "Endorsements", "minutes": 10,
        "definition": "Tank vehicles carry liquid or gas cargo that can surge, changing vehicle balance during acceleration, braking, and turns.",
        "sources": ["NY CDL Manual Section 8"],
        "must_know": ["Surge is liquid movement inside the tank.", "Partly-filled tanks can be more unstable than full tanks.", "Smooth-bore tanks have no baffles and require extra caution.", "Start, stop, and turn smoothly to control surge.", "Know outage/expansion space for liquids when applicable."],
        "pro_tip": "Tank driving is smooth-driving discipline. Every rough input comes back through the liquid.",
        "duplicate_notes": "Merged tanker endorsement and general stability concepts."
    },
    {
        "id": "hazmat", "title": "Hazardous Materials", "category": "Endorsements", "minutes": 18,
        "definition": "Hazmat rules control how hazardous materials are classified, documented, packaged, marked, placarded, loaded, segregated, transported, parked, and handled in emergencies.",
        "sources": ["NY CDL Manual Section 9", "NY HazMat Manual CDL-11"],
        "must_know": ["Drivers must understand shipping papers and keep them accessible and identifiable.", "Placards communicate hazard class to emergency responders.", "Some materials cannot be loaded together due to segregation rules.", "Hazmat endorsement requires TSA threat assessment.", "In an emergency, protect yourself, isolate the area, notify authorities, and do not blindly touch or move leaking material."],
        "pro_tip": "Hazmat is paperwork plus safety behavior. If the papers, labels, packages, and placards do not match, stop and fix it before moving.",
        "duplicate_notes": "Merged CDL Section 9 with the separate CDL-11 HazMat manual into one aligned topic."
    },
    {
        "id": "school_bus", "title": "School Bus", "category": "Endorsements", "minutes": 12,
        "definition": "School bus operation combines passenger safety with special student loading, unloading, railroad crossing, mirror, and emergency evacuation rules.",
        "sources": ["NY CDL Manual School Bus section", "Passenger section"],
        "must_know": ["Student loading and unloading is the highest-risk part of the route.", "Use mirrors and warning lights correctly before opening doors.", "Count students and check danger zones before moving.", "Know evacuation procedures and emergency equipment.", "School Bus endorsement commonly requires ELDT if first-time."],
        "pro_tip": "The bus does not move until every child is accounted for and clear of danger zones.",
        "duplicate_notes": "Combined passenger safety with school-bus-specific procedures."
    },
    {
        "id": "hours_service", "title": "Hours of Service / ELD", "category": "Compliance & Paperwork", "minutes": 12,
        "definition": "Hours of Service rules limit driving and on-duty time to reduce fatigue. ELD systems record duty status for most regulated operations.",
        "sources": ["FMCSA HOS", "CDL compliance notes"],
        "must_know": ["Property-carrying drivers commonly follow 11-hour, 14-hour, 30-minute break, and 60/70-hour rules.", "The 14-hour window does not pause just because you stop working temporarily.", "ELD records must be certified and corrected properly.", "Short-haul exceptions exist but must fit exact criteria.", "Falsifying logs is a serious violation."],
        "pro_tip": "Learn your company ELD before your first solo day. Bad logs can cost more than a late load.",
        "duplicate_notes": "Added as practical compliance knowledge even when not emphasized in every manual section."
    },
    {
        "id": "nyc_routes", "title": "NYC Truck Routes / Parkways", "category": "NYC Operating Knowledge", "minutes": 14,
        "definition": "NYC truck routing separates through truck routes from local truck routes, and most parkways ban commercial vehicles. Truck drivers must route by official truck rules, not passenger-car GPS.",
        "sources": ["NYC DOT Truck Routing", "NY CDL local operating knowledge"],
        "must_know": ["Through routes serve trucks passing through an area.", "Local routes serve trucks with actual pickup/delivery/service in that area.", "Leave the truck route only at the closest practical point to the stop.", "Many NYC parkways ban trucks regardless of height or weight.", "Bridge, tunnel, and street-specific restrictions layer on top of truck-route rules."],
        "pro_tip": "In NYC, the legal route is not always the fastest route. Use official truck-route maps and a real truck GPS.",
        "duplicate_notes": "Consolidates NYC-specific route, parkway, and local/through route rules."
    },
    {
        "id": "clearance", "title": "Low Bridges / Clearance / Weight Limits", "category": "NYC Operating Knowledge", "minutes": 10,
        "definition": "Clearance and structural limits determine whether a truck can safely and legally pass under or over a specific road feature, regardless of the general truck-route designation.",
        "sources": ["NYC bridge/route rules", "NY CDL space management"],
        "must_know": ["Know actual vehicle height, including trailer and roof equipment.", "Trust posted clearance signs over memory or app data.", "Weight limits can make a bridge illegal even on a truck route.", "Parkway bridges often have low clearances and truck bans.", "If unsure, stop before committing and reroute."],
        "pro_tip": "A bridge strike is almost always a planning failure. Measure, enter the height, read signs, and never guess.",
        "duplicate_notes": "Combines overhead space management with NYC low-bridge operating risk."
    },
    {
        "id": "roadside", "title": "Roadside Inspections / Out-of-Service", "category": "Compliance & Paperwork", "minutes": 10,
        "definition": "Roadside inspections check driver credentials, logs, vehicle condition, cargo, and compliance. Serious defects or violations can put the driver or vehicle out of service.",
        "sources": ["NY CDL Manual Section 2", "General enforcement practice"],
        "must_know": ["Keep CDL/CLP, medical card if required, registration, insurance, permits, and logs ready.", "Out-of-service defects must be repaired before operation continues.", "Brake, tire, lighting, coupling, and load securement issues are common inspection problems.", "Be professional and honest during inspection.", "A clean pre-trip prevents many inspection failures."],
        "pro_tip": "Your inspection attitude matters: organized documents and calm communication set the tone.",
        "duplicate_notes": "Merged inspection law language with practical roadside readiness."
    }
]

CATEGORY_ORDER = [
    "Getting Licensed", "Vehicle Systems & Inspection", "Driving Safely", "Weather & Conditions", "Emergencies", "Cargo & Compliance", "Endorsements", "Compliance & Paperwork", "NYC Operating Knowledge"
]


def topics_by_category() -> dict:
    grouped = {c: [] for c in CATEGORY_ORDER}
    for topic in GLOSSARY_TOPICS:
        grouped.setdefault(topic["category"], []).append(topic)
    return grouped


def get_topic(topic_id: str) -> dict | None:
    for topic in GLOSSARY_TOPICS:
        if topic["id"] == topic_id:
            return topic
    return None


def all_topic_titles() -> list:
    return [t["title"] for t in GLOSSARY_TOPICS]


def total_study_minutes() -> int:
    return sum(t.get("minutes", 0) for t in GLOSSARY_TOPICS)


def source_count() -> int:
    return len({src for topic in GLOSSARY_TOPICS for src in topic.get("sources", [])})
