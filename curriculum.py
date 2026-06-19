"""
curriculum.py — Full-depth CDL study curriculum content.
Structured to mirror the real NY CDL Manual chapter organization plus all
federal endorsement modules, with NYC-specific operating knowledge layered in.
"""

MODULES = [
    # ───────────────────────── GETTING STARTED ─────────────────────────
    {
        "id": "m01",
        "exit": "1",
        "title": "Your License Path in New York",
        "tag": "Start Here",
        "section": "Getting Licensed",
        "minutes": 12,
        "content": """
### Before you touch a CDL manual
New York requires you to already hold a valid **NY Class D, Class E, or Non-CDL Class C** license before you can apply for a Commercial Learner's Permit (CLP). If your regular license isn't in good standing — suspensions, unresolved tickets, unpaid surcharges — fix that first. It will block your CDL application.

### The three CDL classes
| Class | What it covers | Typical jobs |
|---|---|---|
| **Class A** | Combination vehicles over 26,001 lbs GVWR, with a towed unit over 10,000 lbs (tractor-trailers, tankers, flatbeds) | OTR, regional, tanker, doubles/triples |
| **Class B** | Single vehicles over 26,001 lbs GVWR, or those vehicles towing a unit under 10,000 lbs (box trucks, dump trucks, transit buses, school buses) | Local delivery, sanitation, construction, bus driving |
| **Class C** | Vehicles under 26,001 lbs GVWR that either transport 16+ passengers (including driver) or carry placarded hazardous materials | Small hazmat routes, passenger vans |

### The real path, step by step
1. **Pick your class.** Class A opens the most doors (you can downgrade-drive Class B/C vehicles too, with the right endorsements). Class B is the right call if you specifically want local box truck, dump truck, or bus work and don't need to pull heavy trailers.
2. **Self-certify your driving type** with NY DMV: Non-excepted interstate, excepted interstate, non-excepted intrastate, or excepted intrastate. This determines if you need a DOT medical card.
3. **Pass your DOT physical** (if non-excepted) and get your medical certificate uploaded to the FMCSA Drug & Alcohol Clearinghouse system.
4. **Study the NY CDL Manual** sections for your class and any endorsements you want.
5. **Pass CDL knowledge tests** at a DMV office — general knowledge plus any endorsement-specific tests (air brakes, combination vehicles, etc.) — and receive your **Commercial Learner Permit (CLP)**.
6. **Complete ELDT** (Entry-Level Driver Training) if required for your situation — see Module 2.
7. **Hold your CLP for at least 14 days** before taking the road test (federal minimum).
8. **Practice** with a CDL holder of the same class in the seat next to you, in a vehicle representative of what you'll drive.
9. **Pass the three-part skills test**: vehicle inspection, basic controls, and road test.

### Common mistakes that cost people weeks
- Booking a road test before confirming your ELDT completion is posted in the FMCSA system — you can be turned away even with a valid CLP.
- Studying only the general knowledge section and skipping endorsement-specific material, then failing the combination vehicle or air brakes test separately.
- Letting your regular license lapse or accumulate points while holding a CLP — NY can suspend the CLP along with it.
""",
        "drill": "Know your class before you spend a dollar. Class A is the most versatile and the most commonly required for OTR/regional freight; Class B is the right, cheaper choice if your target job is specifically local straight truck, dump truck, or bus work.",
    },
    {
        "id": "m02",
        "exit": "2",
        "title": "ELDT — Entry-Level Driver Training",
        "tag": "Federal Rule",
        "section": "Getting Licensed",
        "minutes": 10,
        "content": """
### When ELDT applies to you
Federal ELDT rules (49 CFR Part 380) require completion of an approved training program before you can take your CDL skills test if you are:
- Getting a **Class A or Class B CDL for the first time**
- **Upgrading** from Class B to Class A
- Getting a **School Bus, Passenger, or Hazmat** endorsement for the first time

ELDT does **not** apply if you already held a CDL before February 7, 2022, or if you're only adding endorsements that aren't in the list above (e.g., adding a Tanker endorsement to an existing Class A doesn't require new ELDT).

### Two components of ELDT
1. **Theory instruction** — covers the knowledge areas tested in your CDL knowledge test.
2. **Behind-the-wheel (BTW) training** — there is **no federally mandated minimum hour count** for BTW training; instead, your training provider must certify you've reached proficiency on a checklist of skills.

### The single most important thing to verify
Your training provider — whether a school, employer, or independent instructor — **must be listed on the FMCSA Training Provider Registry (TPR)** at the time of your training, and must actually submit your completion certificate to the TPR system. Many students pay for training only to discover their provider never submitted the paperwork.

**Before paying anyone:** look up the provider at tpr.fmcsa.dot.gov and confirm they appear as an active, registered provider for the training type you need (Class A theory, Class A BTW, Class B theory, Class B BTW, or the specific endorsement).

### What happens if your ELDT isn't posted
The DMV/testing system checks the FMCSA Clearinghouse-linked TPR record before allowing your skills test. If it's missing, you'll be turned away on test day even if you're fully prepared to drive — there is no override.
""",
        "drill": "Before booking your road test, log into your own driver record (or have your school confirm) that your ELDT certificate shows as **posted**, not just 'completed by the school.' Those are different things.",
    },

    # ───────────────────────── NYC OPERATING KNOWLEDGE ─────────────────────────
    {
        "id": "m03",
        "exit": "3",
        "title": "NYC Truck Route Network",
        "tag": "NYC Rules",
        "section": "NYC Operating Knowledge",
        "minutes": 14,
        "content": """
### The two route types
NYC designates its truck network into:
- **Through Truck Routes** — for trucks passing *through* an area without a local origin or destination there. These are the higher-capacity arterials (e.g. major avenues, expressways).
- **Local Truck Routes** — for trucks whose pickup or delivery is actually within that area.

### The core rule
If your origin and destination are both within NYC, you must use **Local Truck Routes**, leaving the network **only at the point closest to your actual pickup, delivery, loading, or service location** — not as a shortcut, and not because a car-GPS app suggested it.

### What counts as a "truck" under NYC routing rules
Any vehicle with **two axles and six tires or more**, or **three or more axles**, regardless of weight, is subject to the Truck Route Network requirements — this catches many box trucks and cube vans that drivers assume are "too small to count."

### Boroughs each have their own quirks
- **Manhattan**: extremely limited truck routes below 60th Street; cross-town routes are tightly restricted; many avenues are one-way, affecting approach planning.
- **Brooklyn/Queens**: industrial belt areas have wider truck access, but residential corridors are tightly restricted, and the BQE has well-known low-clearance and structural weight issues.
- **The Bronx**: major truck routes run along the Cross Bronx and Bruckner corridors; side-street routing is heavily residential.
- **Staten Island**: less dense truck network; the Staten Island Expressway and Korean War Veterans Parkway carry most truck traffic; some parkways are **passenger-vehicle only and ban commercial trucks entirely**, regardless of size.

### Parkway truck bans
NYC parkways (Henry Hudson, FDR Drive, most named "Parkways," Belt Parkway, Cross Island Parkway, Long Island Expressway service roads in some segments) generally **prohibit commercial trucks** outright — this isn't a height/weight restriction, it's a vehicle-class ban. GPS apps not built for trucks will route you onto these anyway.

### Bridges and tunnels — separate restriction layer on top of routing
Truck routing rules don't replace bridge/tunnel-specific restrictions. Some NYC bridges (several smaller crossings, some parkway bridges) prohibit commercial vehicles entirely or restrict by weight/height independent of whether the road segment is a "truck route."
""",
        "drill": "Before entering any block you haven't driven before: confirm it's a Local Truck Route reaching your specific stop, not just a route that looked clear on a car-GPS app. When in doubt, check the NYC DOT truck route map, not Google Maps.",
    },
    {
        "id": "m04",
        "exit": "4",
        "title": "Low Bridges, Clearance, and Structural Limits",
        "tag": "NYC Rules",
        "section": "NYC Operating Knowledge",
        "minutes": 9,
        "content": """
### Why this is NYC's #1 truck-driver trap
NYC and the surrounding metro area have an unusually high number of low parkway bridges, railroad underpasses, and old masonry bridges — many built for passenger cars only, decades before trucking regulations existed. Truck-vs-bridge strikes happen weekly in the metro area, often from drivers trusting a car GPS.

### Your clearance workflow, every single time
1. **Know your actual vehicle height**, measured, not estimated — include the trailer, any roof equipment, and an empty vs. loaded difference if your suspension changes ride height.
2. **Use a truck GPS with your real height entered** — never a default/passenger profile.
3. **Cross-check posted clearance signage physically** — paint, rust, or construction can change clearance without instant map updates.
4. **When a clearance sign and your GPS disagree, trust the sign.** Signs are the legal, current source.
5. **If you cannot confirm clearance and have any doubt, stop and find another route** — reversing a tractor-trailer out of a too-low approach is far more dangerous than the delay.

### Structural weight limits
Separate from height: many older NYC bridges have posted **weight limits** that are lower than the route's general truck allowance. A road can be a legal truck route while a specific bridge on it is weight-restricted — always check both signs independently.
""",
        "drill": "Never trust a clearance number from memory alone on a route you haven't run. Confirm with a current truck GPS profile AND the posted sign before committing the vehicle.",
    },
    {
        "id": "m05",
        "exit": "5",
        "title": "NYC Congestion, Camera Enforcement, and Curb Rules",
        "tag": "NYC Rules",
        "section": "NYC Operating Knowledge",
        "minutes": 8,
        "content": """
### Camera enforcement zones
NYC enforces bus lane and red-light violations heavily by camera, including for commercial trucks. A blocked bus lane, even briefly for a delivery, can generate an automated violation with no officer present. Congestion pricing tolling also applies to commercial vehicles entering the Manhattan congestion zone — factor this into route and delivery-window planning.

### Curb and loading reality
Legal commercial loading zones in NYC are limited and frequently occupied. Professional NYC drivers plan for:
- **Double-parking realities** — know which streets tolerate brief double-parking for active deliveries versus which will result in tickets or tows.
- **Loading zone time limits** — many are restricted to specific hours; some flip to no-standing after a cutoff time.
- **School zones and bus stops** — extra caution and extra enforcement near schools, especially at arrival/dismissal times.

### Bicycle and pedestrian density
NYC has extensive protected bike lane infrastructure layered into many truck routes. Right turns across bike lanes are a leading cause of serious truck-involved collisions nationally in dense urban cores — always do a full mirror and blind-spot check, never assume a bike lane is clear because it was clear seconds ago.
""",
        "drill": "Before any right turn in NYC: check the mirror, check the blind spot, check it again right before the wheels turn — bike and pedestrian positions change in seconds, not minutes.",
    },

    # ───────────────────────── VEHICLE SYSTEMS & INSPECTION ─────────────────────────
    {
        "id": "m06",
        "exit": "6",
        "title": "Pre-Trip Inspection — The Full Flow",
        "tag": "Skills Test",
        "section": "Vehicle Systems & Inspection",
        "minutes": 18,
        "content": """
### Why examiners fail people on this section more than any other
The vehicle inspection test isn't checking if you can find parts — it's checking if you have a **repeatable, complete sequence** you'll actually use every single day. A memorized but disordered list fails; a calm, structured walk doesn't.

### The standard sequence
1. **Vehicle overview** — walk around, look for obvious leaning, leaks, damage before touching anything.
2. **Engine compartment** — check fluid levels (oil, coolant, power steering, washer fluid), belts, hoses, leaks, wiring condition, battery condition/connections (if accessible).
3. **Cab/start-up checks** — gauges, warning lights, mirrors, horn, wipers, heater/defroster, seatbelt.
4. **Steering and suspension** — check steering play, steering linkage, kingpins, springs, shock absorbers, frame.
5. **Brakes** — visually check brake chambers, slack adjusters, brake drums/discs, brake linings/pads (as visible), hoses.
6. **Tires and wheels** — tread depth, sidewall damage, valve stems/caps, rim condition, lug nuts (check for rust trails indicating looseness), tire pressure (by gauge where required, never by kicking).
7. **Lights and reflectors** — headlights (high/low), turn signals, brake lights, clearance/marker lights, reflectors — confirm both function and physical condition.
8. **Coupling system** (combination vehicles) — fifth wheel, kingpin, locking jaws, apron, glad hands, electrical line, safety chains/cables.
9. **Trailer** (if applicable) — landing gear, doors, cargo securement points, ICC bumper, mud flaps.
10. **In-cab final check** — seatbelt, mirrors adjusted, emergency equipment present (fire extinguisher, spare fuses or circuit breakers, warning devices).
11. **Air brake check sequence** (Class A/B air brake equipped vehicles) — see Module 7 for the full breakdown.

### How to talk through it on test day
Speak each check out loud, state what you're checking and what you're looking/listening for — not just "this is the brake chamber." Examiners are listening for understanding, not vocabulary.
""",
        "drill": "Practice the full sequence out loud, daily, on a real vehicle if possible. On test day, confidence comes from doing the same sequence every time, not from rushing through a memorized script.",
    },
    {
        "id": "m07",
        "exit": "7",
        "title": "Air Brake Systems — What You Actually Need to Understand",
        "tag": "Skills Test",
        "section": "Vehicle Systems & Inspection",
        "minutes": 16,
        "content": """
### Why air brakes get their own knowledge test
Air brake systems behave very differently from hydraulic brakes, and a misunderstanding here is a safety-critical failure point — this is tested separately and seriously.

### Core concepts you must actually understand (not just recite)
- **Service brakes** — the normal foot-pedal brakes, applied by air pressure pushing brake chambers.
- **Parking brakes** — on air-brake vehicles, held *released* by air pressure and applied by spring force when air is removed — meaning a total air loss **applies** the brakes (a safety-by-design feature), it doesn't just remove your ability to stop.
- **Emergency brakes** — combine spring brakes (tractor) and either spring brakes or emergency relay valves (trailer) for emergency stops.

### The air brake check sequence you'll be tested on
1. **Engine off, key on**: check low air pressure warning activates at the proper threshold (typically around 60 psi, per manufacturer spec).
2. **With engine running, build air pressure**: confirm air pressure rises to operating range and check **governor cut-out** (the pressure where the compressor stops loading, commonly ~120–135 psi).
3. **Static leak test**: with the engine off and brakes released, air pressure should not drop more than the allowed rate (commonly 3 psi/min for a single vehicle, 4 psi/min for combination) over one minute.
4. **Applied leak test**: with the brakes applied and held, the allowed drop rate is slightly higher (commonly 4 psi/min single, 6 psi/min combination) — apply firm, steady pressure and hold.
5. **Low air warning test**: reduce pressure (by repeated brake applications with engine off) and confirm the warning buzzer/light activates at the proper threshold.
6. **Spring brake pop-out test**: continue reducing pressure and confirm spring brakes automatically activate (pop out) at the proper threshold (commonly 20–45 psi depending on vehicle).
7. **Parking brake test**: with the vehicle stopped and parking brake set, gently attempt to pull against it in low gear to confirm it holds.

### Common test-day failure points
- Rushing the leak tests — they require a full, timed minute each; rushing reads as not understanding why the test exists.
- Confusing the **governor cut-in** (pressure where the compressor starts loading again, commonly ~100–105 psi) with **cut-out** — examiners frequently ask both.
- Not knowing your own specific vehicle's numbers — ranges vary by manufacturer; learn your actual training vehicle's spec sheet, don't just memorize generic numbers.
""",
        "drill": "Don't just memorize numbers — explain out loud *why* each test exists (what failure it's designed to catch) until it's automatic. Examiners can tell the difference between recited numbers and real understanding.",
    },
    {
        "id": "m08",
        "exit": "8",
        "title": "Basic Vehicle Control & Backing",
        "tag": "Road Skills",
        "section": "Vehicle Systems & Inspection",
        "minutes": 12,
        "content": """
### The core basic control maneuvers
- **Straight-line backing** — back in a straight line for a set distance without exceeding the marked boundary lines.
- **Offset backing** (left and right) — back into a lane that's offset from your starting lane, requiring a controlled turn and straighten-out.
- **Alley dock** — back into a space perpendicular to your starting position, the maneuver most representative of real-world loading dock backing.
- **Parallel parking** (sight-side and blind-side, depending on test) — back into a parallel space using mirrors only.

### The mindset that actually passes this section
Small corrections, made early, beat big corrections made late. Examiners watch for **pull-up corrections** — stopping and pulling forward to reset your angle is almost always acceptable and far better than trying to force a bad angle through with the wheel.

### GOAL — your most important habit
**G**et **O**ut **A**nd **L**ook. Before backing in any real-world situation (not just the test), get out and visually confirm your clearance, especially on the side without good mirror visibility (the blind side for a single-mirror setup). A free reset is always better than a crash, a ticket, or a failed test.
""",
        "drill": "Set up wide, correct early and small, and never hesitate to pull forward and reset rather than fighting a bad angle. On the actual road, GOAL every time backing visibility is uncertain.",
    },
    {
        "id": "m09",
        "exit": "9",
        "title": "Turning, Space Management, and Urban Driving",
        "tag": "Road Skills",
        "section": "Vehicle Systems & Inspection",
        "minutes": 10,
        "content": """
### NYC turning realities
Set up wide before the turn, protect the trailer from cutting the curb, and constantly check mirrors through the turn — not just before it. Never force a turn if pedestrians, cyclists, parked cars, or street furniture (bollards, signs, planters) make the swing unsafe; stop and wait rather than clip something.

### Space management on city streets
- **Following distance** — city speeds are lower, but stopping distances for loaded trucks are still long; one second per 10 ft of vehicle length at speeds under 40 mph is a reasonable baseline, more at highway speed.
- **Space to the sides** — in dense traffic, accept that perfect side clearance often isn't available; prioritize the side with the worse consequence if contact occurs (pedestrians/cyclists over parked, empty vehicles).
- **Space ahead at intersections** — never enter an intersection you can't fully clear before the signal changes; gridlock blocking an intersection is both a hazard and (in NYC) a ticketed offense.

### Railroad crossings and drawbridges
Treat every at-grade rail crossing with full stop-look-listen discipline regardless of how familiar the crossing is. NYC and the surrounding region have several active drawbridges — know the signal sequence (warning bell, gates, lights) and never attempt to beat a closing gate.
""",
        "drill": "At every turn: set up wide, check mirrors through the full arc, and treat any blocked sightline as a stop-and-wait situation, not a squeeze-through situation.",
    },

    # ───────────────────────── HOURS, PAPERWORK, COMPLIANCE ─────────────────────────
    {
        "id": "m10",
        "exit": "10",
        "title": "Hours of Service (HOS)",
        "tag": "Federal Rule",
        "section": "Compliance & Paperwork",
        "minutes": 14,
        "content": """
### Why HOS exists
Hours of Service rules exist to prevent fatigue-related crashes — fatigue impairs reaction time and judgment in ways drivers consistently underestimate in themselves.

### The core property-carrying driver limits (most common CDL jobs)
- **11-hour driving limit** — may drive a maximum of 11 hours after 10 consecutive hours off duty.
- **14-hour limit** — may not drive beyond the 14th hour after coming on duty, following 10 hours off duty (this window doesn't pause for breaks — it just runs).
- **30-minute break requirement** — must take a 30-minute break after 8 cumulative hours of driving.
- **60/70-hour limit** — may not drive after 60 hours on duty in 7 consecutive days (or 70 hours in 8 days, depending on your carrier's operating schedule), unless qualifying for a 34-hour restart.

### Sleeper berth provision
Drivers using a sleeper berth may split their required 10 hours off duty into two periods, commonly an 8/2 split, provided neither period is shorter than the regulation requires and time is logged correctly — get the specific current split rules from your ELD training, since this is one of the more frequently updated provisions.

### ELDs (Electronic Logging Devices)
Most CDL operations require an ELD, which automatically tracks driving time via the engine. Know how to: log in/out correctly, certify your records, handle a malfunction (paper logs as backup, with proper notation), and request edits only through the proper driver co-certification process — falsifying logs is a serious federal violation, not a paperwork technicality.

### Short-haul and other exceptions
Certain short-haul operations (commonly: returning to the same work-reporting location within 14 hours, staying within a limited air-mile radius) may qualify for relaxed HOS recordkeeping — this varies, and you should confirm your specific operation's eligibility with your carrier's compliance team rather than assuming.
""",
        "drill": "Learn your ELD system before your first day on a real route — knowing how to certify logs and handle a malfunction calmly is a real job-readiness skill, not just test trivia.",
    },
    {
        "id": "m11",
        "exit": "11",
        "title": "Cargo, Weights, and Securement Basics",
        "tag": "Federal Rule",
        "section": "Compliance & Paperwork",
        "minutes": 11,
        "content": """
### Why this matters even if you're not hauling freight directly
Even local delivery and box truck drivers are responsible for verifying their cargo is legal and secure — "the warehouse loaded it" is not a defense at a roadside inspection.

### Weight basics
- **GVWR** (Gross Vehicle Weight Rating) — the manufacturer's maximum safe loaded weight for the vehicle itself.
- **GCWR** (Gross Combination Weight Rating) — the same, for the tractor + trailer combination.
- **Axle weight limits** — federal bridge formula and state-specific axle limits can restrict total loaded weight even when GVWR isn't exceeded; overloading a single axle while under total GVWR is still a violation.

### Securement fundamentals
- Cargo must be secured to prevent shifting that would affect vehicle handling, and to prevent any part of the load from leaking, blowing, or falling from the vehicle.
- Minimum number and rating of tie-downs scales with cargo weight and length — heavier/longer cargo requires more securement devices, not just tighter ones.
- Always re-check securement after the first 50 miles of a trip (cargo settles), then periodically afterward, and any time you change duty status.

### Special cargo categories
Special rules apply to certain cargo even outside formal hazmat classification — for example, requirements for securing logs, vehicles, large machinery, or items that could shift on uneven terrain. If you're hauling something outside standard palletized freight, confirm the specific securement standard before you load.
""",
        "drill": "Make the 50-mile re-check an automatic habit on every load, every time — not just when you remember.",
    },

    # ───────────────────────── ENDORSEMENTS ─────────────────────────
    {
        "id": "m12",
        "exit": "12",
        "title": "Combination Vehicles Endorsement",
        "tag": "Endorsement",
        "section": "Endorsements",
        "minutes": 10,
        "content": """
### Who needs this
Required for any Class A CDL holder operating a combination vehicle — this is tested alongside your general knowledge test for most Class A applicants, not as an optional add-on.

### Core knowledge areas
- **Coupling and uncoupling procedures** — the full correct sequence, including chocking, height matching, backing under, locking jaw confirmation, and the pull test before driving away.
- **Trailer air brake systems** — how trailer brakes interact with the tractor's system, including glad hand connections and emergency line behavior on breakaway.
- **Splitting/double-clutching** (if your equipment requires it) — many newer trucks use automated or synchronized manuals that don't, but you must understand the technique for older or specialized equipment.
- **Off-tracking** — understanding how a trailer's rear wheels track inside the tractor's path on turns, and how trailer length affects this.
""",
        "drill": "Practice the full coupling sequence including the pull-test every time, even when you're sure it's connected — skipping the pull test is a classic skills-test failure point.",
    },
    {
        "id": "m13",
        "exit": "13",
        "title": "Tanker Endorsement",
        "tag": "Endorsement",
        "section": "Endorsements",
        "minutes": 9,
        "content": """
### Who needs this
Required to operate any vehicle designed to transport liquid or gaseous materials in a tank with a capacity of 1,000+ gallons, whether or not the tank is full.

### Core knowledge areas
- **Surge** — liquid movement inside a partially full tank during acceleration, braking, and turns, which can violently shift the vehicle's effective center of gravity. This is the single most important concept in this endorsement.
- **Baffled vs. unbaffled (smooth bore) tanks** — baffles reduce but don't eliminate surge; smooth-bore tankers (common for milk, food-grade liquids) have no surge-reducing baffles at all and require even more conservative driving.
- **Outage** — tanks are intentionally not filled completely, to allow room for liquid expansion; never assume a tanker is "full" the way a dry van load would be.
- **Driving technique** — slower, earlier braking, wider turns, and extra caution on curves and ramps, because surge effects defeat normal stability assumptions.
""",
        "drill": "Treat every tanker turn and stop as if the load can move independently of the vehicle — because it can. Brake earlier and turn slower than you think you need to.",
    },
    {
        "id": "m14",
        "exit": "14",
        "title": "Doubles/Triples Endorsement",
        "tag": "Endorsement",
        "section": "Endorsements",
        "minutes": 8,
        "content": """
### Who needs this
Required to pull more than one trailer (doubles or triples) — not common in NYC local work, but relevant for regional/OTR career paths.

### Core knowledge areas
- **Converter dolly** — the connecting unit between trailers; understand its coupling and the additional pintle hook/safety chain inspection points it adds.
- **Crack-the-whip effect** — rearward amplification, where steering corrections are magnified at each successive trailer; the last trailer in a triples combination can swing dramatically more than the lead trailer.
- **Coupling/uncoupling order** — there's a specific correct sequence for connecting multiple trailers and dollies; doing it out of order creates real safety risk.
- **Stability** — multiple trailers raise rollover risk on curves and lane changes; speed management becomes more critical than with a single trailer.
""",
        "drill": "If pursuing doubles/triples work, drill the full multi-trailer coupling order until it's automatic — this is one of the least forgiving sequences to get wrong.",
    },
    {
        "id": "m15",
        "exit": "15",
        "title": "Passenger & School Bus Endorsements",
        "tag": "Endorsement",
        "section": "Endorsements",
        "minutes": 12,
        "content": """
### Who needs this
**Passenger (P) endorsement** — required for any vehicle designed to carry 16+ passengers including the driver. **School Bus (S) endorsement** — required in addition to P for actual school bus operation, and carries extra state-specific requirements (often including background checks beyond standard CDL requirements).

### Core knowledge areas
- **Pre-trip specifics for passenger vehicles** — emergency exits, interior lighting, securement of wheelchair lifts (if equipped), first-aid/emergency equipment specific to passenger transport.
- **Loading/unloading procedures** — especially for school buses: the use of the stop-arm, mirror systems for checking the "danger zone" directly around the bus, and railroad crossing procedures specific to buses (some jurisdictions require a stop-and-open-door procedure at all crossings).
- **Passenger management** — securing standees if permitted, managing emergency evacuations, prohibited cargo/passenger combinations.
- **NYC-specific bus considerations** — bus lane navigation, low-bridge sensitivity (buses are tall), and the dense pedestrian environment around stops.

### School bus specific
School bus driving carries the highest public scrutiny and the most jurisdiction-specific add-on rules of any CDL category — confirm your state and district's exact requirements beyond the baseline federal/CDL manual content, since school bus rules vary more than other endorsements.
""",
        "drill": "Drill the danger-zone mirror check sequence for school buses until it's automatic — this is the single highest-stakes habit in this endorsement category.",
    },
    {
        "id": "m16",
        "exit": "16",
        "title": "Hazmat Endorsement",
        "tag": "Endorsement",
        "section": "Endorsements",
        "minutes": 15,
        "content": """
### Who needs this
Required to transport materials in a quantity requiring placarding under federal hazmat regulations. This is the only CDL endorsement requiring a **TSA background check** (Hazmat Endorsement Threat Assessment Program) in addition to the knowledge test.

### Core knowledge areas
- **The Hazardous Materials Table** — how to read it, and how to determine the proper shipping name, hazard class, and packing group for a given material.
- **Placarding requirements** — when placards are required, which placards apply to which hazard classes, and correct placement on the vehicle.
- **Shipping papers** — what must be included, where they must be kept in the cab (within reach, clearly identified), and your responsibilities as the driver to inspect them, not just transport blindly.
- **Loading/unloading and segregation rules** — which hazard classes cannot be loaded together, and required separation distances from people/sources of ignition during loading.
- **Emergency response** — what to do (and not do) in event of a spill or leak, including when to evacuate versus attempt containment, and required notification procedures.
- **Route and parking restrictions** — many hazmat loads have restricted routes (avoiding tunnels, certain bridges, populated areas) — this interacts directly with NYC's already-restrictive tunnel/bridge rules in Module 4.

### Why the TSA process matters for timing
The TSA background check can take weeks. If you need a hazmat endorsement for a job, start this process immediately — it is consistently the longest-lead-time part of any CDL credential.
""",
        "drill": "Practice reading real Hazardous Materials Table entries until identifying hazard class, packing group, and placarding requirement is fast and automatic — this is heavily tested and easy to fumble under time pressure.",
    },

    # ───────────────────────── CAREER ─────────────────────────
    {
        "id": "m17",
        "exit": "17",
        "title": "Career Paths and Money Knowledge",
        "tag": "Career",
        "section": "Career",
        "minutes": 9,
        "content": """
### Common CDL career paths
Local delivery, box truck, dump truck, sanitation, construction material hauling, fuel/tanker delivery, food and beverage distribution, LTL (less-than-truckload) regional, bus and school bus driving, regional routes (home most nights), OTR (over-the-road, multi-day), and owner-operator.

### How endorsements change your earning lanes
Hazmat and tanker endorsements typically open higher-paying specialized freight lanes, but come with more compliance responsibility, more inspection scrutiny, and (for hazmat) the TSA background process. Passenger/school bus work trades freight-style pay scales for different schedules and benefits common in public-sector/transit roles.

### What actually keeps you employed after you're hired
Your CDL gets you *considered* for a job. What keeps you *employed* and *promotable* is: a clean driving record, drug/alcohol compliance with zero shortcuts, professional communication with dispatch and customers, consistent safe backing (low-cost insurance claims matter enormously to carriers), accurate paperwork/logs, on-time delivery performance, patience at customer sites, and visible vehicle-care discipline.

### NYC-specific career notes
NYC-based local driving (sanitation, delivery, construction-adjacent hauling) often pays a premium over equivalent rural/suburban routes specifically because of the route complexity covered in Modules 3–5 — that difficulty is a real, marketable skill once you're experienced in it.
""",
        "drill": "Your CDL gets you considered. Safety habits, reliability, and calm professionalism under NYC's specific operating pressure are what keep you hired and get you referred for better routes.",
    },
]

SECTIONS_ORDER = [
    "Getting Licensed",
    "NYC Operating Knowledge",
    "Vehicle Systems & Inspection",
    "Compliance & Paperwork",
    "Endorsements",
    "Career",
]


def modules_by_section() -> dict:
    """Group MODULES by their section, preserving SECTIONS_ORDER."""
    grouped = {s: [] for s in SECTIONS_ORDER}
    for m in MODULES:
        grouped.setdefault(m["section"], []).append(m)
    return grouped


def total_study_minutes() -> int:
    return sum(m.get("minutes", 0) for m in MODULES)
